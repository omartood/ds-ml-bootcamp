### **Somali TalentLink Needs Assessment Survey – Research Paper**

#### **1\. Title & Collection Method**

**Title:** Somali TalentLink Needs Assessment Survey Dataset

**Collection Method**:  
The dataset was collected through an online survey (Office Forms) shared across Somali youth, students, and professionals. The survey aimed to explore the demand for a local freelancing and task-based platform similar to Upwork or TaskRabbit, but tailored for the Somali context. A total of 42 valid responses were gathered.

---

#### **2\. Description of Features & Labels**

**Features (X):** Demographic and behavioral variables, such as:

* Age group  
* Education level  
* Main skill/profession  
* Previous use of platforms (Upwork/Fiverr)  
* Challenges in online freelancing  
* Payment preferences  
* Trust factors  
* Skills preferred to be advertised

**Label (y)**:  
The most relevant outcome variable is: “Perceived importance of having a local Somali freelancing platform” (rated as “Aad muhiim u ah,” “Muhiim,” “Dhexdhexaad”).  
Another possible target is “Willingness to use Somali TalentLink” (Poster, Tasker, or Both).

---

#### **3\. Dataset Structure**

* **Rows:** 42  respondents  
* **Columns:** 14variables  
* **Format:** Mixed types (categorical, multiple-choice, open-text, datetime)

**Sample (first 5 rows):**

| ID | Age | Education | Main Skill | Used Platforms | Challenges | Importance of Local Platform | Usage Intent | Payment Method | Trust Factor |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 25–34 | Master’s/PhD | Machine Learning Eng. | Yes | Helitaanka macaamiil | Aad muhiim u ah | Tasker | Bank Transfer | Helitaanka macaamiil dhab |
| 2 | 18–24 | Arday Jaamacadeed | Software Developer | No | Helitaanka macaamiil | Aad muhiim u ah | Tasker | EVC/Zaad | Helitaanka macaamiil dhab |
| 3 | 18–24 | Arday Jaamacadeed | IT | No | Helitaanka macaamiil | Muhiim | Both | EVC/Zaad | Helitaanka macaamiil dhab |
| 4 | 18–24 | Arday Jaamacadeed | Data Science | Yes | Helitaanka macaamiil | Aad muhiim u ah | Tasker | EVC/Zaad | Amniga lacagaha |
| 5 | 18–24 | Dhameeyay Jaamacad | FullStack Developer | No | Helitaanka macaamiil | Aad muhiim u ah | Both | EVC/Zaad | Qiimaha adeeg macquul ah |

---

#### **4\. Quality Issues**

* **Missing values:** Some open-text responses are empty (e.g.,“Reasons to like Somali TalentLink”).  
* **Typos / language mix:** Text includes Somali/English mix, minor spelling inconsistencies.  
* **Duplicates:** None detected.  
* **Imbalance:** Most respondents are students or young graduates (18–24) and strongly favor IT-related skills. This may bias results towards tech-oriented users, underrepresenting other professions.  
* **Subjectivity:** Open-ended questions produce qualitative data that requires cleaning and categorization.

---

#### **5\. Use Case in Machine Learning**

The dataset can be used in several ML applications:

* **Classification:**  
  * Predicting whether a respondent is likely to use Somali TalentLink as a Poster, Tasker, or Both, based on demographics and skills.  
  * Predicting perception of importance (High vs. Medium vs. Low).  
* **Clustering (unsupervised):**  
  * Grouping respondents by their skills, payment preferences, and challenges to identify distinct user segments (e.g., IT students, freelancers, non-tech professionals).

[Somali TalentLink Needs Assessment Survey.xlsx](https://snueduso-my.sharepoint.com/:x:/g/personal/zakariye_st_snu_edu_so/EQIKaRSaHqVJhT0iDFMViOwBf-ozh8l_pFk9UoCJFgX-jg?e=Jj8Cq9)

## **—-------------------  Summary Link  —-----------------------**

https://forms.office.com/Pages/AnalysisPage.aspx?AnalyzerToken=Io1khPvAKQFYKVC5Rew4DlDfreo0F4p4\&id=GV0-630ia02RopI0KkoBZNDDcjqVKPtEuLjmUQE0XdNUQUlLQ0RPSzlRSk9TSUhSWDU4N04xTlBMSC4u