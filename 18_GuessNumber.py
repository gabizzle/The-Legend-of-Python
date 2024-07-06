# 18 - Guess Number
# Codédex

# The user has 5 tries to guess the number 6
guess = 0
tries = 0


while guess != 6 and tries < 5: # while guess is not equal to 6 and tries is less than 5
  guess = int(input('Guess the number:  '))
  tries = tries + 1 # increment tries by 1

if guess != 6: # if guess is not equal to 6
  print('You ran out of tries.')
else:
  print('You got it!')