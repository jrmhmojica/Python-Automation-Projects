#IMPORT MODULES
from gettext import find
import requests
from bs4 import BeautifulSoup
import pandas as pd

#INITIALIZE EMPTY LIST
joblist = []

#EXTRACT HTML
def extract(page):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}
    url = f"https://ph.indeed.com/jobs?q=data+analyst&start={page}"
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

#TRANSFORM HTML TO THE CONTENT THAT WE WANT
def transform(soup):
    tds = soup.find_all('td', class_ = "resultContent")
    for item in tds:
        title = item.find('a').text
        company = item.find('span', class_ = "companyName").text
        location = item.find('div', class_ = "companyLocation").text
        try:
            salary = item.find('div', class_ = "metadata salary-snippet-container").text
        except:
            salary = 'Information not available'

        job = {
            'title' : title,
            'company' : company,
            'location' : location,
            'salary' : salary
        }
        joblist.append(job)

#LOOPING THROUGHT THE PAGES
for i in range(0,60,10):
    content = extract(i)
    transform(content)

#PUTTING JOBS INTO A DATAFRAME
df = pd.DataFrame(joblist)

#CREATING A CSV FILE
path = "C:\\Users\\jayja\\OneDrive\\Documents\\Python\\Projects\\Automation Projects\\Indeed Scraper\\"
df.to_csv(path+"indeed_jobs.csv")