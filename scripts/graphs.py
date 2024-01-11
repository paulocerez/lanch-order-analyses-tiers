import matplotlib.pyplot as plt
from averages import avg_gmv_per_order_per_tier, total_gmv_per_tier, total_orders_per_tier

x_values_tiers = avg_gmv_per_order_per_tier.index.tolist()
avg_gmv = avg_gmv_per_order_per_tier.values.tolist()
total_gmv = total_gmv_per_tier.tolist()
total_orders = total_orders_per_tier.tolist()

fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1)

# Plot Average GMV per Order
bars1 = ax1.bar(x_values_tiers, avg_gmv)
ax1.set_xlabel('City Tier')
ax1.set_ylabel('Average GMV per Order')
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 2), va='bottom')

# Plot Total GMV
bars2 = ax2.bar(x_values_tiers, total_gmv)
ax2.set_xlabel('City Tier')
ax2.set_ylabel('Total GMV')
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 2), va='bottom')

# Plot Total Number of Orders
bars3 = ax3.bar(x_values_tiers, total_orders)
ax3.set_xlabel('City Tier')
ax3.set_ylabel('Total No. of Orders')
for bar in bars3:
    yval = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom')  # Assuming total_orders are integers

plt.tight_layout()
plt.show()