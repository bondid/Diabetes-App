import streamlit as st
import pandas as pd
import joblib

#load model 
model = joblib.load(r"C:\Users\deidr\OneDrive\Desktop\Data Science Training\Streamlit\Diabetes App\diabetes_app.pkl") 

#App title and intro 
st.set_page_config(page_title = "Diabetes Prediction app",layout="centered") 
st.title("Diabetes Prediction App") 
st.write("Fill in the details below to predict the likelihood of Diabetes") 

#Input form with s
with st.form("Prediction form"):
    st.subheader("Enter Your Own Data") 

    col1,col2 = st.columns(2) 
    
    with col1: 
        pregnancies = st.slider("Pregnancies",0,10,step = 1) 
        glucose = st.slider("Glucose",0,200,120) 
        blood_pressure = st.slider("Blood Pressure",0,140,70) 
        bmi = st.number_input("BMI",min_value=0.0, max_value = 70.0,value= 25.0) 
        
    with col2: 
        skin_thickness = st.slider("Skin Thickness",0,100,20) 
        insulin = st.slider("Insulin",0,900,80) 
        diabetes_pedigree=st.number_input("Diabetes pedigree function ",0.0,2.5,0.5) 
        age = st.selectbox("Age group",options = [i for i in range(18,81,1)],index=2) 
    
    submitted = st.form_submit_button("Predict") 
    
    #predict 
    if submitted: 
        input_data = pd.DataFrame([[pregnancies,glucose,blood_pressure,bmi,skin_thickness,insulin,diabetes_pedigree,age]], columns = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin', 'BMI','DiabetesPedigreeFunction','Age'])

        prediction = model.predict(input_data)[0] 
        
        if prediction == 1: 
            st.error("Prediction: Positive for Diabetes See a doctor immediately") 
        else: 
            st.success("Prediction: Negative for diabetes")