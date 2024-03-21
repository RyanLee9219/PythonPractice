class PlayCharacter():
  #Class object attribute
  membership = True
  def __init__(self, name ='anonymous',age = 0):
    if (age >18):
      self.name = name
      self.age = age

  def shout(self):
    print(f'My name is {self.name}')

  @classmethod
  def adding_things(cls, num1, num2):
    return cls('Teddy',num1 + num2)

player1 = PlayCharacter('Cindy', 10)
print(PlayCharacter.adding_things(2,3))
player3 = PlayCharacter.adding_things(2,3)

@staticmethod
def adding_things2(num1, num2):
  return num1 + num2
    