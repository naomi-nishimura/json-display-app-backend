from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
from datetime import datetime

whole_data = []

app = Flask(__name__)
CORS(app)

@app.route('/json', methods=['POST'])
def receive_json():
    data = request.json
    now = datetime.now()
    whole_data.append({"createdOn":str(now),"data":data})
    return jsonify(data), 200

@app.route('/')
def index():
    html_string = ""
    for jsonObj in whole_data:
        html_string += f"<p>{jsonObj}</p>"
    return f'<html><h1>テスト結果</h1>{html_string}</html>'

if __name__ == '__main__':
    app.run(debug=True)
