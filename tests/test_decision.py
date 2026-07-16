from src.decision.engine import DecisionEngine

engine = DecisionEngine()

features = {

    "severity_score": 3,

    "powershell_detected": 1,

    "privileged_user": 1

}

mitre = {

    "technique_id": "T1059.001"

}

threat = {

    "blacklisted": True

}

print(engine.decide(features, mitre, threat))