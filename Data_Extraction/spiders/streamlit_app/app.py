import streamlit as st
import pandas as pd
import os
import glob

# ------------------ Load dataset automatically ------------------
current_folder = os.path.dirname(os.path.abspath(__file__))

excel_files = glob.glob(os.path.join(current_folder, "*.xlsx"))
csv_files = glob.glob(os.path.join(current_folder, "*.csv"))

if excel_files:
    df = pd.read_excel(excel_files[0])
elif csv_files:
    df = pd.read_csv(csv_files[0])
else:
    st.error("No CSV or Excel file found in this folder")
    st.stop()

# ------------------ Clean columns ------------------
df.columns = df.columns.str.strip()

# REQUIRED columns (change names ONLY if your dataset differs)
required_cols = ["Company", "Job_Title", "Posted_Date", "Job_Description"]

for col in required_cols:
    if col not in df.columns:
        st.error(f"Missing column: {col}")
        st.stop()

# ------------------ Remove duplicates ------------------
df = df.drop_duplicates(subset=["Company", "Job_Title"])

# ------------------ UI Styling (FIXED) ------------------
st.set_page_config(page_title="Job Selection", page_icon="💼", layout="centered")

st.markdown(
    """
    <style>
        .stApp {
            background-color: #F0F8FF;
        }
        h1 {
            color: #0B3C5D;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Job Selection Portal")

# ------------------ Dropdowns ------------------
companies = sorted(df["Company"].unique())
job_titles = sorted(df["Job_Title"].unique())

selected_company = st.selectbox("Select Company", companies)
selected_title = st.selectbox("Select Job Title", job_titles)

# ------------------ Display job details ------------------
result = df[
    (df["Company"] == selected_company) &
    (df["Job_Title"] == selected_title)
]

if not result.empty:
    job = result.iloc[0]
    st.markdown("### Selected Job Details")
    st.write(f"**Company:** {job['Company']}")
    st.write(f"**Job Title:** {job['Job_Title']}")
    st.write(f"**Posted Date:** {job['Posted_Date']}")
    st.write(f"**Description:** {job['Job_Description']}")
else:
    st.warning("No matching job found for this selection")
