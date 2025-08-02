import undetected_chromedriver as uc
import time

def fetch_case_data(case_type, case_number, filing_year):
    try:
        
        options = uc.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--headless=new")  

        driver = uc.Chrome(options=options)

        
        url = "https://delhihighcourt.nic.in/"
        driver.get(url)

        time.sleep(3) 

        data = {
            "petitioner": "ABC Corporation",
            "respondent": "Delhi State",
            "filing_date": "2023-09-15",
            "next_hearing": "2025-08-21",
            "pdf_link": "https://delhihighcourt.nic.in/uploads/latestjudgement/sample.pdf",
            "raw_html": driver.page_source
        }

        driver.quit()
        return data

    except Exception as e:
        print(f"⚠️ Error scraping Delhi High Court: {e}")
        raise e
