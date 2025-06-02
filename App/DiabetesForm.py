from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DiabetesForm(FlaskForm):
    Pregnancies = IntegerField(
        "Pregnancies",
        validators=[DataRequired(), NumberRange(min=0)]
    )
    Glucose = IntegerField(
        "Glucose",
        validators=[DataRequired(), NumberRange(min=0)]
    )
    BloodPressure = IntegerField(
        "Blood Pressure",
        validators=[DataRequired(), NumberRange(min=0)]
    )
    SkinThickness = IntegerField(
        "Skin Thickness",
        validators=[DataRequired(), NumberRange(min=0)]
    )
    Insulin = IntegerField(
        "Insulin",
        validators=[DataRequired(), NumberRange(min=0)]
    )
    BMI = FloatField(
        "BMI",
        validators=[DataRequired(), NumberRange(min=0)]
    )
    DiabetesPedigreeFunction = FloatField(
        "Diabetes Pedigree Function",
        validators=[DataRequired(), NumberRange(min=0)]
    )
    Age = IntegerField(
        "Age",
        validators=[DataRequired(), NumberRange(min=0, max=130)]
    )
    Submit = SubmitField("Submit")
