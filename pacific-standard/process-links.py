#%%
import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

#%%
with open('./pacific-standard/links.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        links = row

#%%
links = ['https://psmag.com{}'.format(i) for i in links]

#%%
results = []
for l in tqdm(list(set(links))):
    soup = BeautifulSoup(requests.get(l).text, 'html.parser')
    try:
        hed = soup.find('h1').text
    except AttributeError:
        hed = ''
    try:
        subhed = soup.find('div', 'm-detail-header--dek').text
    except AttributeError:
        subhed = ''
    try:
        sections = ';'.join([i.text for i in soup.find_all('li', 'm-breadcrumbs--item')])
    except AttributeError:
        sections = ''
    try:
        byline = soup.find('a', 'm-detail-header--meta-author').text
    except AttributeError:
        byline = ''
    try:
        pub_date = soup.find_all('time')[-1]['datetime']
    except AttributeError:
        pub_date = ''
    try:
        html_body = soup.find('div', 'm-detail--body').encode_contents()
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
