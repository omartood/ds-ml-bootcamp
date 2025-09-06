Definition:
1: Machine Learning is a way of teaching computers to learn from data and make decisions without being explicitly programmed.

Examples:

1. Social Media: TikTok or Facebook learns what videos you like and shows you similar ones.


2. Healthcare: A computer analyzes X-ray images to predict if a patient has a disease.


3. Banking/Mobile Money: EVC/Zaad/Sahal systems detect unusual transactions and protect you from fraud.



👉 In short, Machine Learning = computers learning patterns from data to make smart decisions.







2: Supervised Learning vs Unsupervised Learning

🔹 Supervised Learning

The model is trained using data + correct answers (labels).

Goal: Learn the relationship between input and output.

Example: Training a model with pictures of animals where you tell it “this is a dog” and “this is a cat.” Later, it can correctly classify a new picture as a dog or a cat.


🔹 Unsupervised Learning

The model is given only data, no labels.

Goal: The model finds hidden patterns or groups in the data on its own.

Example: Feeding customer purchase data into the model, and it automatically groups customers into “budget buyers” and “premium buyers” without being told.


👉 Key Difference:

Supervised → Data + Labels

Unsupervised → Data only, no Labels


3: What is Overfitting?

When a model memorizes the training data (even its noise and mistakes), so it performs poorly on new data.

Causes:

● Model too complex

● Too little training data

● Training for too long

● Noisy data


Prevention:

● Use more data

● Simplify the model

● Apply regularization (L1, L2, Dropout)

● Use cross-validation

Early stopping


👉 In short: Overfitting = memorizing training data only. Prevention = more data + simpler model + regularization techniques.


4: How training and test data are split:

● Training data: Usually 70–80% of the dataset. It is used for the model to learn patterns.

● Test data: Usually 20–30% of the dataset. It is kept separate to evaluate the model on new, unseen data.

● Sometimes, a validation set (e.g., 10–15%) is also used to fine-tune the model.


Why this is necessary:

Ensures the model generalizes well and doesn’t just memorize the training data (avoids overfitting).

Shows how the model performs on real-world, unseen data before deployment.


Summary:

● Training = learn

● Test = evaluate


5: Definition:
Machine Learning (ML) = Computers learning from patient data to make predictions and decisions without explicit programming.

Applications in Healthcare:

1. Disease Diagnosis & Prediction:

Detects cancer, predicts diabetes, heart disease.



2. Personalized Treatment:

Tailors treatments based on patient data (genetics, history).



3. Medical Imaging:

Analyzes X-rays, MRIs, segments tumors automatically.



4. Equipment Maintenance:

Predicts when medical devices need service to prevent failure.



5. Operational Efficiency:

Optimizes appointment scheduling, inventory, and patient flow.




Key Takeaway:
ML improves diagnosis, treatment, imaging, equipment reliability, and hospital operations, making healthcare more accurate and efficient.