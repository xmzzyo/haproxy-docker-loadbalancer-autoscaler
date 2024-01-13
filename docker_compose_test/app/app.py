# app.py
from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    # Get the hostname (container ID or hostname) to identify the instance
    hostname = socket.gethostname()
    return f"Hello from Flask web app! Instance ID: {hostname}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
