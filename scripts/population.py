import pandas as pd

def categorize_city(number_of_residents):
    if number_of_residents > 1000000:
        return 'Tier 1'
    elif number_of_residents > 400000:
        return 'Tier 2'
    elif number_of_residents > 100000:
        return 'Tier 3'
    else:
        return 'Tier 4'
    
# skipping rows that have a different number of fields (columns) than expected
    
# fix errors in data instead of on bad-lines-skip
df_city = pd.read_csv('../data/population.csv', delimiter=",", on_bad_lines='skip')

df_city = df_city[['Name', '2022', 'Bundesland']]
df_city['2022'] = df_city['2022'].str.replace('.', '')

df_city['2022'] = pd.to_numeric(df_city['2022'], errors='coerce')
df_city['City Tier'] = df_city['2022'].apply(categorize_city)
print(df_city.head())