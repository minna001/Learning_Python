"""
noofbooks = 2
if(noofbooks ==2):
    print("You have")
    print("Two books")
print("Outside of if statement")
print("\n")
a = 10
if a<100:
    print("less then 100")
else:
    print("more than equal 100")

print("\n")

num = float(input("Enter a number: "))
if num >0:
    print("positive number")
    if num==0:
        print("zero")
else:
    print("Negative Number")

print("\n")

x=1
while x<=4:
    print(x)
    x=x+1
print("Loop Ended")

print("\n")

for i in range (3,6):
    print(i)

print("\n")

for i in range(1,3):
   # print(i)
    for j in range(1,11):
        k=i*j
        print(k, end= ' ')
    print()

print("\n")

for val in "string":
    if val == "i":
        break
    print(val)

print("\n")
"""
"""
for val2 in "init":
    if val2 == "i":
        continue
    print(val2)
print("The End")
"""
"""
for i in "initial":
    if (i == "i"):
        pass
    else:
        print(i)
"""

""" try:
    fh = open("testfile","r")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error Can\'t find file or read data")
else:
    print("Written content in the file successfully") """

""" class Point:
    x = 0
    y = 0

    def set_location(self, x, y):
        self.x = x
        self.y = y
    def distance_from_origin(self):
        return sqrt(self.x * self.x + self.y * self.y)
    
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx * dx + dy * dy)

p = Point(3,-4)
p.distance_from_origin()
Point.distance(p,2)
 p1 = Point()
p1.x = 7
p1.y = -3
p1.name = "Tyler Durden"
print(p1.name)
print(p1.x,p1.y) """
""" 
from math import *

class Point:
    def __init__(self,x,y):
        self.x = y
        self.y = y
    
    def distance_from_origin(self):
        return sqrt(self.x * self.x + self.y * self.y)
    
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx * dx + dy * dy)

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


    distance(self= 3,other=4)   """  


def my_function():
    print("helllo from my function")


my_function()

def my_function2(fname):
    print(fname + " refsnes")

my_function2("Email")
my_function2("Tobias")
my_function2("Linus")

def my_function3(* kids):
    print("The youngest child is " + kids[2])

my_function3("Emil", "tobias", "Linus")

def my_function4(child3, child2, child1):
    print("The youngest child  is" + child3)

my_function4(child1="don",child2="mike",child3="mike")

def my_function5(**kid):
    print("His last name is " + kid["lname"] + kid["fname"])

my_function5(fname = "Tobias",lname = "refsnes")

def my_function6(food):
    for x in food:
        print(x)
fruits = ["apple","Cherry","banana"]
my_function6(fruits)

def myfunction7(x):
    return 5 * x

print(myfunction7(3))
print(myfunction7(5))
print(myfunction7(9))

def funcname(parameter_list):
    """
    docstring
    """
    pass

"""
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
"""
""" 
def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k -1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)


#x = lambda a: a + 10
#print(x(5))

#x = lambda a, b: a * b
#print(x(5,6))


#x = lambda a,b,c : a + b + c
#print(x(5,6,7))

def myfunc(n):
    
    return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(12))
 """

# Arrays


""" cars = ["Ford", "Volvo", "GMC"]
#print(cars)
for car in cars:
    print(car)

carArrayLength = len(cars)
print(carArrayLength)

cars.append("Honda")
cars.count("Ford") """

# Classes

#class Myclass:
 #   x = 5

#p1 = Myclass()
#print(p1.x)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person("john",36)
print(p1.name)
print(p1.age)
p1.age = 40
print(p1.age)