import requests
from bs4 import BeautifulSoup
from csv import writer
import pandas as pd 

empty = []
empty_2 = []
scientific = []
URL = "https://plants.ces.ncsu.edu/find_a_plant/"
page = requests.get(URL)

# bs4 reads the HTML for us
soup = BeautifulSoup(page.content, "html.parser")

# here i am getting bs4 to find all divs with a certain class in the html
sci = soup.find_all("div", class_="plant_1_1")
# this loops finds all h2's inside of the class specified
for plant in sci:
    name = soup.find_all("h2")
    
    for name in name:
        name.find_all("em")
        empty.append(name.text)


common = soup.find_all("span", class_="common_names")
for plant in common:
    name = soup.find_all("span", class_="list_common_names")
    for name in name:
        name.find_all("a")
        empty_2.append(name.text)
        
# removing duplicates 
res2 = []
for i in empty_2:
    if i not in res2:
        res2.append(i)

# removing duplicates
res = []
for i in empty:
    if i not in res:
        res.append(i)

res.remove(' Find a PlantShow Menu')

for element in res:
    scientific.append(element.strip())


scientific.remove('Where Next?')
print(scientific)

#pandas puts it all in a nice little csv
dict = {'Scientific Name': scientific, 'Common Name': res2}
df = pd.DataFrame(dict)
df.to_csv('plants.csv')
