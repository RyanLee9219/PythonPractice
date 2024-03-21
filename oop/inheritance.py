#Users
  # - Wizards
  # - Archers
  # - Ogres
class User:
  def sign_in(self):
    print('logged in')

class Wizard(User):
  def __init__(self,name,power):
    self.name = name
    self.power = power

  def attack(self):
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

wizard1 = Wizard('Potter', 50)
archer1 = Archer('Robin', 230)
ogres1 = Ogres('Ogre', 'punch')
wizard1.attack()
archer1.attack()
ogres1.attack()

wizard1 = Wizard('Merlin',60)

print(isinstance(wizard1,object))