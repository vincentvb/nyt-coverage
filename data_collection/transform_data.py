import pycountry
import pandas as pd
from constants import YEARS, COUNTRY_ISO3, BLACKLIST_COUNTRIES

for year in YEARS:
    try:
        df = pd.read_csv(f"../public/data/{year}_data.csv")
        transformed_rows = []

        for country, num_occurences in df.groupby('country').size().items():
            if country not in BLACKLIST_COUNTRIES:
                current_row = {}
                try:
                    current_row['iso3'] = pycountry.countries.get(name=country).alpha_3
                except:
                    current_row['iso3'] = COUNTRY_ISO3[country]
                current_row['num_occurences'] = num_occurences
                transformed_rows.append(current_row)

        transformed_pd = pd.DataFrame(transformed_rows)
        transformed_pd.to_csv(f"../public/data/{year}_num_data.csv", index=False)
    except Exception as e:
        print(e, "ERR")
        print(f"{year} couldn't transform")
