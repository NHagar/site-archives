#%%
import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

# %%
df = pd.read_csv('pacific-standard/ps-archive.csv')
df['pub_date'] = pd.to_datetime(df['pub_date'], utc=True).dt.tz_localize(None)

# %%
tofix = df[df['byline']=='Pacific Standard Staff']

#%%
results = []
for i,r in tqdm(tofix.iterrows()):
    resp = requests.get(r['link'])
    soup = BeautifulSoup(resp.text, 'html.parser')
    try:
        byline = [i for i in soup.find_all('p') if 'By' in i.text and i.strong.em][0].text.replace('By ', '')
    except (IndexError,AttributeError) as e:
        byline = 'Pacific Standard Staff'
    results.append({'link': r['link'], 'byline_updated': byline})

#%%
rdf = pd.DataFrame(results)

# %%
pd.DataFrame(results).groupby('byline_updated').count().sort_values(by='link', ascending=False)

# %%
joined = df.set_index('link').join(rdf.set_index('link'), how='left').reset_index()


# %%
joined['byline_updated'] = joined['byline_updated'].fillna(joined['byline'])

# %%
joined.to_csv('ps-archive-patched.csv')

# %%
