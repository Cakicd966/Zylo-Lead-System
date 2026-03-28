import pandas as pd
from scraper import search_businesses
from utils import check_website_status

def run(location, niche):
    query = f"{niche} in {location}"
    businesses = search_businesses(query)

    leads = []

    for biz in businesses:
        status = check_website_status(biz["website"])

        if status in ["No Website", "Outdated"]:
            leads.append({
                "Business Name": biz["name"],
                "Website": biz["website"],
                "Website Status": status
            })

    df = pd.DataFrame(leads)
    df.to_csv("leads.csv", index=False)

    print("✅ Leads saved to leads.csv")

if __name__ == "__main__":
    run("London", "plumber")
