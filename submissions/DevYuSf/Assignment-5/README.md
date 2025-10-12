# Assignment 5

**1 What did you implement?**
I implement House prediction model that uses Linear Regression also Random Forest Prediction
I used cleaned house dataset where house price is the target and all other are features except (LogPrice)
**Steps** I took to build this model are:

- collecting the data but this dataset is already give me my teacher
- then cleaning the data
- then processing the data
- then made choose of what type will be my Model
- finaly I choosed and build this Regression model since I want to predict continues values not category
**2 Comparison of Models:**
***Test one***
Single raw 19 Sanity check:
- Actual Price $555,100
- LR Prediction $537,056
- RF Prediction $545,878
***Test two***
Single raw 14 Sanity check
- Actual Price $761,700
- LR Prediction $679,904
- RF Prediction $711,626

***Test three***
Single raw 11 Sanity check

- Actual Price $571,000
- LR Prediction $486,276
- RF Prediction $551,531

As you see Ramdom forest give a closer price to the original one but the Linear Regression doesn't.
This caused by Random Forest could capture non-linear patterns, while Linear Regression tries to fit one straight line to all data.

**3 Understanding Random Forest:**
Random Forest is a supervised machine learning used for classification and regression Tasks also it's called ensemble model because of making predictions from many indivitual decision tree to produce one result for the final.
How Random Forest is working?.
Random Forest is an algorithm creates multiple random subsets of the training data by sampling with replacement which each subset is used to train one decision tree which means each tree sees a splightly different iew view of the data also it makes random choose I mean when splitting a node inside a tree, a model doesn't use all features instead it picks a random subset of the features to consider at each split this makes trees less corrected with each other, all in all Random Forest is takes average of all tree predictions.

**4 Metrics Discussion:**

| Model                      | R²    | MAE    | MSE           | RMSE   |
| -------------------------- | ----- | ------ | ------------- | ------ |
| **Linear Regression (LR)** | 0.848 | 63,086 | 5,718,940,941 | 75,624 |
| **Random Forest (RF)**     | 0.859 | 52,524 | 5,283,317,455 | 72,686 |

as you see these models output:

- R²
  - RF: 0.859
  - LR: 0.848
    >so this means Random Forest is better than Linear Regression
    >because RF is higher than LR
    >for R² higher is better
- MAE (Mean Absolute Error)

  - RF: 52,524
  - LR: 63,086
    >so this means Random Forest is better than Linear Regression
    >because RF is lower than LR
    > for MAE lower is better
- RMSE (Root Mean Squared Error)
  - RF = 72,686
  - LR = 75,624
    >so this means Random Forest is better than Linear Regression
    >because RF is lower than LR
    > for RMSE lower is better
so as you see this information Random Forest is alway better than Linear Regression
The weakness of LR is to Struggles to capture non-linear but it's good at Simple, fast, and easy to interpret.
The weakness of RF is more computationally expensive and harder to interpret but it's good at Can capture complex, non-linear relationships and interactions between features very well.

**Summery**
In my opion I prefer to use Random Forest because it gives more accurate prediction for this house price.
Linear Regression is  simple and fast but it's not seutable for this time because this time I need more complex predictions and Random Forest is good at this one. That's it.
Thanks.
