# 16 - Harry Potter Sorting Hat
# Codédex

# Initialize house points
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

# Question 1
print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
answer = int(input())  # Get user input and convert it to an integer

if answer == 1:
    gryffindor += 1  # Add 1 point to Gryffindor
    ravenclaw += 1  # Add 1 point to Ravenclaw
elif answer == 2:
    hufflepuff += 1  # Add 1 point to Hufflepuff
    slytherin += 1  # Add 1 point to Slytherin
else:
    print("Wrong input.")  # Output message for invalid input

# Question 2
print("\nQ2) When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
answer = int(input())  # Get user input and convert it to an integer

if answer == 1:
    hufflepuff += 2  # Add 2 points to Hufflepuff
elif answer == 2:
    slytherin += 2  # Add 2 points to Slytherin
elif answer == 3:
    ravenclaw += 2  # Add 2 points to Ravenclaw
elif answer == 4:
    gryffindor += 2  # Add 2 points to Gryffindor
else:
    print("Wrong input.")  # Output message for invalid input

# Question 3
print("\nQ3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
answer = int(input())  # Get user input and convert it to an integer

if answer == 1:
    slytherin += 4  # Add 4 points to Slytherin
elif answer == 2:
    hufflepuff += 4  # Add 4 points to Hufflepuff
elif answer == 3:
    ravenclaw += 4  # Add 4 points to Ravenclaw
elif answer == 4:
    gryffindor += 4  # Add 4 points to Gryffindor
else:
    print("Wrong input.")  # Output message for invalid input

# Determine the house with the most points
max_points = max(gryffindor, ravenclaw, hufflepuff, slytherin)  # Find the maximum points among all houses

print("\nThe Sorting Hat has sorted you into...")

# Check which house(s) has the maximum points and print the result
if gryffindor == max_points:
    print("🦁 Gryffindor!")
if ravenclaw == max_points:
    print("🦅 Ravenclaw!")
if hufflepuff == max_points:
    print("🦡 Hufflepuff!")
if slytherin == max_points:
    print("🐍 Slytherin!")
