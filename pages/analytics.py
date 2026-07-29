'''import streamlit as st
import pandas as pd
import plotly.express as px
from database import get_predictions

st.markdown(
    "<div class='main-title'>📊 Analytics Dashboard</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Business Intelligence & Credit Risk Insights</div>",
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

    df["Prediction Time"] = pd.to_datetime(df["Prediction Time"])

    st.markdown("## 📈 Daily Prediction Trend")

    trend = (
        df.groupby(df["Prediction Time"].dt.date)
        .size()
        .reset_index(name="Predictions")
    )

    fig = px.line(
        trend,
        x="Prediction Time",
        y="Predictions",
        markers=True,
        title="Daily Predictions"
    )

    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 🥧 Risk Distribution")

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

        st.plotly_chart(
            pie,
            use_container_width=True
        )

    with col2:

        st.markdown("### 📊 Risk Probability")

        hist = px.histogram(
            df,
            x="Risk Probability",
            nbins=20,
            color="Prediction",
            color_discrete_map={
                "Low Risk":"green",
                "High Risk":"red"
            }
        )

        st.plotly_chart(
            hist,
            use_container_width=True
        )

    st.markdown("---")

    st.markdown("## 💰 Income vs Loan Analysis")

    scatter = px.scatter(
        df,
        x="Annual Income",
        y="Loan Amount",
        color="Prediction",
        size="Risk Probability",
        hover_data=[
            "CIBIL Score"
        ],
        color_discrete_map={
            "Low Risk":"green",
            "High Risk":"red"
        }
    )

    st.plotly_chart(
        scatter,
        use_container_width=True
    )

    st.markdown("---")

    st.markdown("## 🏆 Top 10 Highest Risk Applicants")

    highest = df.sort_values(
        by="Risk Probability",
        ascending=False
    )

    st.dataframe(
        highest.head(10),
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.markdown("## 📉 Average Risk by Prediction")

    avg = (
        df.groupby("Prediction")["Risk Probability"]
        .mean()
        .reset_index()
    )

    avg_chart = px.bar(
        avg,
        x="Prediction",
        y="Risk Probability",
        color="Prediction",
        text_auto=".2f",
        color_discrete_map={
            "Low Risk":"green",
            "High Risk":"red"
        }
    )

    st.plotly_chart(
        avg_chart,
        use_container_width=True
    )

else:

    st.warning("No analytics data available.")'''
import streamlit as st
import pandas as pd
import plotly.express as px
from database import get_predictions

st.markdown(
    "<div class='main-title'>📊 Business Analytics</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Analyze credit risk trends and financial insights</div>",
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

    df["Prediction Time"] = pd.to_datetime(df["Prediction Time"])

    st.markdown("## 📈 Daily Prediction Trend")

    trend = (
        df.groupby(df["Prediction Time"].dt.date)
        .size()
        .reset_index(name="Predictions")
    )

    trend_chart = px.line(
        trend,
        x="Prediction Time",
        y="Predictions",
        markers=True,
        title="Daily Prediction Trend"
    )

    trend_chart.update_layout(height=400)

    st.plotly_chart(
        trend_chart,
        use_container_width=True
    )

    st.write("")

    left, right = st.columns(2)

    with left:

        st.markdown("### 🥧 Risk Distribution")

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

        pie.update_layout(height=400)

        st.plotly_chart(
            pie,
            use_container_width=True
        )

    with right:

        st.markdown("### 📊 Risk Probability Distribution")

        hist = px.histogram(
            df,
            x="Risk Probability",
            nbins=20,
            color="Prediction",
            color_discrete_map={
                "Low Risk":"green",
                "High Risk":"red"
            }
        )

        hist.update_layout(height=400)

        st.plotly_chart(
            hist,
            use_container_width=True
        )

    st.write("")

    left, right = st.columns(2)

    with left:

        st.markdown("### 💰 Income vs Loan Amount")

        scatter = px.scatter(
            df,
            x="Annual Income",
            y="Loan Amount",
            color="Prediction",
            size="Risk Probability",
            hover_data=["CIBIL Score"],
            color_discrete_map={
                "Low Risk":"green",
                "High Risk":"red"
            }
        )

        scatter.update_layout(height=420)

        st.plotly_chart(
            scatter,
            use_container_width=True
        )
    with right:

        st.markdown("### ⭐ CIBIL Score Distribution")

        cibil_chart = px.histogram(
            df,
            x="CIBIL Score",
            nbins=20,
            color="Prediction",
            color_discrete_map={
                "Low Risk": "green",
                "High Risk": "red"
            }
        )

        cibil_chart.update_layout(height=420)

        st.plotly_chart(
            cibil_chart,
            use_container_width=True
        )

    st.write("")

    

    st.markdown("## 📌 Business Insights")

    total_predictions = len(df)

    high_percentage = (
        (len(df[df["Prediction"] == "High Risk"]) / total_predictions) * 100
        if total_predictions > 0 else 0
    )

    low_percentage = (
        (len(df[df["Prediction"] == "Low Risk"]) / total_predictions) * 100
        if total_predictions > 0 else 0
    )

    avg_income = df["Annual Income"].mean()

    avg_loan = df["Loan Amount"].mean()

    avg_cibil = df["CIBIL Score"].mean()

    highest_risk = df["Risk Probability"].max()

    lowest_risk = df["Risk Probability"].min()

    col1, col2 = st.columns(2)

    with col1:

        st.info(f"""
### Portfolio Overview

**Total Predictions**

{total_predictions}

**High Risk Applicants**

{high_percentage:.1f}%

**Low Risk Applicants**

{low_percentage:.1f}%
""")

    with col2:

        st.success(f"""
### Financial Overview

**Average Income**

₹{avg_income:,.0f}

**Average Loan**

₹{avg_loan:,.0f}

**Average CIBIL**

{avg_cibil:.0f}
""")

    st.write("")

    st.warning(f"""
### Risk Summary

• Highest Risk Probability : **{highest_risk:.2f}%**

• Lowest Risk Probability : **{lowest_risk:.2f}%**
""")

    st.markdown("---")

    st.caption(
        "SmartCredit AI • Business Intelligence Dashboard"
    )

else:

    st.warning("No analytics data available.")