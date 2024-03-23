#zip
my_list = [1,2,3,4,5,6,7,8,9,10,11] #immutable
your_list = [10,20,30,40,50,60,70,80,90,100,110]
their_list = [5,4,3,2,1]
def multiply_by2(item):
   return item * 2

def only_odd(item):
  return item % 2 != 0


print(list(zip(my_list,your_list,their_list)))
print(my_list)