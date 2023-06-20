from bs4 import BeautifulSoup
import requests
import csv

results = requests.get('https://www.journalismjobs.com/job-listings')
soup = BeautifulSoup(results.text, 'html.parser')
jobs = soup.find_all('a', class_='job-item')

job_title_lst = []
job_company_lst = []
job_location_lst = []
job_type_lst = []
job_date_lst = []
job_desc_lst = []

for job in jobs:
    job_title = job.find('h3', class_='job-item-title').text
    job_company = job.find('div', class_='job-item-company').text
    job_details = job.find('ul', class_='job-item-details').find_all('li')
    job_location = job_details[0].text.strip()
    job_type = job_details[1].text.strip()
    job_date = job_details[2].text.strip()
    job_desc = job.find('div', class_='job-item-description').text.strip()

    job_title_lst.append(job_title)
    job_company_lst.append(job_company)
    job_location_lst.append(job_location)
    job_type_lst.append(job_type)
    job_date_lst.append(job_date)
    job_desc_lst.append(job_desc)

with open('journalism_job_lists.csv', 'w') as job_file:
    csv_writer = csv.writer(job_file)
    for title, company, location, types, date, desc in zip(job_title_lst, job_company_lst, job_location_lst,
                                                           job_type_lst, job_date_lst, job_desc_lst):
        csv_writer.writerow([title, company, location, types, date, desc])
