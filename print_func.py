txt1 = "My name is {}, I'm {}".format("Raj",36)
print(txt1)
txt2 = "My name is {0}, I'm {1}".format("Raj",36)
print(txt2)
txt3 = "My name is {fname}, I'm {age}".format(fname = "Raj", age = 36)
print(txt3)

price = 45
txt4 = 'The Price of a Notebook is {} INR'
print(txt4.format(price))

# 2 decimal places
txt5 = 'The Price of a Notebook is {:.2f} INR'
print(txt5.format(price))

# Left Shift a string
txt6 = "My name is {:<8}, I'm {}"
my_name = '    Arul'
print(txt6.format(my_name,51))