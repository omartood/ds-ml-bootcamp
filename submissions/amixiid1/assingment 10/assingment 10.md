# 🏡 House Price Prediction  

A full-stack machine learning project for predicting house prices.  
This project integrates **Flask (backend API)** and **Next.js/Bun (frontend)** to provide real-time house price predictions based on user inputs.  

## 🎯 Objective  
The goal of this project is to demonstrate model deployment using a modern workflow:  
- Train regression models on a house dataset  
- Build a Flask REST API for model inference  
- Develop a Next.js/Bun frontend for interaction  
- Integrate backend & frontend for real-time predictions  

## 🚀 Features  
- **Machine Learning Models**: Linear Regression & Random Forest  
- **Prediction Pipeline**: Feature engineering + trained models  
- **Flask API**: Serves predictions via REST endpoints  
- **Next.js/Bun Frontend**: User-friendly client for input & results  
- **Full Deployment**: Backend + frontend + models + dataset included  

## 📂 Project Structure  
```
house-price-prediction/
│── backend/              # Flask API code
│   ├── app.py            # Main API script
│   ├── models/           # Trained ML models
│   ├── requirements.txt  # Python dependencies
│   └── dataset/          # Cleaned dataset
│
│── frontend/             # Next.js + Bun app
│   ├── pages/            # Frontend pages
│   ├── components/       # Reusable UI components
│   └── package.json      # Dependencies
│
│── README.md             # Project documentation
```

## ⚙️ Installation & Setup  

### 1️⃣ Backend (Flask API)  
```bash
cd backend
pip install -r requirements.txt
python app.py
```
API will run on: **http://127.0.0.1:5000/**  

### 2️⃣ Frontend (Next.js with Bun)  
```bash
cd frontend
bun install
bun dev
```
Frontend will run on: **http://localhost:3000/**  

## 🔗 API Usage  
Send a POST request with house features to the Flask API:  

```bash
POST /predict
Content-Type: application/json

{
  "area": 2000,
  "bedrooms": 3,
  "bathrooms": 2,
  "location": "Downtown"
}
```

Response:  
```json
{
  "predicted_price": 250000
}
```

## 📦 Deployment & Access  
- Full code and dataset are available on GitHub:  
  [House Price Prediction Repository](https://github.com/amixiid1/house-price-prediction-ML)  
- Both backend & frontend can be run locally by following the steps above  
- Includes: source code, trained models, dataset, and documentation  

## 📝 Notes  
- Code is clean and modular following best practices  
- Each commit in GitHub has a clear message for traceability  
- Project README explains setup, usage, and licensing  

## 📜 License  
This project is licensed under the **MIT License** – free to use and modify