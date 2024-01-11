import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

from merge_vendor_data_and_orders import df_orders_per_vendor

# No. of orders per city

order_counts = df_merged.groupby('Vendor_City')['Order ID'].count()
print(order_counts)