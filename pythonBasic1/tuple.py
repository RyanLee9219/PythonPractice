#Tuple
my_tuple = (1,2,3,4,5)
my_tuple[1] = 'z' #does not work
print(my_tuple[1])
print(5 in my_tuple)

user = {
  'basket' : [1,2,3],
  'greet' : 'hello',
  'age' :20
}

print(user.items())
new_tuple = my_tuple[1:]
print(new_tuple)
x = my_tuple[0]
y = my_tuple[1]
print(x)
print(y)

x,y,z, *other = (1,2,3,4,5)
print(x)
print(y)
print(z)
print(other)
# Tuple Methods
print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))

