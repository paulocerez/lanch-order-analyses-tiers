# some analyses regarding order volumes

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import pandas as pd

from merge_vendor_data_and_orders import df_orders_per_vendor
from population import df_city

# No. of orders per city
city_order_counts = (df_orders_per_vendor.groupby('Vendor_City')['Order ID'].count()).astype(float)

# No. of vendors per city
vendor_counts = df_orders_per_vendor.groupby('Vendor_City')['Vendor ID'].nunique()

# Population per City
population_per_city = df_city.set_index('Name')['2022']

# Avg. Order Volume per Resident per City
city_avg_order_volume_per_resident = (city_order_counts / population_per_city).dropna()

# Generate CSV

df_city_metrics = pd.DataFrame({
    'No. of orders per city': city_order_counts,
    'No. of vendors per city': vendor_counts,
    'Population per city': population_per_city,
    'Avg. Order Volume per Resident per City': city_avg_order_volume_per_resident
})

# Merging df city and metrics df to include the City Tier
df_city_metrics = df_city_metrics.merge(df_city[['Name', 'City Tier']], left_on = 'City', right_on = 'Name', how = 'left')
# df_city_metrics.drop('Name', axis=1, inplace=True)
# df_city_metrics.rename(columns={'index': 'City'}, inplace=True)

df_city_metrics.reset_index(inplace=True)
# df_city_metrics.to_csv('city_metrics.csv', index=False)