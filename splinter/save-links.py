#%%
import csv
import requests
from bs4 import BeautifulSoup

#%%
start_link = 'https://splinternews.com'

r = requests.get(start_link)
soup = BeautifulSoup(r.text)
links = [i.parent['href'] for i in soup.find_all('h1') if i.parent.name=='a']

next_link = 'https://splinternews.com/{}'.format(soup.find('button', {'class': 'button--tertiary'}).parent['href'])

#%%
next = True
while next==True:
    r = requests.get(next_link)
    soup = BeautifulSoup(r.text)
    links.extend([i.parent['href'] for i in soup.find_all('h1') if i.parent.name=='a'])
    try:
        next_link = 'https://splinternews.com/{}'.format(soup.find('button', {'class': 'button--tertiary'}).parent['href'])
    except Exception:
        next = False

#%%
with open('splinter/links.csv', 'w', newline='', encoding='utf-8') as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    wr.writerow(links)


#%%
len(set([i for i in links if 'splinternews.com' in i]))
