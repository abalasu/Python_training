class LivingThing:
    ''' Class is the blue print of an user defined structure. LivingThing is a class 
that is the base class for all living things '''
    # Class Methods
    # Constructor Method
    def __init__(self, age: int, living_space: str, food_hab: str) -> None:
        ''' This is the constructer method to initialize attributes '''
        print('Base Class init ')
        self.age, self.living_space, self.food_hab = age, living_space, food_hab
        return

    # Print Method
    def print_LivingThing(self):
        ''' This method prints the characteristics of a living thing '''
        print('Base Class print ')
        print('Characteristics are ', self.age, self.living_space, self.food_hab)
        return

# object creation and invocation
dog = LivingThing(9,'Land','Omnivor')
dog.print_LivingThing()
print(dog.__doc__)
print(dog.__init__.__doc__)
print(dog.__class__.__annotations__)
print(dog.__class__.__name__)
print(dog.__module__)
"""
# Inheriance
class Human(LivingThing):
    ''' Human being is a living thing '''
    def __init__(self, age, living_space, food_hab, sex, can_speak):
#       Calling the init function of the base class to initiate        
        super().__init__(age, living_space, food_hab)
        self.sex, self.can_speak = sex, can_speak

    def print_LivingThing(self):
#       Overriding the base class method
        print('Values are ', self.age, self.living_space, self.food_hab, self.sex, self.can_speak)

arul = Human(51, 'Land', 'omnivor', 'M', True)
super(Human, arul).print_LivingThing()
arul.print_LivingThing()

# Python private variables. 
# Variables/Methods with '__' at the begining are private to the class 
class Universe:
    __number_of_stars = 7000000000
    number_of_galaxies = 3500000
    def __pvt_print_universe(self):
        print('In  Private Method ')
        print(self.__number_of_stars, self.number_of_galaxies)

    def print_universe(self):
        print('In Public Method, calling private method')
        Universe.__pvt_print_universe(self)
        print(self.__number_of_stars, self.number_of_galaxies)


my_universe = Universe()
my_universe.print_universe()
my_universe.number_of_galaxies = 45000000
setattr(my_universe,'__number_of_stars', 5000000000)
my_universe.print_universe()
# The below will throw an error as we are trying to call a private method from outside of the class
# my_universe.__pvt_print_universe()
"""