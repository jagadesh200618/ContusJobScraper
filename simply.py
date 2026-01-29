import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import pandas as pd

GEMINI_API_KEY = "AIzaSyAzrD6bL22iYIt9rAukPvodzJfaf8z56gQ"
JOB_URL = "https://www.contus.com/careers.php"
EXCEL_NAME = "extracted_jobs.xlsx"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-3-flash-preview")

def fetch_html(url):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "header", "footer", "nav"]):
        tag.decompose()
    return soup.get_text(separator=" ", strip=True)[:10000]

def extract_job_data(text):
    prompt = f"""
From the text below, extract the following fields.
Return ONLY one line in this format:
job_title | company_name | location | job_description
Text:
{text}
"""
    response = model.generate_content(prompt)
    result = response.text.strip()
    parts = [p.strip() for p in result.split("|")]
    while len(parts) < 4:
        parts.append("")

    job_title, company_name, location, job_description = parts[:4]
    return {
        "job_title": job_title,
        "company_name": company_name,
        "location": location,
        "job_description": job_description,
        "source_url": JOB_URL
    }
def save_to_excel(data):
    df = pd.DataFrame([data])
    df.to_excel(EXCEL_NAME, index=False)
    return df

def main():
    text = fetch_html(JOB_URL)
    job_data = extract_job_data(text)
    df = save_to_excel(job_data)

    print("\n✅ Job data saved successfully!")
    print(df)

if __name__ == "__main__":
    main()
