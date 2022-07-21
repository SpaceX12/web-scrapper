import requests
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd

URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"


titles = ["Proper Name", "Bayer designation", "Distance", "Spectral Class", "Mass", "Radius", "Luminosity"]
stars = []

r = requests.get(url = URL)

soup = BeautifulSoup(r.content, "html.parser")
#print(soup)
table = soup.find('table')
#print(table)

tr_tags = table.find_all('tr')
#print(tr_tags)
temp = []

for tr in tr_tags:
    td = tr.find_all('td')
    row = []
    for i in td:
        row.append(i.text.rstrip())
    temp.append(row)
print(temp)

Star_names = []
Distance =[]
Mass = []
Radius =[]
Lum = []

for i in range(1,len(temp)):
    Star_names.append(temp[i][1])
    Distance.append(temp[i][3])
    Mass.append(temp[i][5])
    Radius.append(temp[i][6])
    Lum.append(temp[i][7])


df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df2)

df2.to_csv('bright_stars.csv')
