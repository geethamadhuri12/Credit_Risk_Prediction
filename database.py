import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_PORT:", os.getenv("DB_PORT"))

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = conn.cursor()

# ==============================
# Save Prediction
# ==============================

def save_prediction(
    annual_income,
    loan_amount,
    cibil_score,
    residential_assets,
    commercial_assets,
    luxury_assets,
    bank_assets,
    risk_probability,
    prediction
):
    sql = """
    INSERT INTO prediction_history(
        annual_income,
        loan_amount,
        cibil_score,
        residential_assets,
        commercial_assets,
        luxury_assets,
        bank_assets,
        risk_probability,
        prediction
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        float(annual_income),
        float(loan_amount),
        int(cibil_score),
        float(residential_assets),
        float(commercial_assets),
        float(luxury_assets),
        float(bank_assets),
        float(risk_probability),
        prediction
    )

    cursor.execute(sql, values)
    conn.commit()


# ==============================
# Fetch Prediction History
# ==============================

def get_predictions():
    cursor.execute("""
        SELECT *
        FROM prediction_history
        ORDER BY prediction_time DESC
    """)

    return cursor.fetchall()
# ==============================
# Clear Prediction History
# ==============================

def clear_predictions():
    cursor.execute("""
        DELETE FROM prediction_history
    """)
    conn.commit()
'''import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="geeth@12",
    database="credit_risk_db"
)

cursor = conn.cursor()


def save_prediction(
    annual_income,
    loan_amount,
    cibil_score,
    residential_assets,
    commercial_assets,
    luxury_assets,
    bank_assets,
    risk_probability,
    prediction
):
    sql = """
    INSERT INTO prediction_history(
        annual_income,
        loan_amount,
        cibil_score,
        residential_assets,
        commercial_assets,
        luxury_assets,
        bank_assets,
        risk_probability,
        prediction
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
    float(annual_income),
    float(loan_amount),
    int(cibil_score),
    float(residential_assets),
    float(commercial_assets),
    float(luxury_assets),
    float(bank_assets),
    float(risk_probability),
    prediction
)

    cursor.execute(sql, values)
    conn.commit()'''