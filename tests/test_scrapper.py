# import module
import re

import requests
from bs4 import BeautifulSoup

from get_html import get_html


# user define function
# Scrape the data
# and get in string
def getdata(url):
    r = requests.get(url)
    return r.text


# Get Html code using parse
def html_code(url):
    # pass the url
    # into getdata function
    # htmldata = getdata(url)
    htmldata = get_html(url)
    # print(htmldata)
    soup = BeautifulSoup(htmldata,  'html.parser')
    # return html code
    return soup


# filter job data using
# find_all function
def job_data(soup):
    # find the Html tag
    # with find()
    # and convert into string
    job_name_data = []
    for item in soup.find_all("h2", class_=re.compile('^jobTitle')):
        job_name_data.append(item.get_text())
    return job_name_data


# filter company_data using
# find_all function


def company_data(soup):
    # find the Html tag
    # with find()
    # and convert into stringdata-testid="company-name"
    company_data = []
    for item in soup.find_all('span', attrs={'data-testid': 'company-name'}):
        company_data.append(item.get_text())

    address_data = []
    for item in soup.find_all("div", attrs={'data-testid': 'text-location'}):
        address_data.append(item.get_text())

    return list(zip(company_data, address_data))


# driver nodes/main function
if __name__ == "__main__":

    # Data for URL
    job = "data+science+internship+python"
    Location = "krakow"
    url = "https://pl.indeed.com/jobs?q=" + job + "&l=" + Location
    print(url)
    # Pass this URL into the soup
    # which will return
    # html string
    soup = html_code(url)
    # call job and company data
    # and store into it var
    job_res = job_data(soup)
    com_res = company_data(soup)

    # Traverse the both data
    for i in range(1, len(job_res)):
        print("Company Name and Address : " + com_res[i][0] + " :: " + com_res[i][1])
        print("Job : " + job_res[i])
        print("-----------------------------")

    print(f'\n Find {len(job_res)} jobs and {len(com_res)} companies')