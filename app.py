'''import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from database import save_prediction,get_predictions

# ==============================
# Load Model & Scaler
# ==============================
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ==============================
# Page Configuration
# ==============================
st.set_page_config(
    page_title="Credit Risk Predictor",
    page_icon="💳",
    layout="centered"
)

# ==============================
# Custom Styling
# ==============================
st.markdown("""
<style>
.main-title{
    text-align:center;
    font-size:36px;
    font-weight:bold;
    color:white;
    background:linear-gradient(90deg,#1f4e79,#2980b9);
    padding:15px;
    border-radius:10px;
}

.low-risk{
    background:#d4edda;
    color:#155724;
    padding:12px;
    border-radius:8px;
    text-align:center;
    font-size:18px;
    font-weight:bold;
}

.high-risk{
    background:#f8d7da;
    color:#721c24;
    padding:12px;
    border-radius:8px;
    text-align:center;
    font-size:18px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">💳 Credit Risk Predictor</div>',
    unsafe_allow_html=True
)

st.write("### Enter Applicant Details")

# ==============================
# Input Fields
# ==============================

income = st.number_input(
    "Applicant Annual Income",
    min_value=0.0,
    step=10000.0
)

loan = st.number_input(
    "Loan Amount",
    min_value=0.0,
    step=10000.0
)

cibil = st.number_input(
    "CIBIL Score",
    min_value=300.0,
    max_value=900.0,
    step=1.0
)

residential = st.number_input(
    "Residential Assets Value",
    min_value=0.0,
    step=10000.0
)

commercial = st.number_input(
    "Commercial Assets Value",
    min_value=0.0,
    step=10000.0
)

luxury = st.number_input(
    "Luxury Assets Value",
    min_value=0.0,
    step=10000.0
)

bank_asset = st.number_input(
    "Bank Asset Value",
    min_value=0.0,
    step=10000.0
)

# ==============================
# Prediction
# ==============================

if st.button("Predict Risk"):

    data = np.array([
        [
            income,
            loan,
            cibil,
            residential,
            commercial,
            luxury,
            bank_asset
        ]
    ])

    data = scaler.transform(data)

    probability = model.predict_proba(data)[0][1]
    risk_percentage = float(probability * 100)

    st.write(f"## Risk Probability: {risk_percentage:.2f}%")

    if probability < 0.5:
        prediction = "Low Risk"

        st.markdown(
            '<div class="low-risk">✅ LOW RISK – Loan Likely Approved</div>',
            unsafe_allow_html=True
        )

    else:
        prediction = "High Risk"

        st.markdown(
            '<div class="high-risk">⚠ HIGH RISK – Loan Likely Rejected</div>',
            unsafe_allow_html=True
        )

    # ==============================
    # Save Prediction to MySQL
    # ==============================

    save_prediction(
        income,
        loan,
        cibil,
        residential,
        commercial,
        luxury,
        bank_asset,
        risk_percentage,
        prediction
    )

    st.success("Prediction saved successfully to MySQL!")

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
# ==============================
# Dashboard & Prediction History
# ==============================

st.markdown("---")

if st.button("📊 View Prediction History"):

    rows = get_predictions()

    if rows:

        df = pd.DataFrame(
            rows,
            columns=[
                "ID",
                "Annual Income",
                "Loan Amount",
                "CIBIL Score",
                "Residential Assets",
                "Commercial Assets",
                "Luxury Assets",
                "Bank Assets",
                "Risk Probability (%)",
                "Prediction",
                "Prediction Time"
            ]
        )

        # ==============================
        # Dashboard
        # ==============================

        st.subheader("📊 Dashboard")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Predictions", len(df))
        col2.metric(
            "Low Risk",
            len(df[df["Prediction"] == "Low Risk"])
        )
        col3.metric(
            "High Risk",
            len(df[df["Prediction"] == "High Risk"])
        )

        # ==============================
        # Pie Chart
        # ==============================

        st.subheader("🥧 Risk Distribution")

        risk_counts = df["Prediction"].value_counts()

        # Assign colors based on prediction labels
        color_map = {
            "Low Risk": "#2ecc71",   # Green
            "High Risk": "#e74c3c"   # Red
        }

        colors = [color_map[label] for label in risk_counts.index]

        fig, ax = plt.subplots(figsize=(5, 5))

        ax.pie(
            risk_counts,
            labels=risk_counts.index,
            autopct="%1.1f%%",
            startangle=90,
            explode=[0.05] * len(risk_counts),
            colors=colors
        )

        ax.axis("equal")

        st.pyplot(fig)

        # ==============================
        # Bar Chart
        # ==============================

        st.subheader("📈 Prediction Distribution")

        st.bar_chart(df["Prediction"].value_counts())

        # ==============================
        # Prediction History
        # ==============================

        st.subheader("📋 Prediction History")

        display_df = df[[
            "Annual Income",
            "Loan Amount",
            "CIBIL Score",
            "Risk Probability (%)",
            "Prediction",
            "Prediction Time"
        ]]

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True
        )

    else:
        st.warning("No prediction history found.") first one
import streamlit as st
from streamlit_option_menu import option_menu

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="SmartCredit AI",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# LOAD CSS
# ----------------------------------------------------

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------

with st.sidebar:

    st.image(
        "https://img.icons8.com/fluency/96/bank-building.png",
        width=90
    )

    st.markdown("## SmartCredit AI")

    st.caption("Credit Risk Intelligence Platform")

    selected = option_menu(
        menu_title=None,
        options=[
            "Dashboard",
            "Predict",
            "Analytics",
            "History",
            "About"
        ],
        icons=[
            "house",
            "cpu",
            "graph-up-arrow",
            "clock-history",
            "info-circle"
        ],
        default_index=0
    )

# ----------------------------------------------------
# PAGE ROUTER
# ----------------------------------------------------

if selected == "Dashboard":
    exec(open("pages/dashboard.py").read())

elif selected == "Predict":
    exec(open("pages/predict.py").read())

elif selected == "Analytics":
    exec(open("pages/analytics.py").read())

elif selected == "History":
    exec(open("pages/history.py").read())

elif selected == "About":
    exec(open("pages/about.py").read())'''
import streamlit as st
from streamlit_option_menu import option_menu

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="SmartCredit AI",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================
# LOAD CSS
# ==============================
try:
    with open("assets/style.css", "r", encoding="utf-8") as css:
        st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("style.css not found!")

# ==============================
# SIDEBAR
# ==============================
with st.sidebar:

    st.markdown("# 🏦")
    st.markdown("## SmartCredit AI")
    st.caption("Credit Risk Intelligence Platform")

    selected = option_menu(
        menu_title=None,
        options=[
            "Dashboard",
            "Predict",
            "Analytics",
            "History"
        ],
        icons=[
            "house",
            "credit-card",
            "bar-chart",
            "clock-history"
        ],
        default_index=0,
    )

# ==============================
# PAGE ROUTING
# ==============================

if selected == "Dashboard":

    with open("pages/dashboard.py", "r", encoding="utf-8") as f:
        exec(f.read())

elif selected == "Predict":

    with open("pages/predict.py", "r", encoding="utf-8") as f:
        exec(f.read())

elif selected == "Analytics":

    with open("pages/analytics.py", "r", encoding="utf-8") as f:
        exec(f.read())

elif selected == "History":

    with open("pages/history.py", "r", encoding="utf-8") as f:
        exec(f.read())

