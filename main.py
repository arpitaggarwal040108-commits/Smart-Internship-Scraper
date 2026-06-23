import requests
from bs4 import BeautifulSoup
import csv
import time
import schedule

CSV_FILE = "internships.csv"
def scrape_jobs():
    print("\n=================================")
    print("Starting Internship Scraper...")
    print("=================================\n")

    keyword = input("Enter keyword (Python, Data Analyst, ML): ").lower()

    url = "https://internshala.com/internships/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        print("Fetching webpage...")

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            print(f"Website returned {response.status_code}")
            return

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        jobs = soup.find_all("div", class_="individual_internship")

        if not jobs:
            print("No internships found.")
            return

        results = []

        print(f"Found {len(jobs)} internships")
        print("Filtering results...\n")

        for job in jobs:

            try:
                title_tag = job.find("h3")

                title = (
                    title_tag.get_text(strip=True)
                    if title_tag
                    else "Not Available"
                )

                company_tag = job.find(
                    "h4",
                    class_="company-name"
                )

                company = (
                    company_tag.get_text(strip=True)
                    if company_tag
                    else "Not Available"
                )

                location_tag = job.find(
                    "a",
                    class_="location_link"
                )

                location = (
                    location_tag.get_text(strip=True)
                    if location_tag
                    else "Not Available"
                )

                date_posted = "Not Available"

                link_tag = job.find("a")

                if link_tag and link_tag.get("href"):
                    link = (
                        "https://internshala.com"
                        + link_tag["href"]
                    )
                else:
                    link = "Not Available"

                if keyword in title.lower():

                    results.append([
                        title,
                        company,
                        location,
                        date_posted,
                        link
                    ])

            except Exception as e:
                print(
                    f"Error reading internship: {e}"
                )

        if len(results) == 0:
            print(
                f"No internships found for '{keyword}'"
            )
            return

        with open(
            CSV_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Title",
                "Company",
                "Location",
                "Date Posted",
                "Link"
            ])

            writer.writerows(results)

        print(
            f"\nSaved {len(results)} internships"
        )
        print(
            f"CSV File Created: {CSV_FILE}"
        )

    except requests.exceptions.ConnectionError:
        print("No internet connection.")

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except Exception as e:
        print(f"Unexpected Error: {e}")


def scheduled_job():
    scrape_jobs()


print("1. Run Now")
print("2. Daily Scheduler")

choice = input("Choose option: ")

if choice == "1":
    scrape_jobs()

elif choice == "2":

    schedule.every().day.at(
        "09:00"
    ).do(scheduled_job)

    print(
        "Scheduler running..."
    )

    while True:
        schedule.run_pending()
        time.sleep(60)

else:
    print("Invalid choice")