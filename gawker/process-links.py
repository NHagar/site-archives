#%%
import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

#%%
with open('./gawker/links.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        links = row

#%%
links = ['https://gawker.com{}'.format(i) for i in links]

#%%
test = requests.get('https://gawker.com/heroic-uhhh-pharmaceutical-company-savagely-undercu-1738185665')
soup = BeautifulSoup(test.text, 'html.parser')
soup.find('h1').text
soup.find("div", {"class": "meta__views"}).text
';'.join([i.text for i in soup.find('div', {'class': 'taglist'}).find_all('li')])
soup.find('div', {'class': 'meta__byline'}).text
soup.find('time')['datetime']
soup.find('article').get_text()
soup.find('div', {'class': 'post-content'}).get_text()
soup
#%%
results = []
for l in tqdm(list(set(links))):
    soup = BeautifulSoup(requests.get(l).text, 'html.parser')
    try:
        hed = soup.find('h1').text
    except AttributeError:
        hed = ''
    try:
        pageviews = soup.find("div", {"class": "meta__views"}).text
    except AttributeError:
        pageviews = ''
    try:
        sections = ';'.join([i.text for i in soup.find('div', {'class': 'taglist'}).find_all('li')])
    except AttributeError:
        sections = ''
    try:
        byline = soup.find('div', {'class': 'meta__byline'}).text
    except AttributeError:
        byline = ''
    try:
        pub_date = soup.find('time')['datetime']
    except AttributeError:
        pub_date = ''
    try:
        html_body = soup.find('div', {'class': 'post-content'}).encode_contents()
    except AttributeError:
        html_body = ''
    try:
        raw_body = soup.find('div', 'm-detail--body').get_text()
    except AttributeError:
        raw_body = ''
    try:
        tags = ';'.join([i.text for i in soup.find('dd', 'm-detail--keywords').children])
    except AttributeError:
        tags = ''
    results.append({'link': l,
                    'hed': hed,
                    'subhed': subhed,
                    'sections': sections,
                    'byline': byline,
                    'pub_date': pub_date,
                    'html_body': html_body,
                    'text_body': raw_body,
                    'tags': tags})

pd.DataFrame(results).to_csv('pacific-standard/ps-archive.csv')
