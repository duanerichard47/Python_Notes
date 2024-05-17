Chapter 6
A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. A key’s value can be a number, a string, a list, or even another dictionary. In fact, you can use any object that you can create in Python as a value in a dictionary.

Accessing Values in a Dictionary To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets, as shown here:
alien_0 = {'color': 'green','points':5}
print(alien_0['color']) >>> output: green

Adding New Key-Value Pairs 
	Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time. To add a new key-value pair, you would give the name of the dictionary followed by the new key in square brackets, along with the new value.

alien_0 = {'color': 'green','points':5}
alien_0['speed']='fast'
alien_0['age']= 102
print(alien_0) >>> output: {'color': 'green',  'points':5, 'speed':'fast',  'age': 102}

Modifying Values in a Dictionary 
	To modify a value in a dictionary, give the name of the dictionary with the key in square brackets and then the new value you want associated with that key.
alien_0['color'] = 'yellow'
print(alien_0) >>> output: {'color': 'yellow',  'points':5, 'speed':'fast',  'age': 102}

Removing Key-Value Pairs 
	When you no longer need a piece of information that’s stored in a dictionary, you can use the del statement to completely remove a key-value pair. All del needs is the name of the dictionary and the key that you want to remove. Remove's the value associated with that key as well.For example,

del alien_0['points']
print(alien_0) >>> output: {'color': 'yellow',  'speed':'fast',  'age': 102}

Using get() to Access Values 
	Using keys in square brackets to retrieve the value you’re interested in from a dictionary might cause one potential problem: if the key you ask for doesn’t exist, you’ll get an error.
For dictionaries specifically, you can use the get() method to set a default value that will be returned if the requested key doesn’t exist. The get() method requires a key as a first argument. As a second optional argument, you can pass the value to be returned if the key doesn’t exist:

The get() method requires a key as a first argument. As a second optional argument, you can pass the value to be returned if the key doesn’t exist:

might

If you leave out the second argument in the call to get() and the key doesn’t exist, Python

will return the value None. The special value None means “no value exists.” This is not an error: it’s a special value meant to indicate the absence of a value.
numbers = {'Al':7, 'Phil':9, 'Greg':11, 'Aaron': 5, 'Dave': 3,}
list_numbers =list(numbers)
print(f"{list_numbers[0]}'s favorite number is : {numbers['Al']}")
print(f"{list_numbers[1]}'s favorite number is : {numbers['Phil']}")
print(f"{list_numbers[2]}'s favorite number is : {numbers['Greg']}")
print(f"{list_numbers[3]}'s favorite number is : {numbers['Aaron']}\n")

numbers = {'Al':7, 'Phil':9, 'Greg':11, 'Aaron': 5, 'Dave': 3,}
dict_keys = list(numbers.keys())
dict_values = list(numbers.values())
print(f"{dict_keys[0]}'s favorite number is : {dict_values[0]}")
print(f"{dict_keys[1]}'s favorite number is : {dict_values[1]}")
print(f"{dict_keys[2]}'s favorite number is : {dict_values[2]}")
print(f"{dict_keys[3]}'s favorite number is : {dict_values[3]}\n")

numbers = {'Al':7, 'Phil':9, 'Greg':11, 'Aaron': 5, 'Dave': 3,}
dict_keys_list=[]
dict_values_list=[]
for k,v in numbers.items():  #for number in numbers will
    dict_keys_list.append(k)
    dict_values_list.append(v)
print(f"{dict_keys_list[0]}'s favorite number is : {dict_values_list[0]}")
print(f"{dict_keys_list[1]}'s favorite number is : {dict_values_list[1]}")
print(f"{dict_keys_list[2]}'s favorite number is : {dict_values_list[2]}")
print(f"{dict_keys_list[3]}'s favorite number is : {dict_values_list[3]}\n")

numbers = {'Al': 7, 'Phil': 9, 'Greg': 11, 'Aaron': 5, 'Dave': 3}
dictkeys = [k for k, v in numbers.items()] #1st k is for: [k] adding k to new list
dictvalues = [v for k, v in numbers.items()]#1st v is for: [v] adding k to new list
print(f"{dictkeys[0]}'s favorite number is : {dictvalues[0]}")
print(f"{dictkeys[1]}'s favorite number is : {dictvalues[1]}")
print(f"{dictkeys[2]}'s favorite number is : {dictvalues[2]}")
print(f"{dictkeys[3]}'s favorite number is : {dictvalues[3]}\n")


dict_keys_only = []  #default for loop on dictionary extracts only key by default
for keys in numbers:
    dict_keys_only.append(keys)
print(dict_keys_only)
print([keys for keys in numbers])#default for loop on dictionary extracts only key by default

list_keys_only=[]
list_values_only=[]
for key in numbers.keys():
    list_keys_only.append(keys)

for value in numbers.values():
    list_values_only.append(value)

d = {'key1': 'aaa', 'key2': 'aaa', 'key3': 'bbb'}

keys = [k for k, v in d.items() if v == 'aaa']
print(keys)
# ['key1', 'key2']

	Looping Through a Dictionary
Looping Through All Key-Value Pairs

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}") To write a for loop for a dictionary, you create names for the two variables that will hold the key and value in each key-value pair. You can choose any names you want for these two variables. This code would work just as well if you had used abbreviations for the variable names, like this:

for k, v in user_0.items() The second half of the for statement includes the name of the dictionary followed by the method items(), which returns a sequence of key-value pairs. The for loop then assigns each of these pairs to the two variables provided. In the preceding example, we use the variables to print each key, followed by the associated value. The "\n" in the first print() call ensures that a blank line is inserted before each key-value pair in the output: 
Key: username
Value: efermi

Key: first
Value: enrico

Key: last
Value: fermi

Looping Through All the Keys in a Dictionary The keys() method is useful when you don’t need to work with all of the values in a dictionary.

for key in user_0.keys():
    print(f"\nKey: {key}")
	Key: username
	Key: first
	Key: last


Looping through the keys is actually the default behavior when looping through a dictionary, so this code would have exactly the same output if you wrote: for name in user_0:

Looping Through a Dictionary’s Keys in a Particular Order 
	Looping through a dictionary returns the items in the same order they were inserted.

	for key in sorted(user_0.keys()):

Looping Through All Values in a Dictionary

	If you are primarily interested in the values that a dictionary contains, you can use the values() method to return a sequence of values without any keys.

	for value in user_0.values():
    print(f"\nValue: {value}")
		Value: efermi
		Value: enrico
		Value: fermi

A set is a collection in which each item must be unique: user_0 = {
    --snip--
    }

print("The following values have been mentioned:")
for value in set(user_0.values()):
    print(value.title()) When you wrap set() around a collection of values that contains duplicate items, Python identifies the unique items in the collection and builds a set from those items. Here we use set() to pull out the unique values in user_0.values().
 You can build a set directly using braces and separating the elements with commas: >>> languages = {'python', 'rust', 'python', 'c'}
>>> languages
{'rust', 'python', 'c'} It’s easy to mistake sets for dictionaries because they’re both wrapped in braces. When you see braces but no key-value pairs,you’re probably looking at a set. Unlike lists and dictionaries, sets do not retain items in any specific order. 

Nesting 
	Sometimes you’ll want to store multiple dictionaries in a list, or a list of items as a value in a dictionary. This is called nesting. You can nest dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary.


A List of Dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

❶ aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien) 
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}

A List in a Dictionary

# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summarize the order.
❶ print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

❷ for topping in pizza['toppings']:
    print(f"\t{topping}")

You ordered a thick-crust pizza with the following toppings:
    mushrooms
    extra cheese

A Dictionary in a Dictionary

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

    }

❶ for username, user_info in users.items():
❷     print(f"\nUsername: {username}")
❸     full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

❹     print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

Username: aeinstein
    Full name: Albert Einstein
    Location: Princeton

Username: mcurie
    Full name: Marie Curie	
