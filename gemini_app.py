import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyDalm4pA1Jn7kjLD5DifyQ3Ex_MxIvRTjo")

# Load model
model = genai.GenerativeModel("gemini-3-flash-preview")

st.title("🤖 Smart_AI")

# Input box
user_input = st.text_input("Ask anything")

# Generate response
if user_input:
    response = model.generate_content(user_input)
    st.write("AI:", response.text)
