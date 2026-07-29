# 💳 SmartCredit AI
### AI-Powered Credit Risk Intelligence Platform

SmartCredit AI is a Machine Learning-powered web application that predicts whether a loan applicant is **High Risk** or **Low Risk** based on financial information. The application provides real-time credit risk prediction, business analytics, and historical record management through an interactive Streamlit dashboard.

---

## 🚀 Features

### 🏠 Dashboard
- Executive overview of loan portfolio
- Total predictions, high-risk & low-risk applicants
- Average CIBIL score and average risk
- Risk distribution charts
- Business summary and recent predictions

### 🔍 Credit Risk Prediction
- Applicant financial information form
- Machine Learning-based prediction
- Risk probability gauge
- Credit decision summary
- AI financial assessment
- Personalized recommendations
- Credit summary report

### 📊 Business Analytics
- Daily prediction trends
- Risk distribution analysis
- Income vs Loan Amount visualization
- CIBIL score distribution
- Portfolio and financial insights

### 📜 Prediction History
- Store prediction records in MySQL
- Search and filter records
- Export prediction history to CSV
- Clear prediction history

---

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Frontend:** Streamlit
- **Machine Learning:** Scikit-learn
- **Database:** MySQL
- **Data Processing:** Pandas, NumPy
- **Visualization:** Plotly
- **Version Control:** Git & GitHub
- **Environment Management:** python-dotenv

---

## 📂 Project Structure

```text
SmartCreditAI/
│
├── app.py
├── database.py
├── model.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
├── README.md
│
├── assets/
│   └── style.css
│
├── pages/
│   ├── dashboard.py
│   ├── predict.py
│   ├── analytics.py
│   └── history.py
│
└── .streamlit/
    └── config.toml
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/geethamadhuri12/Credit_Risk_Prediction.git
cd Credit_Risk_Prediction
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

Create a `.env` file:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=credit_risk
```

### Run the Application

```bash
streamlit run app.py
```

---

## 🧠 Machine Learning Workflow

1. Enter applicant financial details.
2. Preprocess input data.
3. Predict loan risk using the trained ML model.
4. Display risk probability and credit decision.
5. Store prediction in MySQL.
6. Analyze prediction history through interactive dashboards.

---

## 📸 Application Modules

- 🏠 Dashboard
- 🔍 Predict
- 📊 Analytics
- 📜 History

---

## 🔮 Future Enhancements

- User Authentication
- Role-Based Access Control
- Batch Prediction using Excel
- PDF Report Generation
- Cloud Deployment
- Enhanced Machine Learning Models

---

## 👩‍💻 Author

**Kanneboina Geetha Madhuri**

- GitHub: https://github.com/geethamadhuri12
- LinkedIn: https://www.linkedin.com/in/kanneboina-geetha-madhuri-992354322/

---

⭐ If you found this project useful, consider giving it a **star** on GitHub!
