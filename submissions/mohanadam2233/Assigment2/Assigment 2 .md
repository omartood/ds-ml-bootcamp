# Internet Connection Quality Dataset

## Title & Collection Method

**Title:** Internet Connection Quality Dataset  
**Collection Method:**  
I designed a survey questionnaire and collected responses from users about their internet performance. Each respondent provided answers about download speed, upload speed, ping, jitter, packet loss, and rated their overall internet quality.

---

## Description of Features & Labels

### Features (X)

1. **Download Speed (Mbps)** – numeric/categorical ranges  
2. **Upload Speed (Mbps)** – numeric/categorical ranges  
3. **Ping / Latency (ms)** – numeric/categorical ranges  
4. **Stability / Jitter (ms)** – categorical: Very Stable, Average, Unstable  
5. **Packet Loss (%)** – numeric/categorical ranges  

### Label (y)

- **Internet Quality** → Excellent / Good / Average / Poor  

> This makes the problem a **classification task** (predicting internet quality).

---

## Dataset Structure

- **Rows:** 50 users (samples)  
- **Columns:** 6 (5 features + 1 label)  

### Sample Table (10 rows)

| Download Speed       | Upload Speed       | Ping       | Jitter     | Packet Loss          | Internet Quality |
|--------------------|-----------------|-----------|-----------|-------------------|----------------|
| 5 – 20 Mbps (Average) | 1 – 5 Mbps (Average) | 30 – 60 ms (Good) | Average    | 0% (No loss)      | Average        |
| < 5 Mbps (Poor)       | 1 – 5 Mbps (Average) | 60 – 120 ms (Average) | Average | 1 – 2% (Rare loss) | Poor           |
| < 5 Mbps (Poor)       | < 1 Mbps (Poor)     | > 120 ms (Poor)     | Unstable  | 3 – 5% (Frequent loss) | Poor       |
| > 50 Mbps (Excellent) | > 10 Mbps (Excellent) | 30 – 60 ms (Good) | Very Stable | 0% (No loss)     | Excellent      |
| 20 – 50 Mbps (Good)   | 5 – 10 Mbps (Good)   | 60 – 120 ms (Average) | Average | 1 – 2% (Rare loss) | Good         |
| 5 – 20 Mbps (Average) | 1 – 5 Mbps (Average) | 30 – 60 ms (Good) | Average   | 1 – 2% (Rare loss) | Average       |
| < 5 Mbps (Poor)       | 5 – 10 Mbps (Good)   | 60 – 120 ms (Average) | Unstable | 1 – 2% (Rare loss) | Average      |
| > 50 Mbps (Excellent) | > 10 Mbps (Excellent) | < 30 ms (Excellent) | Very Stable | 0% (No loss)    | Excellent     |
| 5 – 20 Mbps (Average) | 1 – 5 Mbps (Average) | 30 – 60 ms (Good) | Average   | 1 – 2% (Rare loss) | Average       |
| 5 – 20 Mbps (Average) | 1 – 5 Mbps (Average) | 30 – 60 ms (Good) | Average   | > 5% (Severe loss) | Good         |

---

## Quality Issues

- **Missing values:** Some users could not measure jitter or packet loss.  
- **Categorical encoding:** Features reported in text (e.g., “5 – 20 Mbps”) must be converted to numeric values or categories for ML.  
- **Imbalance:** Most users rated internet as “Average” or “Good,” fewer as “Excellent” or “Poor.”  
- **Inconsistent reporting:** Some values may contain errors or extreme outliers.  

---

## Use Case

This dataset can be used to train a **classification model** to predict internet quality (Excellent/Good/Average/Poor) based on measurable features.

**Possible algorithms:** Logistic Regression, Decision Tree, Random Forest  

**Potential benefits:**  
- Telecom companies can monitor and improve network quality.  
- Users can evaluate whether they are getting the service they paid for.  
- Researchers can study the impact of features like Ping and Packet Loss on perceived quality.
