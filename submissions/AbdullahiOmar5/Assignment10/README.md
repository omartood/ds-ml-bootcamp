# 📝 Project Overview – House Price Predictor

This project is a full-stack machine learning application designed to predict house prices based on user input. It features a modern **Next.js 15** frontend and a **Flask-based backend** that serves predictions using trained models.

---

## 🔍 Key Highlights

- **Frontend**: Built with Next.js and TypeScript, the UI allows users to input house details (size, bedrooms, bathrooms, location, year built) and select from three prediction models: Linear Regression, Random Forest, or Ensemble Average.
- **Backend**: Processes input data, applies preprocessing, and returns predictions using trained models stored in `backend/models/`.
- **Dataset**: Includes both raw (`house_dataset.csv`) and cleaned (`clean_house-dataset.csv`) versions for training and evaluation.
- **Models**: Trained using scikit-learn and stored as `.joblib` files, with a scaler and training column metadata for consistency.

---

## 📁 Structure Summary

- `client/`: Frontend app with responsive design and real-time validation.
- `backend/`: Python scripts for preprocessing, model training, and API serving.
- `dataset/`: Contains raw and cleaned data files.
- `models/`: Stores trained models and preprocessing artifacts.

---

## 🔗 GitHub Repository

[https://github.com/AbdullahiOmar5/house-price-predictor]
