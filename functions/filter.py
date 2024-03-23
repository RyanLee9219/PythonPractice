#filter() function
my_list = [1,2,3,4,5,6,7,8,9,10,11] #immutable
def multiply_by2(item):
   return item * 2

def only_odd(item):
  return item % 2 != 0
print(list(filter(only_odd, my_list)))
print(my_list)