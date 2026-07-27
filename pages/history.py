'''import streamlit as st
import pandas as pd
from database import get_predictions

st.markdown(
    "<div class='main-title'>📜 Prediction History</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Search, Filter & Export Prediction Records</div>",
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

    st.write("")

    col1, col2 = st.columns([2,1])

    with col1:

        search = st.text_input(
            "🔍 Search",
            placeholder="Search any value..."
        )

    with col2:

        prediction_filter = st.selectbox(
            "Prediction",
            [
                "All",
                "Low Risk",
                "High Risk"
            ]
        )

    filtered_df = df.copy()

    if prediction_filter != "All":

        filtered_df = filtered_df[
            filtered_df["Prediction"] == prediction_filter
        ]

    if search:

        filtered_df = filtered_df[
            filtered_df.astype(str)
            .apply(
                lambda row:
                row.str.contains(
                    search,
                    case=False
                )
            )
            .any(axis=1)
        ]

    st.write("")

    col1,col2,col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Records",
            len(filtered_df)
        )

    with col2:

        st.metric(
            "Low Risk",
            len(
                filtered_df[
                    filtered_df["Prediction"]=="Low Risk"
                ]
            )
        )

    with col3:

        st.metric(
            "High Risk",
            len(
                filtered_df[
                    filtered_df["Prediction"]=="High Risk"
                ]
            )
        )

    st.write("")

    display_df = filtered_df[
        [
            "Annual Income",
            "Loan Amount",
            "CIBIL Score",
            "Risk Probability",
            "Prediction",
            "Prediction Time"
        ]
    ]

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

    csv = display_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="📥 Download Prediction History",
        data=csv,
        file_name="prediction_history.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.write("")

    st.success(
        f"Showing {len(display_df)} records."
    )

else:

    st.warning("No prediction history available.")

st.markdown("---")

st.caption(
    "SmartCredit AI • Prediction History Module"
)'''
import streamlit as st
import pandas as pd
from database import get_predictions

st.markdown(
    "<div class='main-title'>📜 Prediction History</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Manage, search and export prediction records</div>",
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

    st.markdown("## 🔍 Search & Filter")

    col1, col2, col3 = st.columns(3)

    with col1:

        search = st.text_input(
            "Search",
            placeholder="Income, Loan, CIBIL..."
        )

    with col2:

        prediction_filter = st.selectbox(
            "Prediction",
            [
                "All",
                "Low Risk",
                "High Risk"
            ]
        )

    with col3:

        date_filter = st.selectbox(
            "Date",
            [
                "All Time",
                "Today",
                "Last 7 Days",
                "Last 30 Days"
            ]
        )

    filtered_df = df.copy()

    if prediction_filter != "All":

        filtered_df = filtered_df[
            filtered_df["Prediction"] == prediction_filter
        ]

    if date_filter == "Today":

        filtered_df = filtered_df[
            filtered_df["Prediction Time"].dt.date
            == pd.Timestamp.today().date()
        ]

    elif date_filter == "Last 7 Days":

        filtered_df = filtered_df[
            filtered_df["Prediction Time"]
            >= pd.Timestamp.now() - pd.Timedelta(days=7)
        ]

    elif date_filter == "Last 30 Days":

        filtered_df = filtered_df[
            filtered_df["Prediction Time"]
            >= pd.Timestamp.now() - pd.Timedelta(days=30)
        ]

    if search:

        search = search.lower()

        filtered_df = filtered_df[
            filtered_df.astype(str)
            .apply(
                lambda row: row.str.lower().str.contains(search).any(),
                axis=1
            )
        ]

    st.markdown("## 📋 Prediction Records")

    st.dataframe(
        filtered_df[
            [
                "Annual Income",
                "Loan Amount",
                "CIBIL Score",
                "Risk Probability",
                "Prediction",
                "Prediction Time"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )
    st.write("")

    st.markdown("## ⚙ Actions")

    col1, col2 = st.columns(2)

    with col1:

        csv = filtered_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Export Filtered Records",
            data=csv,
            file_name="prediction_history.csv",
            mime="text/csv",
            use_container_width=True
        )

    with col2:

        if st.button(
            "🗑 Clear Prediction History",
            use_container_width=True,
            type="secondary"
        ):

            st.session_state["confirm_delete"] = True

    if st.session_state.get("confirm_delete", False):

        st.warning(
            "⚠ This action will permanently delete all prediction records."
        )

        yes_col, no_col = st.columns(2)

        with yes_col:

            if st.button(
                "✅ Yes, Delete All",
                use_container_width=True
            ):
                from database import clear_predictions

                clear_predictions()

                st.success("Prediction history cleared successfully.")

                st.session_state["confirm_delete"] = False

                st.rerun()

        with no_col:

            if st.button(
                "❌ Cancel",
                use_container_width=True
            ):
                st.session_state["confirm_delete"] = False

                st.rerun()

    st.markdown("---")

    st.caption(
        f"Showing {len(filtered_df)} of {len(df)} records"
    )

    st.caption(
        "SmartCredit AI • Prediction History"
    )

else:

    st.info("No prediction records found.")