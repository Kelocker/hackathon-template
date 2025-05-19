# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # enable cross-origin requests for React

@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello from Flask!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')