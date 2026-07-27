'''import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from database import get_predictions

st.markdown(
    "<div class='main-title'>🏦 SmartCredit AI Dashboard</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>AI Powered Credit Risk Intelligence Platform</div>",
    unsafe_allow_html=True
)

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
            "Risk Probability",
            "Prediction",
            "Prediction Time"
        ]
    )

else:

    df = pd.DataFrame(
        columns=[
            "Annual Income",
            "Loan Amount",
            "CIBIL Score",
            "Residential Assets",
            "Commercial Assets",
            "Luxury Assets",
            "Bank Assets",
            "Risk Probability",
            "Prediction",
            "Prediction Time"
        ]
    )

total = len(df)

low = len(df[df["Prediction"] == "Low Risk"])

high = len(df[df["Prediction"] == "High Risk"])

average = (
    df["Risk Probability"].mean()
    if total > 0
    else 0
)

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.markdown(f"""
<div class="card">
<div class="metric-title">TOTAL PREDICTIONS</div>
<div class="metric-value">{total}</div>
</div>
""", unsafe_allow_html=True)

with c2:

    st.markdown(f"""
<div class="card">
<div class="metric-title">LOW RISK</div>
<div class="metric-value" style="color:#16A34A;">{low}</div>
</div>
""", unsafe_allow_html=True)

with c3:

    st.markdown(f"""
<div class="card">
<div class="metric-title">HIGH RISK</div>
<div class="metric-value" style="color:#DC2626;">{high}</div>
</div>
""", unsafe_allow_html=True)

with c4:

    st.markdown(f"""
<div class="card">
<div class="metric-title">AVERAGE RISK</div>
<div class="metric-value">{average:.1f}%</div>
</div>
""", unsafe_allow_html=True)

st.write("")

left, right = st.columns([1.2, 1])

with left:

    st.markdown("### 📊 Risk Distribution")

    if total > 0:

        fig = px.pie(
            df,
            names="Prediction",
            hole=0.65,
            color="Prediction",
            color_discrete_map={
                "Low Risk": "#16A34A",
                "High Risk": "#DC2626"
            }
        )

        fig.update_layout(height=420)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info("No prediction data available.")

with right:

    st.markdown("### 🎯 Average Risk")

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=average,
            title={"text": "Risk %"},
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

    gauge.update_layout(height=420)

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

st.write("")

st.markdown("### 📈 Recent Predictions")

if total > 0:

    recent = df[[
        "Annual Income",
        "Loan Amount",
        "CIBIL Score",
        "Risk Probability",
        "Prediction",
        "Prediction Time"
    ]].head(10)

    st.dataframe(
        recent,
        use_container_width=True,
        hide_index=True
    )

else:

    st.warning("Prediction history is empty.")'''
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from database import get_predictions

st.markdown(
    "<div class='main-title'>🏦 SmartCredit AI Dashboard</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>AI Powered Credit Risk Intelligence Platform</div>",
    unsafe_allow_html=True
)

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
            "Risk Probability",
            "Prediction",
            "Prediction Time"
        ]
    )

else:

    df = pd.DataFrame(
        columns=[
            "Annual Income",
            "Loan Amount",
            "CIBIL Score",
            "Residential Assets",
            "Commercial Assets",
            "Luxury Assets",
            "Bank Assets",
            "Risk Probability",
            "Prediction",
            "Prediction Time"
        ]
    )

total = len(df)

low = len(df[df["Prediction"] == "Low Risk"])

high = len(df[df["Prediction"] == "High Risk"])

average_risk = (
    df["Risk Probability"].mean()
    if total > 0 else 0
)

average_cibil = (
    df["CIBIL Score"].mean()
    if total > 0 else 0
)

total_loan = (
    df["Loan Amount"].sum()
    if total > 0 else 0
)

st.markdown("## 📊 Executive Overview")

r1c1, r1c2, r1c3 = st.columns(3)

with r1c1:

    st.metric(
        "📊 Total Predictions",
        total
    )

with r1c2:

    st.metric(
        "🟢 Low Risk",
        low
    )

with r1c3:

    st.metric(
        "🔴 High Risk",
        high
    )

r2c1, r2c2, r2c3 = st.columns(3)

with r2c1:

    st.metric(
        "⚠ Average Risk",
        f"{average_risk:.1f}%"
    )

with r2c2:

    st.metric(
        "⭐ Avg CIBIL",
        f"{average_cibil:.0f}"
    )

with r2c3:

    st.metric(
        "💰 Total Loan Amount",
        f"₹{total_loan:,.0f}"
    )

st.write("")

left, right = st.columns([1.1,1])

with left:

    st.markdown("### 🥧 Risk Distribution")

    if total > 0:

        pie = px.pie(
            df,
            names="Prediction",
            hole=0.65,
            color="Prediction",
            color_discrete_map={
                "Low Risk":"green",
                "High Risk":"red"
            }
        )

        pie.update_layout(
            height=420,
            showlegend=True
        )

        st.plotly_chart(
            pie,
            use_container_width=True
        )

    else:

        st.info("No prediction data available.")

with right:

    st.markdown("### 🎯 Average Risk")

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=average_risk,
            title={"text":"Risk %"},
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

    gauge.update_layout(
        height=420
    )

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

st.write("")

st.markdown("## 💰 Financial Analysis")

left,right = st.columns(2)

with left:

    if total>0:

        loan_chart = px.histogram(
            df,
            x="Loan Amount",
            nbins=20,
            title="Loan Amount Distribution"
        )

        loan_chart.update_layout(
            height=400
        )

        st.plotly_chart(
            loan_chart,
            use_container_width=True
        )
with right:

    if total > 0:

        income_chart = px.scatter(
            df,
            x="Annual Income",
            y="CIBIL Score",
            color="Prediction",
            size="Risk Probability",
            hover_data=[
                "Loan Amount"
            ],
            color_discrete_map={
                "Low Risk": "green",
                "High Risk": "red"
            },
            title="Income vs CIBIL Score"
        )

        income_chart.update_layout(
            height=400
        )

        st.plotly_chart(
            income_chart,
            use_container_width=True
        )

st.write("")

st.markdown("## 📌 Business Summary")

b1, b2, b3 = st.columns(3)

with b1:

    highest_risk = (
        df["Risk Probability"].max()
        if total > 0 else 0
    )

    st.info(f"""
### Highest Risk

**{highest_risk:.2f}%**
""")

with b2:

    avg_income = (
        df["Annual Income"].mean()
        if total > 0 else 0
    )

    st.success(f"""
### Average Income

**₹{avg_income:,.0f}**
""")

with b3:

    avg_loan = (
        df["Loan Amount"].mean()
        if total > 0 else 0
    )

    st.warning(f"""
### Average Loan

**₹{avg_loan:,.0f}**
""")

st.write("")

st.markdown("## 🕒 Recent Predictions")

if total > 0:

    recent = df[
        [
            "Annual Income",
            "Loan Amount",
            "CIBIL Score",
            "Risk Probability",
            "Prediction",
            "Prediction Time"
        ]
    ].head(5)

    st.dataframe(
        recent,
        use_container_width=True,
        hide_index=True
    )

else:

    st.warning(
        "Prediction history is empty."
    )

st.write("")

st.markdown("---")

st.caption(
    "SmartCredit AI Dashboard • Executive Overview"
)