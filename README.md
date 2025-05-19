# 🎓University-Admission-Predictor
  Predict your chances of getting into a university using your academic profile with the help of Machine Learning!
  
  🔗Live app : https://aditya-hub31-university-admission-predictor-main-2d82fa.streamlit.app

## 📌 Project Overview
    This project is a Machine Learning-based web application that predicts the probability of admission into a university based on factors such as GRE score, TOEFL score, university rating, SOP & LOR strength, CGPA, and research experience.

Built with:
  -Python, Scikit-learn
  -Pandas / Numpy / Matplotlib
  -Streamlit for Web Deployment
  -Plotly for interactive visualizations

## 🚀 Features
  🔢 Input student academic profile
  🎯 Predict admission probability using trained ML model
  📊 Beautiful gauge chart (speedometer-style) visualization
  🗂️ Logs recent predictions with timestamp
  📥 Downloadable CSV log of all predictions

## 🧠 Machine Learning Process
📁 Dataset:
  GRE Score: Graduate Record Examination score (out of 340)
  TOEFL Score: Test of English as a Foreign Language score (out of 120)
  University Rating: Rating of the university (1 to 5)
  SOP(Statement of Purpose): Quality rating of the SOP (1 to 5)
  LOR(Letter of Recommendation): Strength rating of the LOR (1 to 5)
  CGPA: Academic GPA (on a 10-point scale)
  Research Experience: 1 if research experience, 0 if none

## 📊 Exploratory Data Analysis (EDA):
  Visualized distributions using histograms for all major features
  Checked data types and missing values
  Cleaned dataset by removing unimportant columns and replacing invalid 0s with NaN

## 🛠️ Model Building:
Tested multiple regression models:
  Linear Regression ✅ 
  Lasso Regression
  Support Vector Regression (SVR)
  Decision Tree
  Random Forest
  KNN
  XGBoost
  CatBoost
  Extra Trees
  
## 🕸️Model Chosen: Linear Regression – best accuracy and cross-validation score

To avoid retraining the model every time the application runs, we saved the trained model using the Joblib library using an .pkl file! 

## 🚀 Deploying with Streamlit
  To make our prediction model interactive and accessible via the web, we used Streamlit, a powerful and easy-to-use Python framework for deploying machine learning apps.

  Using Streamlit, we created a user-friendly interface where users can input their academic details and instantly receive their predicted chance of university admission. We also included features like:
🎛️ Form inputs for academic parameters,
📈 Gauge chart to visualize prediction,
🧾 Logging of predictions with download option.

You can check out the live app here: 
🔗 https://aditya-hub31-university-admission-predictor-main-2d82fa.streamlit.app


### 📊 Sample Prediction
  GRE = 337
  TOEFL = 118
  University Rating = 4
  SOP = 4.5
  LOR = 4.5
  CGPA = 9.65
  Research = 1
Output: Chance of getting into UCLA is 95.23%


## 📸 App Screenshots
![Prediction Screenshot](https://github.com/user-attachments/assets/74d8ec07-49b4-4dd4-ac2a-e637791d6494)
![Graph Screenshot](https://github.com/user-attachments/assets/c2194707-9477-4f41-951d-f87a0f459d3b)


## 🤝 Connect with Me
- [LinkedIn](https://www.linkedin.com/in/aditya-32m5/)
- [GitHub](https://github.com/Aditya-hub31)
- Email: karnatiadityagoud@gmail.com



