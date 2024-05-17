**not, !, is not, is, !=, ==,   != means not equal value, is not means not equal value and if equal value not the same memory space
Boolean Operators-Comparison operators ==,!=,<,>,<=,>=  at least(>=) at most(<=)
Boolean Logical Operators and, or, not in, in

Iteration. Repeat code. Loops . Types: For, While, Do while
	The for loop is used when the number of iterations is known. The while loop is used when the number of iterations is unknown.

For loop- 
for (int i = 0; i < 5; i++)    for (statement 1; statement 2; statement 3) { // code block to be executed }
Statement 1 is executed (one time) before the execution of the code block. Statement 2 defines the condition for executing the code block. Statement 3 is executed (every time) after the code block has been executed.
Frequently used for iterating through list, string,  dictionary, or Range using “for x in list1”. 
	While loop-
while (condition) {  // code block to be executed} #frequently will use while True: code with break/continue. A flag. A not empty data structure. Or a comparison For loop is used when the number of iterations is known(usually a list type object), whereas execution is done in a while loop until the statement in the program is proved wrong

i = 1  
 while i < 6:
  print(i),   i += 1
Do While loop- makes sure initial block of code is always run at least once.

Concatenation -   print(7  *  ‘.’),   print(‘add’  +  ‘ this together’)
Pizza_topping =[‘cheese’, ‘ham’, ‘anchovy’], print(“Your pizza toppings are”, pizza_toppings)  output ..Your pizza toppings are [‘cheese’, ‘ham’, ‘anchovy’],


Conditional statement:  If, Elif, Else.(other languages use switches)
Memory address:  function id(). id() function in python is used to find the memory address referenced by a variable.
id() function will return a base 10 number. This can be converted to a hex number by using python’s inbuilt hex function.hex9id()


>>> a = list((1, 2, 3))
>>> isinstance(a, list)
True

>>> class Person:			class list:
   def __init__(self, name):		def __init__(self,())
       self.name = name				self.()=()
>>> emmy = Person("Emmy")                 [a = list((1, 2, 3))]
>>> isinstance(emmy, Person)            [ isinstance(a, list)]
True
>>>type(Person)
<class ‘type’>
>>>type(list)
<class ‘type’>
>>>type(emmy)
<class ‘__main__.Person’>
>>>type(a)
<class ‘list’>
