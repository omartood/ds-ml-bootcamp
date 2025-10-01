# Price Prediction Model

## Overview
This repository contains a machine learning project for predicting house prices using **Random Forest** and **Linear Regression** models. It includes:

- **Data preprocessing**
- **Model training**
- A **Flask backend server**
- A **Next.js frontend client** for making predictions

The goal is to provide an end-to-end solution for predicting house prices from input features.

---

## Features
- Predict house prices using:
  - **Linear Regression** (`lr`)  
  - **Random Forest** (`rf`)
- Preprocessing steps for cleaning and preparing datasets
- **Flask backend server** (`server.py`) with a REST API endpoint `/predict`
- **Next.js frontend** for a user-friendly interface
- Organized structure for datasets, models, notebooks, and dependencies

---

## Repository Structure
price-prediction/
│
├── client/ # Next.js frontend
├── dataset/ # Raw and processed datasets
├── models/ # Saved trained models
├── model.ipynb # Notebook for model training
├── preprocess.ipynb # Notebook for data preprocessing
├── server.py # Flask backend server for predictions
├── util.py # Utility functions
└── requirements.txt # Python dependencies

yaml
Copy code

---

## Installation

### Backend (Flask)
1. Clone the repository:
```bash
git clone https://github.com/maajid7ahmed/price-prediction.git
cd price-prediction
Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install Python dependencies:

bash
Copy code
pip install -r requirements.txt
Dependencies include:

Flask

pandas

scikit-learn

numpy

joblib

Run the Flask server:

bash
Copy code
python server.py
The server will run by default on http://localhost:8000.

Frontend (Next.js Client)
Navigate to the client folder:

bash
Copy code
cd client
Install dependencies:

bash
Copy code
npm install
# or
yarn
Create a .env.local file in the client folder with the backend URL:

env
Copy code
NEXT_PUBLIC_API_URL=http://localhost:8000
Start the Next.js development server:

bash
Copy code
npm run dev
# or
yarn dev
The client will run on http://localhost:3000 and make API calls to your Flask backend.

API Endpoint
/predict
Method: POST
Query Parameter: model=lr|rf (lr = Linear Regression, rf = Random Forest)

Expected JSON Body:

json
Copy code
{
  "Bathrooms": 2,
  "Bedrooms": 3,
  "Location": "City",      // options: City | Suburb | Rural
  "Size_sqft": 1500,
  "YearBuilt": 2010
}
Response Example:

json
Copy code
{
  "prediction": 350000
}
Message:

json
Copy code
{
  "message": "House Price Prediction API"
}
Usage
Backend (Flask)
preprocess.ipynb: Clean and preprocess your dataset

model.ipynb: Train models and save them in the models/ folder

server.py: Run the Flask server to handle /predict requests

Frontend (Next.js)
Access the web app via http://localhost:3000

Input features and get predicted house prices in real-time

Models
Linear Regression (lr): Simple and interpretable for linear relationships

Random Forest (rf): Handles non-linear relationships and generally gives higher accuracy

Dependencies
Backend (Flask):

Python 3.x

Flask

pandas

scikit-learn

numpy

joblib

Frontend (Next.js):

Node.js / npm

Next.js

React

Author
maajid7ahmed
GitHub: https://github.com/maajid7ahmed

License
MIT License
