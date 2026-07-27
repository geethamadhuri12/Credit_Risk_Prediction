import streamlit as st
import pickle
import numpy as np

# ==============================
# Load Model & Scaler
# ==============================
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ==============================
# Page Configuration
# ==============================
st.set_page_config(page_title="Credit Risk Predictor", page_icon="💳", layout="centered")

# ==============================
# Custom Styling
# ==============================
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: white;
        background: linear-gradient(90deg, #1f4e79, #2980b9);
        padding: 15px;
        border-radius: 10px;
    }
    .low-risk {
        background-color: #d4edda;
        color: #155724;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        font-size: 18px;
    }
    .high-risk {
        background-color: #f8d7da;
        color: #721c24;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">💳 Credit Risk Predictor</div>', unsafe_allow_html=True)

st.write("### Enter Applicant Details")

# ==============================
# Input Fields
# ==============================

income = st.number_input("Applicant Annual Income", min_value=0.0, step=10000.0)
loan = st.number_input("Loan Amount", min_value=0.0, step=10000.0)
cibil = st.number_input("CIBIL Score", min_value=300.0, max_value=900.0, step=1.0)

residential = st.number_input("Residential Assets Value", min_value=0.0, step=10000.0)
commercial = st.number_input("Commercial Assets Value", min_value=0.0, step=10000.0)
luxury = st.number_input("Luxury Assets Value", min_value=0.0, step=10000.0)
bank_asset = st.number_input("Bank Asset Value", min_value=0.0, step=10000.0)

# ==============================
# Prediction
# ==============================

if st.button("Predict Risk"):

    data = np.array([[income, loan, cibil, residential, commercial, luxury, bank_asset]])
    data = scaler.transform(data)

    probability = model.predict_proba(data)[0][1]  # Probability of High Risk
    risk_percentage = probability * 100

    st.write(f"## Risk Probability: {risk_percentage:.2f}%")

    # Risk Badge
    if probability < 0.5:
        st.markdown('<div class="low-risk">✅ LOW RISK – Loan Likely Approved</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="high-risk">⚠ HIGH RISK – Loan Likely Rejected</div>', unsafe_allow_html=True)

    # ==============================
    # Explanation Section
    # ==============================

    st.write("### Explanation of Factors")

    if income > 500000:
        st.success("✔ High Income")
    else:
        st.warning("⚠ Low Income")

    if loan > income:
        st.error("⚠ Loan Amount Higher than Income")
    else:
        st.success("✔ Loan Amount Reasonable")

    if cibil > 700:
        st.success("✔ Good CIBIL Score")
    else:
        st.error("⚠ Poor CIBIL Score")

    if residential + commercial + luxury + bank_asset > 500000:
        st.success("✔ Strong Asset Support")
    else:
        st.warning("⚠ Low Asset Backup")
