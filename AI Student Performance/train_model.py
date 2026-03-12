import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score


print("Loading dataset...")

df = pd.read_csv("Dataset/student-mat.csv")

# ------------------------
# Feature Engineering
# ------------------------

df["average"] = (df["G1"] + df["G2"] + df["G3"]) / 3
df["pass"] = (df["average"] >= 10).astype(int)

# ------------------------
# เลือก feature ที่ใช้จริง
# ------------------------

features = [
    "age",
    "studytime",
    "failures",
    "absences",
    "G1",
    "G2",
    "G3"
]

X = df[features]
y = df["pass"]

# ------------------------
# Split dataset
# ------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ------------------------
# Models
# ------------------------

rf = RandomForestClassifier(n_estimators=200, random_state=42)
gb = GradientBoostingClassifier(random_state=42)

ensemble = VotingClassifier(
    estimators=[
        ("rf", rf),
        ("gb", gb)
    ],
    voting="hard"
)

print("Training model...")

ensemble.fit(X_train, y_train)

# ------------------------
# Evaluate
# ------------------------

pred = ensemble.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print("Accuracy:", accuracy)

# ------------------------
# Save model
# ------------------------

joblib.dump(ensemble, "student_model.pkl")

print("Model saved as student_model.pkl")