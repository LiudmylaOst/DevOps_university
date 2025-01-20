from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api')
def get_message():
    return jsonify(message="Hello from the backend!")
