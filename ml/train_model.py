import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("../data/gaming_dataset.csv")

# Drop unnecessary columns
df = df.drop(columns=["record_id", "primary_game"], errors="ignore")

# Handle missing values
df = df.fillna(df.median(numeric_only=True))

# Encode categorical features
encoders = {}
categorical_cols = df.select_dtypes(include=["object"]).columns

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Separate features and target
X = df.drop("gaming_addiction_risk_level", axis=1)
y = df["gaming_addiction_risk_level"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=300, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)

print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "model.pkl")
joblib.dump(encoders, "encoders.pkl")

print("\nModel and encoders saved successfully.")
