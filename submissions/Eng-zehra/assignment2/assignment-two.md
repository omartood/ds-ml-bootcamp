## Research Paper: Pharmacy Location Suitability

### Title & Collection Method

**Title:** Pharmacy Location Suitability Dataset
**Collection Method:** I designed a questionnaire and asked 50 neighborhood friends on WhatsApp. Each friend provided answers about whether they regularly buy medicine, distance to the nearest pharmacy, their need for a nearby pharmacy, current pharmacy ratings, safety of the area, and whether they think it is suitable or not suitable for a new pharmacy.

---

### Description of Features & Labels

**Features (X):**

* **Buyer** (Yes / No)
* **Distance** (0–5, 6–15, 16–30, >30 minutes)
* **NeedPharm** (Yes / No)
* **Rating** (Excellent, Good, Average, Poor)
* **Safety** (Yes, No, Unsure)

**Label (Y):**

* **Suitability** (Suitable / Not Suitable)

---

### Dataset Structure

* **Rows:** 50 neighbors (sample size)
* **Columns:** 6 (5 features + 1 label)

| Buyer | Distance | NeedPharm | Rating | Safety | Suitability  |
| ----- | -------- | --------- | ------ | ------ | ------------ |
| Yes   | 6-15     | No        | Exc    | Yes    | Not Suitable |
| Yes   | 0-5      | Yes       | Exc    | Yes    | Suitable     |
| Yes   | 16-30    | Yes       | Avg    | Yes    | Suitable     |
| Yes   | 6-15     | Yes       | Avg    | Unsure | Not Suitable |
| Yes   | 16-30    | Yes       | Avg    | Yes    | Suitable     |
| No    | 0-5      | Yes       | Good   | Yes    | Suitable     |
| Yes   | >30      | Yes       | Poor   | No     | Not Suitable |
| Yes   | 0-5      | Yes       | Good   | Yes    | Suitable     |
| No    | 6-15     | Yes       | Exc    | Unsure | Not Suitable |
| Yes   | 0-5      | Yes       | Avg    | Yes    | Suitable     |
| Yes   | 16-30    | No        | Good   | Yes    | Not Suitable |
| No    | 0-5      | Yes       | Poor   | Yes    | Suitable     |
| Yes   | 6-15     | Yes       | Good   | No     | Not Suitable |
| Yes   | 0-5      | Yes       | Exc    | Yes    | Suitable     |
| Yes   | 0-5      | No        | Avg    | Yes    | Not Suitable |
| Yes   | 16-30    | Yes       | Poor   | Yes    | Suitable     |
| Yes   | 0-5      | Yes       | Good   | Yes    | Suitable     |
| No    | 6-15     | Yes       | Good   | Unsure | Not Suitable |
| Yes   | 0-5      | Yes       | Exc    | Yes    | Suitable     |
| Yes   | >30      | Yes       | Avg    | Yes    | Suitable     |
| Yes   | 0-5      | No        | Poor   | No     | Not Suitable |
| No    | 16-30    | Yes       | Good   | Yes    | Suitable     |
| Yes   | 0-5      | Yes       | Exc    | Yes    | Suitable     |
| Yes   | 6-15     | Yes       | Avg    | Unsure | Not Suitable |
| Yes   | 0-5      | Yes       | Good   | Yes    | Suitable     |
| No    | >30      | No        | Poor   | Yes    | Not Suitable |
| Yes   | 16-30    | Yes       | Good   | Yes    | Suitable     |
| Yes   | 0-5      | Yes       | Avg    | Yes    | Suitable     |
| No    | 6-15     | Yes       | Poor   | No     | Not Suitable |
| Yes   | 0-5      | Yes       | Exc    | Yes    | Suitable     |
| Yes   | 0-5      | Yes       | Good   | Yes    | Suitable     |
| Yes   | 16-30    | No        | Poor   | Unsure | Not Suitable |
| Yes   | 6-15     | Yes       | Good   | Yes    | Suitable     |
| Yes   | 0-5      | Yes       | Exc    | Yes    | Suitable     |
| No    | >30      | Yes       | Avg    | No     | Not Suitable |
| Yes   | 0-5      | Yes       | Good   | Yes    | Suitable     |
| Yes   | 16-30    | Yes       | Avg    | Yes    | Suitable     |
| Yes   | 6-15     | Yes       | Good   | Unsure | Not Suitable |
| Yes   | 0-5      | Yes       | Exc    | Yes    | Suitable     |
| No    | 0-5      | No        | Poor   | Yes    | Not Suitable |
| Yes   | 0-5      | Yes       | Avg    | Yes    | Suitable     |
| Yes   | 16-30    | Yes       | Good   | Yes    | Suitable     |
| Yes   | 6-15     | No        | Exc    | Yes    | Not Suitable |
| Yes   | >30      | Yes       | Good   | Yes    | Suitable     |
| Yes   | 0-5      | Yes       | Exc    | Yes    | Suitable     |
| No    | 6-15     | Yes       | Poor   | Unsure | Not Suitable |
| Yes   | 0-5      | Yes       | Good   | Yes    | Suitable     |
| Yes   | 16-30    | Yes       | Avg    | Yes    | Suitable     |
| Yes   | 0-5      | Yes       | Exc    | Yes    | Suitable     |
| Yes   | >30      | No        | Poor   | No     | Not Suitable |

---

### Quality Issues

* **Missing values:** Some neighbors skipped questions such as *Safety* or *Pharmacy Rating*.
* **Categorical text:** Buyer, Distance, NeedPharm, Rating, and Safety must be encoded for ML models.
* **Imbalance:** Most respondents answered *Yes* to NeedPharm (90.4%), while only a few answered *No* (9.6%) — leading to class imbalance.
* **Inconsistent reporting:** Some neighbors answered *Unsure* for Safety, which may need preprocessing.

---

### Use Case

This dataset can be used to train a classification model to predict whether a neighborhood location is **Suitable** or **Not Suitable** for opening a pharmacy.

* **Possible algorithms:** Logistic Regression, Decision Tree, Random Forest.
* **Practical Impact:** Helps pharmacy investors and urban planners identify the best locations to open new pharmacies, reduce competition in saturated areas, and improve accessibility for communities.
