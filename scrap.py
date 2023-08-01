from bs4 import BeautifulSoup
import requests
import pandas as pandas


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


#Points 
points = soup.find_all('td', class_='destacado')
team_points = list()

count = 0
for point in points:
    if count < 20:
      team_points.append(point.text)
    else:
       break
    count+=1


data_frame = pandas.DataFrame({'Name': team_names, 'Points': team_points}, index = list(range(1, 21)) )  
print(data_frame)