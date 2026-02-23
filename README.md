# 🎓 AI Placement Readiness & Study Recommendation System
An end-to-end Machine Learning project that predicts student placement probability and recommends optimized study hours using supervised learning models.
This project demonstrates:
✔ Exploratory Data Analysis (EDA)  
✔ Model comparison (Logistic vs Random Forest)  
✔ Feature scaling  
✔ Model evaluation  
✔ Model persistence using joblib  
✔ Streamlit deployment  
✔ Automated PDF report generation  


# 📌 Problem Statement
To build a system that:
1. Predicts whether a student is placement-ready.
2. Provides probability-based readiness score.
3. Recommends optimal daily study hours.
4. Generates a personalized improvement plan.

# 📊 Exploratory Data Analysis (EDA)
- Dataset overview and missing value analysis
- Placement status distribution
- CGPA distribution
- Correlation heatmap
- Year vs Placement analysis
- Coding study hours vs Placement comparison
Key insights:
- CGPA positively correlates with placement
- Coding study hours strongly influence placement probability
- Final-year students have higher placement rates

# 🧠 Model Development (`model.ipynb`)
### Classification Models Compared:
- Logistic Regression
- Random Forest Classifier
Metrics Used:
- Accuracy Score
- ROC-AUC Score
- Classification Report
Logistic Regression was selected for deployment due to:
- Good ROC-AUC performance
- Simplicity
- Better interpretability
- Less overfitting compared to Random Forest
### Regression Models Compared:
- Linear Regression
- Random Forest Regressor
Metrics Used:
- MAE
- RMSE
- R² Score
Linear Regression was selected for study hour recommendation because:
- Stable performance
- Lower complexity
- Faster prediction
- Sufficient generalization


# ⚙️ Final Training Script (`train_model.py`)

Workflow:

1. Load dataset
2. Split into training and testing sets
3. Apply StandardScaler
4. Train Logistic Regression (Classification)
5. Train Linear Regression (Regression)
6. Evaluate models
7. Retrain on full dataset
8. Save models using joblib

# 🚀 Streamlit Deployment (`app.py`)

Features:

- Multi-page navigation using session state
- Custom professional UI with CSS
- Real-time placement probability prediction
- Study hour recommendation (clipped between 2–10 hours)
- Level-based improvement plan
- Downloadable PDF report
- Dynamic user input handling

---

# 🖥️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
- ReportLab

---

<h4 align="center" style="color=red;">✨ Thank You ✨</h4> 
<h3 align="center" style="color:#e74c3c;">Created By: Dishari Ghosh</h3>


