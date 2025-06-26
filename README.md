# 🚢 Titanic Survival Prediction App

A fully functional Machine Learning web application built using **Streamlit** that predicts whether a passenger would survive the Titanic disaster based on features such as age, sex, passenger class, and family aboard.

🔗 **Live Demo**: [https://titanicshipsurvival.streamlit.app](https://titanicshipsurvival.streamlit.app)

---

## 📌 Features

- Trained using the famous [Titanic dataset](https://www.kaggle.com/c/titanic)
- Supports prediction based on:
  - Passenger class (`Pclass`)
  - Sex (`Sex`)
  - Age (`Age`)
  - Number of siblings/spouses aboard (`SibSp`)
  - Number of parents/children aboard (`Parch`)
- User-friendly interface powered by **Streamlit**
- Encodes inputs automatically and runs trained model predictions
- Realtime prediction result with clear UI

---

## 🧠 Model

- Algorithm: `Logistic Regression` (or your actual model name)
- Preprocessing includes:
  - Label Encoding for categorical features
  - Scikit-learn pipeline (optional)
- Model saved using `joblib`

---

## 🛠️ Technologies Used

- Python
- Pandas & NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## 🚀 How to Run Locally

1. Clone the repo:
```bash
git clone https://github.com/your-username/titanic-predictor.git
cd titanic-predictor

2.Install dependencies:
pip install -r requirements.txt

Run the app:
streamlit run app.py
```
file structure
├── app.py                  # Main Streamlit app
├── titanic_model.pkl       # Trained ML model
├── sex_encoder.pkl         # Encoder for 'Sex' feature
├── requirements.txt
├── README.md
