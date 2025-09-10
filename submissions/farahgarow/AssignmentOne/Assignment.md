### Assignemt week_1 Introduction to ML

1. 🚗 **Define Machine Learning using Real life examples**

    Machine Learning is when computers learn patterns from data and improve their performance without being directly programmed.

    Instead of rules, ML uses experience (data) to get better.

 **Real-life Example: ML Helps in Car GPS**

    **🚦🚦Traffic Prediction (Machine Learning)**

        ✍️GPS apps collect live data from millions of phones and cars.

        ✍️ML analyzes historical traffic patterns (e.g., "this road is usually busy at 5 pm") + live data (current slowdowns).

        ✍️It then predicts traffic jams and suggests faster alternative routes.

    🚛 Example: If you drive from Garowe to Bosaso, Google Maps can predict whether the road will be clear or slow, based on past and live data.

2.**Compare Supervised Learning and Unsupervised Learning, giving an example of each**

    📚 **Scenario: Online Courses Platform**

    1. Supervised Learning

        The machine learns from labeled data (data that already has the correct answer)
        Supervised Learning works whenever we have input + known output (labels), and the machine learns this mapping to make predictions.

    **Supervised Learning Example**

        Goal: Predict which course a student might be interested in.

        How: Train on past data where input = student profile (age, profession, previous courses) and output (label) = course they enrolled in.

        Use Case:

             🧑‍💻 A student completed “Beginner Python.” The model predicts they will likely want “Intermediate Python.”

            📩 You can send them a personalized message recommending the next course.

    2. Unsupervised Learning

        The machine learns from unlabeled data (no predefined answers).

        **Example**

     Goal: Group learners with similar behavior.

     How: Use clustering to find groups (no labels needed).

     **Use Case:**

        Group 1: Students interested in Programming 💻

        Group 2: Students interested in Business 📊

        Group 3: Students interested in Design 🎨

        You can send targeted course announcements to each group, instead of sending the same message to everyon

**3.What causes Overfitting? How can it be prevented?**
       Overfitting happens when a model learns the training data too well, including noise and random details, instead of just the underlying patterns
    **Real-Life Overfitting Scenarios**

    👸 **Hiring Employees**

         Cause (Overfitting):
           A company only hires candidates from one university because previous good employees came from there.

         ⚠️Problem:
            They may miss out on great talent from other schools (model is too specific).

        ⏮️Prevention:

            Broaden selection criteria.

            diverse hiring data (more training data).

**4. Explain how training data and test data are split, and why this process is necessary**
    Training data is a foundation compenet in mechine learning, purpose of traing data are a learn pattern and build knowledge, it contains input features and known outputs (labels), while Test data evaluate the model's performance and generalization, Testin data helps check if the model is overfitting or underfittin.
    
    Common Ratios:

        70% training / 30% test

        80% training / 20% test

        60% training / 20% validation / 20% test

    ✍️✍️Process is Necessary
       
       1. Prevents Overfitting

            If you test the model on the same data it trained on, it will look perfect even if it fails on new data.

        2.Measures Generalization

            Test data simulates real-world unseen data to check if the model can make accurate predictions outside the training set.

        3.Model Selection and Tuning

            Helps compare models and tune hyperparameters (like tree depth, learning rate) using a separate validation set without leaking information from test data.

        4.Reliable Performance Metrics

            Provides unbiased metrics like accuracy, precision, recall, or RMSE.
**5.Find one case study (research paper or article) that explains how Machine Learning has been applied in healthcare, business, or transportation. Summarize its findings.**

    Business:📱 SAHAL – Data-Driven Financial Services

                ✍️While specific ML applications in SAHAL are less documented, the platform's integration into Somalia's mobile money ecosystem suggests potential uses of ML for:

                ✍️Predictive Analytics: Forecasting user behavior and transaction trends.

                ✍️Risk Assessment: Evaluating creditworthiness and financial risks.

                ✍️Personalized Services: Tailoring financial products to individual user needs.