# some analyses regarding order volumes


import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

from merge_vendor_data_and_orders import df_orders_per_vendor

# No. of orders per city
order_counts = df_orders_per_vendor.groupby('Vendor_City')['Order ID'].count()

# No. of vendors per city
vendor_counts = df_orders_per_vendor.groupby('Vendor_City')['Vendor ID'].nunique()

# No. of orders per cluster
tier_order_counts = df_orders_per_vendor.groupby('City Tier')['Order ID'].count()

print(tier_order_counts)