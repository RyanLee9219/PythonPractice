#square
my_list = [5,4,3]
print(list(map(lambda my_list: my_list**2, my_list)))

#list sorting
a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key=lambda x: x[1])
print(a)
print(list(map(lambda a: a[1], a)))
