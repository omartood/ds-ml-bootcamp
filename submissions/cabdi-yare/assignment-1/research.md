# Introduction

## 1 What is Machine Learning?

Machine learning is a sub-domain of artificial intelligence (AI). The goal of machine learning is usually to understand the structure of the data and to match that data to models that can be understood and used by humans.

While artificial intelligence and machine learning are often used together, they are two different concepts. AI is a broad concept—decision-making machines, learning new skills, and problem-solving in the same way for people. Machine learning is a subset of AI that enables intelligent systems to independently learn new things from the data.

### Real-life example of machine learning

*Self-Driving Automobiles:* One of the most advanced applications of machine learning is autonomous driving. The vehicle's system gathers a great deal of information about its environment using a range of sensors, including lidar, radar, and cameras. To identify things like pedestrians, other vehicles, traffic lights, and road signs, a machine learning model analyses this data in real time. To learn how to respond to various situations, like when to brake, accelerate, or turn, the model is trained on endless hours of driving data all without the need for human input.

## 2 Compare Supervised Learning and Unsupervised Learning, giving an example of each

### Supervised Learning

Supervised learning algorithms are designed to learn by example. It is called supervised learning because the process of an algorithm learning from the training dataset can be thought of as a teacher supervising the learning process. In supervised learning, the data consists of an input variable and an output variable, or the dataset is labeled. Labeled data means the input data and its associated output are available in the dataset.

During the training process, the algorithm searches for the patterns in the input data and correlates with the desired output data. After the training process, a supervised learning algorithm will take the unseen data as inputs and will determine which label the new inputs will be classified as based on prior training data. The objective of a supervised learning model is to predict the correct label for the newly presented input data.

There are two main parts of Supervised Learning:

*   *Regression:* Algorithms are used if there is a relationship between the input variable and the output variable. It is used when the value of the output variable is continuous or real.
*   *Classification:* Is the process of grouping the output into different classes based on one or more input variables. Classification is used when the value of the output variable is discrete or categorical.

*Example of Regression:*

*House Price Prediction:*

A real estate company wants to predict the sale price of a new house. They can use supervised learning for this task. The algorithm would be trained on a dataset of houses that have already been sold. Each data point would consist of various features about the house, such as:

*   Square footage
*   Number of bedrooms
*   Location
*   Year built

Crucially, each of these data points is labeled with the actual sale price. The algorithm learns the relationship between the features and the price. Once trained, the model can be given the features of a new, unseen house and it can predict its selling price. This type of supervised learning, where the output is a continuous numerical value, is called regression.

### Unsupervised Learning

Unsupervised learning deals with unlabeled data, meaning it has input data but no corresponding output variable. It is further classified into Clustering and Association.

*   *Clustering:* is used to find the hidden structure or pattern in uncategorized data. The algorithm processes the data and divides it into different clusters (groups) based on similarities.
*   *Association:* is used to find relationships between data in a large dataset. It determines sets of items that occur together.
*   *Reinforcement Learning:* This is feedback-based machine learning. In reinforcement learning, a machine or agent automatically learns from feedback without any labeled data. The agent learns from its own experience.

*Example of Unsupervised Learning*

*Customer Segmentation:*

Customer segmentation is a common application of unsupervised learning. A retail company may have a massive dataset of customer information, including demographics and purchasing history, but without any pre-defined groups. The unsupervised learning algorithm can analyze this unlabeled data and cluster customers into distinct groups based on similar behaviors or traits. For instance, it might identify a group of "high-spenders" who frequently buy luxury goods and another group of "bargain hunters" who only shop during sales. This information can then be used to create targeted marketing campaigns for each segment.

## 3 How causes Overfitting? & How can it be preferred

Overfitting is a fundamental issue in supervised machine learning which prevents us from perfectly generalizing the models to well fit observed data on training data, as well as unseen data on testing set. Because of the presence of noise, the limited size of training set, and the complexity of classifiers, overfitting happens. To reduce the effects of overfitting, various strategies are proposed to address.

### Reasons for Overfitting

Overfitting has two primary causes:

1.  *Overly Complex Model:* A model may begin to fit the random fluctuations in the training data instead of the underlying trend if it contains too many parameters, layers, or features for the size and complexity of the dataset.
2.  *Inadequate Training Data:* A training dataset that is too small may not fully represent the variety of data that could be available, and the model may be able to quickly learn the few examples it has seen.

### Avoiding Overfitting

Striking the correct balance between a model's generalisability and complexity is necessary to avoid overfitting. Here are a few typical methods:

*   *Regularisation:* This method penalises the model's loss function for having a lot of coefficients. Regularisation promotes simpler models that are less prone to overfit by penalising complexity.
*   *Expand the Training Data:* The model is forced to learn the true underlying patterns and finds it more difficult to memorise specific examples in a larger, more varied dataset. Another way to artificially expand the dataset's size is through data augmentation.
*   *Early Stopping:* You can keep an eye on the model's performance on a separate validation set while it's being trained. You stop training if the model begins to perform worse on the validation set, which is a sign that overfitting is beginning.

## 4 Explain how training data and test data are split, and why this process is necessary.

The segmentation of the data sets is essential for determining the effectiveness of any machine learning model with regard to its application to other data sets, hence the need to evaluate the model on the test set. This evaluation is performed to see whether the model has learned the data too well, which is known as overfitting. The model also needs to have some semblance of the real life application of the data to be effective. The model needs to capture the essence of the evaluation set.

### The Splitting Process

It is very normal for data splits to be done using predefined ratios. In most cases, 80/20 data splits are very common.

*   *Training Data:* The pieces that are most crucial to the model are those that assist the model understand and define the multi-dimensional data. The patterns and geometrical data figures of different classes will all be used towards building a model.
*   *Test Data:* The model, after all the training and adjustments, has a structure that is built and skeletal. This skeletal structure helps evaluate the model. This skeletal structure is known as the test set and is unseen data for the model. Randomization is common for splitting data. This is done in order to avoid any biases that might be present due to unseen gaps in the data set.

### Importance of Data Split

The more novel and new the data is to the model, the better the evaluation for the model. In the absence of a test set, the model is said to suffer from overfitting. This is when the model computes the training data too many times. The model has a very difficult time with new data, and thus needs to be able to acquire new information in order to adapt to emerging patterns.

## 5. Machine Learning in Modern Agriculture: A Review of Techniques for Crop Production

Agriculture, the foundation of civilization, continues to be the backbone of economies in many countries, including India. With its significant contribution to GDP and employment, India's agricultural sector is vital. However, it faces challenges from various factors, including climate, geography, and socioeconomic conditions, which lead to changes in production performance across different regions. To address these challenges and improve crop yield prediction, a new approach using machine learning (ML) has emerged.

ML combines computer science and statistics to enhance predictive capabilities, providing data scientists and analysts with the tools to extract intricate knowledge from raw data. This article explores a range of ML techniques and their applications in agricultural crop production.

### Key Machine Learning Techniques and Applications

*   *Artificial Neural Networks (ANN):* ANNs are a supervised learning technique inspired by the human brain's biological processes. Once trained, they can predict patterns and provide meaningful solutions even when input data is incomplete or inaccurate. ANNs are highly adaptable and can identify complex relationships between inputs and outputs. They have been used to forecast potato production in Iran and monitor rice crops. Research has shown that ANNs can be more accurate than traditional methods like multiple linear regression for predicting corn and soybean yields.

*   *Information Fuzzy Networks:* This technique, particularly the Neuro-fuzzy Inference System (ANFIS), is used to handle situations with incomplete or uncertain information. Researchers have used it with remote sensing data to predict crop yield, even with a limited number of past years of data available.

*   *Decision Tree:* A decision tree is a model that uses a series of nodes and branches to classify data. The process involves two steps: growing a large tree and then pruning it to reduce overfitting. Studies have used this algorithm to predict soybean productivity, finding that relative humidity is a major influencing factor. The C4.5 algorithm, a type of decision tree, has been used in a tool called 'Crop Advisor' to forecast the effect of weather on crop yields in Madhya Pradesh, India.

*   *Regression Analysis:* Regression analysis is a widely used statistical method for crop production forecasting. It models the relationship between a response variable (yield) and explanatory variables (weather, soil properties). Various models, including linear, polynomial, and nonlinear regression, have been applied to forecast yields for crops like corn and sugarcane. One study concluded that regression analysis could successfully forecast sugarcane yield two months before harvest.

*   *Clustering:* Clustering is the process of grouping similar objects together. The k-means algorithm is a common and important clustering method used in data analysis. A modified k-means algorithm has been evaluated for crop prediction, showing maximum accuracy in classifying meteorological data and identifying patterns associated with severe weather.

*   *Time Series Analysis:* This method analyzes data collected over time to extract meaningful statistics and predict future values. It treats yield as a function of time and has been used to set up forecasting models based on past yield data.

*   *Markov Chain Model:* A Markov chain is a stochastic process where the next state of a system depends only on its current state. This approach has been applied to forecast cotton and sugarcane yields. A second-order Markov chain model was found to be more effective for forecasting sugarcane than both regression and first-order Markov chain models.

### Conclusion

With a growing volume of data from various sources, the application of machine learning in agriculture is becoming increasingly essential for uncovering hidden knowledge and developing objective pre-harvest forecasting methodologies. This integration of computer science and agriculture is a rapidly advancing field with significant potential for the future.