import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, roc_auc_score, mean_absolute_error, r2_score
df = pd.read_csv("placement.csv")
X = df.drop(["Placement_Status", "Study_Hours"], axis=1)
y_class = df["Placement_Status"]
y_reg = df["Study_Hours"]
X_train, X_test, y_class_train, y_class_test, y_reg_train, y_reg_test = train_test_split(
    X, y_class, y_reg, test_size=0.2, random_state=42
)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
log_model = LogisticRegression()
log_model.fit(X_train_scaled, y_class_train)
log_preds = log_model.predict(X_test_scaled)
log_probs = log_model.predict_proba(X_test_scaled)[:, 1]
print("Placement Model Accuracy:", accuracy_score(y_class_test, log_preds))
print("Placement Model ROC AUC:", roc_auc_score(y_class_test, log_probs))
lin_model = LinearRegression()
lin_model.fit(X_train, y_reg_train)
lin_preds = lin_model.predict(X_test)
print("Study Model MAE:", mean_absolute_error(y_reg_test, lin_preds))
print("Study Model R2 Score:", r2_score(y_reg_test, lin_preds))
X_scaled_full = scaler.fit_transform(X)
final_log_model = LogisticRegression()
final_log_model.fit(X_scaled_full, y_class)
final_lin_model = LinearRegression()
final_lin_model.fit(X, y_reg)
joblib.dump(final_log_model, "placement_model.pkl")
joblib.dump(final_lin_model, "study_recommendation_model.pkl")
joblib.dump(scaler, "scaler.pkl")
print("✅ Models Saved Successfully!")