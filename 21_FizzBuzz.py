# 21 - Fizz Buzz
# Codédex

# for every in range(100):
#  print(f'{100 - every}/100 \n')

# Loop through numbers from 1 to 100
for num in range(1, 101):
    # Check if the number is divisible by both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        # If true, print 'FizzBuzz'
        print('FizzBuzz')
    # Check if the number is divisible by 3 only
    elif num % 3 == 0:
        # If true, print 'Fizz'
        print('Fizz')
    # Check if the number is divisible by 5 only
    elif num % 5 == 0:
        # If true, print 'Buzz'
        print('Buzz')
    # If the number is not divisible by either 3 or 5
    else:
        # Print the number itself
        print(num)

# Reasoning:

# Specific to General:
# The condition num % 3 == 0 and num % 5 == 0 is the most specific case because it requires both conditions to be true.
# If this condition were placed after the individual checks for num % 3 == 0 and num % 5 == 0, 
# it would never be reached because the earlier checks would capture those numbers first.

# Order of Checks:
# If the checks for num % 3 == 0 or num % 5 == 0 came first,
# any number divisible by both 3 and 5 would be caught by these checks and the more specific case would be missed.