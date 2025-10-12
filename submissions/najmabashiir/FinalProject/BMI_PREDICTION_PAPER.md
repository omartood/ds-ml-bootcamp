# BMI Prediction System Using Machine Learning

(https://github.com/najmabashiir/BMI_Prediction) --this is my github when you visit you see my full project

*A Comparative Study of Gradient Boosting and Random Forest Algorithms*

---

## Abstract

This paper presents a comprehensive BMI prediction system utilizing machine learning algorithms. We developed and compared two models—Gradient Boosting Regressor and Random Forest Regressor—achieving prediction accuracies of 99.79% and 99.34% respectively. The system includes a REST API backend built with Flask and a modern web interface using Next.js 15 and Tailwind CSS.

*Keywords:* BMI Prediction, Machine Learning, Gradient Boosting, Random Forest, Flask API, Next.js

---

## 1. Introduction

### 1.1 Background
Body Mass Index (BMI) is a critical health indicator used to assess body composition based on height and weight. Accurate BMI prediction can help healthcare professionals and individuals monitor health status and make informed decisions.

### 1.2 Objectives
- Develop accurate BMI prediction models using machine learning
- Compare performance of different algorithms
- Create accessible API and web interface
- Implement robust data preprocessing pipeline

---

## 2. Methodology

### 2.1 Dataset
- *Size:* 1,001 records after preprocessing
- *Features:* Height (cm), Weight (kg), Age, Gender
- *Target:* BMI value
- *Categories:* Underweight, Normal, Overweight, Obese

### 2.2 Data Preprocessing Pipeline

#### Step 1: Missing Values
- Checked all columns for null values
- No missing values detected in the dataset

#### Step 2: Duplicate Removal
- Identified and removed duplicate records
- Ensured data uniqueness

#### Step 3: Range Validation
Applied realistic constraints:
- *Height:* 130-230 cm
- *Weight:* 30-300 kg
- *Age:* 1-120 years
- *BMI:* 10-60
- *Gender:* Male/Female only

#### Step 4: BMI Calculation Verification
- Verified BMI formula: weight / (height/100)²
- Tolerance: ±0.5 BMI units
- Corrected inconsistencies

#### Step 5: Feature Encoding
- Gender encoded as binary (Male: 1, Female: 0)
- Preserved original data integrity

### 2.3 Models Implemented

#### Gradient Boosting Regressor
python
GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)


#### Random Forest Regressor
python
RandomForestRegressor(
    n_estimators=100,
    max_depth=20,
    min_samples_split=5,
    random_state=42
)


### 2.4 Training Configuration
- *Train/Test Split:* 80/20
- *Random State:* 42 (for reproducibility)
- *Cross-Validation:* Performed during development
- *Evaluation Metrics:* R², MAE, RMSE

---

## 3. Results

### 3.1 Model Performance

| Model | R² Score | MAE | RMSE | Accuracy |
|-------|----------|-----|------|----------|
| Gradient Boosting | 0.9979 | 0.0853 | 0.1290 | 99.79% |
| Random Forest | 0.9934 | 0.1534 | 0.2295 | 99.34% |

### 3.2 Key Findings
- *Gradient Boosting* achieved superior performance with 99.79% accuracy
- *Random Forest* provided excellent results with 99.34% accuracy
- Both models showed minimal prediction errors (MAE < 0.16)
- Low RMSE values indicate reliable predictions

### 3.3 Model Comparison
- *Gradient Boosting:* Better for high-precision requirements
- *Random Forest:* Faster training, good generalization
- *Difference:* ~0.45% accuracy gap
- *Recommendation:* Use Gradient Boosting for critical applications

---

## 4. System Architecture

### 4.1 Backend API (Flask)

*Endpoints:*
- GET / - Health check and model information
- POST /predict - Single BMI prediction
- POST /predict/batch - Batch predictions
- POST /predict/model - Model-specific prediction
- POST /predict/compare - Compare both models

*Features:*
- Input validation and error handling
- CORS support for cross-origin requests
- JSON request/response format
- Model serialization with pickle

### 4.2 Frontend (Next.js 15)

*Components:*
- Landing page with hero section
- BMI calculator interface
- Real-time API status monitoring
- Model comparison view
- Professional dark gradient theme

*Technologies:*
- React 18 with TypeScript
- Tailwind CSS for styling
- Responsive design
- Form validation

---

## 5. Usage Examples

### API Request
bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "height_cm": 170,
    "weight_kg": 70,
    "age": 25,
    "gender": "Male"
  }'


### API Response
json
{
  "success": true,
  "prediction": {
    "bmi": 24.22,
    "category": "Normal",
    "model_used": "gradient_boosting"
  },
  "input_data": {
    "height_cm": 170,
    "weight_kg": 70,
    "age": 25,
    "gender": "Male"
  }
}


---

## 6. Deployment

### Requirements

Python 3.8+
scikit-learn==1.3.0
pandas==2.0.3
flask==2.3.3
flask-cors==4.0.0
Node.js 18+
Next.js 15


### Quick Start
bash
# Backend
app.py

# Frontend
cd frontend
npm install
npm run dev


---

## 7. Conclusions

### 7.1 Achievements
- Developed highly accurate BMI prediction models (>99% accuracy)
- Implemented comprehensive data preprocessing
- Created production-ready API and web interface
- Enabled model comparison for informed decision-making

### 7.2 Future Work
- Integration with health monitoring systems
- Mobile application development
- Additional health metrics prediction
- Real-time data validation
- Model deployment on cloud platforms

### 7.3 Impact
This system demonstrates the effectiveness of machine learning in health assessment applications, providing accessible, accurate, and user-friendly BMI predictions for healthcare and personal use.

---

## References

1. *Scikit-learn Documentation* - Machine Learning in Python
2. *Flask Framework* - Python Web Development
3. *Next.js* - React Framework for Production
4. *BMI Standards* - WHO Guidelines

---

## Appendix

### A. File Structure

bmi/
├── app.py                          # Flask API
├── bmi_prediction_model.py         # Model training
├── train_random_forest_model.py    # RF training
├── bmi_model.pkl                   # Trained GB model
├── bmi_model_rf.pkl                # Trained RF model
├── gender_encoder.pkl              # Label encoder
├── bmi_data_cleaned_phase1.csv     # Dataset
├── requirements.txt                # Dependencies
├── README.md                       # Documentation
└── frontend/                       # Next.js app
    ├── app/
    │   ├── page.tsx               # Landing page
    │   └── calculator/page.tsx    # Calculator
    └── components/                # React components


### B. Model Parameters

*Gradient Boosting:*
- Estimators: 100
- Learning Rate: 0.1
- Max Depth: 5
- Subsample: 1.0

*Random Forest:*
- Estimators: 100
- Max Depth: 20
- Min Samples Split: 5
- Min Samples Leaf: 1

---

*Date:* October 2025  
*Version:* 1.0  
*License:* MIT