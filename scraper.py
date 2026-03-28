import requests
from bs4 import BeautifulSoup

def search_businesses(query, pages=3):
    headers = {"User-Agent": "Mozilla/5.0"}
    results = []

    for page in range(pages):
        url = f"https://www.bing.com/search?q={query.replace(' ', '+')}&first={page*10}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        for item in soup.select("li.b_algo"):
            title = item.select_one("h2")
            link = item.select_one("a")

            if title and link:
                results.append({
                    "name": title.text.strip(),
                    "website": link["href"]
                })

    return results
