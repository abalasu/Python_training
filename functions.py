def sum(a, b, c):
    d = a + b + c
    return d

def concat_names(*names):
    fullname = ''
    for x in names:
        fullname = fullname + ' ' + x 
    return fullname

def func_with_keyword_parms(**names):
    salary = 0
    print(names)
    for key, value in names.items():
        print("%s == %s" % (key, value))
        if (key == 'da') | (key == 'hra') | (key == 'basic'):
            salary = salary + value
    return salary

print('Sum of 3 numbers is ', sum(5,6,7))
print('Concatenating names ', concat_names('Arul', 'Bala'))
print('Concatenating names ', concat_names('Arul', 'Bala', 'Nagarathinam'))
print('Keyword Parameters ', func_with_keyword_parms(name='arul',age=20,gender='m',da=1000,hra=2000,basic=6000))
