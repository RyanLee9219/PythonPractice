def sum(num1,num2):
  return num1+num2 

#Should do one thing really well,
#Should return something.

total = sum(10,5)
print(sum(10,total)) 

print(sum(10,sum(10,5)))

def sum(num1,num2):
  def another_func(n1,n2):
    return n1+n2
  return another_func(num1,num2)

  

total = sum(10,20)
print(total)

 