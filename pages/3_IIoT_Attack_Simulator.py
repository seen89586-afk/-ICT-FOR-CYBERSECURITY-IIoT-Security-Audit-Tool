import streamlit as st

st.title("⚠️ IIoT Attack Simulator")

attack = st.selectbox(
    "Select Attack",
    ["Weak Password", "Unpatched Sensor", "Phishing Email", "Data Breach"]
)

if attack == "Weak Password":

    st.error("Threat: Hackers may access industrial devices.")
    st.success("Solution: Use strong passwords.")

elif attack == "Unpatched Sensor":

    st.error("Threat: Hackers may control sensors.")
    st.success("Solution: Update device firmware.")

elif attack == "Phishing Email":

    st.error("Threat: Employees may leak information.")
    st.success("Solution: Employee training.")

else:

    st.error("Threat: Sensitive data may be stolen.")
    st.success("Solution: Backup and encrypt data.")
