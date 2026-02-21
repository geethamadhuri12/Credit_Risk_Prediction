import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score
from xgboost import XGBClassifier

# ==============================
# 1. Load Dataset
# ==============================

df = pd.read_csv("loan_data.csv")

print("Original Shape:", df.shape)

# Clean column names
df.columns = df.columns.str.strip()

# Clean loan_status properly
df["loan_status"] = df["loan_status"].astype(str).str.strip().str.lower()

print("Loan status unique values:", df["loan_status"].unique())

# ==============================
# 2. Select Features
# ==============================

features = [
    "income_annum",
    "loan_amount",
    "cibil_score",
    "residential_assets_value",
    "commercial_assets_value",
    "luxury_assets_value",
    "bank_asset_value"
]

target = "loan_status"

df = df[features + [target]]

# Remove missing values
df.dropna(inplace=True)

print("Shape after cleaning:", df.shape)

# ==============================
# 3. Convert Target Properly
# ==============================

df[target] = df[target].map({"approved": 0, "rejected": 1})

print("After mapping:", df[target].unique())

# Remove any remaining NaN rows
df = df.dropna()

print("Final dataset shape:", df.shape)

# ==============================
# 4. Split Data
# ==============================

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==============================
# 5. Scale Features
# ==============================

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ==============================
# 6. Train Model
# ==============================

model = XGBClassifier(eval_metric="logloss")
model.fit(X_train, y_train)

# ==============================
# 7. Evaluate
# ==============================

y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# ==============================
# 8. Save Model
# ==============================

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))

print("\n✅ Model trained & saved successfully!")
