### How to run these analyses

Upload data sources to the data folder -> Expected input: A CSV containing food order data and one containing unique vendors.

All of the calculated metrics are order and performance related.
* Tiers are categorized per population size in the cities. See logic in the first cell of analytics.ipynb.

#### How to run the Jupyter Notebook
Run all cells in analytics.ipynb -> This calculates the metrics in separated cells and inserts the outcomes into different CSV's that can be used for further visualizations or analyses.


### **City Metrics:**

- `No. of orders per city (city_order_counts)` → total no. of orders placed per city
- `No. of vendors per city (vendor_counts)` → total no. of vendors operating per city
- `Population per city (population_per_city)` → population size per city
- `Avg. Order Volume per Resident per City (city_avg_order_volume_per_resident)` → average no. of orders placed per resident per city
- `Avg. No. of Partners per City (vendor_counts)`→ the avg. no. of partners per city

### **Overall Metrics:**

- `Total No. of Orders (total_orders)` → total no. of orders placed
- `No. of Orders per Vendor (total_orders_per_vendor)` → no. of orders placed per vendor
- `Avg. No. of Orders per Vendor (avg_number_of_orders_per_vendor)` → avg. no. of orders placed per vendor
- `No. of unique Vendors (count_vendors)` → total no. of unique vendors

### **Tier/Cluster Metrics:**

- `No. of orders per cluster (tier_order_counts)` → total no. of orders placed per tier
- `No. of different fulfilment types per cluster (total_no_own_delivery)` → total no. of different fulfilment types used per tier
- `Avg. rating of fulfilment types per cluster (avg_rating_per_fulfilment_type)` → avg. rating of fulfilment types per tier
- `Avg. AOV (avg_gmv_per_order_per_tier)` → avg. AOV per order per tier
- `Total GMV (total_gmv_per_tier)` → total GMV per tier
- `Total Order Volume (total_orders_per_tier)` → total volume of orders per tier
- `Total Population per Tier (total_population_per_tier)` → population size per tier
- `Avg. Order Volume per Resident Per Tier (tier_avg_order_volume_per_resident)` → avg. volume of orders per resident per tier
- `Avg. Rating of Partners in Tiers (avg_rating_partners)` → avg. rating of partners per tier
- `No. of unique Vendors per Tier (count_vendors_per_tier)` → no. of unique vendors per tier
- `Avg. Orders per Vendor per Tier (avg_no_orders_per_vendor_per_tier)` → avg. no. of orders per vendor per tier