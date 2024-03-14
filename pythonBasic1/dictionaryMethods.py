#Dictionary 
user = {
  'basket' : [1,2,3],
  'greet' : 'hello',
  'age' :20
}

user2 = dict(name= 'RyanRyan')
print(user2)

print('age' in user.keys())
print('hello' in user.values())
print(user.items())

user.clear()
print(user)

user2 = user.copy() 
print(user.clear()) 
print(user2)
print(user.pop('age'))
print(user)
print(user.popitem())
print(user)

print(user.update({'age': 55}))
print(user)