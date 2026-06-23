# Smart Internship Scraper

A Python-based automation tool that scrapes internship listings from Internshala based on user-defined keywords and exports the results to a CSV file for easy analysis and tracking.

---

## Overview

Smart Internship Scraper automates the process of searching for internships by fetching listings directly from Internshala, filtering them according to a keyword, and storing relevant information such as location, stipend, duration, and application links.

This project demonstrates practical skills in:

* Web Scraping
* Data Extraction
* Python Automation
* CSV File Handling
* Task Scheduling
* Error Handling

---

## Features

✅ Search internships using custom keywords

✅ Extract internship details automatically

✅ Save results in CSV format

✅ Generate direct application links

✅ Daily scheduled scraping support

✅ Handles network errors and timeouts gracefully

✅ Lightweight and beginner-friendly

---

## Technologies Used

* Python 3
* Requests
* BeautifulSoup4
* CSV
* Schedule

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

### Clone Repository

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

Run the application:

```bash
python main.py
```

Choose an option:

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

The scraper will fetch matching internships and save them to:

```text
internships.csv
```

---

## Sample Output

### Terminal Output

```text
Starting Internship Scraper...

Enter keyword: Data Analyst

Fetching webpage...
Internship cards found: 94

Matched: Teacher for Data Analyst Course
Matched: MIS Lead Handling And Data Analyst

Saved 2 matching internships
CSV File Created: internships.csv
```

### CSV Output

| Title                              | Location            | Stipend       | Duration |
| ---------------------------------- | ------------------- | ------------- | -------- |
| Teacher for Data Analyst Course    | Delhi (Hybrid)      | ₹12,000/month | 2 Months |
| MIS Lead Handling And Data Analyst | Mumbai, Navi Mumbai | ₹9,000/month  | 3 Months |

---

## Scheduler Mode

The scraper can be configured to run automatically every day.

Example:

```python
schedule.every().day.at("09:00").do(scrape_jobs)
```

Useful for monitoring new internship opportunities without manual searching.

---

## Error Handling

The project includes handling for:

* Internet connection failures
* Request timeouts
* Invalid responses
* Unexpected exceptions

---

## Future Improvements

* Export results to Excel (.xlsx)
* Email notifications
* Internship ranking by relevance
* Stipend-based filtering
* Company name extraction
* Database integration
* AI-powered internship recommendations
* Web dashboard using Flask

---

## Learning Outcomes

Through this project, I gained hands-on experience in:

* Web scraping using BeautifulSoup
* HTTP requests using Requests
* Data storage using CSV
* Python automation workflows
* Scheduling recurring tasks
* Git and GitHub version control

---

## Author

Arpit Aggarwal

B.Tech Student | Delhi Technological University (DTU)

Interested in Software Development, Automation, AI/ML, and Data Science.

---

## License

This project is intended for educational and learning purposes.
