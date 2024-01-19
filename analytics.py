import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# Merges

# Function to assign tiers
def categorize_city(number_of_residents):
    if number_of_residents > 1000000:
        return 'Tier 1'
    elif number_of_residents > 400000:
        return 'Tier 2'
    elif number_of_residents > 100000:
        return 'Tier 3'
    else:
        return 'Tier 4'
    
# Read Population CSV from Wikipedia

# fix errors in data instead of on bad-lines-skip
df_city = pd.read_csv('./data/population.csv', delimiter=",", usecols=range(10))

# Extract necessary data
df_city = df_city[['Name', '2022', 'Bundesland']]
df_city['2022'] = df_city['2022'].str.replace('.', '')
df_city['2022'] = pd.to_numeric(df_city['2022'], errors='coerce')

# Assign Tiers by calling the function
df_city['City Tier'] = df_city['2022'].apply(categorize_city)

# Read vendor data csv
df_vendor = pd.read_csv('./data/vendors.csv', delimiter=",", low_memory=False)

# Extract relevant data
df_vendor_subset = df_vendor[['Vendor ID', 'Vendor Name Platform', 'Brand', 'City', 'Region', 'Legal Entity Name']]

df_city = df_city.rename(columns={'2022': 'Population', 'Name': 'Vendor_City'})

# Merge Vendor Data with Tiers
df_merged = pd.merge(df_city, df_vendor_subset, left_on='Vendor_City', right_on='City')
# inplace=True -> modify original df, axis=1 -> column (row -> axis=0)
# df_merged.drop('City', axis=1, inplace=True)

# Read food order csv
df_orders = pd.read_csv('./data/food_orders.csv', delimiter=",", low_memory=False)

# Extract relevant data
df_orders_subset = df_orders[['Vendor ID','Vendor Name','Order ID','Ordered At','Vendor Region','Brand','Order Source Name','Order Source Type', 'Fulfilment Type', 'Gmv', 'Rating Food', 'Rating Delivery', 'Vouchers Total Value Gross']]

# Merge Vendor Data with Tiers through Vendor Data <> Tier DF
df_orders_per_vendor = pd.merge(df_merged, df_orders_subset, on='Vendor ID')
# df_orders_per_vendor["Average Rating"] = (df_orders_per_vendor['Rating Food']+df_orders_per_vendor["Rating Delivery"]) / 2
# inplace=True -> modify original df, axis=1 -> column (row -> axis=0)
# print(df_orders_per_vendor['Ordered At'].head())
# print(df_orders_per_vendor.columns.tolist())




# Calculations

# some analyses regarding order volumes per city

# No. of orders per city
city_order_counts = (df_orders_per_vendor.groupby('Vendor_City')['Order ID'].count()).astype(float)

# No. of vendors per city
vendor_counts = df_orders_per_vendor.groupby('Vendor_City')['Vendor ID'].nunique()

# Population per City
population_per_city = df_city.set_index('Vendor_City')['Population']

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
df_city_metrics.reset_index(inplace=True)
df_city_metrics.rename(columns={'index': 'City'}, inplace=True)
df_city_metrics = df_city_metrics.merge(df_city[['Vendor_City', 'City Tier']], on='Vendor_City', how='left')
# df_city_metrics.drop('Name', axis=1, inplace=True)

df_city_metrics.to_csv('city_metrics.csv', index=False)


# These are just helpers for the calculations in other sheets

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
    'No. of Orders per Vendor': total_orders_per_vendor,
    'No. of unique Vendors': count_vendors,
    'Avg. order GMV per vendor': avg_order_value_per_vendor
})

df_overall_metrics.reset_index(inplace=True)
df_overall_metrics.to_csv('overall_metrics.csv', index=False)


# some analyses regarding average numbers per city tiers

# No. of orders per Tier
tier_order_counts = df_orders_per_vendor.groupby('City Tier')['Order ID'].count().astype(float)

# Avg. GMV per Tier
avg_aov_per_order_per_tier = df_orders_per_vendor.groupby('City Tier')['Gmv'].mean()

# Total GMV per Tier
total_gmv_per_tier = df_orders_per_vendor.groupby('City Tier')['Gmv'].sum()

# Total Population per Tier
total_population_per_tier = df_city.groupby('City Tier')['Population'].sum().astype(float)

# Avg. Order Volume per Resident Per Tier
tier_avg_order_volume_per_resident = tier_order_counts / total_population_per_tier

# Avg. Rating of Partners in Tiers

# No. of different fulfilment types per Tier
total_no_own_delivery = df_orders_per_vendor.groupby('Fulfilment Type')['Order ID'].count()

# Avg. Rating of fulfilment types per Tier
# avg_rating_per_fulfilment_type = df_orders_per_vendor.groupby(['Fulfilment Type', 'City Tier'])['Average Rating'].mean()

# No. of unique Vendors per Tier
count_vendors_per_tier = df_orders_per_vendor.groupby('City Tier')['Vendor ID'].nunique()

# Avg. Orders per Vendor per Tier
avg_no_orders_per_vendor_per_tier = tier_order_counts / count_vendors_per_tier


# Combine all metrics into a single DataFrame
df_tier_metrics = pd.DataFrame({
    'No. of orders per Tier': tier_order_counts,
    'Avg. AOV per Tier': avg_aov_per_order_per_tier,
    'Total GMV per Tier': total_gmv_per_tier,
    'Total Population per Tier': total_population_per_tier,
    'Avg. Order Volume per Resident Per Tier': tier_avg_order_volume_per_resident,
    'No. of different fulfilment types per Tier': total_no_own_delivery,
    # 'Avg. Rating of fulfilment types per Tier': avg_rating_per_fulfilment_type,
    'No. of unique Vendors per Tier': count_vendors_per_tier,
    'Avg. Orders per Vendor per Tier': avg_no_orders_per_vendor_per_tier
})

df_metrics_general = pd.DataFrame({
    'Total No. of Orders': total_orders,
    'Avg. No. of Orders': avg_number_of_orders,
})






# Reset the index
df_tier_metrics.reset_index(inplace=True)

# Export to CSV
df_tier_metrics.to_csv('tier_metrics.csv', index=False)