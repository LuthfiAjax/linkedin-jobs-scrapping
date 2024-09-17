import logging
import json
import os
import time
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData, EventMetrics
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters, OnSiteOrRemoteFilters, SalaryBaseFilters
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime

li_at_cookie = "###"  # fill with your browser cookies

logging.basicConfig(level=logging.INFO)

results = []

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=chrome_options)


def set_cookie(driver):
    driver.get('https://www.linkedin.com')
    driver.add_cookie({
        'name': 'li_at',
        'value': li_at_cookie,
        'domain': '.linkedin.com'
    })


def on_data(data: EventData):
    job_data = {
        'job_id': data.job_id if data.job_id else '',
        'link': data.link if data.link else '',
        'apply_link': data.apply_link if data.apply_link else '',
        'title': data.title if data.title else '',
        'company': data.company if data.company else '',
        'company_link': data.company_link if data.company_link else '',
        'company_img_link': data.company_img_link if data.company_img_link else '',
        'place': data.place if data.place else '',
        'description': data.description if data.description else '',
        'date': data.date if data.date else '',
        'insights': data.insights if data.insights else '',
        'skills': data.skills if data.skills else '',
    }
    results.append(job_data)


def on_metrics(metrics: EventMetrics):
    print('[PAGE METRICS]', metrics)


def on_error(error):
    print('[ERROR]', error)


def on_end():
    if not os.path.exists('results'):
        os.makedirs('results')

    filename = datetime.now().strftime("results/%Y-%m-%d_%H-%M-%S.json")

    with open(filename, 'w') as f:
        json.dump(results, f, indent=4)

    print(f'[SCRAPING ENDED] Results saved to {filename}')


scraper = LinkedinScraper(
    chrome_executable_path=None,
    chrome_binary_location=None,
    chrome_options=chrome_options,
    headless=True,
    max_workers=1,
    slow_mo=6.0,
    page_load_timeout=60
)

scraper.on(Events.DATA, on_data)
scraper.on(Events.ERROR, on_error)
scraper.on(Events.END, on_end)

queries = [
    Query(
        query='Software Engineer',
        options=QueryOptions(
            locations=['Jakarta, Indonesia'],
            apply_link=True,
            skip_promoted_jobs=True,
            limit=2,
            filters=QueryFilters(
                relevance=RelevanceFilters.RECENT,
                time=TimeFilters.MONTH,
                type=[TypeFilters.FULL_TIME],
                on_site_or_remote=[OnSiteOrRemoteFilters.REMOTE],
                experience=[ExperienceLevelFilters.MID_SENIOR],
                base_salary=SalaryBaseFilters.SALARY_100K
            )
        )
    )
]

scraper.run(queries)

driver.quit()
