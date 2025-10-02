# Car Price Prediction – Final Project

This repository contains my completed **Car Price Prediction** machine learning project.
The project demonstrates end-to-end development of an ML system, from training to deployment.

## 📌 Project Overview

* **Problem:** Predicting used car prices based on features like Year, Odometer, Doors, Accidents, Location, and Car Model.
* **Dataset & Preprocessing:** Data cleaned, encoded categorical variables, scaled numeric features.
* **Models:** Linear Regression (LR) and Random Forest (RF).
* **Evaluation:** Compared metrics to select the best performing model.
* **Deployment:** Built a Flask API (`/predict`) and a frontend (Next.js) to test predictions.

## 🗂️ Repository Structure

```
Car-price-prediction-ML/
│── models/              # Trained models (joblib files)
│── app.py               # Flask API
│── utils.py             # Preprocessing utilities
│── model.py             # Training + evaluation code
│── requirements.txt     # Dependencies
│── project_paper.md     # Project paper (3–5 pages)
│── README.md            # Documentation
```

## 🚀 Running the Project

### 1. Clone the repo

```bash
git clone https://github.com/amixiid1/Car-price-prediction-ML.git
cd Car-price-prediction-ML
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask API

```bash
python app.py
```

API will be available at:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

Test endpoint:

```bash
POST /predict?model=rf
{
  "Year": 2018,
  "Odometer_km": 45000,
  "Doors": 4,
  "Accidents": 0,
  "Location": "City",
  "CarModel": "Toyota Corolla"
}
```

### 4. Frontend (Optional)

Frontend built with Next.js (see `src/app/page.tsx`) can call the API.

## 📑 Project Paper

Detailed documentation, including problem statement, dataset, models, results, and lessons learned is in:

* [`project_paper.md`](./project_paper.md)

## 🔗 GitHub Repository

[Car-price-prediction-ML – Full Project](https://github.com/amixiid1/Car-price-prediction-ML)

---

✅ **final project end.**
