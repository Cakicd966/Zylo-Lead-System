import sys
import pandas as pd
from scraper import search_businesses
from utils import check_website_status, scrape_contact_info, is_valid_business_site

if len(sys.argv) >= 3:
    location = sys.argv[1]
    niche = sys.argv[2]
else:
    location = input("Enter location: ")
    niche = input("Enter business type: ")

LOCATIONS = [location]
NICHE = niche

def run():
    all_leads = []
    seen_websites = set()

    for location in LOCATIONS:
        print(f"Searching in {location} for {NICHE}...")
        query = f"{NICHE} in {location}"
        businesses = search_businesses(query, pages=3)

        for biz in businesses:
            website = biz.get("website", "")
            if not website:
                continue
            if website in seen_websites:
                continue
            seen_websites.add(website)

            if not is_valid_business_site(website):
                continue

            status = check_website_status(website)
            contact = scrape_contact_info(website)

            score = 0
            if status == "No Website":
                score += 2
            if not contact["emails"]:
                score += 1

            all_leads.append({
                "Business Name": biz.get("name", ""),
                "Location": location,
                "Website": website,
                "Status": status,
                "Phone": ", ".join(contact["phones"]),
                "Email": ", ".join(contact["emails"]),
                "Score": score
            })

    df = pd.DataFrame(all_leads)
    df.to_csv("leads.csv", index=False)
    print("Leads saved to leads.csv")

if __name__ == "__main__":
    run()
