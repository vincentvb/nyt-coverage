import requests
from constants import MONTHS, YEARS, ALL_COUNTRIES
from os import environ
from time import sleep
import pandas as pd

API_KEY = None

if environ.get('API_KEY') is None:
    raise EnvironmentError("Failed because API_KEY is not set")
else:
    API_KEY = environ.get('API_KEY')

def check_match(value):
    for country in ALL_COUNTRIES:
        if value in country:
            return True
    return False
    
for year in YEARS:
    all_dics_year = []
    for month in MONTHS:
        data = requests.get(f'https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={API_KEY}')
        articles = data.json()['response']['docs']
        for article in articles:
            for keyword in article['keywords']:
                if keyword['name'] == 'glocations' and check_match(keyword['value']):
                    article_dic = {}
                    article_dic['country'] = keyword['value']
                    article_dic['date'] = article['pub_date']
                    all_dics_year.append(article_dic)
        print(f"{month} {year} done processing")
        sleep(4)
    
    df = pd.DataFrame(all_dics_year)
    df.to_csv(f"../public/data/{year}_data.csv", index=False)