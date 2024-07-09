# 39 - Slot Machine
# Codédex

'''
import random

dice = [1, 2, 3, 4, 5, 6]

print(random.choices(dice))

Outputs a random number from the list dice
'''

'''
import random

dice = [1, 2, 3, 4, 5, 6]

print(random.choices(dice, k=3))

Outputs 3 random numbers from the list dice (and can be repeated)
'''

import random

symbols = ['🍒', ' 🍇', '🍉', '7️⃣']

results = random.choices(symbols, k=3)
print(f'{results[0]} | {results[1]} | {results[2]}')

if (results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣'):
 print('Jackpot! 💰')
else:
 print('Thanks for playing!')