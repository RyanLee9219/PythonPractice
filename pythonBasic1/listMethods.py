#List Methods
basket = [1,2,3,4,5]


#adding
basket.append(100)

new_list = basket.insert(5,100)
new_list = basket.extend([100])
print(basket)
print(new_list)

#removing
basket.pop()
basket.pop()
basket.pop(0)

new_list = basket.pop(4)
new_list = basket.clear()
print(new_list)

basket = ['a','b','c','x','d','e','d','a']

print(basket.index('d',0,4))
print('d' in basket) #true
print('x' in basket) #false
print('y' in 'hi my name is Ryan') #true

print(basket.count('d'))

# print(basket.sort())
# basket.sort()
new_basket = basket[:]
new_basket.sort()
print(sorted(new_basket))
print(new_basket)


print(sorted(basket)) #new copy of basket
print(basket)
basket.sort()
basket.reverse()
print(basket)