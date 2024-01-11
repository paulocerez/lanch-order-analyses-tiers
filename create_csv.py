# import pandas as pd

# # Assuming df is your DataFrame and you've calculated the metrics as new columns in it

# # City Metrics
# df_city_metrics = df[['city_order_counts', 'vendor_counts', 'population_per_city', 
#                       'city_avg_order_volume_per_resident', 'vendor_counts']]

# # Overall Metrics
# df_overall_metrics = df[['total_orders', 'total_orders_per_vendor', 
#                          'avg_number_of_orders_per_vendor', 'count_vendors']]

# # Tier Metrics
# df_tier_metrics = df[['tier_order_counts', 'total_no_own_delivery', 
#                       'avg_rating_per_fulfilment_type', 'avg_gmv_per_order_per_tier',
#                       'total_gmv_per_tier', 'total_orders_per_tier', 
#                       'total_population_per_tier', 'tier_avg_order_volume_per_resident',
#                       'avg_rating_partners', 'count_vendors_per_tier', 
#                       'avg_no_orders_per_vendor_per_tier']]

# # Export to CSV
# df_city_metrics.to_csv('city_metrics.csv', index=False)
# df_overall_metrics.to_csv('overall_metrics.csv', index=False)
# df_tier_metrics.to_csv('tier_metrics.csv', index=False)