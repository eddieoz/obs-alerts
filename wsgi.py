from app import app
from flask_socketio import SocketIO
 
if __name__ == "__main__":
        socketio = SocketIO(app)
        # app.run()