import os
import random
import pandas as pd

# -----------------------------------------
# Configuration
# -----------------------------------------

NUM_SAMPLES = 10000

# Automatically create folders if they don't exist
os.makedirs("src/ml/data", exist_ok=True)


# -----------------------------------------
# Generate One Synthetic Alert
# -----------------------------------------

def generate_alert():

    severity = random.choice([
        "Low",
        "Medium",
        "High",
        "Critical"
    ])

    powershell = random.randint(0, 1)

    privileged = random.randint(0, 1)

    blacklisted = random.randint(0, 1)

    mitre_match = random.randint(0, 1)

    source_private = random.randint(0, 1)

    is_tcp = random.randint(0, 1)

    severity_score = {
        "Low": 1,
        "Medium": 2,
        "High": 3,
        "Critical": 4
    }[severity]

    # Risk scoring logic
    score = (
        severity_score * 2
        + powershell * 2
        + privileged
        + blacklisted * 3
        + mitre_match
    )

    risk = 1 if score >= 8 else 0

    return {

        "severity_score": severity_score,

        "source_private": source_private,

        "is_tcp": is_tcp,

        "privileged_user": privileged,

        "powershell_detected": powershell,

        "blacklisted": blacklisted,

        "mitre_match": mitre_match,

        "risk": risk

    }


# -----------------------------------------
# Generate Dataset
# -----------------------------------------

data = []

for _ in range(NUM_SAMPLES):
    data.append(generate_alert())

df = pd.DataFrame(data)


# -----------------------------------------
# Save Dataset
# -----------------------------------------

dataset_path = "src/ml/data/soc_dataset.csv"

df.to_csv(
    dataset_path,
    index=False
)


# -----------------------------------------
# Display Information
# -----------------------------------------

print("=" * 50)
print("AI SOC Synthetic Dataset Generated Successfully")
print("=" * 50)

print("\nFirst 5 Rows:\n")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nRisk Distribution:")
print(df["risk"].value_counts())

print("\nDataset saved at:")
print(dataset_path)