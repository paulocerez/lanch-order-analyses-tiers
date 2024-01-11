import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

from merge_vendor_data_and_orders import df_orders_per_vendor

# No. of Orders per Vendor
total_orders_per_vendor = df_orders_per_vendor.groupby('Vendor ID')['Order ID'].count().sort_values(ascending=False)

# Avg. No. of Orders per Vendor
avg_number_of_orders_per_vendor = df_orders_per_vendor.groupby('Vendor ID')['Order ID'].sum()

print(total_orders_per_vendor)