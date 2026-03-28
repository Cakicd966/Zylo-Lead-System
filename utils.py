import requests
import re
from bs4 import BeautifulSoup

def extract_emails(text):
    return list(set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)))

def extract_phone(text):
    phones = re.findall(r"\+?\d[\d\s\-]{7,}\d", text)
    return list(set(phones))

def scrape_contact_info(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)

        soup = BeautifulSoup(response.text, "lxml")
        text = soup.get_text()

        emails = extract_emails(text)
        phones = extract_phone(text)

        return {
            "emails": emails[:2],
            "phones": phones[:2]
        }

    except:
        return {
            "emails": [],
            "phones": []
        }

def check_website_status(url):
    if not url:
        return "No Website"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return "Broken"

        content = response.text.lower()

        if "2018" in content or "2019" in content:
            return "Outdated"

        return "Active"

    except:
        return "No Website"
