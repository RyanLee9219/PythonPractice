class User:
  def sign_in(self):
    print('logged in')

  def attack(self):
    print('do nothing')

class Wizard(User):
  def __init__(self,name,power):
    self.name = name
    self.power = power

  def attack(self):
    User.attack(self)
    print(f'attacking with power of {self.power}')

class Archer(User):
  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows

  def attack(self):
    print(f'attacking with arrows : arrows left - {self.num_arrows}')

class Ogres(User):
  def __init__(self, name, punch):
    self.name = name
    self.punch = punch

  def attack(self):
    print(f'attacking with punch : {self.punch}')

wizard1 = Wizard('Merlin',60)
archer1 = Archer('Robin', 30)

# def player_attack(char):
#   char.attack()

# for char in [wizard1, archer1]:
#   char.attack()

print(wizard1.attack())