# 20 - 99 Bottles of Beers 1
# Codédex

# String concatenation
# for i in range(5):
  # print('The square of ' + str(i) + ' is ' + str(i*i))

# String interpolation
# for i in range(5):
  # print(f'The square of {i} is {i*i}')

# Output of concatenation/interpolation
# The square of 0 is 0
# The square of 1 is 1
# The square of 2 is 4
# The square of 3 is 9
# The square of 4 is 16

for beer in range(99):
    print(f'{99 - beer} bottles of beer on the wall, \n{99 - beer} bottles of beer.')
    print(f'Take one down, pass it around. \n{98 - beer} bottles on the wall.\n')

# Output of the 99 Bottles of Beer

# 99 bottles of beer on the wall
# 99 bottles of beer
# Take one down, pass it around
# 98 bottles of beer on the wall

# until it reaches 0 bottles of beer on the wall