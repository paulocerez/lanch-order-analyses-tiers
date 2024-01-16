# some analyses regarding average numbers per city tiers
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

from merge_vendor_data_and_orders import df_orders_per_vendor
from population import df_city

# No. of orders per Tier
tier_order_counts = df_orders_per_vendor.groupby('City Tier')['Order ID'].count()

# Avg. GMV per Tier
avg_aov_per_order_per_tier = df_orders_per_vendor.groupby('City Tier')['Gmv'].mean()

# Total GMV per Tier
total_gmv_per_tier = df_orders_per_vendor.groupby('City Tier')['Gmv'].sum()

# Total Order Volume per Tier
total_orders_per_tier = df_orders_per_vendor.groupby('City Tier')['Order ID'].count().astype(float)

# Total Population per Tier
total_population_per_tier = df_city.groupby('City Tier')['2022'].sum().astype(float)

# Avg. Order Volume per Resident Per Tier
tier_avg_order_volume_per_resident = total_orders_per_tier / total_population_per_tier

# Avg. Rating of Partners in Tiers
avg_rating_partners = df_orders_per_vendor.groupby('City Tier')['Average Rating'].mean()

# No. of different fulfilment types per Tier
total_no_own_delivery = df_orders_per_vendor.groupby('Fulfilment Type')['Order ID'].count()

# Avg. Rating of fulfilment types per Tier
avg_rating_per_fulfilment_type = df_orders_per_vendor.groupby(['Fulfilment Type', 'City Tier'])['Average Rating'].mean()

# No. of unique Vendors per Tier
count_vendors_per_tier = df_orders_per_vendor.groupby('City Tier')['Vendor ID'].nunique()

# Avg. Orders per Vendor per Tier
avg_no_orders_per_vendor_per_tier = total_orders_per_tier / count_vendors_per_tier


# Combine all metrics into a single DataFrame
df_metrics = pd.DataFrame({
    'No. of orders per Tier': tier_order_counts,
    'Avg. AOV per Tier': avg_aov_per_order_per_tier,
    'Total GMV per Tier': total_gmv_per_tier,
    'Total Order Volume per Tier': total_orders_per_tier,
    'Total Population per Tier': total_population_per_tier,
    'Avg. Order Volume per Resident Per Tier': tier_avg_order_volume_per_resident,
    'Avg. Rating of Partners in Tiers': avg_rating_partners,
    'No. of different fulfilment types per Tier': total_no_own_delivery,
    'Avg. Rating of fulfilment types per Tier': avg_rating_per_fulfilment_type,
    'No. of unique Vendors per Tier': count_vendors_per_tier,
    'Avg. Orders per Vendor per Tier': avg_no_orders_per_vendor_per_tier
})

# Reset the index
df_metrics.reset_index(inplace=True)

# Export to CSV
df_metrics.to_csv('tier_metrics.csv', index=False)