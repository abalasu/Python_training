"""
# Saving a function in a variable
def shout(s):
    return s.upper()
def whisper(s):
    return s.lower()

x = shout
print(x('Ganesh'))

# Passing a function as a parameter
def greet(func):
    greeting = func("Hello")
    print(greeting)

greet(shout)
greet(whisper)

# Function returning another function
def fun_creator(x):
    def inner_fun(y):
        return x+y
    return inner_fun

new_incrementer_10 = fun_creator(10)
print(new_incrementer_10(40))

# First decorator
import time
def exec_time_calc(func_name):
    print('Step 1 - Decorator wrapper Starts ', func_name.__name__)
    def inner_fun(*arg, **kwarg):
        print('Step 3 - Decorator inner function starts - has the actual parms ')
        st_time = time.time()
        print('Step 4 - Decorator inner function calls actual function with parms')
        func_name(*arg, **kwarg)
        print('Step 7 - Actual function returns back to decorator function ')
        ed_time = time.time()
        print('    Time taken by ', func_name.__name__, ed_time - st_time)
        print('Step 8 - Decorator function completes and returns back to the main function ')
    return inner_fun

@exec_time_calc
def multiplier(a, b):
    print('Step 5 - Execution of the actual function ')
    print('    Value of ', a ,'*', b, ' is ', a*b)
    time.sleep(2)
    print('Step 6 - Actual function completes and passes back to the decorator ')
    return

# Second decorator
def hello_decorator(func):
    print("Decorator initiated by ", func.__name__)
    def inner1(*args, **kwargs):
        print("Parms before Execution ", args, kwargs)         
        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("Returned value after Execution ", returned_value)        
        # returning the value to the original frame
        return returned_value
    return inner1
  
# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the actual function")
    return a + b
 
a, b = 1, 2
# getting the value through return of the function
print("Sum = ", sum_two_numbers(a, b))

print('Step 2 - Main Func Starts and calls actual function ')
multiplier(4,45)
print('Step 9 - Main Func Ends ')
"""

# code for testing decorator chaining
def decor1(func):
    print("In outer of decor1")
    def inner():
        print("In inner of decor1 before func call")
        x = func()
        print("In inner of decor1 after func call ", x)
        return x * x
    return inner
 
def decor2(func):
    print("In outer of decor2")
    def inner():
        print("In inner of decor2 before func call")
        x = func()
        print("In inner of decor2 after func call", x)
        return 2 * x
    return inner
 
@decor1
@decor2
def num1():
    print("Starting num1 function ")
    return 10

print(num1())
