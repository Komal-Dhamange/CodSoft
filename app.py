import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load Dataset
df = pd.read_csv("Iris.csv")

print("Dataset Loaded Successfully!\n")

# Encode Species
encoder = LabelEncoder()
df["species"] = encoder.fit_transform(df["species"])

# Features and Target
X = df[[
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width"
]]

y = df["species"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("=" * 50)
print("Iris Flower Classification")
print("=" * 50)

print(f"\nAccuracy : {accuracy * 100:.2f}%\n")

print("Classification Report:\n")
print(classification_report(y_test, y_pred))

# Sample Prediction
sample = pd.DataFrame([{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}])

prediction = model.predict(sample)

flower = encoder.inverse_transform(prediction)

print("\nPredicted Flower Species:")
print(flower[0])