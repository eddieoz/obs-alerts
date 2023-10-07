Flask Socket.IO Example
This is a simple Flask application that demonstrates how to use Flask Socket.IO to create a real-time communication between the client and server.

Installation
Clone the repository: git clone https://github.com/username/flask-socketio-example.git
Install the dependencies: pip install -r requirements.txt
Usage
Start the server: python app.py
Open a web browser and navigate to http://localhost:5000
Click the "Trigger Alert" button to trigger an alert that will be displayed on the page.
Code Overview
The app.py file contains the Flask application code. It defines two routes: / and /trigger_alert. The / route renders the index.html template, which contains a button that triggers an alert when clicked. The /trigger_alert route handles the alert trigger by emitting a show_alert event with the alert data to the connected clients.

The SocketIO class from the flask_socketio package is used to create a new instance of the Socket.IO server, which is bound to the Flask application instance. This allows the server to handle real-time communication between the client and server.

License
This project is licensed under the MIT License. See the LICENSE file for details.

