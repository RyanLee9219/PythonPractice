from functools import reduce
my_list = [1,2,3]

def multiply_by2(item):
   return item * 2

def only_odd(item):
  return item % 2 != 0

def acuuumulator(acc, item):
  print(acc, item)
  return acc + item
  
print(reduce(acuuumulator,my_list,10))
print(my_list)