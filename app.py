from flask import Flask, render_template, request
from scraper import fetch_case_data
from database import log_query
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/fetch", methods=["POST"])
def fetch():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    filing_year = request.form['filing_year']

    try:
        data = fetch_case_data(case_type, case_number, filing_year)
        log_query(case_type, case_number, filing_year, data['raw_html'])
        return render_template("result.html", data=data)
    except Exception as e:
        return render_template("result.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)