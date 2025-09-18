# 📝 Reflection Paper: House Price Prediction Models

## 🚀 What Did I Implement?

In this project, I used two different machine learning models, **Linear Regression** and **Random Forest Regressor**, to predict house prices. I followed a clear set of steps: First, I loaded the dataset and then separated the input features (`x`), which included `Size_sqft`, `Bedrooms`, `Bathrooms`, and `YearBuilt`, from the output feature (`y`), which is `Price`. Next, I split the dataset into a training set for the models to learn from, and a testing set to evaluate their performance. After that, I built both models. I then evaluated the performance of both models using various metrics. Finally, I performed a single row prediction, also known as a sanity check, to compare the actual price with the predictions from both models.

---

## 📊 Comparison of Models

When I tested the models on the three sanity check houses from my dataset (at indixes 2, 3, and 4), their predictions differed significantly.

| Index | Actual Price | Linear Regression Predicted Price | Random Forest Predicted Price |
| :--- | :--- | :--- | :--- |
| 2 | \$292,500 | \$188,637 | \$290,899 |
| 3 | \$554,800 | \$594,041 | \$557,028 |
| 4 | \$535,300 | \$609,615 | \$538,756 |

The **Linear Regression** model's predictions were often **quite far from the actual price**. For example, on house number 2, it was off by over \$100,000, predicting a much lower price. In contrast, the **Random Forest** model was consistently **much more accurate**, with predictions that were very close to the actual prices. This shows that the **Random Forest** model gave more realistic results. Its ability to produce predictions so close to the actual price makes it a much more reliable model for this task.

---

## 🌳 Understanding Random Forest

A **Random Forest** is a more complex and powerful model than Linear Regression. To put it simply, it's not just one model; it's a team of many different "mini-models" called **decision trees**.

- **What is a Random Forest?** It's a type of machine learning model that is built using an "ensemble," or a collection of many individual decision trees.
- **How does it work?** Each decision tree in the forest makes its own prediction. The **Random Forest** model then takes all of these individual predictions and averages them to come up with one final, more accurate prediction. This method of using a "forest" of trees helps to smooth out any errors or weird predictions that a single tree might make on its own. It's a bit like getting a second opinion from many experts instead of just one.

---

## 📈 Discussion of Performance Metrics

To evaluate the models' overall performance, I also looked at several key metrics. The following table provides a comparison of their results:

| Metric | Linear Regression | Random Forest Regressor |
| :--- | :--- | :--- |
| R² Score | 0.85 | 0.86 |
| Mean Absolute Error (MAE) | \$63,086 | \$52,524 |
| Mean Squared Error (MSE) | 5,718,940,941 | 5,283,317,455 |
| Root Mean Squared Error (RMSE) | \$75,624 | \$72,686 |

The **R² score** for the **Random Forest** model was 0.86. This was slightly better than the **Linear Regression** model's score, which was 0.85. The **R² score** is a metric that shows how well a model's predictions align with the actual data. **A higher R² score is always preferable**, as it indicates a stronger fit for the data. Therefore, the **Random Forest** model was a slightly better overall fit for this task.

The error metrics, which measure **how "off" the predictions were**, also showed that **Random Forest** performed better. Its **Mean Absolute Error (MAE)** was 52,524, and its **Root Mean Squared Error (RMSE)** was 72,686, both lower than **Linear Regression's** **MAE** of 63,086 and **RMSE** of 75,624. **Lower error numbers are better**, which confirms that the **Random Forest** model made fewer and smaller mistakes.

---

## ✨ My Findings

Based on both the single sanity checks and the overall performance metrics, I prefer the **Random Forest** model for predicting price. While linear regression is a good starting point and is easier to understand, its predictions are not as accurate. The **Random Forest** model, with its ability to combine the opinions of many decision trees, proved to be more reliable and produced predictions that were much closer to the actual prices. This makes it a better choice for a task like house price prediction, where accuracy is crucial. This reflection shows my understanding of the project's outcomes and my reasoning for choosing the better-performing model.