import streamlit as st

st.title("🎬 Book My Show")

st.header("User Details")
name = st.text_input("Enter Name")

st.header("Movie Selection")
movie = st.selectbox("Select Movie", ["Leo", "Jailer", "Vikram", "Master"])
theatre = st.selectbox("Select Theatre", ["PVR", "INOX", "AGS"])
show_time = st.selectbox("Show Time", ["10:00 AM", "2:00 PM", "6:00 PM", "10:00 PM"])

st.header("Ticket Details")
tickets = st.number_input("Number of Tickets", min_value=1, max_value=10)

if st.button("Book Ticket"):
    amount = tickets * 200
    st.success("✅ Movie Ticket Booked Successfully!")
    st.write("Name:", name)
    st.write("Movie:", movie)
    st.write("Theatre:", theatre)
    st.write("Show Time:", show_time)
    st.write("Tickets:", tickets)
    st.write("Total Amount: ₹", amount)
