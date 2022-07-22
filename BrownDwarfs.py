from numpy import append
import requests
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd

URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"


titles = ["Brown Dwarf", "Constellation", "Declination", "Distance", "Mass", "Radius"]
stars = []

r = requests.get(url = URL)

soup = BeautifulSoup(r.content, "html.parser")

table = soup.find_all('table')

table_rows = table[7].find_all('tr')
temp = []

for tr in table_rows:
    td = tr.find_all('td')
    row = []
    for i in td:
        row.append(i.text.rstrip())
    temp.append(row)

Brown_dwarf = []
Constellion = []
Declination = []
Distance = []
Mass = []
Radius = []

for i in range(1,len(temp)):
    Brown_dwarf.append(temp[i][0])
    Constellion.append(temp[i][1])
    Declination.append(temp[i][3])
    Distance.append(temp[i][5])
    Mass.append(temp[i][7])
    Radius.append(temp[i][8]) 

brownDf = pd.DataFrame(list(zip(Brown_dwarf, Constellion, Declination ,Distance ,Mass ,Radius)),
    columns=['Brown Dwarf', 'Constellation', 'Declination', 'Distance', 'Mass', 'Radius'])

brownDf.to_csv('Brown Dwarfs.csv')
