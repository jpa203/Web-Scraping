from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.ncaa.com/rankings/soccer-women/d1/ncaa-womens-soccer-rpi'

result = requests.get(url)

soup = BeautifulSoup(result.text,'html.parser')

check = soup.find_all('tr')

names_lst = []
conference_lst = []
record_lst = []


for info in check[1:]:
    details = info.find_all('td')
    names = details[1].text.strip()
    conference = details[2].text.strip()
    record = details[3].text.strip()

    names_lst.append(names)
    conference_lst.append(conference)
    record_lst.append(record)

print(names_lst)
print(conference_lst)
print(record_lst)

with open ('ncaa_rankings.csv', 'w') as ncaa_file:
    csv_writer = csv.writer(ncaa_file)
    for names, conference, record in zip(names_lst, conference_lst, record_lst):
        csv_writer.writerow([names, conference, record])
