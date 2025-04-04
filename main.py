import streamlit as st
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set Background
set_background("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo55q8aIv2qYhNSm8b7Fo0wb9-pbp7BAGzdw&s")

# Initialize session state to store user inputs
if 'user_inputs' not in st.session_state:
    st.session_state['user_inputs'] = {}

st.title("Customer Churn Prediction")

# User inputs
st.session_state['user_inputs']['gender'] = st.radio("Gender", ["Female", "Male"])
st.session_state['user_inputs']['SeniorCitizen'] = st.radio("Senior Citizen", [0, 1])
st.session_state['user_inputs']['Partner'] = st.radio("Partner", ["Yes", "No"])
st.session_state['user_inputs']['Dependents'] = st.radio("Dependents", ["Yes", "No"])
st.session_state['user_inputs']['tenure'] = st.number_input("Tenure", min_value=0, max_value=100, step=1)
st.session_state['user_inputs']['PhoneService'] = st.radio("Phone Service", ["Yes", "No"])
st.session_state['user_inputs']['MultipleLines'] = st.radio("Multiple Lines", ["No phone service", "No", "Yes"])
st.session_state['user_inputs']['InternetService'] = st.radio("Internet Service", ["DSL", "Fiber optic", "No"])
st.session_state['user_inputs']['OnlineSecurity'] = st.radio("Online Security", ["Yes", "No"])
st.session_state['user_inputs']['OnlineBackup'] = st.radio("Online Backup", ["Yes", "No"])
st.session_state['user_inputs']['DeviceProtection'] = st.radio("Device Protection", ["Yes", "No"])
st.session_state['user_inputs']['TechSupport'] = st.radio("Tech Support", ["Yes", "No"])
st.session_state['user_inputs']['StreamingTV'] = st.radio("Streaming TV", ["Yes", "No"])
st.session_state['user_inputs']['StreamingMovies'] = st.radio("Streaming Movies", ["Yes", "No"])
st.session_state['user_inputs']['Contract'] = st.radio("Contract", ["Month-to-month", "One year", "Two year"])
st.session_state['user_inputs']['PaperlessBilling'] = st.radio("Paperless Billing", ["Yes", "No"])
st.session_state['user_inputs']['PaymentMethod'] = st.radio("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
st.session_state['user_inputs']['MonthlyCharges'] = st.number_input("Monthly Charges", min_value=0.0, step=0.1)
st.session_state['user_inputs']['TotalCharges'] = st.number_input("Total Charges", min_value=0.0, step=0.1)

if st.button("Submit"):
    st.success("Inputs submitted successfully. Navigate to the 'Result' page to view the prediction.")
