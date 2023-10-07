from flask import Flask, render_template, request
from flask_socketio import SocketIO
from urllib.parse import unquote_plus
import os
port = int(os.environ.get("PORT", 5002))

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*")

@app.route('/')
def index():
    """
    Renders the index.html template when the root URL is accessed.
    """
    return render_template('index.html')

@app.route('/trigger_alert')
def trigger_alert():
    """
    Triggers an alert by emitting a 'show_alert' event with the alert data to the connected clients.

    Returns:
        str: A message indicating that the alert has been triggered.
    """
    gif_url = request.args.get('gif')
    audio_url = unquote_plus(request.args.get('audio'))
    text = request.args.get('text')
    width = request.args.get('width')
    height = request.args.get('height')
    fontFamily = request.args.get('fontFamily')
    fontSize = request.args.get('fontSize')
    borderColor = request.args.get('borderColor')
    borderWidth = request.args.get('borderWidth', '1px')  # Default to 1px if not provided
    color = request.args.get('color')
    duration = int(request.args.get('duration', 10000))  # Default to 10 seconds if not provided

    alert_data = {
        "gif": gif_url,
        "audio": audio_url,
        "text": text,
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
