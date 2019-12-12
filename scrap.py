import pandas as pd  
import requests
from bs4 import BeautifulSoup

#set up some array to gather looping result
url = [] 
active = [] 

#data for array for scrapping
listing_id = ["https://www.resortpro.net/redawning-api/1.0/getListing.php?listing_id=37695&code=1c7ghi","https://www.resortpro.net/redawning-api/1.0/getListing.php?listing_id=37681&code=1c7ghi","https://www.resortpro.net/redawning-api/1.0/getListing.php?listing_id=37701&code=1c7ghi","https://www.resortpro.net/redawning-api/1.0/getListing.php?listing_id=37704&code=1c7ghi","https://www.resortpro.net/redawning-api/1.0/getListing.php?listing_id=37672&code=1c7ghi"]

#starting looping
for id in listing_id:
    r= requests.get(id)
    soup= BeautifulSoup(r.content, "lxml")

    # append sooping result into array 
    url.append(id)
    active.append(soup.active.string) #active meann we scrap <active> field, string means we only grap the string without <active></active>

# dictionary of lists  , url and status are the header. header url contain arrayurl, status header contain arrayactive
dict = {'url': url, 'status': active}  
     
df = pd.DataFrame(dict) 
  
# saving the dataframe 
df.to_csv('mmz.csv')