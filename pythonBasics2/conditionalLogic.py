is_old = True
is_licenced = True

# if is_old:
#   print('you are old enough to drive!')

# elif is_licenced:
#   print('you can drive now')
# else:
#   print('checkcheck')

# print('okoko')

if is_old and is_licenced:
  print('you are old enough to drive, and you have a licence!')

else:
  print('you are not of age')

# Truthy and Falsy
# is_old = bool('hello')
# is_licenced = bool(5)
# print(bool('')) #false
# print(bool(0)) #false

# password = '123'
# username = 'johnny'
# if password and username:
#   print(f'your password is {password} and your username is {username}')
  
# Ternary Operator
is_friend = False;
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)

# Short Circuiting
is_friend = True
is_user = True

if is_friend and is_user:
  print('best friends forever')