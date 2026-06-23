# Smart Internship Scraper

A Python-based web scraping and automation tool that fetches internship opportunities from Internshala based on user-defined keywords and exports the results into a structured CSV file.

---

## Features

* Search internships using custom keywords (Python, Data Analyst, Machine Learning, etc.)
* Extract internship details automatically
* Save results to a CSV file
* Generate direct internship application links
* Daily scheduler support for automated scraping
* Network timeout and error handling
* Lightweight and easy to use

---

## Technologies Used

* Python 3
* Requests
* BeautifulSoup4
* CSV
* Schedule

---

## Project Workflow

```text
User Enters Keyword
        ↓
Send HTTP Request to Internshala
        ↓
Download Webpage HTML
        ↓
Parse HTML using BeautifulSoup
        ↓
Extract Internship Listings
        ↓
Filter Relevant Results
        ↓
Store Data in CSV
        ↓
(Optional) Run Automatically Every Day
```

---

## Project Structure

```text
Smart-Internship-Scraper/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── page.html
└── internships.csv
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Internship-Scraper.git
cd Smart-Internship-Scraper
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Run the scraper:

```bash
python main.py
```

Choose one of the available options:

```text
1. Run Now
2. Daily Scheduler
```

Enter a keyword:

```text
Python
Data Analyst
Machine Learning
AI
Web Development
```

---

## Sample Terminal Output

```text
=================================
Starting Internship Scraper...
=================================

Enter keyword: Data Analyst

Fetching webpage...
Internship cards found: 94

Matched: Teacher for Data Analyst Course
Matched: MIS Lead Handling And Data Analyst

Saved 2 matching internships
CSV File Created: internships.csv
```

---

## Sample CSV Output

```csv
Title,Location,Stipend,Duration,Link
Teacher for data analyst course Krutrim Insights,Delhi (Hybrid),₹12,000/month,2 Months,...
MIS- Lead Handling And Data Analyst BNM Business Solutions LLP,Mumbai,₹9,000/month,3 Months,...
```

---

## Scheduler Mode

The application can automatically run every day using the built-in scheduler.

Example:

```python
schedule.every().day.at("09:00").do(scrape_jobs)
```

This helps users monitor new internship opportunities without manually running the script.

---

## Error Handling

The scraper handles:

* Internet connection failures
* Request timeouts
* Invalid server responses
* Unexpected runtime exceptions

---

## Learning Outcomes

This project helped develop practical experience in:

* Web Scraping
* HTTP Requests
* HTML Parsing
* Data Extraction
* Python Automation
* CSV File Handling
* Task Scheduling
* Git & GitHub

---

## Future Improvements

* Excel (.xlsx) Export
* Email Notifications
* Internship Ranking System
* Company Name Extraction
* Database Integration
* Flask Web Interface
* AI-Based Internship Recommendations

---

## Author

**Arpit Aggarwal**

B.Tech Student | Delhi Technological University (DTU)

Interested in Software Development, Automation, AI/ML, and Data Science.

---

## License

This project is intended for educational and learning purposes.
