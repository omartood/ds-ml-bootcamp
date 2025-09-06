# Answer

## 1. Definition of Machine Learning with a Real-Life Example

**Machine Learning (ML)** simply define computer learn data that store to make decisions.

**Real-life example:**  

- The car’s sensors.
- Healthcare Diagnosis .
- Voice Assistants.
---

## 2. Comparison of Supervised Learning and Unsupervised Learning

| Aspect                  | Supervised Learning                                  | Unsupervised Learning                              |
|-------------------------|----------------------------------------------------|--------------------------------------------------|
| **Definition**          | labeled data (input-output pairs).                  |  unlabeled data.             |
| **Example**            | have (x and y).                                      | only have x.       |
| **Example use case**    | Email spam detection (labeled emails: spam or not) | Customer segmentation for marketing without prior labels |

---

## 3. Overfitting: Causes and Prevention

**Overfitting**   memorization, not generalization → prevent with regularization, more data, simpler models.

### Causes of Overfitting
- Model too complex (too many parameters) relative to the amount of training data.  
- Training for too many iterations or epochs.  
- Insufficient or noisy training data.

### How to Prevent Overfitting
- Use simpler models or reduce model complexity.  
- Regularization (L1 or L2) to penalize complexity.  
- Early stopping when validation performance degrades.  
- Increase training data size.  
- Use cross-validation.  
- Dropout in neural networks.

---

## 4. Training Data and Test Data: Splitting and Importance

- **Training data:** Used to teach the model patterns.  
- **Test data:** Used to evaluate the model’s performance on unseen data.

### Why split data?
- To evaluate the model’s generalization to new data.  
- To prevent overfitting by not training and testing on the same data.

---


# Case Study: Machine Learning in Healthcare

## AI for Faster Coeliac Disease Diagnosis

### Overview
Researchers at the **University of Cambridge** developed an AI tool to **accelerate the diagnosis of coeliac disease**, a chronic autoimmune condition often underdiagnosed due to lengthy diagnostic processes.

---
### What Was Done
- Trained on **4,000+ biopsy images** from **five hospitals** using scanners from multiple manufacturers.  
- Compared with standard pathologist assessments.  
- Published in *NEJM AI (New England Journal of Medicine AI)*.

---

### Key Findings
- **Speed:** AI produced results in **under 1 minute**, compared to **5–10 minutes** by pathologists.  
- **Accuracy:** Performed at the **same level as trained specialists**.  
- **Patient Benefits:** Faster diagnosis → quicker treatment and reduced waiting times.  
- **System Benefits:** Helps reduce **NHS waiting lists** and pathologist workload.

---

### Considerations
- Requires investment in **digital pathology infrastructure**.  
- **Validation across diverse populations** still needed.  
- Training and IT integration are essential for adoption.

---

## Summary Table

| Aspect           | Details                                                                 |
|------------------|-------------------------------------------------------------------------|
| **Condition**    | Coeliac disease (autoimmune, gluten-triggered)                         |
| **ML Technique** | AI trained on biopsy images from multiple hospitals/scanners            |
| **Performance**  | Under 1 minute per case; accuracy comparable to pathologists            |
| **Benefits**     | Quicker treatment, reduced waiting times, decreased pathologist burden  |
| **Challenges**   | Requires digital systems, IT integration, workforce training            |

