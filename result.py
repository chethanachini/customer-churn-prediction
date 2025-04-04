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

st.title("Churn Prediction Result")

# Check if user inputs are available in session state
if 'user_inputs' in st.session_state:
    user_inputs = st.session_state['user_inputs']
    
    # Display user inputs
    st.subheader("User Inputs:")
    for key, value in user_inputs.items():
        st.write(f"**{key}**: {value}")
    
    # Implement your prediction logic here
    # For demonstration purposes, we'll use a simple rule-based approach
    if user_inputs['Contract'] == 'Month-to-month' and user_inputs['tenure'] < 12:
        prediction = "Likely to Churn"
    else:
        prediction = "Unlikely to Churn"
    
    # Display prediction result
    st.subheader("Prediction:")
    st.write(f"The customer is **{prediction}**.")
else:
    st.warning("No user inputs found. Please go back to the main page and submit the required information.")
