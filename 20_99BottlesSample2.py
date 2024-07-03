
# 99 means the starting point of the range
# 0 means the ending point of the range
# -1 means the step of the range

# f means the string interpolation NOT concatenation

for beers in range(99, 0, -1):
    print(f'{beers} bottles of beer on the wall')
    print(f'{beers} bottles of beer')
    print('Take one down, pass it around')
    print(f'{beers-1} bottles of beer on the wall\n')
