# 38 - Pokédex
# Codédex

class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry              # int
    self.name = name                # str
    self.types = types              # str 
    self.description = description  # str
    self.is_caught = is_caught      # bool

  def speak(self):
    print(f'ENTRY NUMBER: {self.entry}\nNAME: {self.name}\nTYPE: {self.types}\nDESCRIPTION: {self.description}')
    
    is_caught_status = "has been caught" if self.is_caught else "has not been caught"
    print(f"{self.name} {is_caught_status}.\n")

venusaur = Pokemon(3, 'Venusaur', 'Grass, Poison', "While it basks in the sun, it can convert the light into energy. As a result, it is more powerful in the summertime.", False)
gengar = Pokemon(94, 'Gengar', "Ghost, Poison", "To steal the life of its target, it slips into the prey's shadow and silently waits for an opportunity.", True)
snorlax = Pokemon(143, 'Snorlax', 'Normal', "This gluttonous Pokémon eats constantly, apart from when it's asleep. It devours nearly 900 pounds of food per day.", True) 

venusaur.speak()
gengar.speak()
snorlax.speak()