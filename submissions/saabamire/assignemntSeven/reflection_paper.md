# Reflection Paper -- Spam Detection Models

## What I Implemented

In this project, I used three machine learning models to check if an
email is **spam** or **ham (not spam)**.
The models are:
- Logistic Regression 
- Random Forest
- Naive Bayes (MultinomialNB)

I first cleaned the email text and changed it into numbers using TF-IDF.
Then I trained each model and tested them to see how well they can
detect spam.

------------------------------------------------------------------------

## Comparison of Models

I also tested with three example messages (spam-like, normal, and
mixed).
- Logistic Regression sometimes missed spam emails.
- Naive Bayes did better, but it still missed some spam.
- Random Forest worked the best and gave the most correct answers.

So, not all models agreed, but **Random Forest gave the most realistic
predictions**.

------------------------------------------------------------------------

## Understanding Naive Bayes

Naive Bayes is a simple model that uses **probability** to guess if a
message is spam or not.
It assumes each word in the email is independent, even if that is not
always true.

-   **Why used in spam detection?** Because spam words like *"free"*,
    *"win"*, and *"offer"* appear more often in spam than normal emails.
    Naive Bayes can easily catch this.
-   **Advantages:** Easy, fast, works well for text, and does not need a
    lot of training data.
-   **Limitations:** The independence assumption is not always correct,
    so it can make mistakes.

------------------------------------------------------------------------

## Metrics Discussion

-   **Accuracy**: Logistic Regression (0.97), Random Forest (0.98),
    Naive Bayes (0.98)
-   **Precision**: All three are 1.00 (no ham marked as spam).
-   **Recall**: Logistic Regression (0.76), Random Forest (0.87), Naive
    Bayes (0.83).
-   **F1-Score**: Logistic Regression (0.86), Random Forest (0.93),
    Naive Bayes (0.90).

**Confusion Matrix meaning:**
- False Positive = Ham marked as Spam. (All models had 0 → very good).
- False Negative = Spam marked as Ham. Logistic Regression had the most
mistakes (36). Random Forest had the least mistakes (19).

------------------------------------------------------------------------

## Findings

From my tests, **Random Forest is the best model**.
- It has high recall, high F1-score, and no false positives.
- It finds more spam compared to the other two models.

Naive Bayes is still good, simple, and fast. Logistic Regression worked,
but it missed too many spam emails.

**Recommendation:** I would recommend **Random Forest** for spam
detection because it is the most balanced and reliable.
