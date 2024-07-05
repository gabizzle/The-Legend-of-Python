import random

answer = input('Would you like a Fortune? [y/n] ')

def fortune_cookie():
    random_num = random.randint(0, 7)

    if answer == 'y':
        if random_num == 0:
            print("Outlook not so good.")
        elif random_num == 1:
            print("Don't pursue happiness, create it.")
        elif random_num == 2:
            print("All things are difficult before they are easy.")
        elif random_num == 3:
            print("Someone in your life needs a letter from you.")
        elif random_num == 4:
            print("Don't just think. Act.")
        elif random_num == 5:
            print("Your heart will skip a beat.")
        elif random_num == 6:
            print("The fortune you search for is in another cookie.")
        elif random_num == 7:
            print("Help! I'm being held prisoner in a Chinese bakery!")
    elif answer == 'n':
        print("Try again next time.")

fortune_cookie()