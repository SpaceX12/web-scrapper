import requests
from bs4 import BeautifulSoup
import time
import csv

URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
r = requests.get(URL)

def scrape():
    titles = ["Proper Name", "Bayer designation", "Distance", "Spectral Class", "Mass", "Radius", "Luminosity"]
    stars = []

    r = requests.get(url = URL)
    
    soup = BeautifulSoup(r.content, "html.parser")
    ults = soup.find_all("tr")[1].contents[1]

    for ult in ults :
        td_tags = soup.find_all("td")
        temp = []

        for index, td_tag in enumerate(td_tags):
            if index == 1:
                temp.append(td_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp.append(td_tag.contents[0])
                except:
                    temp.append("")
                    
            stars.append(temp)
    
    with open("StarResearch.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(titles)
        writer.writerows(stars)

scrape()

