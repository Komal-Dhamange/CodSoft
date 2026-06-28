# Iris Flower Classification

## Overview

The Iris Flower Classification project is a Machine Learning application that classifies iris flowers into different species based on their sepal and petal measurements.

Using the famous Iris dataset, the model learns patterns from flower characteristics and predicts the correct flower species with high accuracy.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Random Forest Classifier
* VS Code

---

## Features

* Data Loading and Preprocessing
* Label Encoding
* Feature Selection
* Train-Test Split
* Random Forest Model Training
* Species Prediction
* Accuracy Evaluation
* Classification Report Generation

---

## Dataset Information

The dataset contains the following features:

* sepal_length
* sepal_width
* petal_length
* petal_width
* species

Target Variable:

* Iris-setosa
* Iris-versicolor
* Iris-virginica

---

## Machine Learning Workflow

1. Load Dataset
2. Data Preprocessing
3. Encode Target Labels
4. Split Dataset into Training and Testing Sets
5. Train Random Forest Classifier
6. Predict Flower Species
7. Evaluate Model Performance
8. Generate Classification Report

---

## Model Performance

### Accuracy

**100.00% Accuracy**

### Classification Metrics

| Metric    | Value   |
| --------- | ------- |
| Accuracy  | 100.00% |
| Precision | 1.00    |
| Recall    | 1.00    |
| F1-Score  | 1.00    |

---

## Project Structure

```text
Iris_Flower_Classification/
│
├── Iris.csv
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Installation

```bash
pip install pandas numpy scikit-learn
```

---

## Run Project

```bash
python app.py
```

---

## Output

```text
Dataset Loaded Successfully!

==================================================
Iris Flower Classification
==================================================

Accuracy : 100.00%

Predicted Flower Species:
Iris-setosa
```

---

## Future Enhancements

* Hyperparameter Tuning
* Cross Validation
* Model Comparison
* Interactive Web Interface using Streamlit
* Real-Time Flower Classification

---

## Conclusion

This project demonstrates the implementation of Machine Learning for multi-class classification problems. Using the Random Forest Classifier, the model successfully classifies iris flowers into their respective species with 100% accuracy, making it an excellent example of supervised learning and predictive analytics.
