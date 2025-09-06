
Assignment 2 Name: Burhaan Cabdulahi Cabdiraxmaan  name Githup :{marcossbc} 
# 📊 Putland Market Product Prices Dataset

## 1. Title & Data Collection Method
**Title:** Putland Market Product Prices Dataset

**Collection Method:**  
This dataset was collected by recording prices of various products sold in Putland markets, specifically **Injida Market**.  
The data was gathered using *direct observation* and *manual recording*.

**Purpose:**  
The dataset aims to provide real-world data for **Machine Learning** tasks, related to food and household product prices used daily by customers.

---

## 2. Features & Labels Description
The dataset contains **6 features + Date**:

1. **Date** – The date when the data was collected.  
2. **Product** – Name of the product (Rice, Sugar, Milk, Bread, Oil, Meat, Chicken, Flour, Fish, Eggs).  
3. **Origin** – Source of the product: *Imported* or *Domestic*.  
4. **Unit Price ($)** – Price of the product in dollars.  
   - Note: **Sugar** price is fixed at $15 per standard unit.  
5. **Market Location** – Market where the price was recorded: *Injida Market*.  
6. **Availability** – Level of product availability: *High, Medium, Low*.  
7. **Category** – Type of product: *Foodgrain, Dairy, Meat, Bakery, Oil*.

**Label (y):**  
- *Unit Price ($)* can be used as the **target variable** for regression tasks.

---

## 3. Dataset Structure
- **Rows (records):** 50  
- **Columns (features):** 6 + Date  

### Example (10 rows):

| Product | Origin  | Unit Price ($) | Market Location | Availability | Category  |
| ------- | ------- | --------------- | --------------- | ------------ | --------- |
| Rice    | Imported | 15.85           | Injida          | High         | Foodgrain |
| Sugar   | Imported | 15.00           | Injida          | Medium       | Foodgrain |
| Milk    | Domestic | 12.50           | Injida          | High         | Dairy     |
| Bread   | Domestic | 4.20            | Injida          | High         | Bakery    |
| Oil     | Imported | 25.10           | Injida          | Medium       | Oil       |
| Meat    | Domestic | 32.00           | Injida          | High         | Meat      |
| Chicken | Imported | 40.00           | Injida          | Low          | Meat      |
| Flour   | Imported | 18.30           | Injida          | Medium       | Foodgrain |
| Fish    | Domestic | 27.50           | Injida          | Low          | Meat      |
| Eggs    | Domestic | 9.80            | Injida          | High         | Dairy     |

---

## 4. Data Challenges
The dataset has several real-world challenges:

- **Missing values:** Some rows may lack price or availability information.  
- **Duplicates:** Same products may appear multiple times with different prices.  
- **Typos / Inconsistent text:** Market names may be misspelled.  
- **Imbalance:** Availability is mostly *High*, while *Low* is rare.  
- **Special rule:** Sugar price is fixed at $15 per standard unit, unlike other products.

---

## 5. Machine Learning Use Cases

- **Regression:**  
  - Predict product prices based on origin, market, and availability.  
  - Example: Predicting next week’s Rice price.

- **Classification:**  
  - Predict Availability (High/Medium/Low) based on price and origin.  
  - Example: Determining if a product will be available or scarce in the market.

- **Clustering:**  
  - Group similar products or markets based on prices.  
  - Example: Comparing *Injida Market* with other markets to observe pricing patterns.
