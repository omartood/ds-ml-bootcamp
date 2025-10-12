# ⚽ Premier League Match Prediction Project


---

## 📌 Project Overview
The **Premier League Match Prediction Project** estimates whether a football match will end in a **Home Win**, **Draw**, or **Away Win** using key match statistics and team performance indicators.  
It demonstrates how **Machine Learning** can analyze football data to predict outcomes based on past performances and match metrics.

---

## ✨ Key Features
- **Backend:** Flask API processes input data and generates predictions using trained ML models.  
- **Frontend:** Next.js 15 + Tailwind CSS provide an interactive, modern UI for entering match details and displaying real-time results.  
- **Machine Learning Models:** Logistic Regression, Random Forest, and XGBoost trained on historical Premier League data to forecast results.

---

## 🧑‍💻 Input Features
The prediction model uses the following inputs:

- `HomeTeam` – Home team name  
- `AwayTeam` – Away team name  
- `HS / AS` – Shots by home and away teams  
- `HST / AST` – Shots on target by home and away teams  
- `HC / AC` – Corners by home and away teams  
- `H2H` – Head-to-head record between teams  
- `L5MatchWinHome / L5HLoss` – Last 5 match results for the home team  
- `L5AwayWin / L5AwayLoss` – Last 5 match results for the away team  
- `model` – ML algorithm to use (`lr`, `rf`, or `xgb`)

---

📝 Example Prediction Input
```json
{
  "HomeTeam": "Liverpool",
  "AwayTeam": "Chelsea",
  "HS": 18,
  "AS": 12,
  "HST": 7,
  "AST": 5,
  "HC": 10,
  "AC": 3,
  "H2H": "3-1-1",
  "L5MatchWinHome": 4,
  "L5HLoss": 1,
  "L5AwayWin": 2,
  "L5AwayLoss": 3,
  "model": "lr"
}
```

📊 Example Output
```
{
  "home": 62,
  "draw": 20,
  "away": 18,
  "best": "Home"
}

```
```
```
💻Frontend (Next.js + Tailwind CSS)
```
cd client
npm install
npm run dev
```
---
🛠 Tech Stack

• Frontend: Next.js, React, Tailwind CSS
• Backend: Flask (Python)
• Machine Learning: Scikit-learn, XGBoost, Pandas, NumPy

---

👨‍💻 About the Author
• Mubarik Caydiid Sugaal – Frontend Developer & ML
🌐 GitHub: {"github.com/MubaarigCaydiid"}
📧 Email: mubaarigcaydiid331@gmail.com
⚡ Project: Premier League Match Prediction
---
👍Thanks
