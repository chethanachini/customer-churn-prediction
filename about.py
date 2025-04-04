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

st.title("Churn Prediction ")

st.markdown("""
This project predicts customer churn using machine learning. It takes customer details such as tenure, service subscriptions, contract type, and payment method as input. The data is processed using pre-trained encoders, and a trained model predicts whether the customer is likely to churn. The system helps businesses take proactive retention measures. 
""")

# Navigation Button
if st.button("🔙 Go Back"):
    st.switch_page("main.py")
