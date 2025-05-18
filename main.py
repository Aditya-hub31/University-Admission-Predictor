import joblib
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import datetime
import plotly.graph_objects as go



# Load the trained model
model = joblib.load('admission_prediction_model.pkl')  

st.title("🎓University Admission Prediction")  
                                                                     #input values from a user
GRE = st.number_input("GRE Score", min_value=260, max_value=340, value=320)
TOEFL = st.number_input("TOEFL Score", min_value=0, max_value=120, value=110)
University_Rating = st.number_input("University Rating", min_value=1, max_value=5, value=3)
SOP = st.number_input("SOP Strength", min_value=1.0, max_value=5.0, value=3.0)
LOR = st.number_input("LOR Strength", min_value=1.0, max_value=5.0, value=3.0)
CGPA = st.number_input("CGPA", min_value=1.0, max_value=10.0, value=8.0)
Research = st.selectbox("Research Experience", [0,1])



def show_gauge_chart(chance):          #shows the prediction percentage in a GUAGE chart (speedometer)
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = chance,
        title = {'text': "Admission Chance (%)"},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkblue"},
            'steps' : [
                {'range': [0, 50], 'color': "red"},
                {'range': [50, 75], 'color': "yellow"},
                {'range': [75, 100], 'color': "green"}],
            'threshold' : {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': chance}}))

    fig.update_layout(height=300)
    st.plotly_chart(fig)


        #prediction button

if st.button("Predict Admission Chance"):  #predicting logic
    input_features = np.array([[GRE, TOEFL, University_Rating, SOP, LOR, CGPA, Research]])
    prediction = model.predict(input_features)
    predicted_chance = round(prediction[0]*100, 2)
    # st.write(f"Chance of admission: {predicted_chance}%")
    st.success(f"Chance of admission: {predicted_chance}%")

    user_input = {
        "GRE": GRE,
        "TOEFL": TOEFL,
        "University Rating": University_Rating,
        "SOP": SOP,
        "LOR": LOR,
        "CGPA": CGPA,
        "Research": Research
    }

    predicted_chance = round(prediction[0]*100, 2)
    show_gauge_chart(predicted_chance)        #calling the function of gauge chart 







#not just prediction - but also saves user data into another file. DATA LOGGING
    log_entry = {
        "Timestamp": datetime.datetime.now(),
        "GRE": GRE,
        "TOEFL": TOEFL,
        "University Rating": University_Rating,
        "SOP": SOP,
        "LOR": LOR,
        "CGPA": CGPA,
        "Research": Research,
        "Predicted Chance": predicted_chance
        
    }
    log_file = "prediction_log.csv" #save into this file
 

    if os.path.exists(log_file):
        df = pd.read_csv(log_file)
        df = pd.concat([df, pd.DataFrame([log_entry])], ignore_index=True)

    else:
        df = pd.DataFrame([log_entry])

    df.to_csv(log_file, index=False)


    st.subheader("📄 Recent Predictions")
    st.dataframe(df.tail(5))  #showing recent 5 input to user from the file
    with open(log_file, "rb") as file:     #downlaod button
        st.download_button(
            label="📥 Download Prediction Log",
            data=file,
            file_name="prediction_log.csv",
            mime="text/csv"
            )




