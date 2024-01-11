# These are just helpers for the calculations in other sheets

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import pandas as pd

from merge_vendor_data_and_orders import df_orders_per_vendor

# Total No. of Orders
total_orders = df_orders_per_vendor['Order ID'].count()

# No. of Orders per Vendor
total_orders_per_vendor = df_orders_per_vendor.groupby('Vendor ID')['Order ID'].count().sort_values(ascending=False)

# Avg. No. of Orders
avg_number_of_orders= df_orders_per_vendor.groupby('Vendor ID')['Order ID'].count().mean()

# No. of unique Vendors
count_vendors = df_orders_per_vendor['Vendor ID'].nunique()

# Avg. order GMV per vendor
avg_order_value_per_vendor = df_orders_per_vendor.groupby('Vendor ID')['Gmv'].mean()

# Generate CSV

df_overall_metrics = pd.DataFrame({
    'Total No. of Orders': total_orders,
    'No. of Orders per Vendor': total_orders_per_vendor,
    'Avg. No. of Orders': avg_number_of_orders,
    'No. of unique Vendors': count_vendors,
    'Avg. order GMV per vendor': avg_order_value_per_vendor
})

df_overall_metrics.reset_index(inplace=True)
df_overall_metrics.to_csv('overall_metrics.csv', index=False)