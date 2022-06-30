#IMPORT MODULES
import requests
from bs4 import BeautifulSoup
import pandas as pd
import config as c

#INITIALIZE EMPTY LIST
show_list = []

#EXTRACTING THE HTML CONTENT
def extract():
    url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
    headers = {'User-Agent' : c.ua}
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

#TRANSFORMING THE HTML ACCORDING TO REQUIREMENT
def transform(soup):
    show_container = soup.find('tbody', class_ = "lister-list")
    shows = show_container.find_all('tr')

    for item in shows:
        rank_title_year = item.find('td', class_ = "titleColumn").text.strip().replace("\n"," ")
        rank = rank_title_year[:3].strip(" .")
        year = rank_title_year[-5:-1]
        title = rank_title_year.strip(f"().{rank}{year} ")
        rating = item.find('td', class_ = "imdbRating").text.strip()
        
        show = {
            'RANK' : rank,
            'TITLE' : title,
            'YEAR' : year,
            'RATING' : rating
        }

        show_list.append(show)

#CALLING THE FUNCTIONS
content = extract()
transform(content)

#CONVERTING TO CSV FILE
df = pd.DataFrame(show_list)
path = (c.file_path + "IMDB Top 250 Shows Scraper/")
df.to_csv(path + "imdbtop250shows.csv", index=False)