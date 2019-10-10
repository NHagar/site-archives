#%%
import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

#%%
with open('./splinter/links.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        links = row

#%%
links = list(set([i for i in links if 'splinternews.com' in i]))

#%%
links[0]
test = BeautifulSoup(requests.get(links[0]).text, 'html.parser')
test.find('h1').text
test.find('meta', {'name': 'keywords'})['content'].replace(', ', ';')
test.find('meta', {'name': 'author'})
[i.text for i in test.select('a[data-ga*=Author]') if len(i.text)>0][0]
test.find_all('time')
test.select('a[class*=time]')[0].text
test.select('div[title*=Visitors]')[0].find_all('span')[-1].text
test.find('div', {'class': 'js_post-content'}).text

#%%
results = []
for l in tqdm(links):
    soup = BeautifulSoup(requests.get(l).text, 'html.parser')
    try:
        hed = soup.find('h1').text
    except AttributeError:
        hed = ''
    try:
        sections = soup.find('meta', {'name': 'keywords'})['content'].replace(', ', ';')
    except TypeError:
        sections = ''
    try:
        byline = [i.text for i in soup.select('a[data-ga*=Author]') if len(i.text)>0][0]
    except AttributeError:
        byline = ''
    try:
        pub_date = soup.select('a[class*=time]')[0].text
    except AttributeError:
        pub_date = ''
    try:
        html_body = soup.find('div', {'class': 'js_post-content'}).encode_contents()
    except AttributeError:
        html_body = ''
    try:
        raw_body = soup.find('div', {'class': 'js_post-content'}).get_text()
    except AttributeError:
        raw_body = ''
    try:
        pageviews = soup.select('div[title*=Visitors]')[0].find_all('span')[-1].text
    except AttributeError:
        pageviews = ''
    results.append({'link': l,
                    'hed': hed,
                    'sections': sections,
                    'byline': byline,
                    'pub_date': pub_date,
                    'html_body': html_body,
                    'text_body': raw_body,
                    'pageviews': pageviews})
