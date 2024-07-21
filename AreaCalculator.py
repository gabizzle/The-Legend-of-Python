# Codédex – Area Calculator
# GitHub & Codédex: @gabizzle
# 07/20/2024

import math

print('----------------------------------------------')
print('               Area Calculator  📐            ')
print('----------------------------------------------')
print('     1) Triangle')
print('     2) Rectangle')
print('     3) Square')
print('     4) Circle')
print('     5) Quit\n')
print('Choose Shape by picking a number from 1 to 5: ')

choice = int(input())

# Triangle
if choice == 1:
    print('TRIANGLE')
    base = float(input('Enter the base: '))
    height = float(input('Enter the height: '))

    area = 0.5 * base * height
    
    print(f'The area of the triangle is {area}')

# Rectangle
elif choice == 2:
    print('RECTANGLE')
    length = float(input('Enter the length: '))
    width = float(input('Enter the width: '))

    area = length * width
    
    print(f'The area of the rectangle is {area}')

# Square
elif choice == 3:
    print('SQUARE')
    side = float(input('Enter the side: '))

    area = side * side
    
    print(f'The area of the square is {area}')

# Circle
elif choice == 4:
    print('CIRCLE')
    radius = float(input('Enter the radius: '))

    # or use 3.14 without 'import math' & 'math.pi'
    area = math.pi * radius * radius
    
    print(f'The area of the circle is {area}')

# Quit
elif choice == 5:
    print('Goodbye!')