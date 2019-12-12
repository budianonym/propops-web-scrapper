import pandas as pd  
import requests
from bs4 import BeautifulSoup
from list import listing_id

#set up some array to gather looping result
url = [] 
active = [] 

#starting looping
for id in listing_id:
    r= requests.get(id)
    soup= BeautifulSoup(r.content, "lxml")

    #append sooping result into array 
    url.append(id)
    active.append(soup.active.string) #active meann we scrap <active> field, string means we only grap the string without <active></active>

# dictionary of lists  , url and status are the header. header url contain arrayurl, status header contain arrayactive
dict = {'url': url, 'status': active}  
     
df = pd.DataFrame(dict) 
  
# saving the dataframe 
df.to_csv('mmz.csv')