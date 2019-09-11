Recommended usage for collecting links:
`scrapy runspider scrape-thinkprogress.py -o thinkprogress.csv`

## Note: this will produce duplicates since posts can have multiple tags
Run dedup to get a clean list of links only:
`python dedup-links.py`

Run the save-info script to get information on everything
`scrapy runspider save-thinkprogress-info.py -o info-thinkprogress.csv`
