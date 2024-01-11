import pandas as pd
from assign_clusters import df_merged

df_orders = pd.read_csv('food_orders.csv', delimiter=",", low_memory=False)
df_orders_subset = df_orders[['Vendor ID','Vendor Name','Order ID','Ordered At','Vendor Region','Brand','Order Source Name','Order Source Type', 'Fulfilment Type', 'Gmv', 'Rating Food', 'Rating Delivery', 'Vouchers Total Value Gross']]

df_orders_per_vendor = pd.merge(df_merged, df_orders_subset, on='Vendor ID')
# inplace=True -> modify original df, axis=1 -> column (row -> axis=0)
# print(df_orders_per_vendor.head())
# print(df_orders_per_vendor['Ordered At'].head())
# print(df_orders_per_vendor.columns.tolist())


# df_city = df_city.rename(columns={'2022': 'Population', 'Name': 'Vendor_City'})
