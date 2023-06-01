# class variable vs instant variable
## class variable : is shared by every instance of the class. For example, high_demand is a class variable
class occupations:
    high_demand = 'Accountant'
my_occupation = occupations()
print(my_occupation.high_demand)
## instant variable: specific to the object it is attached to. For example:
my_occupation.salary = 100000

# constructor def __init__(self,variable): usually used to store all variables that are changed depends on users' input
# class variables are used to store variables that are unchanged regardless of the input
# For example: circumfances = pi * radius *2 - pi is a constant number and will be defined as a class variable
# radius is changed depending on users' input, will be defined in the constructor
class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
    def circumfences(self):
        return 2* self.pi *self.radius
circle1 = Circle(10)
print(circle1.circumfences())


