from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://colombia.as.com/resultados/futbol/colombia_ii/clasificacion/"
page = requests.get(url)
# Formatting the content as html
soup = BeautifulSoup(page.content, 'html.parser')

#Team names
names = soup.find_all('span', class_='nombre-equipo')
team_names = list()

count = 0
for team in names:
    if count < 20:
      team_names.append(team.text)
    else:
       break
    count+=1
    
print(team_names)