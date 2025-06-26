import streamlit as st
import joblib
import pandas as pd


# Load model or pipeline
model = joblib.load("titanic_modela.pkl")  
encoder = joblib.load("encoder.pkl")  #labelencoder for categorical variables
# UI
st.title("🚢 Titanic Survival Prediction")
pclass = st.selectbox("Passenger Class", [1, 2, 3])
age = st.slider("Age", 0, 100, 25)
sex = st.radio("Sex", ["male", "female"])
sibsp = st.slider("Siblings/Spouses Aboard", 0, 5, 1)
parch = st.slider("Parents/Children Aboard (Parch)", 0, 5, 0)

encoded_sex = encoder.transform([sex])[0]
# Predict
if st.button("Predict Survival"):
    input_df = pd.DataFrame({
        'Pclass': [pclass],
        'Age': [age],
        'Sex': [encoded_sex],
        'SibSp': [sibsp],
        'Parch': [parch]
    })

    prediction = model.predict(input_df)
    st.success(f"🎯 Prediction: {'Survived' if prediction[0] == 1 else 'Did not survive'}")
