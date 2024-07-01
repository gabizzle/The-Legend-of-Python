# The Cyclone

height = int(input("What is your height? "))
credits = int(input("How many credits do you have? "))

if height >= 137 and credits >= 10:             # the height requirement is 137 cm and the cost is 10 credits
    print("Enjoy the ride!")
elif credits >= 10 and height < 137:            # if they have enough credits, but they aren't tall enough
    print("You are not tall enough to ride.")
elif height >= 137 and credits < 10:            # if they are tall enough, but they don't have enough credits
    print("You don't have enough credits.")
else:
    print("You did not meet the requirements.")