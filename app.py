from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/json', methods=['POST'])
def receive_json():
    data = request.json
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True,port=5000)
