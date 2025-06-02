import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

# Load data
df = pd.read_csv('./diabetes.csv')

# Replace zero values with NaN
zero_features = ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI']
df[zero_features] = df[zero_features].replace(0, np.nan)

# Fill missing values with median
df.fillna(df.median(), inplace=True)

# Separate features and target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert y to NumPy array
y = y.to_numpy()

# Set up model and cross-validation
logreg = LogisticRegression(max_iter=1000, random_state=42)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

all_y_true = []
all_y_pred = []

# Split data and implement Cross-validation loop
for train_index, test_index in skf.split(X_scaled, y):
    X_train_fold, X_test_fold = X_scaled[train_index], X_scaled[test_index]
    y_train_fold, y_test_fold = y[train_index], y[test_index]

    logreg.fit(X_train_fold, y_train_fold)
    y_pred_fold = logreg.predict(X_test_fold)

    all_y_true.extend(y_test_fold)
    all_y_pred.extend(y_pred_fold)


# Generate report as a dictionary
report_dict = classification_report(all_y_true, all_y_pred, output_dict=True)

# Convert to DataFrame
report_df = pd.DataFrame(report_dict).transpose().round(2)

# Display results
print("\n🔍 Cross-Validated Classification Report:", report_df)

# Save model and scaler
joblib.dump(logreg, 'model/logistic_model.joblib')
joblib.dump(scaler, 'model/scaler.joblib')

# Load model and scaler
loaded_model = joblib.load('model/logistic_model.joblib')
loaded_scaler = joblib.load('model/scaler.joblib')

# Use them
X_test_scaled = loaded_scaler.transform(X)
predictions = loaded_model.predict(X_test_scaled)

print(predictions)