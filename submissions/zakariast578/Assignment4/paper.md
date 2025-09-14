

## **Assignment Four Theory Questions**

### **1\. Introduction to Regression**

**Regression** in machine learning is a type of supervised learning used to predict a continuous numerical value. The goal is to find the relationship between an independent variable (or variables) and a dependent variable, allowing us to predict future outcomes based on that relationship.

**difference between regression and classification** is the type of output they produce. **Regression** predicts a **continuous, numerical value**, like a price or temperature. **Classification**, on the other hand, predicts a **discrete, categorical label**, such as "spam" or "not spam."

* **Regression Example**: Predicting the **price of a house** based on its size, location, and number of bedrooms.  
* **Classification Example**: Determining if an email is **spam or not spam** based on its content and sender.

---

### **2\. Types of Regression**

### **Linear Regression**

**How it works**: Linear regression finds the best-fit straight line that represents the relationship between a single independent variable (x) and a dependent variable (y). The model's equation is y=mx+b, where m is the slope and b is the y-intercept.

* **Use Case**: Predicting a person's **weight** based on their height.  
* **Advantages**: It's **simple and highly interpretable**. It's easy to understand how each input variable affects the output.  
* **Limitations**: It assumes a **linear relationship** between variables, which isn't always true in real-world data. It can't capture complex, non-linear patterns.

### **Multiple Linear Regression**

**How it works**: This is an extension of linear regression that models the relationship between **multiple independent variables** and a single dependent variable.

**Use Case**: Predicting the **sales of a product** based on advertising spending, time of year, and competitor prices.

* **Advantages**: It's still **interpretable** and can handle multiple predictors at once, making it more flexible than simple linear regression.  
* **Limitations**: It still assumes a **linear relationship** between the independent variables and the dependent variable. It can be sensitive to multicollinearity, where independent variables are highly correlated with each other.

### **Polynomial Regression**

**How it works**: Polynomial regression models the relationship between variables as an **n-th degree polynomial**. It fits a curved line to the data, which can capture more complex, non-linear relationships. 

**Use Case**: Predicting the **path of a projectile** over time, as its trajectory is a parabolic curve.

* **Advantages**: It can model **non-linear relationships** very effectively, providing a much better fit for certain types of data.  
* **Limitations**: It can be prone to **overfitting**, especially with a high-degree polynomial, as it may fit the noise in the data rather than the underlying pattern. The model becomes less interpretable as the polynomial degree increases.

---

### **3\. Regression Metrics**

| Metric | Definition | Units | Sensitivity to Large Errors | Meaning |
| :---- | :---- | :---- | :---- | :---- |
| **MAE** | The **Mean Absolute Error** is the average of the absolute differences between the predicted and actual values. | Same as the dependent variable | Less sensitive | Measures the average magnitude of the errors without considering their direction. |
| **MSE** | The **Mean Squared Error** is the average of the squared differences between the predicted and actual values. | Squared units of the dependent variable | Highly sensitive | Penalizes larger errors more heavily, as the errors are squared. |
| **RMSE** | The **Root Mean Squared Error** is the square root of the MSE. | Same as the dependent variable | Highly sensitive | Like MSE, it penalizes larger errors. Its advantage is that its units are the same as the original target variable, making it easier to interpret. |
| **R²** | The **Coefficient of Determination** is a value between 0 and 1 that indicates the proportion of the variance in the dependent variable that can be predicted from the independent variable(s). | Unitless | Not applicable | A value of 1 indicates a perfect fit, while 0 means the model explains none of the variance. It shows how well the model fits the data. |

---

### **4\. Underfitting and Overfitting**

**Underfitting** occurs when a model is **too simple** to capture the underlying patterns in the data. The model has high bias and low variance, and it performs poorly on both the training data and new, unseen data. It essentially fails to learn the relationships between the variables.

**Overfitting** occurs when a model is **too complex** and learns the noise and random fluctuations in the training data, rather than the true underlying relationship. This results in a model with very low training error but high test error. It performs exceptionally well on the data it was trained on but fails to generalize to new data.

**Causes of overfitting**, especially in **polynomial regression**, include using a **high-degree polynomial**. A higher degree allows the model to create a highly complex, "wiggly" curve that perfectly fits every data point, including the noise. While this seems good for the training data, it means the model is memorizing the specific points instead of learning the general trend.

**Methods to prevent overfitting**:

* **Cross-validation**: This technique divides the data into multiple subsets. The model is trained on some subsets and validated on others. This helps to check if the model generalizes well to different parts of the data, and it's a good way to find the right level of complexity.  
* **Regularization**: This method adds a penalty to the model's loss function for having large coefficients. It discourages the model from becoming too complex and helps to shrink the coefficients, reducing the model's sensitivity to noise. Common types are **Lasso (L1)** and **Ridge (L2)** regularization.  
* **Feature Selection**: Removing irrelevant or redundant features can simplify the model and reduce the chance of overfitting. A simpler model is less likely to memorize noise.

---

### 

### **5\. Real-World Case Study**

#### **Project: Predicting Diabetes Progression**

* **Goal**: The primary goal of this project was to **forecast the progression of diabetes** in patients over a one-year period. By using clinical data, the model aimed to provide a quantitative measure of how the disease might advance, helping healthcare providers identify and prioritize patients who are at a higher risk of rapid progression.  
* **Data Used**: The study utilized the **Diabetes Dataset from scikit-learn**, a well-known benchmark dataset in machine learning.1 This dataset includes measurements for 442 patients, each with 10 key features:2  
  * Age  
  * Body Mass Index (BMI)  
  * Blood Pressure  
  * Various blood serum measurements (e.g., blood sugar levels)  
* **Regression Model Applied**: The researchers applied a **Multiple Linear Regression** model to the dataset. This model was chosen to analyze the relationship between the 10 independent variables (the clinical features) and the single dependent variable, which was the measure of disease progression one year after the baseline. The model found a linear equation that best fit the data, indicating how each factor contributed to the overall progression score.  
* **Key Results**: The model provided crucial insights into which factors had the **strongest effect on diabetes progression**. The analysis showed that **Body Mass Index (BMI)** and **blood sugar levels** were among the most significant predictors. This information is invaluable for clinical practice, as it helps healthcare providers understand the key risk factors and allows them to design more targeted interventions and preventative strategies for high-risk patients. The model served as a tool for a data-driven approach to patient care and risk assessment.


**References**

  1.Madhubala, V., Porkodi, P., Selvapriya, R., & Tamilzhchelvi, P. (2019). Diabetics Prediction Based on Multi-Linear Regression Using R Language. *Asian Journal of Computer Science and Technology*, *8*(S2), 17–19. [https://doi.org/10.51983/ajcst-2019.8.S2.2033](https://doi.org/10.51983/ajcst-2019.8.S2.2033)

