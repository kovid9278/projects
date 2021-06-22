import sys
import time
import requests
from bs4 import BeautifulSoup

response = requests.get('https://phones-calls.com/state-index/aux-nevada?page=1')
html     = response.text
soup     = BeautifulSoup(html,'html.parser')
data1    = soup.find_all('a', {'class' : ''})
x        = len(data1)
file_list= []
for y in range(1,x):
    url = 'https://phones-calls.com' + data1[y]['href']    
    response = requests.get(url)
    html     = response.text
    soup     = BeautifulSoup(html,'html.parser')
    data     = soup.find_all('tr')
    z        = len(soup.find_all('tr'))
    for i in range(1,z) :
        data_dict    = {}
        info                  = data[i].find_all('td')
        data_dict['name']     = info[0].text
        data_dict['phone']    = info[1].text
        data_dict['address']  = info[2].text
        if len(url.split('/')[-1].split('-')) == 4:
            data_dict['city']     = url.split('/')[-1].split('-')[0]
            data_dict['state']    = url.split('/')[-1].split('-')[1]
            data_dict['area_code']= url.split('/')[-1].split('-')[2]
            data_dict['prefix']   = url.split('/')[-1].split('-')[3]
            data_dict['phn_Code'] = url.split('/')[-1].split('-')[2] + '-' + url.split('/')[-1].split('-')[3]
        else :
            data_dict['city']     = url.split('/')[-1].split('-')[0] + ' ' + url.split('/')[-1].split('-')[1]
            data_dict['state']    = url.split('/')[-1].split('-')[2]
            data_dict['area_code']= url.split('/')[-1].split('-')[3]
            data_dict['prefix']   = url.split('/')[-1].split('-')[-1]
            data_dict['phn_Code'] = url.split('/')[-1].split('-')[3] + '-' + url.split('/')[-1].split('-')[-1]
        
        file_list.append(data_dict)
        
import pandas as pd 
phn_db = pd.DataFrame(file_list)
phn_db.to_csv('aux nevada page 1.csv')
