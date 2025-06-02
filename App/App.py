from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    # met deze data kan dr nou verder mee gewerkt worden in het model
    data = request.form
    json_data = jsonify(data)
    return json_data


@app.route('/')
def index():
    return render_template("index.html")
