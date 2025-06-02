from flask import Flask, jsonify, render_template, request, redirect, url_for
import secrets
from DiabetesForm import DiabetesForm
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

logreg = joblib.load('model/logistic_model.joblib')
scaler = joblib.load('model/scaler.joblib')


def predict_diabetes_from_json(json_input, model, scaler) -> tuple[int, float]:
    """
    Predict diabetes outcome from a single patient's data in JSON format.

    Parameters:
        json_input (dict): JSON-like dictionary with patient feature values.
        model (sklearn model): Trained classifier (e.g., LogisticRegression).
        scaler (StandardScaler): Fitted scaler object.

    Returns:
        dict: {'prediction': 0 or 1, 'probability': float}
    """
    feature_columns = [
        'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
        'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'
    ]
    try:
        input_df = pd.DataFrame([json_input], columns=feature_columns)

        zero_replace_features = ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI']
        input_df[zero_replace_features] = input_df[zero_replace_features].replace(0, np.nan)

        input_df.fillna(input_df.median(), inplace=True)

        input_scaled = scaler.transform(input_df)

        prediction = int(model.predict(input_scaled)[0])
        probability = float(model.predict_proba(input_scaled)[0][1])

        return (prediction, round(probability, 4))

    except Exception:
        return (0, 0)


@app.route('/', methods=['POST', 'GET'])
def index():
    form = DiabetesForm()
    if form.validate_on_submit():
        print("boe")
        # met deze data kan dr nou verder mee gewerkt worden in het model
        data = request.form
        json_data = jsonify(data)
        Risk, Prob = predict_diabetes_from_json(
            json_data,
            model=logreg,
            scaler=scaler
        )
        print(Risk, Prob)
        riskString: str = "Risk of Diabetes Detected" if Risk == 1 else "No Risk of Diabetes Detected"
        ReturnValue = f"There is {riskString} with a certainty of {Prob*100}%"
        return render_template('index.html', form=form, output=ReturnValue)
    return render_template('index.html', form=form, output="Nothing")