# 36 - Favorite Cities
# Codedex

class City():
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

tokyo = City('Tokyo', 'Japan', 15, 'Shibuya')
new_york = City('New York City', 'USA', 20, 'Central Park, Times Square, Brooklyn Bridge')
milan = City('Milan', 'Italy', 30, 'Duomo Milano, Vaticano')

print(vars(tokyo))
print(vars(new_york))
print(vars(milan))