# Credit Risk Prediction System

## Overview

The Credit Risk Prediction System is a Machine Learning web application that predicts whether a loan applicant is at **High Risk** or **Low Risk** based on financial information. The application provides real-time predictions through an interactive Streamlit interface and stores every prediction in a MySQL database for future analysis.

This project demonstrates the complete Machine Learning workflow, including data preprocessing, model training, prediction, database integration, and visualization.

---

## Features

- Predicts applicant credit risk using a trained Machine Learning model.
- Interactive Streamlit web interface for easy user interaction.
- Real-time prediction probability with risk classification.
- Stores prediction history in a MySQL database.
- Displays prediction history with timestamps.
- Interactive dashboard with summary metrics.
- Pie chart and bar chart for prediction analytics.
- Clean and responsive user interface.

---

## Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- MySQL
- Pickle

---

## Project Structure

```
Credit_Risk_Prediction/
│
├── app.py
├── database.py
├── train.py
├── model.pkl
├── scaler.pkl
├── columns.pkl
├── loan_data.csv
├── eda.ipynb
├── test_db.py
├── requirements.txt
└── README.md
```

---

## Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Scaling
4. Model Training
5. Model Serialization
6. Streamlit Deployment
7. MySQL Integration
8. Dashboard Visualization

---

## Input Features

- Annual Income
- Loan Amount
- CIBIL Score
- Residential Assets Value
- Commercial Assets Value
- Luxury Assets Value
- Bank Assets Value

---

## Prediction Output

The system predicts:

- Low Risk
- High Risk

Along with:

- Risk Probability (%)
- Prediction Timestamp

---

## Dashboard Features

- Total Predictions
- High Risk Count
- Low Risk Count
- Prediction History
- Pie Chart Visualization
- Bar Chart Visualization

---

## Database Integration

Every prediction is automatically stored in a MySQL database with:

- Applicant Financial Details
- Prediction Result
- Risk Probability
- Prediction Time

This enables historical tracking and analytical reporting.

---

## Installation

Clone the repository

```bash
git clone https://github.com/geethamadhuri12/Credit_Risk_Prediction.git
```

Move into the project directory

```bash
cd Credit_Risk_Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Future Enhancements

- User Authentication
- Loan Approval Recommendation
- Explainable AI (SHAP/LIME)
- Cloud Deployment
- PDF Report Generation
- Email Notification System
- REST API Integration

---

## Author

**Geetha Madhuri**

GitHub:
https://github.com/geethamadhuri12

LinkedIn:
https://www.linkedin.com/in/kanneboina-geetha-madhuri-992354322

---
