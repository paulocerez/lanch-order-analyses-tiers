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

# Avg. Order Volume per Resident
avg_order_volume_per_resident = city_order_counts / population_per_city

print(city_order_counts)