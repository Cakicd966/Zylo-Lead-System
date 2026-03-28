import requests

def check_website_status(url):
    if not url:
        return "No Website"

    try:
        response = requests.get(url, timeout=5)
        
        if response.status_code != 200:
            return "Broken"

        content = response.text.lower()

        if "2020" in content or "2019" in content:
            return "Outdated"

        return "Active"

    except:
        return "No Website"
