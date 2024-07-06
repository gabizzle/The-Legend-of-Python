# 36 - Favorite Cities
# Codédex

class City():
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

tokyo = City('Tokyo', 'Japan', 15, 'Shibuya')
new_york = City('New York City', 'USA', 20, 'Central Park, Times Square, Brooklyn Bridge')
paris = City('Paris', 'France', 30, 'Eiffel Tower, Louvre, Palais Garnier')

print(vars(tokyo))
print(vars(new_york))
print(vars(paris))