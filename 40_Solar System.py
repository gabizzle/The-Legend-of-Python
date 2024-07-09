# 40 - Solar System
# Codédex

'''
from random import sample

famous_houses = [
  '🐺 Stark',
  '🐉 Targaryen',
  '🦌 Baratheon',
  '🦑 Greyjoy',
  '🦁 Lannister'
]

example = sample(famous_houses, 2)

print(f'Example: {example}')
'''

# Using 'from' and 'as'
'''
from random import sample as samp

import random as rd

example = samp(['Stark', 'Targaryen', 'Baratheon', 'Greyjoy', 'Lannister'], 2)

print('Example: ' + example[0] + ' ' + example[1])
'''
from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)
radius = 6371

if random_planet == 'Mercury':
    radius = 2440
elif random_planet == 'Venus':
    radius = 6052
elif random_planet == 'Earth':
    radius = 6371
elif random_planet == 'Mars':
    radius = 3390
elif random_planet == 'Saturn':
    radius = 58232
else:
    print('Oops! An error occurred.')

planet_area = 4 * pi * radius * radius

print(f'Area of {random_planet}: {planet_area} sq mi')