from assign_clusters import df_merged

cities_per_tier = df_merged['Vendor_City'].groupby(df_merged['City Tier']).unique().apply(list).to_dict()
# print(cities_per_tier)