import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time

CSV_FILE = "internships.csv"


def scrape_jobs():
    print("\n=================================")
    print("Starting Internship Scraper...")
    print("=================================\n")

    keyword = input(
        "Enter keyword (Python, Data Analyst, ML): "
    ).strip().lower()

    url = f"https://internshala.com/internships/keywords-{keyword}/"

    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        print("Fetching webpage...")

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        cards = soup.find_all(
            "div",
            attrs={"internshipid": True}
        )

        print(
            f"Internship cards found: {len(cards)}"
        )

        results = []

        for card in cards:

            try:
                text = card.get_text(
                    " ",
                    strip=True
                )

                if "Actively hiring" in text:
                    title = text.split(
                        "Actively hiring"
                    )[0].strip()
                else:
                    title = text[:100].strip()

                words = title.split()

                if len(words) > 8:
                    title = " ".join(words[:8])

                search_terms = keyword.split()

                title_lower = title.lower()

                if not any(
                    term in title_lower
                    for term in search_terms
                ):
                    continue
                location = "N/A"
                location_tag = card.find(
                    "div",
                    class_="locations"
                )
                if location_tag:
                    location = location_tag.get_text(
                        " ",
                        strip=True
                    )

                stipend = "N/A"

                stipend_tag = card.find(
                    "span",
                    class_="stipend"
                )
                if stipend_tag:
                    stipend = stipend_tag.get_text(
                        strip=True
                    )

                duration = "N/A"

                words = text.split()

                for i in range(len(words)):
                    if words[i] in [
                        "Month",
                        "Months"
                    ]:
                        if i > 0:
                            duration = (
                                words[i - 1]
                                + " "
                                + words[i]
                            )
                        break

                link = (
                    "https://internshala.com"
                    + card.get(
                        "data-href",
                        ""
                    )
                )

                print(f"Found: {title}")

                results.append({
                    "Title": title,
                    "Location": location,
                    "Stipend": stipend,
                    "Duration": duration,
                    "Link": link
                })

            except Exception as e:
                print(
                    f"Skipped card: {e}"
                )

        if len(results) == 0:
            print(
                f"No internships found for '{keyword}'"
            )
            return

        df = pd.DataFrame(results)

        df.drop_duplicates(
            subset=["Title", "Link"],
            inplace=True
        )

        df.to_csv(
            CSV_FILE,
            index=False,
            encoding="utf-8"
        )

        print(
            f"\nSaved {len(df)} internships"
        )

        print(
            f"CSV Updated: {CSV_FILE}"
        )

    except requests.exceptions.ConnectionError:
        print("No internet connection.")

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except Exception as e:
        print(f"Error: {e}")


def scheduled_job():
    print("\nRunning scheduled scrape...")
    scrape_jobs()


print("1. Run Now")
print("2. Daily Scheduler")

choice = input(
    "Choose option: "
)

if choice == "1":

    scrape_jobs()

elif choice == "2":

    schedule.every().day.at(
        "09:00"
    ).do(scheduled_job)

    print("\n=================================")
    print("Scheduler Running")
    print("=================================")
    print("Next Run: Every Day at 09:00 AM")
    print("Press Ctrl + C to Exit\n")

    while True:
        schedule.run_pending()
        time.sleep(60)

else:
    print("Invalid choice")