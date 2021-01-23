# Example of Class
class Student():    # follow camel casing for class name

    # Class Object Attribute
    # same for any instance of a class
    college = 'NIT Durgapur'

    # constructor for the class
    def __init__(self, name, roll):
        # self connect this method to the instance of the class

        # name, roll will be attribute of an instance of the class
        self.name = name
        self.roll = roll

    # string representation of a instance of class
    def __str__(self):
        return ("My name is %s and I study in %s" %(self.name, Student.college))

    def __del__(self):
        print('A student name has been deleted.')

    # methods
    def find_details(self):
        print('Name is %s' %self.name)
        print('Roll: %d' %self.roll)
        print('Studies in: %s' %Student.college)

# creating instance of Student class
my_id = Student('Samrat', 31)



# Inheritance Example
class Animal():     # Base class
    def __init__(self):
        print('Animal class created!')

    def my_identity(self):
        print('I am an Animal.')

    def eat(self):
        print('I am eating.')

# inheriting from Animal class
class Tiger(Animal):    # Derived class
    def __init__(self):
        # creating an instance of animal class while
        # creating instance of dog class
        Animal.__init__(self)
        print('Tiger created!')

    # overwriting inherited base class methods
    def my_identity(self):
        print('I am a Tiger.')

    def roar(self):
        print('ROOOOAAARRR')