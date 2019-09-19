'''
dedup-links.py

Short script to remove duplicates and save just the list of links
'''

import pandas as pd

csv_path = 'thinkprogress.csv'
out_path = 'deduped-thinkprogress-links-only.csv'

all_links = pd.read_csv(csv_path)
dedup_links = list(set(all_links['link']))

print("{} total links, {} after dedup".format(len(all_links['link']),len(dedup_links)))

print("Saving deduped list...")
dedup_df = pd.DataFrame(dedup_links)
dedup_df.to_csv(out_path,header=False, index=False)
print("Done!")
