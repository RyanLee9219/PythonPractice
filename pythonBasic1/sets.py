#set

my_set ={1,2,3,4,5,5}
print(my_set) #return unique items {12345}
my_set.add(100)
my_set.add(2)
print(my_set)
your_set = {4,5,6,7,8,9,10}


my_list = [1,2,3,4,5,5]
my_set = {1,2,3,4,5,5}
my_set.add(100)
my_set.add(2)
print(my_set)
print(set(my_list))

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}
print(my_set.difference(your_set))
print(my_set.discard(5))
print(my_set)
print(my_set.difference_update(your_set))
print(my_set)

print(my_set.intersection(your_set))
print(my_set.isdisjoint(your_set))
print(my_set.union(your_set))
print(my_set | your_set)
print(my_set & your_set)
print(my_set.issubset(your_set))
print(my_set.issuperset(your_set))
print(your_set.issuperset(my_set))


