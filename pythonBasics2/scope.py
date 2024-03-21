#Scope - what variables do I have access to?
if True:
  x=10
  
def some_func():
  total = 100
  print(x)

a = 1
def parent():
  a = 10
  def confusion():
    return sum
  return confusion()
  a=5
  return a
print(parent())
print(a) #1



#1 - start with local
#2 - Parent local?
#3 - global 
#4 - built in python functions.

#global 
total = 0
def count(total):
  total += 1
  return total

print(count(count(count(total))))