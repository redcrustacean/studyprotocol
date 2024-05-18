


print("Running...")

import requests
import re 
from bs4 import BeautifulSoup

print("Please input NCT number..  INCLUDE letters NCT")
nctnumber = input()

print("You have entered ",nctnumber)


# URL of the ClinicalTrials.gov study page 
#JL - need to concatenate nctnumber to general url
url = "https://classic.clinicaltrials.gov/ct2/show/"
url = url + nctnumber
print(url)

urlprefix = 'https://classic.clinicaltrials.gov'
# Send a GET request to the page
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful

# Parse the page content
soup = BeautifulSoup(response.text, 'html.parser')


links = soup.find_all('a')
for link in soup.find_all('a', href=True):
    if link['href'].lower().endswith(".pdf"):
        print(urlprefix + link['href'])

       #  print('https://classic.clinicaltrials.gov' + link['href'])
        response = requests.get(urlprefix + link.get('href'))
        pdf = open(f"protocol{nctnumber}.pdf", 'wb')
        pdf.write(response.content)
        # pdf.close()
        # print("File ", i, " downloaded")


print("PDF file downloaded")

