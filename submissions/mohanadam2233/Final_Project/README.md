# Fake News Detection Project

The Fake News Detection Project identifies whether a piece of news is **real or fake** using advanced machine learning models. The project leverages **Natural Language Processing (NLP)** and machine learning algorithms to provide accurate predictions through a modern web interface.

---

## Key Features

* **Backend**: Flask API handles text preprocessing, feature extraction (TF-IDF), and model predictions.
* **Frontend**: React + Vite + Tailwind CSS provides a modern, responsive interface for news input and prediction results.
* **Machine Learning Models**: Naive Bayes, Logistic Regression, and Random Forest trained on cleaned news datasets.
* **Metrics**: Each model provides **predicted label**, **confidence**, **accuracy**, and **F1-score**.

---
```json
{
  "text": "This is a sample news text to check predictions...",
  "predictions": {
    "NaiveBayes": {
      "label": "Fake",
      "confidence": 0.93,
      "accuracy": 0.91,
      "f1_score": 0.90
    },
    "LogisticRegression": {
      "label": "Real",
      "confidence": 0.98,
      "accuracy": 0.98,
      "f1_score": 0.98
    },
    "RandomForest": {
      "label": "Fake",
      "confidence": 0.99,
      "accuracy": 0.99,
      "f1_score": 0.99
    }
  }
}
```
## GitHub Repository

Explore the full code here: https://github.com/mohanadam2233/Fake-news-detection

