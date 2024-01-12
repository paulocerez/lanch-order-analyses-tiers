### How to run these analyses

Upload data sources to the data folder -> Expected input: Three CSV's containing food order data, population data, list of unique vendors.

Run three files in the scripts folder to calculate metrics and insert the results into csv sheets.

- cities.py -> City-related metrics
- tiers.py -> Tier*-related metrics
- overall.py -> Overall metrics

All of these metrics are order-performance-related.
* Tiers are categorized per population size in the cities. See the logic in population.py