# *args **kwargs

def super_func(name, *args, i='hi', **kwargs):
  total = 0
  for items in kwargs.values():
    total += items
  return sum(args) + total

print(super_func('andy',1,2,3,4,5, num1=5,num2=10))

# Rule: params, *args, default parameters, **kwargs

def highest_even(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  return max(evens)

print(highest_even([10,2,3,4,8,11]))