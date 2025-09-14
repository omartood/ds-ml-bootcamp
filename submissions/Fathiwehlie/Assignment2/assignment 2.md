
 # E-Learning and Internet Usage Study

 This dataset focuses on E-Learning and Internet Usage Patterns.
The data was collected through an **online survey**, in which participants were asked to provide information about their education level, primary device used, daily internet usage, hours spent on educational and other activities, and preferred learning methods.

### Purpose:
To explore patterns in users’ online behavior and learning habits without pre-defined labels. Clustering groups similar users based on these features, helping to identify Heavy, Moderate, and Casual learners.

**Features for Clustering (X)**

* Education Level

* Primary Device Used

* Daily Internet Usage

* Hours on Educational Activities

* Hours on Other Activities

* Learning Method Preference

**Label (y)**: None (unsupervised – no label)

**Why**:

The features capture users’ behavior and preferences, which clustering uses to group similar users such as:

* Heavy learners
* Moderate learners
* Casual learners

This helps understand user patterns without needing prior knowledge of “Useful” or “Not Useful.”


## Dataset Size

Rows (Feature): 41 samples

Columns (Label): 8

## Sample Table (5 rows)

| Timestamp          | Education Level | Primary Device | Daily Internet Usage | Main Purpose of Internet Use | Hours on Educational Activities | Hours on Other Activities | Learning Method Preference |
|-------------------|----------------|----------------|--------------------|-----------------------------|-------------------------------|--------------------------|---------------------------|
| 06/09/2025 12:16:18 | University     | Laptop         | 1–3 hours          | Work                        | 1–2 hour                      | 1–2 hour                 | Self-learning  |
| 06/09/2025 12:33:41 | High school    | Laptop         | 4–6 hours          | Education / Learning        | 3–4 hour                      | 1–2 hour                 | Self-learning |
| 06/09/2025 15:41:56 | University     | Laptop         | 1–3 hours          | Education / Learning        | 1–2 hour                      | 3–4 hour                 | Self-learning |
| 06/09/2025 15:47:02 | University     | Laptop         | 1–3 hours          | Education / Learning        | 3–4 hour                      | 1–2 hour                 | Self-learning  |
| 06/09/2025 15:52:43 | Graduate       | Smart Phone    | 4–6 hours          | Education / Learning        | 3–4 hour                      | 1–2 hour                 | Self-learning  |

# Quality Issues

* Missing values: Some fields, like hours spent online or learning method, are incomplete (e.g., 0 hours).

* Inconsistent formatting / Typos: Time formats differ (1–2 hour vs. 1–2 hours), and some learning method entries are incomplete.

* Feature imbalance: Some features, like hours on educational activities, may dominate the clustering, while others like device type or learning method may have less variation, affecting the grouping results.

# Use Case

This dataset is suitable for clustering in a machine learning project. By using features like daily internet usage, hours on educational and other activities, device type, and learning method, clustering algorithms can group users into patterns such as Heavy, Moderate, and Casual learners. This helps understand user behavior and learning habits without needing pre-defined labels.




