import streamlit as st
st.title("Streamlit Website ")
name = st.text_input("Enter your name")
submit = st.button("Submit")
if submit:
    st.write("Hello,", name)
