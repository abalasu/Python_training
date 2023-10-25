fp = open('d:/pythondata/test_results.xml','rt') # Open text file in read mode
fp1 = open('d:/pythondata/test_results.txt','a') # Open file in oputput mode
fp1.write(fp.read()) # Copy data from fp to fp1
fp.close() # Close fp
fp1.close() # Close fp1

fp = open('d:/pythondata/file_read_list.csv','rt') # Open text file in read mode
x = fp.read()
print(type(x))
li = list(x.split(","))
int_li = [int(x) for x in li]
print(int_li)
print(sum(int_li))

class student:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.gender = sex

fp = open('d:/pythondata/struct_file.csv','a+')
a = student('Arul',45,'M')
x = vars(a)
print(x)
o = []
for m, n in x.items():
    o.append(n)
fp.write(str(o) + '\n')
b = student('Ganpa',46,'M')
x = vars(b)
o = []
for m, n in x.items():
    o.append(n)
fp.write(str(o) + '\n')
fp.close()

fp = open('d:/pythondata/struct_file.csv','r')
i = True
while i == True:
    a = fp.readline().rstrip('\n')
    if a == '':
        i = False
    print(a)

