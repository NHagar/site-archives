#%%
import csv
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

#%%
#Initial links from front page
r = requests.get('https://gawker.com/')
html = BeautifulSoup(r.text, 'html.parser')
links = [i.a['href'] for i in html.find_all('h1')]

#%%
#Links from following pages
for i in tqdm(range(1,9470)):
    r = requests.get('https://gawker.com/page_{}'.format(i))
    html = BeautifulSoup(r.text, 'html.parser')
    links.extend([j.a['href'] for j in html.find_all('h1')])

with open('gawker/links.csv', 'w', newline='', encoding='utf-8') as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    wr.writerow(links)
