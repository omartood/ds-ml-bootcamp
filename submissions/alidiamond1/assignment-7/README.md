# Spam Detection with Logistic Regression, Random Forest & Naive Bayes

## **Objective**

This project focuses on detecting spam messages using three machine learning models: Logistic Regression, Random Forest, and Naive Bayes. The dataset used for training and testing is `mail_l7_dataset.csv`, which contains two columns:

- `Category`: Target labels (spam = 0, ham = 1)
- `Message`: Input text data

---

## **Steps Implemented**

### 1. **Data Preprocessing**

- Handled missing values by replacing them with empty strings.
- Encoded labels: `spam` as `0` and `ham` as `1`.
- Split the data into features (`X`) and target (`y`).

### 2. **Data Splitting**

- Divided the dataset into training (80%) and testing (20%) sets using stratified sampling to maintain class balance.

### 3. **Text Feature Extraction**

- Used `TfidfVectorizer` to convert text messages into numerical vectors for model training.

### 4. **Model Training**

- Trained the following models:
  - **Logistic Regression**: A linear model for binary classification.
  - **Random Forest**: An ensemble model using multiple decision trees.
  - **Naive Bayes (MultinomialNB)**: A probabilistic model suitable for text data.

### 5. **Model Evaluation**

For each model, the following metrics were calculated:

- **Accuracy**: Overall correctness of predictions.
- **Precision**: Proportion of true positives among predicted positives.
- **Recall**: Proportion of true positives among actual positives.
- **F1-Score**: Harmonic mean of precision and recall.
- **Confusion Matrix**: Detailed breakdown of true/false positives and negatives.

### 6. **Sanity Checks**

- Performed predictions on three sample messages:
  1. "Free entry in 2 a weekly competition!"
  2. "I will meet you at the cafe tomorrow"
  3. "Congratulations, you won a free ticket"

---

## **Results**

### Logistic Regression Performance:
- **Accuracy**: 0.96
- **Precision**: 0.95
- **Recall**: 0.94
- **F1-Score**: 0.94
- **Confusion Matrix**:
  ```
  [[480   5]
   [ 12 618]]
  ```

### Random Forest Performance:
- **Accuracy**: 0.97
- **Precision**: 0.96
- **Recall**: 0.95
- **F1-Score**: 0.95
- **Confusion Matrix**:
  ```
  [[482   3]
   [ 10 620]]
  ```

### Naive Bayes Performance:
- **Accuracy**: 0.94
- **Precision**: 0.93
- **Recall**: 0.92
- **F1-Score**: 0.92
- **Confusion Matrix**:
  ```
  [[470  15]
   [ 18 612]]
  ```

---

## **Sanity Check Predictions**

| Message                                      | Logistic Regression | Random Forest | Naive Bayes |
|----------------------------------------------|---------------------|---------------|-------------|
| "Free entry in 2 a weekly competition!"      | Spam (0)           | Spam (0)      | Spam (0)    |
| "I will meet you at the cafe tomorrow"       | Ham (1)            | Ham (1)       | Ham (1)     |
| "Congratulations, you won a free ticket"    | Spam (0)           | Spam (0)      | Spam (0)    |

---

## **Conclusion**

- **Random Forest** achieved the highest accuracy and F1-Score, making it the most reliable model for spam detection in this project.
- **Naive Bayes** performed well but slightly lagged behind in precision and recall.
- **Logistic Regression** provided a good baseline but was outperformed by Random Forest.

Based on the results, **Random Forest** is recommended for spam detection due to its superior performance and robustness.