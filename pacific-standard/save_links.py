#%%
import csv
import requests
from bs4 import BeautifulSoup

#%%
#Start with links taken manually from the homepage
starting_links = ["/news/ideology-can-skew-our-views-on-the-healthiness-of-food",
                  "/news/this-congress-has-made-more-progress-on-early-gun-bills-than-any-other-in-the-last-ten-years",
                  "/news/indias-clampdown-on-kashmir-threatens-afghanistan-peace-negotiations",
                  "/news/fast-food-restaurants-between-home-and-work-linked-to-obesity",
                  "/news/how-much-longer-can-venezuelas-neighboring-countries-take-the-refugee-crisis",
                  "/news/lessons-from-the-bp-oil-spill-a-reading-list",
                  "/news/after-a-weekend-of-deadly-shootings-republicans-offer-renewed-support-for-red-flag-laws",
                  "/news/an-update-on-the-coal-country-protests",
                  "/news/domestic-disputes-are-more-likely-to-turn-deadly-in-cities-where-guns-are-easy-to-obtain",
                  "/environment/how-much-can-dietary-changes-and-food-production-practices-help-mitigate-climate-change",
                  "/social-justice/las-manos-jóvenes-que-nos-alimentan",
                  "/ideas/fall-books-preview-2019-zadie-smith-margaret-atwood-carmen-maria-machado",
                  "/social-justice/people-are-being-killed-like-flies-denied-asylum-in-the-u-s-cameroonians-fear-increasing-violence-back-home",
                  "/social-justice/outer-space-treaties-didnt-anticipate-the-privatization-of-space-travel-can-they-be-enforced",
                  "/social-justice/the-fault-in-our-star-names",
                  "/social-justice/the-farms-of-the-future-were-built-for-outer-space-will-they-work-on-earth",
                  "/ideas/yaejis-cutting-commentary-on-beauty-routines",
                  "/ideas/can-live-theater-help-spur-climate-action-ojai-playwrights-conference",
                  "/social-justice/the-young-hands-that-feed-us",
                  "/social-justice/educational-fight-or-flight",
                  "/social-justice/searching-for-indigenous-woman-savanna-lafontaine-greywind",
                  "/social-justice/sustained-outrage-in-west-virginia",
                  "/ideas/most-controversial-tree-in-the-world-gmo-genetic-engineering",
                  "/social-justice/the-definition-of-refugee-is-out-of-date-and-its-leaving-people-behind",
                  "/social-justice/how-health-officials-in-pro-life-states-are-quietly-dismantling-abortion-access",
                  "/ideas/alicia-elliott-and-arielle-twist-indigenous-writing-continues-to-set-bar-for-literary-excellence",
                  "/social-justice/what-its-like-to-get-reproductive-care-at-an-anti-abortion-anti-contraception-clinic",
                  "/news/ideology-can-skew-our-views-on-the-healthiness-of-food",
                  "/news/this-congress-has-made-more-progress-on-early-gun-bills-than-any-other-in-the-last-ten-years",
                  "/news/indias-clampdown-on-kashmir-threatens-afghanistan-peace-negotiations",
                  "/news/fast-food-restaurants-between-home-and-work-linked-to-obesity",
                  "/ideas/jia-tolentino-talks-to-samantha-irby-about-trick-mirror",
                  "/social-justice/amid-its-war-on-fair-housing-protections-hud-takes-a-rare-aggressive-action-against-los-angeles",
                  "/social-justice/ice-denies-claims-that-it-detains-immigrants-during-tragedies-like-the-el-paso-massacre"]

#%%
#Pull next page based on API token
html = requests.get('https://psmag.com/.api/stream-html/?moreResultsToken=MTg6OTo3ZTFiYTVlY2Y1ZTJiYWU4ZGM4OTlhZTBiYjg3MjNhNw==&initialSlots=e30=')
#Parse and extract story links
soup = BeautifulSoup(html.json()['html'], 'html.parser')
links = [i.a['href'] for i in soup.find_all('phoenix-ellipsis', 'm-card--header')]
starting_links.extend(links)
#Get token for next story links and starting point
next_links = soup.find('div', 'm-component-footer--container')['stream-more-items']
first = soup.find('div', 'm-component-footer--container')['initial-slots']

#%%
#Loop through tokens until end of feed
nl = True
while nl == True:
    html = requests.get('https://psmag.com/.api/stream-html/?moreResultsToken={0}&initialSlots={1}'.format(next_links, first))
    soup = BeautifulSoup(html.json()['html'], 'html.parser')
    links = [i.a['href'] for i in soup.find_all('phoenix-ellipsis', 'm-card--header')]
    starting_links.extend(links)
    print(len(starting_links))
    try:
        next_links = soup.find('div', 'm-component-footer--container')['stream-more-items']
        first = soup.find('div', 'm-component-footer--container')['initial-slots']
    except KeyError:
        nl = False

#%%
with open('links.csv', 'w', newline='', encoding='utf-8') as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    wr.writerow(starting_links)
