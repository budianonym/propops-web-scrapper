import pandas as pd 
import requests
from bs4 import BeautifulSoup
import time

data = pd.read_csv("mmz.csv") 
datatodictionary = data.to_dict()['url']
sources = []

for i in datatodictionary:
    sources.append(datatodictionary[i])

timenow = int(time.time())
#set up some array to gather looping result
url = []
active = []

#starting looping
for id in sources:
    r = requests.get(id)
    soup = BeautifulSoup(r.content, "html.parser")

    #append sooping result into array
    url.append(id)
    # active mean we scrap <active> field, string means we only grap the string without <active></active>
    active.append(soup.active.string)

# dictionary of lists  , url and status are the header. header url contain arrayurl, status header contain arrayactive
dict = {'url': url, 'status': active}

df = pd.DataFrame(dict)

# saving the dataframe, adding current timestamp to unique file name
df.to_csv('result{}.csv'. format(timenow))