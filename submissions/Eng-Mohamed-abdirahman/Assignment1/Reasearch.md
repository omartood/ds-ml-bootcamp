### <u>Assignment Day 1</u>

**Name**: Mohamed Abdirahman Mohamed

## Machine Learning

Machine learning (ML) is an important tool in the real world, offering countless solutions to problems across various fields, including **healthcare**, **financial services**, and **regulation**. Its importance lies in its ability to demonstrate effectiveness and knowledge by using data, statistics, and patterns to make better decisions, solve problems, and improve society.

Using ML can lead to increased productivity, improved security, updated marketing strategies, and the solution of social problems. As a result, the importance of ML continues to grow, helping us move toward a better and safer future.

---

## Difference between Supervised and Unsupervised Learning

The main difference between supervised and unsupervised learning is **how they use data** and their **goals**.

### Supervised Learning

**Supervised learning** relies on a **labeled dataset**, where each input is paired with a corresponding output label. The goal is to learn the relationship between the inputs and outputs so the model can predict outcomes for new, unseen data. An example is classifying emails as spam or not spam.

In supervised learning:

* A machine is given a dataset with input features (like age or salary) and corresponding labels (like "yes/no" or "high/low").
* The machine learns the dataset by finding patterns. For example, it might learn that a high temperature likely means a sunny day.
* Once trained, the machine can predict the label for new input data.

#### Analogies for Supervised Learning

1.  **A teacher guiding a student**: The teacher provides examples (labeled data) and explains the correct answers (output labels). If the child makes a mistake, the teacher corrects them, helping them improve over time. 

[Image of a teacher helping a student]

2.  **Sorting mail**: You are given labeled examples of different types of mail (e.g., "bill" or "ad"). By examining these, you learn patterns and can then sort new mail into the correct categories even without explicit labels.

### Unsupervised Learning

**Unsupervised learning** works with **unlabeled data**, aiming to uncover hidden patterns or structures within the dataset. Its goal is to group customers based on their shopping habits or detect anomalies in a dataset.

In unsupervised learning:

* The machine is given a dataset with only input features and **no labels**.
* The machine tries to find structure in the data, grouping similar data points together or identifying trends.
* The process provides insights, such as clusters of similar data or patterns that were not obvious before.

#### Analogies for Unsupervised Learning

1.  **Sorting books without labels**: You are given a box of books with no labels. You organize them by noticing similarities, such as some being mystery novels and others being textbooks, and then grouping them together. This reflects how unsupervised learning **clusters data based on similarities**. 
2.  **Exploring a new city**: You explore a new city without a map or guide and start grouping landmarks you see. Buildings with tall spires might be churches, and open spaces with greenery might be parks. You identify patterns and organize your observations independently, just like an unsupervised learning algorithm.

---

### Comparison Table: Supervised vs. Unsupervised Learning

| Aspect | Supervised Learning | Unsupervised Learning |
| :--- | :--- | :--- |
| **Input Data** | Uses **labeled data** (input features + corresponding outputs). | Uses **unlabeled data** (only input features, no outputs). |
| **Goal** | Predicts outcomes or classifies data based on **known labels**. | Discovers **hidden patterns**, structures, or groupings in data. |
| **Computational Complexity** | Less complex, as the model learns from labeled data with clear guidance. | More complex, as the model must find patterns without any guidance. |
| **Types** | **Classification** (for discrete outputs) or **regression** (for continuous outputs). | **Clustering** and **association**. |
| **Testing the Model** | Can be tested and evaluated using **labeled test data**. | Cannot be tested in the traditional sense, as there are **no labels**. |

---

## Overfitting in Machine Learning

You can only get accurate predictions if the machine learning model **generalizes** to all types of data within its domain. **Overfitting** occurs when a model fits too closely to its training data and cannot generalize to new data.

### Why Overfitting Occurs

Overfitting happens for several reasons:

* The training dataset is **too small** and doesn't accurately represent all possible input values.
* The training data contains a large amount of irrelevant information, known as **noisy data**.
* The model **trains for too long** on a single sample set of data.
* The model has a **high complexity**, so it learns the noise within the training data instead of the underlying patterns.

### How to Detect Overfitting

The best way to detect overfitting is to test the model on more data that represents all possible input values and types. A **high error rate** on the testing data indicates overfitting.

#### K-Fold Cross-Validation

One common method for testing for overfitting is **K-fold cross-validation**. In this method, data scientists divide the training set into **K equally sized subsets** called **folds**. The training process consists of a series of iterations, where during each iteration, a different fold is used as the **validation data**, and the model is trained on the remaining **K-1 subsets**. The model's performance is then observed and scored on the validation sample.

### Splitting Data

Splitting a dataset into training and test sets is crucial for preventing overfitting. This process, often done by a simple random split, ensures that the model is evaluated on data it has never seen, providing an **unbiased measure of its performance**.

* A common split is **80% for training** and **20% for testing**, though this can vary.
* The most common method for splitting is the **holdout method**, which divides the dataset into a **training set**, a **test set**, and an optional **validation set**. 

The primary reason for splitting data is to prevent **overfitting**, which makes a model perform exceptionally well on training data but poorly on new data. By testing on a separate, unseen test set, you can get a more realistic and unbiased assessment of the model's performance, which simulates how it would perform in the real world.

---

## Machine Learning in Healthcare

The healthcare industry uses ML to help medical professionals care for patients and manage clinical data. The ability of ML to **improve decision-making** and **reduce risks** in the medical field is a significant advantage.

According to the International Data Corporation (IDC), the future value of the AI market is expected to triple between 2025 and 2030, leading to an increasing number of jobs for those with ML skills. Building on the basics of ML can lead to innovative solutions and diverse career paths in healthcare.

### Real-Life Examples of ML in Healthcare

* **Disease Diagnosis and Risk Prediction**: AI and ML can analyze patient data and X-rays to **predict the chances of a patient developing a disease**, enabling doctors to identify diseases at early stages. 
* **Medical Imaging Analysis**: ML can be applied to analyze medical images like X-rays and mammograms to **identify tumors**, making diagnostic interventions more accurate and efficient than conventional techniques.
* **Drug Discovery and Development**: AI can analyze large populations of data to **identify potential drug candidates**, which helps accelerate the development of necessary drugs.
* **Virtual Assistants and Chatbots**: These tools can answer patient questions, book appointments, and offer preliminary medical guidance, thus **relieving healthcare practitioners** of some of their duties.