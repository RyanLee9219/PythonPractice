#Parameters
#Default Parameters
def say_hello1(name='Darth Vader', emoji='😈'):
  print(f'hellloooo {name} {emoji}')
  
def say_hello(name, emoji):
  print(f'hellloooo {name} {emoji}')

#Positional arguments
say_hello('Ryan' , ':)')
say_hello('Tim' , ':)')
say_hello('Sean' , ':)')

#Keyword arguments
say_hello(emoji=':)', name='Bibi')

say_hello1('Timmy')
say_hello1(emoji=':)')

#Docstrings
def test(a):
  '''
  Info: this function tests and prints param a
  '''
  print(a)
print(test.__doc__)