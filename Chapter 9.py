Chapter 9 Classes 
Making an object from a class is called instantiation, and you work with instances of a class.
A function that’s part of a class is a method. Everything you learned about functions applies to methods as well; the only practical difference for now is the way we’ll call methods. The __init__() method ❷ is a special method that Python runs automatically whenever we create a new instance based on the Dog class. This method has two leading underscores and two trailing underscores, a convention that helps prevent Python’s default method names from conflicting with your method names. Make sure to use two underscores on each side of __init__(). If you use just one on each side, the method won’t be called automatically when you use your class, which can result in errors that are difficult to identify.
Setting a Default Value for an Attribute When an instance is created, attributes can be defined without being passed in as parameters. These attributes can be defined in the __init__() method, where they are assigned a default value.

Modifying Attribute Values You can change an attribute’s value in three ways: you can change the value directly through an instance, set the value through a method, or increment the value (add a certain amount to it) through a method. Let’s look at each of these approaches.

Inheritance You don’t always have to start from scratch when writing a class. If the class you’re writing is a specialized version of another class you wrote, you can use inheritance. When one class inherits from another, it takes on the attributes and methods of the first class. The original class is called the parent class, and the new class is the child class. The child class can inherit any or all of the attributes and methods of its parent class, but it’s also free to define new attributes and methods of its own.

The __init__() Method for a Child Class When you’re writing a new class based on an existing class, you’ll often want to call the __init__() method from the parent class. This will initialize any attributes that were defined in the parent __init__() method and make them available in the child class. As an example, let’s model an electric car. An electric car is just a specific kind of car, so we can base our new ElectricCar class on the Car class we wrote earlier. Then we’ll only have to write code for the attributes and behaviors specific to electric cars. Let’s start by making a simple version of the ElectricCar class, which does everything the Car class does: 
electric_car.py ❶ 
class Car:
    """A simple attempt to represent a car."""
def __init__(self, make, model, year):
        """Initialize attributes to describe a car.""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
self.odometer_reading += miles

❷ class ElectricCar(Car):    #transfered methods from Car class
    """Represent aspects of a car, specific to electric vehicles."""
						# class rule of as long as have pass or one method don’t have to write init function. This case don’t for child and parent class
❸     def __init__(self, make, model, year):        #information needed to create Parent class
        """Initialize attributes of the parent class."""
❹         super().__init__(make, model, year)  #super represents all the methods in the Parent class


❺ my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
We start with Car ❶. When you create a child class, the parent class must be part of the current file and must appear before the child class in the file. We then define the child class, ElectricCar ❷. The name of the parent class must be included in parentheses in the definition of a child class. The __init__() method takes in the information required to make a Car instance ❸. The super() function ❹ is a special function that allows you to call a method from the parent class.
This line tells Python to call the __init__() method from Car, which gives an ElectricCar instance all the attributes defined in that method. The name super comes from a convention of calling the parent class a superclass and the child class a subclass.
Defining Attributes and Methods for the Child Class Once you have a child class that inherits from a parent class, you can add any new attributes and methods necessary to differentiate the child class from the parent class.
Overriding Methods from the Parent Class You can override any method from the parent class that doesn’t fit what you’re trying to model with
the child class. To do this, you define a method in the child class with the same name as the method you want to override in the parent class. Python will disregard the parent class method and only pay attention to the method you define in the child class.

When modeling something from the real world in code, you may find that you’re adding more and more detail to a class. You’ll find that you have a growing list of attributes and methods and that your files are becoming lengthy. In these situations, you might recognize that part of one class can be written as a separate class. You can break your large class into smaller classes that work together; this approach is called composition.
Importing Classes As you add more functionality to your classes, your files can get long, even when you use inheritance and composition properly. In keeping with the overall philosophy of Python, you’ll want to keep your files as uncluttered as possible. To help, Python lets you store classes in modules and then import the classes you need into your main program.
car.py 
❶ """A class that can be used to represent a car."""

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """


my_car.py 
❶ from car import Car

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

Importing Multiple Classes from a Module You can import as many classes as you need into a program file. If we want to make a regular car and an electric car in the same file, we need to import both classes, Car and ElectricCar: 
my_cars.py ❶ from car import Car, ElectricCar
Importing an Entire Module You can also import an entire module and then access the classes you need using dot notation. This approach is simple and results in code that is easy to read. Because every call that creates an instance of a class includes the module name, you won’t have naming conflicts with any names used in the current file. Here’s what it looks like to import the entire car module and then create a regular car and an electric car: 
my_cars.py ❶ import car
Importing All Classes from a Module You can import every class from a module using the following syntax: from module_name import * This method is not recommended for two reasons. First, it’s helpful to be able to read the import statements at the top of a file and get a clear sense of which classes a program uses. With this approach it’s unclear which classes you’re using from the module. This approach can also lead to confusion with names in the file. If you accidentally import a class with the same name as something else in your program file, you can create errors that are hard to diagnose. I show this here because even though it’s not a recommended approach, you’re likely to see it in other people’s code at some point. If you need to import many classes from a module, you’re better off importing the entire module and using the module_name.ClassName syntax. You won’t see all the classes used at the top of the file, but you’ll see clearly where the module is used in the program. You’ll also avoid the potential naming conflicts that can arise when you import every class in a module. 
Importing a Module into a Module 
Sometimes you’ll want to spread out your classes over several modules to keep any one file from growing too large and avoid storing unrelated classes in the same module. When you store your classes in several modules, you may find that a class in one module depends on a class in another module. When this happens, you can import the required class into the first module.
Using Aliases As you saw in Chapter 8, aliases can be quite helpful when using modules to organize your projects’ code. You can use aliases when importing classes as well. As an example, consider a program where you want to make a bunch of electric cars. It might get tedious to type (and read) ElectricCar over and over again. You can give ElectricCar an alias in the import statement:
from electric_car import ElectricCar as EC Now you can use this alias whenever you want to make an electric car: my_leaf = EC('nissan', 'leaf', 2024) You can also give a module an alias. Here’s how to import the entire electric_car module using an alias: import electric_car as ec Now you can use this module alias with the full class name: my_leaf = ec.ElectricCar('nissan', 'leaf', 2024)
The Python Standard Library The Python standard library is a set of modules included with every Python installation. Now that you have a basic understanding of how functions and classes work, you can start to use modules like these that other programmers have written. You can use any function or class in the standard library by including a simple import statement at the top of your file. Let’s look at one module, random, which can be useful in modeling many real-world situations.
https://pymotw.com/3/
