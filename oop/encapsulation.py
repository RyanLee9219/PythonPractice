#Encapsulation
class PlayCharacter():
  def __init__(self, name,age):
      self.name = name
      self.age = age

  def run(self):
    print('run')
    
  def speak(self):
    print(f'My name is {self.name}, and I am {self.age} years old')

player1 = PlayCharacter('Ryan', 32)
print(player1.name)
print(player1.age)


