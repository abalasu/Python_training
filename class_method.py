from itertools import count


class city:
    name = 'Virudhunagar'
    lattitude = 732423
    longitude = 643333
    state = 'Tamil Nadu'
    country = 'India'
    population = 83005
    def __init__(self, name, lattitude, longitude, state, country, population):
        self.name = name
        self.lattitude = lattitude
        self.longitude = longitude
        self.state = state
        self.country = country
        self.population = population

    def print_city(self):
        print('City Details')
        print(self.name, self.lattitude, self.longitude, self.state, self.country, self.population)

    def print_projected_poulation(self, projection):
        print('Current Population ', self.population)
        print('Projected Population ')
        print(self.population * projection)

# Class Mehod the old way
print('Class Methods')
city.print_city_details = classmethod(city.print_city)
city.print_city_details()


# Python program to demonstrate use of a class method and static method in the new way.
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        print('Value of cls is ', cls)
        return cls(name, date.today().year - year)
 
    # static methods are not associated with an object. Method can be directly invoked with clasname.methodname
    @staticmethod
    def isAdult(age):
        return age > 18
        
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('arul', 1996)
print(type(person1), type(person2))
print(person1.age)
print(person2.age)
print(person2.name)

# Invoking static method defined in a class
print(Person.isAdult(22))

# Inheritance
print('Inheritance')
class Living_Thing:
    life_expectancy = 10
    type_of_lt = 'aquatic'
    def __init__(self, le, tolt):
        print('From base class init ')
        self.life_expectancy = le
        self.type_of_lt = tolt
        return
    def print_elements(self):
        print('Life expectancy ',self.life_expectancy)
        print('Type of Living Thing ', self.type_of_lt)
        return
class Human(Living_Thing):
    gender = None
    name = None
    country = None
    def __init__(self, name, gender, country, life_expectancy, tolt):
        super().__init__(life_expectancy, tolt)
        self.gender = gender
        self.name = name
        self.country = country
    def print_elements(self):
        print('Name ', self.name)
        print('Gender ', self.gender)
        print('Country ', self.country)
        super().print_elements()

Arul = Human('Arul', 'M', 'India', 60, 'Terrestrial')
Arul.print_elements()

"""
Identifiers:
-  Contain only (A-z, 0-9, and _ )
-  Start with a lowercase letter or _.
-  Single leading _ :  private
-  Double leading __ :  strong private
-  Start & End  __ : Language defined Special Name of Object/ Method
-  Class names start with an uppercase letter.
-
"""
print('Access Modifiers')
class BankAccount(object):
    def __init__(self, name, money, password):
        self.name = name            # Public
        self._money = money         # Private : Package Level
        self.__password = password  # Super Private

    def earn_money(self, amount):
        self._money += amount
        print("Salary Received: ", amount, " Updated Balance is: ", self._money)

    def withdraw_money(self, amount):
        self._money -= amount
        print("Money Withdraw: ", amount, " Updated Balance is: ", self._money)

    def show_balance(self):
        print(" Current Balance is: ", self._money)

    def show_pwd(self):
        print(" The password is ", self.__password)

Hitesh_account = BankAccount("Hitesh", 1000, "PWD")  # Object Initalization

# Method Call
Hitesh_account.earn_money(100)

# Show Balance
Hitesh_account.show_balance()
print("PUBLIC ACCESS:", Hitesh_account.name)  # Public Access
# account._money is accessible because it is only hidden by convention
print("PROTECTED ACCESS:", Hitesh_account._money)  # Protected Access
# account.__password will throw error but account._BankAccount__password will not
# because __password is super private
# print("Private Access:", Hitesh_account.__password)
print('Printing pwd by calling method')
Hitesh_account.show_pwd()
print("PRIVATE ACCESS:", Hitesh_account._BankAccount__password)

# Method Call
Hitesh_account.withdraw_money(200)

# Show Balance
print(Hitesh_account.show_balance())

# account._money is accessible because it is only hidden by convention
print(Hitesh_account._monxey)  # Protected Access