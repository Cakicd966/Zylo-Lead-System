import requests
from bs4 import BeautifulSoup

def search_businesses(query):
    url = f"https://www.bing.com/search?q={query.replace(' ', '+')}"
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for item in soup.select("li.b_algo"):
        title = item.select_one("h2")
        link = item.select_one("a")

        if title and link:
            results.append({
                "name": title.text,
                "website": link["href"]
            })

    return results
