# 24 – Inventory
# Codedex

# Example
# stock1_prices = [2.52, 2.44, 2.32, 2.41, 2.51, 2.50, 2.44]
# stock2_prices = [8.36, 8.31, 8.21, 8.21, 8.25, 8.11, 8.13]

# print(len(stock1_prices))      # Output: 7
# print(max(stock1_prices))      # Output: 2.52
# print(min(stock2_prices))      # Output: 8.11

############

lego_parts = [8980, 7323, 5343, 82700, 92232, 1203, 7319, 8903, 2328, 1279, 679, 589]

# Which LEGO part are the elves running low on? Use min() to find out.
print("Minimum:", min(lego_parts))

# Is there a LEGO part that the elves are overstocking? Use max() to find out.
print("Maximum:", max(lego_parts))