# OBS Alerts Application

This application provides real-time alerts for OBS through a simple web interface. It uses Flask and WebSockets to achieve real-time capabilities.

## Features

- Receive a GET request to trigger alerts.
- Show alerts on the OBS with user-defined parameters (e.g., image size, text font, size, color).
- WebSockets for real-time updates.

## Setup and Running

### Prerequisites

- Python 3.9+
- Docker (for containerized deployment)

### Local Development

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-dir>
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

The application will be available at `http://localhost:5002`.

### Deployment with Docker
1. Update `Dockerfile` and add an `API_KEY`

2. Build the Docker image:
   ```
   docker build -t flask-obs-app .
   ```

3. Run the Docker container:
   ```
   docker run -p 5002:5002 flask-obs-app
   ```

The application will be available at `http://localhost:5002`.

## Usage

1. To trigger an alert, send a GET request to the `/trigger` endpoint with the desired parameters. For example:
   ```
   http://localhost:5002/trigger?api_key=<API_KEY>&gif=<gif-url>&audio=<audio-url>&text=Hello&text_color=red&text_font_size=20px&image_width=50%
   ```

2. OBS will display the alert based on the parameters provided in the request.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
