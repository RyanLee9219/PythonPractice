for item in 'Zero to Mastery':
  print(item)

for item in (1,2,3,4,5):
  print(item)
  print(item)
  print(item)
user = {
  'name': 'Golem',
  'age': 5006,
  'can_swim':False
}

for item in user.items():
  print(item)

for item in user.values():
  print(item)

for item in user.keys():
  print(item)

for item in (1,2,3,4,5):
  for x in ['a','b','c']:
    print(1,'c')

#iterable - list, dictionary, tuple, set, string
#iterated -> one by one check each item in the collection.

# counter
my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0
for item in my_list:
  counter = counter + item
  print(counter)
