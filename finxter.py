numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers if n % 2 == 1]
print(squares)

# 1, 9, 25

first_dict = {'a': 1, 'b': 2, 'c': 3}
second_dict = {'c': 4, 'd': 5}
third_dict = {'a': 6, 'e': 7}
print({**first_dict})
combined_dict = {**first_dict, **second_dict, **third_dict}
print(combined_dict)
print(len(combined_dict))

x = "global"
def outer_function():
    x = "outer"
    def inner_function():
        nonlocal x
        x = "inner"
        print(x)
    inner_function()
    print(x)

outer_function()
print(x)

# inner, inner, outer

l1 = [1,2,4]
l2 = [5,2,1]
print(l1)
print(*l1)

def myprint(*a1):
    print(a1)
    return

myprint(*l1)

def func(x):
    return x+1

f = func
print(f(2), func(2))

def fun_print(a,b,c):
    return a,b,c


a,b,c = fun_print(*l1)
print(a)
print(b)
print(c)