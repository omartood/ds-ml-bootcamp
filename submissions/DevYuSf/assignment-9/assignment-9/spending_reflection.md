# Assigment 9

I Implemented Spending Pattern Analysis with K-Means (Clustering)

- first I imported the necessary library like panadas and sklearn also elbowk
- secondaly I Read my file using pandas and checking is there null values but I didn't get any null values
- Thirdy I pick key before that i check wich K is the best also i used elbowk to know which k is the best
- further more I go with the process really the process is cool and you can look it the code of the jupyter file, thanks.

**which key and why**
I choosed 4 the why is, it's the not have more different 4 and 5 and I pick 4 also I use elbowk to choose the key and it displayed me number 4.
**Cluster Interpretation**

- my model is working with 4 numbers:
  - 0 ---> low income high spending
  - 1 ---> low income low spending
  - 2 ---> high income low spending
  - 3 ---> high income high spending
Category 3 and 0 is our target becase they spend more to our business

**Limitations & Next Steps**
Limitations:

- Current clustering only considers income and spending.

- It ignores other valuable information such as:

- Age (young vs. older customers might have different behaviors).

- Frequency of Visits (regular vs. occasional shoppers).

- Online vs. Offline Purchases (digital vs. in-store behavior).

Next Step:

- Extend clustering with 3 features (e.g., add Age to Income & Spending) and compare results.

- Alternatively, test a different clustering algorithm (DBSCAN) to see if natural clusters appear without pre-selecting K.
