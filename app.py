from flask import Flask, render_template, request
from flask_socketio import SocketIO
from urllib.parse import unquote_plus
import logging
logging.basicConfig(level=logging.DEBUG)

import json
import random
import os
port = int(os.environ.get("PORT", 5002))
api_key = os.environ.get("API_KEY", '')

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*")

@app.route('/')
def index():
    """
    Renders the index.html template when the root URL is accessed.
    """
    return render_template('index.html')

@app.route('/trigger_alert', methods=['GET', 'POST'])
def trigger_alert():
    """
    Triggers an alert by emitting a 'show_alert' event with the alert data to the connected clients.

    Returns:
        str: A message indicating that the alert has been triggered.
    """
    # if request.method == 'GET':
    
    if (not request.args.get('api_key') or request.args.get('api_key') != os.environ.get("API_KEY", '')):
        return "Invalid API key"
    gif_url = request.args.get('gif', 'https://media0.giphy.com/media/vKHKDIdvxvN7vTAEOM/giphy.gif')
    audio_url = unquote_plus(request.args.get('audio', 'https://www.myinstants.com/media/sounds/mrbitcoin.mp3'))
    text = request.args.get('text', 'Hey!')
    tts = request.args.get('tts', '')
    width = request.args.get('width', '40%')
    height = request.args.get('height', '40%')
    fontFamily = request.args.get('fontFamily', 'Arial')
    fontSize = request.args.get('fontSize', '30px')
    borderColor = request.args.get('borderColor', 'black')
    borderWidth = request.args.get('borderWidth', '1px')  # Default to 1px if not provided
    color = request.args.get('color', 'white')
    duration = int(request.args.get('duration', 10000))  # Default to 10 seconds if not provided

    if request.method == 'POST':        
        # Get the alert data from the request body
        data = request.json
        
        
        # LN Bits integration
        # Should have LNURLP working and register the callback URL
        
        # Check if data['amount'] exists
        if 'amount' in data:
            option = random.randint(0,1)
            if option == 0:
                gif_url = "https://cdn.zebedee.io/streamer/images/d095a7bb-3d92-4775-9107-6401f8c52417_satoshi-red-socks-craig-wright.gif"
                audio_url = unquote_plus('https://www.myinstants.com/media/sounds/cwisnotsatoshi.mp3')
                width = '70%'
            else:
                gif_url = "https://media1.giphy.com/media/l49JMVDvP8D38LHwI/giphy.gif"
                audio_url = unquote_plus('https://www.myinstants.com/media/sounds/mrbitcoin.mp3')
                width = '40%'
                
            if 'comment' in data:
                if data['comment'] != '':
                    amount = int(data['amount']/1000)
                    if amount >= 2100:
                        audio_url = "https://www.myinstants.com/media/sounds/bitcoin-dono-mix.mp3"
                        tts = f"https://api.streamelements.com/kappa/v2/speech?voice=Vitoria&text={data['comment']}"             
                    text = f"\nVocê recebeu {amount} sats!\n{''.join(data['comment'])}"
            
        # gif_url = data['gif']
        # width = data['width']
        # height = data['height']
        # fontFamily = data['fontFamily']
        # fontSize = data['fontSize']
        # borderColor = data['borderColor']
        # borderWidth = data['borderWidth']
        # color = data['color']
        # duration = data['duration']


    alert_data = {
        "gif": gif_url,
        "audio": audio_url,
        "text": text,
        "tts": tts,
        "width": width,
        "height": height,
        "fontFamily": fontFamily,
        "fontSize": fontSize,
        "borderColor": borderColor,
        "borderWidth": borderWidth,
        "color": color,
        "duration": duration
    }
    socketio.emit('show_alert', alert_data)
    return "Alert triggered"

if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=port)
