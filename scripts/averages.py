# some analyses regarding average numbers per city tiers

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

from merge_vendor_data_and_orders import df_orders_per_vendor

# Avg. GMV
avg_gmv_per_order_per_tier = df_orders_per_vendor.groupby('City Tier')['Gmv'].mean()

# Total GMV
total_gmv_per_tier = df_orders_per_vendor.groupby('City Tier')['Gmv'].sum()

# Total Order Volume
total_orders_per_tier = df_orders_per_vendor.groupby('City Tier')['Order ID'].count()


# print(total_gmv_per_tier, total_orders_per_tier)