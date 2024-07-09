# 41 – Birthday Messages Main
# Codédex
# Used with BDAYMessages.py

import datetime, BDayMessages

today = datetime.date(2024, 7, 9)
next_birthday = datetime.date(2025, 5, 22)

days_away = (next_birthday - today).days

if today == next_birthday:
  print(f'{BDayMessages.random_message}')
else:
  print(f'My next birthday is {days_away} days away!')