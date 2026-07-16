import streamlit as st
import requests

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI SOC Decision Engine",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI SOC Decision Engine")
st.write("Analyze security alerts using the AI SOC Decision Engine.")

# -----------------------------
# Input Form
# -----------------------------
st.subheader("Alert Information")

alert_name = st.text_input(
    "Alert Name",
    value="PowerShell Execution"
)

severity = st.selectbox(
    "Severity",
    ["Low", "Medium", "High", "Critical"],
    index=2
)

source_ip = st.text_input(
    "Source IP",
    value="192.168.10.5"
)

destination_ip = st.text_input(
    "Destination IP",
    value="8.8.8.8"
)

protocol = st.selectbox(
    "Protocol",
    ["TCP", "UDP"],
    index=0
)

username = st.text_input(
    "Username",
    value="administrator"
)

hostname = st.text_input(
    "Hostname",
    value="SERVER-01"
)

description = st.text_area(
    "Description",
    value="Suspicious PowerShell execution"
)

# -----------------------------
# Analyze Button
# -----------------------------
if st.button("🚀 Analyze Alert"):

    payload = {
        "alert_id": "ALT-1001",
        "alert_name": alert_name,
        "severity": severity,
        "timestamp": "2026-07-10T12:00:00",
        "source_ip": source_ip,
        "destination_ip": destination_ip,
        "protocol": protocol,
        "username": username,
        "hostname": hostname,
        "description": description
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/alerts",
            json=payload,
            timeout=10
        )

        response.raise_for_status()

        result = response.json()

        st.success("✅ Alert Processed Successfully")

        st.divider()

        # -----------------------------
        # Metrics
        # -----------------------------
        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Risk Score",
                result["decision"]["risk_score"]
            )

            st.metric(
                "ML Confidence",
                f"{result['decision']['probability']*100:.2f}%"
            )

            st.metric(
                "Decision",
                result["decision"]["decision"]
            )

        with col2:
            st.metric(
                "MITRE Technique",
                result["mitre"]["technique_id"]
            )

            st.metric(
                "Threat Reputation",
                result["threat"]["reputation"]
            )

        st.divider()

        # -----------------------------
        # Features
        # -----------------------------
        # -----------------------------------------
        # Extracted Features
        # -----------------------------------------

        st.divider()

        st.subheader("📊 Extracted Features")

        features = result["features"]

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Severity Score",
                features["severity_score"]
            )

            st.metric(
                "Private Source",
                "Yes" if features["source_private"] else "No"
            )

            st.metric(
                "Protocol",
                "TCP" if features["is_tcp"] else "UDP"
            )

        with col2:

            st.metric(
                "Privileged User",
                "Yes" if features["privileged_user"] else "No"
            )

            st.metric(
                "PowerShell",
                "Detected" if features["powershell_detected"] else "Not Detected"
            )

            st.metric(
                "Blacklisted",
                "Yes" if features["blacklisted"] else "No"
            )

        # -----------------------------------------
        # Threat Intelligence
        # -----------------------------------------

        st.divider()

        st.subheader("🌍 Threat Intelligence")

        threat = result["threat"]

        st.info(
            f"""
IP Address : {threat['ip']}

Reputation : {threat['reputation']}

Blacklisted : {threat['blacklisted']}
"""
        )

        # -----------------------------------------
        # MITRE ATT&CK
        # -----------------------------------------

        st.divider()

        st.subheader("🛡️ MITRE ATT&CK")

        mitre = result["mitre"]

        st.success(
            f"""
Technique : {mitre['technique']}

Technique ID : {mitre['technique_id']}

Tactic : {mitre['tactic']}
"""
        )

        # -----------------------------------------
        # AI Explanation
        # -----------------------------------------

        st.divider()

        st.subheader("🤖 AI Explanation")

        for line in result["explanation"]:

            st.write("✅", line)

        # -----------------------------------------
        # Parsed Alert
        # -----------------------------------------

        st.divider()

        with st.expander("📄 Complete Parsed Alert"):

            st.json(result["alert"])

    except requests.exceptions.ConnectionError:
        st.error(
            "❌ Cannot connect to FastAPI.\n\n"
            "Make sure the backend is running:\n\n"
            "uvicorn app:app --reload"
        )

    except Exception as e:
        st.error(f"Error: {e}")

        decision = result["decision"]["decision"]

if decision == "Escalate":
    st.error("🔴 ESCALATE IMMEDIATELY")

elif decision == "Investigate":
    st.warning("🟡 INVESTIGATE")

else:
    st.success("🟢 CLOSE ALERT")

    st.divider()

st.subheader("👨‍💻 Analyst Summary")

st.write(
    f"""
The AI SOC Engine analyzed the alert and assigned a
risk score of **{result['decision']['risk_score']}**
with an ML confidence of
**{result['decision']['probability']*100:.2f}%**.

Final recommendation:

**{result['decision']['decision']}**
"""
)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes import router

app = FastAPI(
    title="AI SOC Decision Engine",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)