# some analyses regarding order volumes

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

from merge_vendor_data_and_orders import df_orders_per_vendor
from population import df_city

# No. of orders per city
city_order_counts = (df_orders_per_vendor.groupby('Vendor_City')['Order ID'].count()).astype(float)

# No. of vendors per city
vendor_counts = df_orders_per_vendor.groupby('Vendor_City')['Vendor ID'].nunique()

# No. of orders per cluster
tier_order_counts = df_orders_per_vendor.groupby('City Tier')['Order ID'].count()

# Population per City
population_per_city = df_city.set_index('Name')['2022']
0
# Avg. Order Volume per Resident per City
city_avg_order_volume_per_resident = (city_order_counts / population_per_city).dropna()

# Avg. No. of Partners per City
vendor_counts = df_orders_per_vendor.groupby('Vendor_City')['Vendor ID'].nunique()

# No. of different fulfilment types per cluster
total_no_own_delivery = df_orders_per_vendor.groupby('Fulfilment Type')['Order ID'].count()

# Avg. rating of fulfilment types per cluster
avg_rating_per_fulfilment_type = df_orders_per_vendor.groupby(['Fulfilment Type', 'City Tier'])['Average Rating'].mean()

print(avg_rating_per_fulfilment_type)