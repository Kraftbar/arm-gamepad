# HTTP POST server script (http_post_server.py)
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_drawing():
    data = request.json
    print(f"Received coordinates: {data}")
    return '', 200

if __name__ == "__main__":
    app.run(host='192.168.0.52', port=12355)
