'''import streamlit as st
import pickle
import numpy as np
import plotly.graph_objects as go

from database import save_prediction

# =====================================================
# LOAD MODEL
# =====================================================

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.markdown(
    "<div class='main-title'>💳 Credit Risk Prediction</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Enter applicant financial information</div>",
    unsafe_allow_html=True
)

st.write("")

left, right = st.columns(2)

# =====================================================
# LEFT COLUMN
# =====================================================

with left:

    income = st.number_input(
        "Annual Income (₹)",
        min_value=0.0,
        step=10000.0
    )

    cibil = st.slider(
        "CIBIL Score",
        300,
        900,
        700
    )

    residential = st.number_input(
        "Residential Assets (₹)",
        min_value=0.0,
        step=10000.0
    )

    luxury = st.number_input(
        "Luxury Assets (₹)",
        min_value=0.0,
        step=10000.0
    )

# =====================================================
# RIGHT COLUMN
# =====================================================

with right:

    loan = st.number_input(
        "Loan Amount (₹)",
        min_value=0.0,
        step=10000.0
    )

    commercial = st.number_input(
        "Commercial Assets (₹)",
        min_value=0.0,
        step=10000.0
    )

    bank = st.number_input(
        "Bank Assets (₹)",
        min_value=0.0,
        step=10000.0
    )

st.write("")

predict = st.button(
    "🚀 Analyze Credit Risk",
    use_container_width=True
)

# =====================================================
# PREDICTION
# =====================================================

if predict:

    values = np.array([[
        income,
        loan,
        cibil,
        residential,
        commercial,
        luxury,
        bank
    ]])

    scaled = scaler.transform(values)

    probability = model.predict_proba(scaled)[0][1]

    risk = probability * 100

    prediction = (
        "High Risk"
        if probability >= 0.5
        else "Low Risk"
    )

    save_prediction(
        income,
        loan,
        cibil,
        residential,
        commercial,
        luxury,
        bank,
        risk,
        prediction
    )

    st.success("Prediction saved successfully.")

    st.write("")

    c1, c2 = st.columns([1, 1])

    with c1:

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=risk,
                title={"text": "Risk Probability"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "#2563EB"},
                    "steps": [
                        {"range": [0, 40], "color": "#BBF7D0"},
                        {"range": [40, 70], "color": "#FDE68A"},
                        {"range": [70, 100], "color": "#FECACA"},
                    ],
                },
            )
        )

        gauge.update_layout(height=350)

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

    with c2:

        if prediction == "Low Risk":

            st.markdown("""
<div class="low-risk">

<h2>✅ LOW RISK</h2>

<h4>Loan Approval Probability is High</h4>

</div>
""", unsafe_allow_html=True)

        else:

            st.markdown("""
<div class="high-risk">

<h2>⚠ HIGH RISK</h2>

<h4>Loan Approval Probability is Low</h4>

</div>
""", unsafe_allow_html=True)

        st.metric(
            "Risk Probability",
            f"{risk:.2f}%"
        )

        st.metric(
            "Prediction",
            prediction
        )

    st.markdown("---")

    st.subheader("📊 AI Financial Assessment")

    a1, a2 = st.columns(2)

    with a1:

        if income >= 500000:
            st.success("✔ Strong Annual Income")
        else:
            st.warning("Annual Income is below the preferred range.")

        if cibil >= 750:
            st.success("✔ Excellent CIBIL Score")
        elif cibil >= 700:
            st.info("✔ Good CIBIL Score")
        else:
            st.error("Poor CIBIL Score")

    with a2:

        total_assets = (
            residential +
            commercial +
            luxury +
            bank
        )

        if total_assets >= 500000:
            st.success("✔ Strong Asset Portfolio")
        else:
            st.warning("Limited Asset Portfolio")

        if loan <= income:
            st.success("✔ Healthy Loan-to-Income Ratio")
        else:
            st.error("Loan exceeds Annual Income")

    st.markdown("---")

    st.subheader("💡 AI Recommendation")

    if prediction == "Low Risk":

        st.success("""
### Recommendation

✅ Loan can be approved.

Suggested Improvements

• Continue maintaining a good credit history.

• Keep loan repayments on time.

• Avoid unnecessary debt.
""")

    else:

        st.error("""
### Recommendation

⚠ Applicant has higher financial risk.

Suggested Improvements

• Improve CIBIL Score.

• Reduce existing liabilities.

• Increase annual income.

• Build stronger financial assets.
""")'''
import streamlit as st
import pickle
import numpy as np
import plotly.graph_objects as go

from database import save_prediction

# =====================================================
# LOAD MODEL
# =====================================================

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.markdown(
    "<div class='main-title'>💳 Credit Risk Prediction</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Analyze applicant financial profile using AI</div>",
    unsafe_allow_html=True
)

st.write("")

st.markdown("## 📝 Applicant Information")

col1, col2 = st.columns(2)

with col1:

    income = st.number_input(
        "Annual Income (₹)",
        min_value=0.0,
        step=10000.0,
        format="%.2f"
    )

    cibil = st.slider(
        "CIBIL Score",
        300,
        900,
        700
    )

    residential = st.number_input(
        "Residential Assets (₹)",
        min_value=0.0,
        step=10000.0,
        format="%.2f"
    )

    luxury = st.number_input(
        "Luxury Assets (₹)",
        min_value=0.0,
        step=10000.0,
        format="%.2f"
    )

with col2:

    loan = st.number_input(
        "Loan Amount (₹)",
        min_value=0.0,
        step=10000.0,
        format="%.2f"
    )

    commercial = st.number_input(
        "Commercial Assets (₹)",
        min_value=0.0,
        step=10000.0,
        format="%.2f"
    )

    bank = st.number_input(
        "Bank Assets (₹)",
        min_value=0.0,
        step=10000.0,
        format="%.2f"
    )

st.write("")

predict = st.button(
    "🚀 Analyze Credit Risk",
    use_container_width=True
)

if predict:

    values = np.array([[
        income,
        loan,
        cibil,
        residential,
        commercial,
        luxury,
        bank
    ]])

    scaled = scaler.transform(values)

    probability = model.predict_proba(scaled)[0][1]

    risk = probability * 100

    prediction = (
        "High Risk"
        if probability >= 0.5
        else "Low Risk"
    )

    save_prediction(
        income,
        loan,
        cibil,
        residential,
        commercial,
        luxury,
        bank,
        risk,
        prediction
    )

    st.success("Prediction completed successfully.")

    st.write("")

    left, right = st.columns([1,1])

    with left:

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=risk,
                title={"text":"Risk Probability"},
                gauge={
                    "axis":{"range":[0,100]},
                    "bar":{"color":"royalblue"},
                    "steps":[
                        {"range":[0,40],"color":"#BBF7D0"},
                        {"range":[40,70],"color":"#FDE68A"},
                        {"range":[70,100],"color":"#FECACA"},
                    ]
                }
            )
        )

        gauge.update_layout(height=350)

        st.plotly_chart(
            gauge,
            use_container_width=True
        )
    with right:

        st.markdown("## 📄 Credit Decision")

        if prediction == "Low Risk":

            grade = "A"
            health = "Excellent"
            decision = "Eligible for Loan"

            st.success(f"""
### ✅ LOW RISK

**Decision:** {decision}

**Risk Probability:** {risk:.2f}%

**Credit Grade:** {grade}

**Financial Health:** {health}
""")

        else:

            grade = "C"
            health = "Needs Improvement"
            decision = "Review Required"

            st.error(f"""
### ⚠ HIGH RISK

**Decision:** {decision}

**Risk Probability:** {risk:.2f}%

**Credit Grade:** {grade}

**Financial Health:** {health}
""")

    st.markdown("---")

    st.subheader("📊 AI Financial Assessment")

    loan_ratio = (
        (loan / income) * 100
        if income > 0
        else 0
    )

    asset_total = (
        residential +
        commercial +
        luxury +
        bank
    )

    col1, col2 = st.columns(2)

    with col1:

        if income >= 500000:
            st.success("✔ Strong Annual Income")
        else:
            st.warning("Annual Income is below the preferred range.")

        if cibil >= 750:
            st.success("✔ Excellent CIBIL Score")
        elif cibil >= 700:
            st.info("✔ Good CIBIL Score")
        else:
            st.error("Poor CIBIL Score")

        if loan_ratio <= 50:
            st.success(
                f"✔ Healthy Loan-to-Income Ratio ({loan_ratio:.1f}%)"
            )
        else:
            st.error(
                f"High Loan-to-Income Ratio ({loan_ratio:.1f}%)"
            )

    with col2:

        if asset_total >= 500000:
            st.success("✔ Strong Asset Portfolio")
        else:
            st.warning("Limited Asset Portfolio")

        st.info(
            f"Total Assets: ₹{asset_total:,.0f}"
        )

        if cibil >= 800:
            rating = "Excellent"
        elif cibil >= 750:
            rating = "Very Good"
        elif cibil >= 700:
            rating = "Good"
        elif cibil >= 650:
            rating = "Fair"
        else:
            rating = "Poor"

        st.info(
            f"Credit Rating: {rating}"
        )

        st.markdown("---")
        st.subheader("💡 AI Recommendation")

    if prediction == "Low Risk":

        st.success("""
### Recommendation

The applicant demonstrates a strong financial profile and is considered a low-risk borrower.

#### Positive Factors

- Excellent repayment potential
- Healthy financial assets
- Good credit behaviour
- Stable financial profile

#### Suggested Decision

✅ Loan can be approved with minimal financial risk.
""")

    else:

        st.error("""
### Recommendation

The applicant requires additional financial review before loan approval.

#### Areas for Improvement

- Improve CIBIL Score
- Reduce existing liabilities
- Increase annual income
- Build stronger financial assets

#### Suggested Decision

⚠ Manual verification is recommended before approval.
""")

    st.markdown("---")

    st.subheader("📋 Credit Summary")

    summary1, summary2 = st.columns(2)

    with summary1:

        st.info(f"""
### Applicant Summary

**Annual Income**

₹{income:,.0f}

**Loan Amount**

₹{loan:,.0f}

**CIBIL Score**

{cibil}

**Credit Rating**

{rating}
""")

    with summary2:

        st.info(f"""
### Decision Summary

**Prediction**

{prediction}

**Risk Probability**

{risk:.2f}%

**Loan-to-Income Ratio**

{loan_ratio:.1f}%

**Financial Health**

{health}
""")

    st.markdown("---")

    st.caption(
        "SmartCredit AI • Credit Decision Engine"
    )
