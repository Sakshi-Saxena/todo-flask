from flask import Flask, render_template
from flask import request

import requests

BACKEND_URL = "http://127.0.0.1:5001"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    request_data = dict(request.form)
    requests.post(f"{BACKEND_URL}/submit", json=request_data)
    return "data submitted successfully"



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)