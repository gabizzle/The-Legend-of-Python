# 33 -  Drive Thru
# Codédex

# Write code below 💖

#def function_name(parameter1, parameter2):
  # The code inside
#  return value

def get_item(x):
  if x == 1:
    return '🍔 Cheeseburger'
  elif x == 2:
    return '🍟 Fries'
  elif x == 3:
    return '🥤 Soda'
  elif x == 4:
    return '🍦 Ice Cream'
  elif x == 5:
    return '🍪 Cookie'
  else:
    return "invalid option"

def welcome():
  print('Welcome to Sonnyboy\'s Diner!')
  print('Here\'s the menu:')
  print('1. 🍔 Cheeseburger')
  print('2. 🍟 Fries')
  print('3. 🥤 Soda')
  print('4. 🍦 Ice Cream')
  print('5. 🍪 Cookie')

welcome()

option = int(input('What would you like to order? '))
print(get_item(option))

# using 'print' in any part of the code instead of 'return' outputs "None" at the end of the output