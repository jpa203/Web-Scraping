from bs4 import BeautifulSoup
import requests
import csv

urls = ''

with open('websites.txt', 'r') as f:
    for line in f.read():
        urls += line

urls = list(urls.split())

name_lst = []
position_lst = []
email_lst = []

for url in urls:

    print(f'CURRENTLY PARSING: {url}')
    print()

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    try:
        for information in soup.find_all('tr', class_='sidearm-staff-member'):
            names = information.find("th", attrs={'headers': "col-fullname"}).text.strip()
            positions = information.find("td", attrs={'headers': "col-staff_title"}).text.strip()
            emails = information.find("td", attrs={'headers': "col-staff_email"}).script
            target = emails.text.split('var firstHalf = "')[1]
            fh = target.split('";')[0]
            lh = target.split('var secondHalf = "')[1].split('";')[0]
            emails = fh + '@' + lh

            name_lst.append(names)
            position_lst.append(positions)
            email_lst.append(emails)


    except Exception as e:
        print(f'For {names}, this URL did not work {url}')
        print()


with open('athletic_department_information.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    for name, position, email in zip(name_lst, position_lst, email_lst):
        if 'Communication' in position:
            csv_writer.writerow([name, position, email])
