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
        #AI return data
        data: Unknown = request.form 
        json_data : Unkown = jsonify(data)
        print(json_data)
        Risk, Prob = 1,1
        riskString = "Risk of Diabetes Detected" if Risk == 1 else "No Risk of Diabetes Detected"
        ReturnValue = f"There is {riskString} with a certainty of {Prob*100}%"
        return render_template('index.html', form=form, output=ReturnValue)
        # return json_data
    return render_template('index.html', form=form, output="Nothing")

    