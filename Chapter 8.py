Chapter 8
Functions
functions, which are named blocks of code designed to do one specific job. When you want to perform a particular task that you’ve defined in a function, you call the function responsible for it. If you need to
perform that task multiple times throughout your program, you don’t need to type all the code for the same task again and again; you just call the function dedicated to handling that task, and the call tells Python to run the code inside the function.
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user(‘jesse’)

This is the function definition, which tells Python the name of the function and, if applicable, what kind of information the function needs to do its job. The parentheses hold that information.
Any indented lines that follow def greet_user(): make up the body of the function. The text on the second line is a comment called a docstring, which describes what the function does.
When you want to use this function, you have to call it. A function call tells Python to execute the code in the function. 
The variable username in the definition of greet_user() is an example of a parameter, a piece of information the function needs to do its job. The value 'jesse' in greet_user('jesse') is an example of an argument. An argument is a piece of information that’s passed from a function call to a function. When we call the function, we place the value we want the function to work with in parentheses.

You can use positional arguments, which need to be in the same order the parameters were written; keyword arguments, where each argument consists of a variable name and a value; default Values and lists and dictionaries of values.

❶ def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

❷ describe_pet('hamster', 'harry')

Keyword Arguments A keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the argument, so when you pass the argument to the function, there’s no confusion (you won’t end up with a harry named Hamster). Keyword arguments free you from having to worry about correctly ordering your arguments in the function call, and they clarify the role of each value in the function call. Let’s rewrite pets.py using keyword arguments to call describe_pet(): 
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')

The order of keyword arguments doesn’t matter because Python knows where each value should go. The following two function calls are equivalent: describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

Default Values When writing a function, you can define a default value for each parameter. If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter’s default value. 
Function call can now omit an argument for that parameter. Beware of positioning. Default arguments should be listed last in function definition. This allows function call to use easier to write positional arguments.

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
I have a dog.
My dog's name is Willie.

Equivalent Function Calls Because positional arguments, keyword arguments, and default values can all be used together, you’ll often have several equivalent ways to call a function.
Making an Argument Optional - Making an Argument Optional Sometimes it makes sense to make an argument optional, so that people using the function can choose to provide extra information only if they want to. You can use default values to make an argument optional. Frequently just set it to an empty string.
Returning a Dictionary – call usually enters the values, but can enter keys or keys and values in call. Dict={‘key1’:value1,’key2’:value2} format should be in function definition. 

Passing an Arbitrary Number of Arguments Sometimes you won’t know ahead of time how many arguments a function needs to accept. Fortunately, Python allows a function to
collect an arbitrary number of arguments from the calling statement. *name. Think of it as infinite list of parameters called name with None default value.Will automatically be a list of that name

The asterisk in the parameter name *toppings tells Python to make a tuple called toppings, containing all the values this function receives. The print() call in the function body produces output showing that Python can handle a function call with one value and a call with three values. It treats the different calls similarly. Note that Python packs the arguments into a tuple, even if the function receives only one value:

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
('pepperoni',)
('mushrooms', 'green peppers', 'extra cheese')
Mixing Positional and Arbitrary Arguments If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition. Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter.
def make_pizza(size, *toppings):
Using Arbitrary Keyword Arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
❶    	 user_info['first_name'] = first
    	user_info['last_name'] = last
    	return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
{'location': 'princeton', 'field': 'physics',
'first_name': 'albert', 'last_name': 'einstein'}

print(user_profile) The definition of build_profile() expects a first and last name, and then it allows the user to pass in as many name-value pairs as they want. The double asterisks before the parameter **user_info cause Python to create a dictionary called user_info containing all the extra name-value pairs the function receives.
You’ll often see the parameter name **kwargs used to collect nonspecific keyword arguments. To be used in a dictionary of that name. Note in call the key is written without any “” ‘’

Storing Your Functions in Modules One advantage of functions is the way they separate blocks of code from your main program. When you use descriptive names for your functions, your programs become much easier to follow. You can go a step further by storing your functions in a separate file called a module and then importing that module into your main program. An import statement tells Python to make the code in a module available in the currently running program file.

There are several ways to import a module, and I’ll show you each of these briefly. 
Importing an Entire Module
pizza.py 
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

making_pizzas.py 
import pizza                   # don’t need the .py at end

❶ pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

When Python reads this file, the line import pizza tells Python to open the file pizza.py and copy all the functions from it into this program. You don’t actually see code being copied between files because Python copies the code behind the scenes, just before the program runs. All you need to know is that any function defined in pizza.py will now be available in making_pizzas.py. To call a function from an imported module, enter the name of the module you imported, pizza, followed by the name of the function, make_pizza(), separated by a dot ❶. This code produces the same output as the original program that didn’t import a module:
This first approach to importing, in which you simply write import followed by the name of the module, makes every function from the module available in your program. If you use this kind of import statement to import an entire module named module_name.py, each function in the module is available through the following syntax: module_name.function_name()

Importing Specific Functions You can also import a specific function from a module. Here’s the general syntax for this approach: from module_name import function_name.
You can import as many functions as you want from a module by separating each function’s name with a comma: from module_name import function_0, function_1, function_2 The making_pizzas.py example would look like this if we want to import just the function we’re going to use: 
from pizza import make_pizza            # don’t need the .py or () at end

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') With this syntax, you don’t need to use the dot notation when you call a function. Because we’ve explicitly imported the function make_pizza() in the import statement, we can call it by name when we use the function.
Using as to Give a Function an Alias If the name of a function you’re importing might conflict with an existing name in your program, or if the function name is long, you can use a short, unique alias—an alternate name similar to a nickname for the function. You’ll give the function this special nickname when you import the function. Here we give the function make_pizza() an alias, mp(), by importing make_pizza as mp. The as keyword renames a function using the alias you provide: from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese') The import statement shown here renames the function make_pizza() to mp() in this program.
Anytime we want to call make_pizza() we can simply write mp() instead, and Python will run the code in make_pizza() while avoiding any confusion with another make_pizza() function you might have written in this program file. The general syntax for providing an alias is: from module_name import function_name as fn Using as to Give a Module an Alias You can also provide an alias for a module name. Giving a module a short alias, like p for pizza, allows you to call the module’s functions more quickly. Calling p.make_pizza() is more concise than calling pizza.make_pizza(): import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
The module pizza is given the alias p in the import statement, but all of the module’s functions retain their original names. Calling the functions by writing p.make_pizza() is not only more concise than pizza.make_pizza(), but it also redirects your attention from the module name and allows you to focus on the descriptive names of its functions. These function names, which clearly tell you what each function does, are more important to the readability of your code than using the full module name. The general syntax for this approach is: import module_name as mn

Importing All Functions in a Module You can tell Python to import every function in a module by using the asterisk (*) operator:   # the advantage over import pizza is that if calling function don’t have to put pizza.function name. Can just put function name.
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') The asterisk in the import statement tells Python to copy every function from the module pizza into this program file. Because every function is imported, you can call each function by name without using the dot notation. However, it’s best not to use this approach when you’re working with larger modules that you didn’t write: if the module has a function name that matches an existing name in your project, you can get unexpected results. Python may see several functions or variables with the same name, and instead of importing all the functions separately, it will overwrite the functions.
The best approach is to import the function or functions you want, or import the entire module and use the dot notation. This leads to clear code that’s easy to read and understand. I include this section so you’ll recognize import statements like the following when you see them in other people’s code: from module_name import * Styling Functions You need to keep a few details in mind when you’re styling functions. Functions should have descriptive names, and these names should use lowercase letters and underscores. Descriptive names help you and others understand what your code is trying to do. Module names should use these conventions as well.
Every function should have a comment that explains concisely what the function does. This comment should appear immediately after the function definition and use the docstring format. In a well-documented function, other programmers can use the function by reading only the description in the docstring. They should be able to trust that the code works as described, and as long as they know the name of the function, the arguments it needs, and the kind of value it returns, they should be able to use it in their programs. If you specify a default value for a parameter, no spaces should be used on either side of the equal sign: def function_name(parameter_0, parameter_1='default value') The same convention should be used for keyword arguments in function calls:
function_name(value_0, parameter_1='value') PEP 8 (https://www.python.org/dev/peps/pep-0008) recommends that you limit lines of code to 79 characters so every line is visible in a reasonably sized editor window. If a set of parameters causes a function’s definition to be longer than 79 characters, press ENTER after the opening parenthesis on the definition line. On the next line, press the TAB key twice to separate the list of arguments from the body of the function, which will only be indented one level. Most editors automatically line up any additional lines of arguments to match the indentation you have established on the first line: def function_name(
        parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5):
    function body... If your program or module has more than one function, you can separate each by two blank lines to make it easier to see where one function ends and the next one begins. All import statements should be written at the beginning of a file. The only exception is if you use comments at the beginning of your file to describe the overall program..

import module_name(file_name)
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import*
