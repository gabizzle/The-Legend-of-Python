# Magic 8 Ball

# Explanation

# import random
# num = random.randint(1, 9) # Generates a number between 1 to 9
# print(num)

import random

question = input('Question: ')
random_num = random.randint(1, 8)

if random_num == 1:
  print("Yes - definitely.")
elif random_num == 2:
    print("It is decidedly so.")
elif random_num == 3:
    print("Without a doubt.")
elif random_num == 3:
    print("Reply hazy, try again.")
elif random_num == 4:
    print("Ask again later.")
elif random_num == 5:
    print("Better not tell you now.")
elif random_num == 6:
    print("My sources say no.")
elif random_num == 7:
    print("Outlook not so good.")
elif random_num == 8:
    print("Very doubtful.")
else:
    print("Invalid. Try again.")