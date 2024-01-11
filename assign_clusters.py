import pandas as pd
from population import df_city

df_vendor = pd.read_csv('vendors.csv', delimiter=",")
df_vendor_subset = df_vendor[['Vendor ID', 'Vendor Name Platform', 'Brand', 'City', 'Region', 'Legal Entity Name']]

df_city = df_city.rename(columns={'2022': 'Population', 'Name': 'Vendor_City'})


df_merged = pd.merge(df_city, df_vendor_subset, left_on='Vendor_City', right_on='City')
# inplace=True -> modify original df, axis=1 -> column (row -> axis=0)
# df_merged.drop('City', axis=1, inplace=True)

# print(df_merged['Population'].isna().any())
# print(df_merged.head(5))