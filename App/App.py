from flask import Flask, jsonify, render_template, request, redirect, url_for
import secrets
from DiabetesForm import DiabetesForm

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)


@app.route('/', methods=['POST', 'GET'])
def index():
    form = DiabetesForm()
    if form.validate_on_submit():
        # met deze data kan dr nou verder mee gewerkt worden in het model
        data = request.form
        json_data = jsonify(data)
        return json_data
    return render_template('index.html', form=form, output="Nothing")
