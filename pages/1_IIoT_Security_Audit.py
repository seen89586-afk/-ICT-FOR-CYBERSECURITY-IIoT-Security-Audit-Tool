import streamlit as st

st.title("⭐ IIoT Security Audit Tool")

score = 0

device_update = st.radio("Are IoT devices updated regularly?", ["Yes", "No"])
wifi_password = st.radio("Is a strong Wi-Fi password used?", ["Yes", "No"])
mfa = st.radio("Is two-factor authentication enabled?", ["Yes", "No"])
training = st.radio("Are employees trained in cybersecurity?", ["Yes", "No"])
backup = st.radio("Is data backed up regularly?", ["Yes", "No"])

if st.button("Generate Security Score"):

    if device_update == "Yes":
        score += 20

    if wifi_password == "Yes":
        score += 20

    if mfa == "Yes":
        score += 20

    if training == "Yes":
        score += 20

    if backup == "Yes":
        score += 20

    st.subheader(f"Security Score: {score}/100")

    if score >= 80:
        st.success("🟢 Excellent Security")

    elif score >= 60:
        st.warning("🟡 Moderate Security")

    else:
        st.error("🔴 Poor Security")
