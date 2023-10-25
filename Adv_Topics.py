# Generator Function
def my_generator(n):
    i = 0
    while i<n:
#        print('Before Yield')
# The function is returned back to main as it executes the yield statement
        yield i
# The function restarts after the yield statement from this point
        print('After Yield')
        i += 1

# Main Function
for value in my_generator(5):
    print('Print from main ', value)

"""
print("Iterators")

my_list=[3,2,5,9]
iterator = iter(my_list)
print(next(iterator))
print(next(iterator))
print('in the loop')
for element in iterator:
	print(element)

# Custom Iterators
class PowTwo:
    """Class to implement an iterator of powers of two"""
    def __init__(self, max):
        self.max = max
    def __iter__(self):
        print('The Iter Method gets automatically called')
        self.n = 0
        return self
    def __next__(self):
        print('In Next method')
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

# create an object
numbers = PowTwo(3)
for i in numbers:
    print(i)
    
"""