# some analyses regarding average numbers per city tiers

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

from merge_vendor_data_and_orders import df_orders_per_vendor
from population import df_city

# Avg. GMV
avg_gmv_per_order_per_tier = df_orders_per_vendor.groupby('City Tier')['Gmv'].mean()

# Total GMV
total_gmv_per_tier = df_orders_per_vendor.groupby('City Tier')['Gmv'].sum()

# Total Order Volume
total_orders_per_tier = df_orders_per_vendor.groupby('City Tier')['Order ID'].count().astype(float)

# Total Population per Tier
total_population_per_tier = df_city.groupby('City Tier')['2022'].sum().astype(float)

# Avg. Order Volume per Resident Per Tier
tier_avg_order_volume_per_resident = total_orders_per_tier / total_population_per_tier

print(tier_avg_order_volume_per_resident)