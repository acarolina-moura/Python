import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url="https://www.accuweather.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
r= requests.get(url, headers=headers)


soup = BeautifulSoup(r.content, 'html5lib')


data=[]

for mainrow in soup.findAll('div', attrs = {'class':['nearby-locations-list']}):
    for row in mainrow.findAll('a', attrs = {'class':['nearby-location weather-card']}):
      
        location = row.find('span', attrs = {'class':'text title no-wrap'}).get_text().strip()
        temp = row.find('span', attrs = {'class':'text temp'}).get_text().strip()
                
               
        one = {} 
        one['localização']=location
        one['temperatura']=temp
                  
        data.append(one)

df=pd.DataFrame(data)
print(df)
df.to_csv("temperaturas.csv",index="False",encoding="utf-8-sig")
