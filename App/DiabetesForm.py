from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DiabetesForm(FlaskForm):
    Pregnancies = IntegerField(
        "Pregnancies",
        validators=[NumberRange(min=-1)],
        render_kw={"placeholder": "Number of times pregnant"}
    )
    Glucose = IntegerField(
        "Glucose",
        validators=[DataRequired(), NumberRange(min=0)],
        render_kw={"placeholder": "Plasma glucose concentration"}
    )
    BloodPressure = IntegerField(
        "Blood Pressure",
        validators=[DataRequired(), NumberRange(min=0)],
        render_kw={"placeholder": "Diastolic blood pressure (mm Hg)"}
    )
    SkinThickness = IntegerField(
        "Skin Thickness",
        validators=[DataRequired(), NumberRange(min=0)],
        render_kw={"placeholder": "Triceps skin fold thickness (mm)"}
    )
    Insulin = IntegerField(
        "Insulin",
        validators=[DataRequired(), NumberRange(min=0)],
        render_kw={"placeholder": "2-Hour serum insulin (mu U/ml)"}
    )
    BMI = FloatField(
        "BMI",
        validators=[DataRequired(), NumberRange(min=0)],
        render_kw={
            "placeholder": "Body mass index (weight in kg/(height in m)^2)"
        }
    )
    DiabetesPedigreeFunction = FloatField(
        "Diabetes Pedigree Function",
        validators=[DataRequired(), NumberRange(min=0)],
        render_kw={"placeholder": "Diabetes pedigree function"}
    )
    Age = IntegerField(
        "Age",
        validators=[DataRequired(), NumberRange(min=0, max=130)],
        render_kw={"placeholder": "Age in years"}
    )
    Submit = SubmitField("Submit")
