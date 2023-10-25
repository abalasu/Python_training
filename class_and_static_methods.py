class Fruit:
    name = 'Fruits'
    taste = 'Sour'
    shape = 'round'
    __odor = 'Good'
    def __init__(self, name, taste, shape, odor):
        self.name = name
        self.taste = taste
        self.shape = shape
        self.__odor = odor

    @classmethod
    def printName(cls):
        print('The name is:', cls.name)

    @staticmethod
    def printTaste():
        print('The taste is ', Fruit.taste)
        
    def __print_private(self):
        print('Odor is ', self.__odor)
    
#   instance method
    def printInstance(self):
        print(self.name)
        print(self.taste)
        print(self.shape)
        self.__print_private()

Fruit.printName()
Fruit.printTaste()
#Fruit.printInstance()
x = Fruit('Apple','sweet','round','good')
#x.__print_private()
"""
x = Fruit('Apple','sweet','round','good')
x.shape = 'square'
y = Fruit('jack fruit','sweet','oval','bad')
#print(id(x.name))
#print(id(Fruit.name))
x.printInstance()
y.printInstance()

Fruit.printName()
Fruit.printTaste()
print(Fruit.__dict__)
"""