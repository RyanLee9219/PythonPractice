#Dictionary
dictionary ={
  123 : [1,2,3],
  True : 'hello',
  '[100]' : True
}

# print(dictionary[123]) #work
# print(dictionary[True]) #work
# print(dictionary[[100]]) #does not work
#dictionary keys

dictionary={
  '123' : [1,2,3],
  '123' : 'hello'  
}
print(dictionary['123']) #hello - overrides the previous value
