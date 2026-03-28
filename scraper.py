import requests
from bs4 import BeautifulSoup

def search_businesses(query):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for g in soup.select("div.tF2Cxc"):
        title = g.select_one("h3")
        link = g.select_one("a")

        if title and link:
            results.append({
                "name": title.text,
                "website": link["href"]
            })

    return results
