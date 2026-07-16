import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from xgboost import XGBClassifier

# -------------------------------
# Load Dataset
# -------------------------------

df = pd.read_csv("src/ml/data/soc_dataset.csv")

# -------------------------------
# Features and Labels
# -------------------------------

X = df.drop("risk", axis=1)

y = df["risk"]

# -------------------------------
# Train/Test Split
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -------------------------------
# Train Model
# -------------------------------

model = XGBClassifier(

    n_estimators=100,

    max_depth=5,

    learning_rate=0.1,

    random_state=42,

    eval_metric="logloss"

)

model.fit(X_train, y_train)

# -------------------------------
# Evaluate
# -------------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("=" * 50)
print("MODEL TRAINED")
print("=" * 50)

print(f"\nAccuracy : {accuracy:.4f}\n")

print(classification_report(y_test, predictions))

# -------------------------------
# Save Model
# -------------------------------

os.makedirs("src/ml/models", exist_ok=True)

joblib.dump(
    model,
    "src/ml/models/xgboost_model.pkl"
)

print("\nModel Saved Successfully!")