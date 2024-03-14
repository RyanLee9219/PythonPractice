basket = ['a','b','c','x','d','e','d','a']
basket.sort()
basket.reverse()
# print(basket[::-1]) 
# print(basket)

# print(list(range(1,100))) #from 1
# print(list(range(100))) #from 0 to 99
# print(list(range(101))) #from 0 to 100

new_sentence = ' '.join(['hi','my','name','is','Ryan'])
print(new_sentence)

# List Unpacking
a,b,c, *other,d = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(c)
print(other)