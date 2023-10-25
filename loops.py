# while loop
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  if i == 4:
      break

# for loop
list1 = ['apple','orange','cherry','kiwi','mango']
for x in list1:
    if x == 'cherry':
        continue
    print(x)
    if x == 'kiwi':
        break

# lambda function
x = lambda a: a * 2
print(x)
print(x(2))

def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler)
print(mytripler)
print(mydoubler(3))
print(mytripler(4))

strconcat = lambda str1, str2 : str1 + str2
print(strconcat('arul ', 'bala'))

# list comprehension
list = ['Loks','Ganpa','Satya','Gova','Mohaan','Arul']
newlist = [name.upper() for name in list]
print(newlist)
newlist = [name for name in list if 'a' not in name]
print(newlist)
newlist = [x for x in range(10) if x%2 == 0]
print(newlist)
newlist = [name if name=='Arul' else 'Loks' for name in list]
print(newlist)
