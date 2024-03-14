print(type("hi hello there 24!"))
username = 'supercoder'
password = 'supersecret'
long_string = '''
WOW
O O
___
'''
print(long_string)
first_name = 'Ryan'
last_name = 'lee'
full_name = first_name + ' ' + last_name
print(full_name)

#string concatenation 
print('hello' + ' Ryan')

#Type conversion
print(type(str(100))) #string 
print(type(int(str(100)))) #int

a = str(100)
b = int(a)
c = type(b)
print(c)

#formatted strings

name = 'Ryan'
age = 31

# print('hi ' + name + '. You are ' + str(age) + ' years old')

# print(f'hi {name}. You are {age} years old') **

# print('hi {}. You are {} years old'.format('Ryan', '31'))
# print('hi {}. You are {} years old'.format(name, age))

# print('hi {1}. You are {0} years old'.format(name, age))

print('hi {new_name}. You are {age} years old'.format(new_name='sally',age =100))

selfish = 'me me me'
        #  01234567  
print(selfish [0])
selfish = '01234567'
print(selfish[0:8])
print(selfish[0:8:2])#0246
print(selfish[1:]) #1234567
print(selfish[:5]) #01234
print(selfish[::1]) #default behavior
print(selfish[-1]) #7
print(selfish[::-1]) #76543210 reverse order of String **
#selfish[start:stop:stepover]
#immutability
selfish = '01234567'
selfish = selfish + '8'
print(selfish)

