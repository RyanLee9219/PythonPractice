li = [1,2,3,4,5] #arrays 
li2 = ['a','b','c']
li3 = [1,2,'a',True] 

#List slicing

amazon_cart = [
  'notebooks', 
  'sunglasses',
  'toys',
  'grapes'
]
amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

#Matrix = two or more dimensional lists(arrays)
matrix = [
  [1,5,1],
  [0,1,0],
  [1,0,1]
]

print(matrix[0][1])

