import pandas as pd
from scraper import search_businesses
from utils import check_website_status, scrape_contact_info

LOCATIONS = ["London", "Manchester", "Birmingham"]
NICHE = "plumber"

def run():
    all_leads = []
seen_websites = set()

    for location in LOCATIONS:
        print(f"🔍 Searching in {location}...")

        query = f"{NICHE} in {location}"
        businesses = search_businesses(query)

        for biz in businesses:
            website = biz["website"]
            if website in seen_websites:
    continue

seen_websites.add(website)
            status = check_website_status(website)

            if status in ["No Website", "Outdated"]:
                contact = scrape_contact_info(website)
                score = 0

if status == "No Website":
    score += 2
if not contact["emails"]:
    score += 1

all_leads.append({
    "Business Name": biz["name"],
    "Location": location,
    "Website": website,
    "Status": status,
    "Phone": ", ".join(contact["phones"]),
    "Email": ", ".join(contact["emails"]),
    "Score": score
})

                all_leads.append({
                    "Business Name": biz["name"],
                    "Location": location,
                    "Website": website,
                    "Status": status,
                    "Phone": ", ".join(contact["phones"]),
                    "Email": ", ".join(contact["emails"])
                })

    df = pd.DataFrame(all_leads)
    df.to_csv("leads.csv", index=False)

    print("🔥 DONE — leads saved to leads.csv")

if __name__ == "__main__":
    run()
