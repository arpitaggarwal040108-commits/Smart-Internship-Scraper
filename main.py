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

    keyword = input(
        "Enter keyword (Python, Data Analyst, ML): "
    ).lower()

    url = f"https://internshala.com/internships/keywords-{keyword}/"

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
            print(
                f"Website returned {response.status_code}"
            )
            return

        with open(
            "page.html",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(response.text)

        print("HTML saved to page.html")

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        internships = soup.find_all(
            "div",
            attrs={"internshipid": True}
        )

        print(
            f"Internship cards found: {len(internships)}"
        )

        results = []

        for internship in internships:

            try:
                text = internship.get_text(
                    " ",
                    strip=True
                )

                title = text.split(
                    "Actively hiring"
                )[0].strip()

                # Filter only using title
                if keyword not in title.lower():
                    continue

                location = "N/A"

                location_tag = internship.find(
                    "div",
                    class_="locations"
                )

                if location_tag:
                    location = location_tag.get_text(
                        " ",
                        strip=True
                    )

                stipend = "N/A"

                stipend_tag = internship.find(
                    "span",
                    class_="stipend"
                )

                if stipend_tag:
                    stipend = stipend_tag.get_text(
                        strip=True
                    )

                duration = "N/A"

                row_items = internship.find_all(
                    "div",
                    class_="row-1-item"
                )

                if len(row_items) >= 3:
                    duration = row_items[2].get_text(
                        " ",
                        strip=True
                    )

                link = (
                    "https://internshala.com"
                    + internship.get(
                        "data-href",
                        ""
                    )
                )

                print(f"Matched: {title}")

                results.append([
                    title,
                    location,
                    stipend,
                    duration,
                    link
                ])

            except Exception:
                continue

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
                "Location",
                "Stipend",
                "Duration",
                "Link"
            ])

            writer.writerows(results)

        print(
            f"\nSaved {len(results)} matching internships"
        )

        print(
            f"CSV File Created: {CSV_FILE}"
        )

    except requests.exceptions.ConnectionError:
        print("No internet connection.")

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except Exception as e:
        print(
            f"Unexpected Error: {e}"
        )


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

    print("\n=================================")
    print("Scheduler Running")
    print("=================================")
    print("Next run: Every day at 09:00 AM")
    print("Waiting for scheduled tasks...")
    print("Press Ctrl + C to exit\n")

    while True:
        schedule.run_pending()
        time.sleep(60)

else:
    print("Invalid choice")