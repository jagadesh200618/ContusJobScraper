import requests
from bs4 import BeautifulSoup
import pandas as pd

# STEP 1: GET HTML
url = "https://www.contus.com/careers.php"
response = requests.get(url)

print("Status code:", response.status_code)

# STEP 2: Extract TEXT
soup = BeautifulSoup(response.text, "html.parser")
page_text = soup.get_text(separator="\n", strip=True)
lines = page_text.split("\n")

# STEP 3: SEND TEXT TO "MODEL" (simulation)
job_keywords = [
    "developer", "engineer", "designer",
    "architect", "tester", "lead", "manager"
]

extracted_blocks = []

for i, line in enumerate(lines):
    clean_line = line.strip()

    # ✅ FILTER: likely job title rules
    if (
        3 <= len(clean_line.split()) <= 6 and     # short title
        any(k in clean_line.lower() for k in job_keywords)
    ):
        description = " ".join(lines[i:i+4])

        extracted_blocks.append({
            "job_title": clean_line,
            "description": description
        })

print("Extracted blocks:", len(extracted_blocks))

# STEP 4: CREATE JOB ATTRIBUTES
jobs = []

for item in extracted_blocks:
    jobs.append({
        "job_title": item["job_title"],
        "description": item["description"],
        "company": "CONTUS TECH",
        "location": "Chennai, India",
        "source_url": url
    })

# STEP 5: SAVE TO EXCEL
df = pd.DataFrame(jobs)
df.to_excel("contus_jobs_with_description.xlsx", index=False)

print("Excel file created successfully")



