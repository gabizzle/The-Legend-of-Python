# 37 - Bank Account
# Codédex

'''
class Student: 
  def __init__(self, name, year, enrolled, gpa):
    self.name = name
    self.year = year
    self.enrolled = enrolled
    self.gpa = gpa
  
  def display_info(self):
    print('The student ' + self.name + '\'s GPA is ' + str(self.gpa) + '!')

mitsuha = Student('宮水三葉', 11, False, 4.0)
taki = Student('立花瀧', 11, True, 3.8)

mitsuha.display_info()
taki.display_info()

# Output:
# The student 宮水三葉's GPA is 4.0!
# The student 立花瀧's GPA is 3.8!

#################

class Student: 
  def __init__(self, name, year, enrolled, gpa):
    self.name = name
    self.year = year
    self.enrolled = enrolled
    self.gpa = gpa
  
  def display_info(self):
    print('The student ' + self.name + '\'s is ' + str(self.gpa) + '!')
  
  def graduation(self):
    if self.enrolled and self.gpa > 2.5 and self.year == 12:
      print(self.name + ' will be able to graduate this year!')
'''
# Write code below 💖

class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self, amount):
    self.balance = self.balance + amount
    return self.balance

  def withdraw(self, amount):
    self.balance = self.balance - amount
    return self.balance

  def display_balance(self):
    print(f"${self.balance}")

savings = BankAccount('Bella', 'the Cat', 123456, 'Savings', 56789, 300)

savings.deposit(96)

savings.display_balance() # Output: $396

savings.withdraw(25)

savings.display_balance() # Output: $371
