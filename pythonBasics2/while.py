# i = 0
# while i < 50:
#   print(i)
#   i += 1
#   break
# else:
#   print('done with all the work')

my_list = [1,2,3]
for item in my_list:
  continue
  print(item)
# i = 0
# while i < len(my_list):
#   print(my_list[i])
#   i += 1

# while True:
#   input('say something: ')
#   break

while True:
  response = input('say something: ')
  if (response == 'bye'):
    break