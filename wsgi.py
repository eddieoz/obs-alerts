from app import app
from flask_socketio import SocketIO

# Create a SocketIO instance and run the Flask app if this file is executed directly
if __name__ == "__main__":
        socketio = SocketIO(app)
