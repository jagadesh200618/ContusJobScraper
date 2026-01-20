import scrapy
import json
import re
from w3lib.html import remove_tags


class JatoSpider(scrapy.Spider):
    name = "jato"
    allowed_domains = ["careers.jato.com"]

    start_urls = [
        "https://careers.jato.com/jobs/automotive-data-analyst",
    ]

    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    def parse(self, response):
        json_scripts = response.xpath(
            '//script[@type="application/ld+json"]/text()'
        ).getall()

        found = False

        for script in json_scripts:
            try:
                data = json.loads(script)

                # ✅ HANDLE LIST OR DICT
                if isinstance(data, list):
                    items = data
                else:
                    items = [data]

                for item in items:
                    if item.get("@type") == "JobPosting":
                        found = True

                        job = {}
                        job["ROLE"] = item.get("title", "")
                        job["DATE_POSTED"] = item.get("datePosted", "")
                        job["EMPLOYMENT_TYPE"] = item.get("employmentType", "")
                        job["LINK"] = response.url

                        raw_desc = item.get("description", "")
                        job["DESCRIPTION"] = re.sub(
                            r"\s+", " ", remove_tags(raw_desc)
                        ).strip()

                        hiring = item.get("hiringOrganization", {})
                        job["COMPANY_NAME"] = hiring.get("name", "JATO Dynamics")

                        location = item.get("jobLocation", [])
                        if isinstance(location, list) and location:
                            address = location[0].get("address", {})
                        else:
                            address = {}

                        job["CITY"] = address.get("addressLocality", "")
                        job["COUNTRY"] = address.get("addressCountry", "")

                        yield job   # ✅ DATA SENT TO EXCEL

            except Exception as e:
                self.logger.warning(f"JSON error: {e}")

        if not found:
            self.logger.warning("❌ No JobPosting JSON-LD found on page")
