📝 Project Overview – Phishing Website Detection using Machine Learning 🎣

This project is a machine learning-powered API designed for real-time phishing website detection. It analyzes and classifies suspicious URLs using features such as URL structure, domain behavior, and embedded symbols to determine whether a site is legitimate or malicious.

🛠️ Core Technology

- **Machine Learning Model:** A trained Random Forest classifier predicts whether a given URL is phishing or safe, based on 20 selected features.
- **Flask-based Backend:** The application runs as a Flask RESTful API. It accepts a URL via POST request, extracts features, scales them, and returns a JSON response with the prediction and probability.
- **Data Pipeline:** Includes scripts for preprocessing, feature engineering, model training, and saving the pipeline for deployment.

🚀 Key Features

- **RESTful Prediction Endpoint:** Lightweight and fast, allowing external systems to submit URLs and receive instant phishing predictions.
- **Scalable Architecture:** Designed as a backend-only service, ideal for integration into browser extensions, security dashboards, or mobile apps.
- **No Frontend Dependency:** Pure API design ensures flexibility for microservice deployment and automation workflows.

## 🔗 GitHub Repository

[https://github.com/AbdullahiOmar5/Phishing-Detection-Project]
