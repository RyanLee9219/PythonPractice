class PlayCharacter():
  #Class object attribute
  membership = True
  def __init__(self, name ='anonymous',age = 0):
    if (age >18):
      self.name = name
      self.age = age

  def shout(self):
    print(f'My name is {self.name}')
  
player1 = PlayCharacter('Cindy', 10)
player2 = PlayCharacter('Tom', 17)

player1.name = '!!!'
player1.age = 100

print(player1.name)
print(player1.age)
# print(player1.run())
print(player1.shout())
print(player2.shout())

