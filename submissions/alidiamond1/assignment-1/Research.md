# Research Assignment: Introduction to Machine Learning

## 1. Definition of Machine Learning

Machine Learning (ML) is a domain of artificial intelligence (AI) focused on building systems that can learn from data and improve their performance at a specific task without being explicitly reprogrammed for every new scenario. The system infers patterns and rules directly from examples.

**Real-Life Example: Predictive Text and Autocorrect**

The keyboard on a smartphone is a common example. It doesn't have a pre-written list of every word you might type next. Instead, an ML model has been trained on massive volumes of text data (e.g., books, articles, anonymized typing data). It learns the probability that certain words follow others. When you type "Good," the model calculates that "morning," "luck," and "job" have a high probability of being the next word based on its training. It also learns your personal frequently used words and adapts its predictions over time, all without a human programmer defining these rules manually.

## 2. Comparison: Supervised vs. Unsupervised Learning

| Feature | Supervised Learning | Unsupervised Learning |
|---------|-------------------|---------------------|
| **Input Data** | Labeled data. Each training example is paired with an output label. | Unlabeled data. The algorithm is given data without explicit instructions. |
| **Goal** | To learn a mapping from inputs to outputs to predict the label for new, unseen data. | To infer the natural structure or hidden patterns within the data. |
| **Process** | Similar to learning with a teacher who provides the correct answers. | Similar to independent learning without guidance; the algorithm must find structure on its own. |
| **Common Tasks** | Classification (discrete labels) and Regression (continuous values). | Clustering, Association, and Dimensionality Reduction. |
| **Example** | **Weather Prediction**: A model is trained on historical weather data (inputs: temperature, humidity, pressure) that is labeled with the outcome (e.g., 'Rain' or 'No Rain'). It learns the complex relationships between the input features and the outcome. It can then predict if it will rain tomorrow based on new sensor data. | **Market Basket Analysis**: A retailer analyzes point-of-sale transaction data. An unsupervised learning algorithm (like association rule learning) sifts through all transactions to discover items that are frequently bought together (e.g., 'customers who buy pasta and tomato sauce are 70% likely to also buy Parmesan cheese'). |

## 3. Causes and Prevention of Overfitting

### What Causes Overfitting?

Overfitting occurs when a model learns the noise and random fluctuations in the training data as if they were true underlying concepts. This results in a model that is overly complex and performs poorly on new data. Key causes include:

• **Excessively Complex Model**: Using a model with too much capacity for a simple problem.
• **Noisy Data**: Training data with irrelevant information or errors.
• **Inadequate Data Size**: Dataset too small to represent the population's variability.
• **Feature Overload**: Including too many irrelevant input features that enable spurious correlations.

### How Can it be Prevented?

• **Cross-Validation**: e.g., k-fold cross-validation for robust performance estimates.
• **Regularization (L1/L2)**: Penalize large weights to discourage complexity.
• **Dimensionality Reduction**: Techniques like PCA to remove noise and redundancy.
• **Early Stopping**: Stop training when validation performance stops improving.
• **Ensemble Methods**: Combine many simple models (e.g., Random Forests) to reduce variance.

## 4. Train/Test Split: Process and Necessity

### The Process:

• **Training Set**: Commonly 70–80% of the data; used to train the model.
• **Test Set**: Commonly 20–30% of the data; held out for final evaluation only.

### The Necessity:

The core goal of any ML model is to perform well on new, unseen data. The train/test split simulates this scenario. Evaluating on the same data used for training measures memorization rather than generalization; a separate test set acts as a proxy for future real-world data and helps detect overfitting.

## 5. Case Study: Machine Learning in Healthcare

### Case Study: AI-Powered Early Detection of Diabetic Retinopathy

Researchers developed an ML model that analyzes retinal images to detect early signs of diabetic retinopathy, a disease that can lead to blindness if untreated. The system was trained on tens of thousands of labeled images from multiple hospitals. Using deep convolutional neural networks (CNNs), the model learned to identify subtle features in the retina that are indicative of disease, which are often missed by human ophthalmologists in the early stages.

The model was tested on an independent dataset and achieved sensitivity and specificity rates exceeding 90%, outperforming traditional diagnostic methods. Hospitals integrating this system were able to screen patients faster and prioritize those needing urgent care, demonstrating the real-world impact of ML in improving healthcare outcomes (Gulshan et al., 2016).

## References

Murphy, K. P. (2012). *Machine Learning: A Probabilistic Perspective*. MIT Press.

Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O'Reilly Media.

Gulshan, V., Peng, L., Coram, M., et al. (2016). Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy in Retinal Fundus Photographs. *JAMA*, 316(22), 2402–2410.

Byanjankar, A., Heikkilä, M., & Mezei, J. (2015). Predicting credit risk in peer-to-peer lending: A neural network approach. *2015 IEEE Symposium Series on Computational Intelligence*.