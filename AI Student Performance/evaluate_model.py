import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


print("Loading trained model...")

# -------------------------
# Load trained model
# -------------------------

model = joblib.load("student_model.pkl")

print("Model loaded successfully")


# -------------------------
# Load dataset
# -------------------------

df = pd.read_csv("Dataset/student-mat.csv")

print("Dataset shape:", df.shape)


# -------------------------
# Feature Engineering
# -------------------------

df["average"] = (df["G1"] + df["G2"] + df["G3"]) / 3
df["pass"] = (df["average"] >= 10).astype(int)


# -------------------------
# Encode categorical columns
# -------------------------

le = LabelEncoder()

categorical_cols = df.select_dtypes(include=["object","string"]).columns

for col in categorical_cols:
    df[col] = le.fit_transform(df[col])


# -------------------------
# Prepare data
# -------------------------

X = df.drop(["pass", "average"], axis=1)
y = df["pass"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# -------------------------
# Evaluate model
# -------------------------

pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print("\n==============================")
print("MODEL EVALUATION")
print("==============================")

print("\nAccuracy:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, pred))

print("\nClassification Report:")
print(classification_report(y_test, pred))