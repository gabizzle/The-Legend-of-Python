# 32 Stonks
# Codedex

# price_at(x) that finds the price on a given day x.
# max_price(a, b) that finds the maximum price from day a to day b.
# min_price(a, b) that finds the minimum price from day a to day b.

stock_prices = [ 6.15, 5.81, 5.70, 5.65, 5.33, 5.62, 5.19, 6.13, 7.20, 7.34, 7.95, 7.53, 7.39, 7.59, 7.27 ]

def price_at(i):
  return stock_prices[i-1]

def max_price(a, b):
  mx = 0    # 0 is the minimum possible price (Starting with 0 ensures that any price from the list will be larger initially.)
  for i in range(a, b + 1):
    mx = max(mx, price_at(i))
  return mx

def min_price(a, b):
  mn = price_at(a)    # Starting with the first price in the range.
  for i in range(a, b + 1):
    mn = min(mn, price_at(i))
  return mn

print(max_price(1, 15))
print(min_price(5, 10))
print(price_at(3))