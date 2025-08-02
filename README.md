# 🏛️ Court Data Fetcher & Mini Dashboard

A full-stack web application that lets users search for Delhi High Court case metadata by case type, number, and filing year. This project was built as part of an AI internship assignment and demonstrates end-to-end web scraping, data logging, and frontend design.

---

## 🚀 Demo

https://user-demo-video-link.com (Add your Loom/YouTube link here)

---

## 📌 Features

- 🔎 Search by **Case Type**, **Case Number**, and **Filing Year**
- 🧠 Scraping powered by **Selenium + undetected-chromedriver** (for stealth)
- 🖼️ Responsive, modern UI using HTML + CSS (Google Fonts + cool theme)
- 🧾 Fetch simulated metadata:
  - Petitioner & Respondent
  - Filing Date & Next Hearing Date
  - PDF link to latest order/judgment
- 💾 Logs all queries to **SQLite database**
- ❌ Graceful error handling for timeouts or invalid input
- ⚙️ Ready-to-run on local server (Flask)

---

## 🎯 Target Website

Delhi High Court Official Website:  
🔗 [https://delhihighcourt.nic.in](https://delhihighcourt.nic.in)

---

## 🧠 Tech Stack

| Layer        | Tools Used                             |
|--------------|----------------------------------------|
| Backend      | Python + Flask                         |
| Web Scraper  | Selenium + undetected-chromedriver     |
| Frontend     | HTML, CSS, Google Fonts                |
| Database     | SQLite                                 |
| Deployment   | Localhost via Flask dev server         |

---

## 📂 Project Structure
court-data-fetcher-dashboard/
├── app.py # Flask app entry point
├── scraper.py # Court website scraper (Delhi High Court)
├── database.py # Logs all queries to SQLite
├── init_db.py # One-time script to initialize DB
├── requirements.txt # Python dependencies
├── templates/ # HTML templates
│ ├── index.html
│ └── result.html
├── models/
│ └── case_log.db # SQLite DB file (created on run)
├── static/
│ └── favicon.ico # (Optional)
└── README.md

## 🛠️ Installation & Setup

1. **Clone the repo:**
```bash
git clone https://github.com/your-username/Court-data-fetcher-dashboard.git
cd Court-data-fetcher-dashboard
```
## 🙏 Acknowledgements

- [Delhi High Court](https://delhihighcourt.nic.in) public website – for openly available case metadata
- Python open-source ecosystem – including Flask, Selenium, and undetected-chromedriver
- **Internship assignment** by *Think Act Rise Foundation* – for framing the project challenge

---

## 💡 Future Improvements

- 🎯 **Real scraping with CAPTCHA bypass** using 2Captcha or AI models
- 🧾 **Paginated results** to show complete case history or orders
- 📊 **Charts & data visualization** of case frequency, delays, etc.
- ☁️ **Deploy to cloud** (Render/Heroku) with Docker & persistent database
