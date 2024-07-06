# Janken / Rock Paper Scissors
# Player vs Computer
# Codédex

# Initialize
player = 0
computer = 0


print('-------------------------------')
print('  Welcome to Janken じゃん拳!   ')
print('   (Rock, Paper, Scissors)     ')
print('-------------------------------')
print('     1) Rock')
print('     2) Paper')
print('     3) Scissors\n')
print('Enter your choice:')

choice = int(input())

if choice == 1:
    player += 1
    print('You chose Rock!')
elif choice == 2:
    player += 1
    print('You chose Paper!')
elif choice == 3:
    player += 1
    print('You chose Scissors!')
else:
    print('Wrong input. Please select 1, 2, or 3.')