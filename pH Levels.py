# pH Levels

ph = int(input("Enter the pH value between 0-14: "))

############
# No min/max

# if ph >= 7:
  # print("Basic")
# elif ph <=7:
  # print("Acidic")

#############

if ph <= 7:
  print("Basic")
elif ph <= 14 :
  print("Acidic")
else:
  print("Invalid")