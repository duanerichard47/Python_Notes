Chapter 10 Files and Exceptions

Reading from a File
When you want to work with the information in a text file, the first step is to read the file into memory. You can then work through all of the file’s contents at once or work through the contents line by line.
Here’s a program that opens this file, reads it, and prints the contents of the file to the screen:

file_reader.py from pathlib import Path    #Path is a Class

❶ path = Path('pi_digits.txt')   # file contents are saved into Class instance of Path. Saved to an unknown parameter variable
❷ contents = path.read_text()  # .reat_text() is a method inside Path class. Returns file content as a string
print(contents)
To work with the contents of a file, we need to tell Python the path to the file. A path is the exact location of a file or folder on a system. Python provides a module called pathlib that makes it easier to work with files and directories, no matter which operating system you or your program’s users are working with. A module that provides specific functionality like this is often called a library, hence the name pathlib. We start by importing the Path class from pathlib. There’s a lot you can do with a Path object that points to a file. For example, you can check that the file exists before working with it, read the file’s contents, or write new data to the file. Here, we build a Path object representing the file pi_digits.txt, which we assign to the variable path ❶. Since this file is saved in the same directory as the .py file we’re writing, the filename is all that Path needs to access the file.
Once we have a Path object representing pi_digits.txt, we use the read_text() method to read the entire contents of the file ❷. The contents of the file are returned as a single string, which we assign to the variable contents. When we print the value of contents, we see the entire contents of the text file:
method chaining example contents = path.read_text().rstrip()
Relative and Absolute File Paths
There are two main ways to specify paths in programming. A relative file path tells Python to look for a given location relative to the directory where the currently running program file is stored. Since text_files is inside python_work, we need to build a path that starts with the directory text_files, and ends with the filename. Here’s how to build this path: 
path = Path('text_files/filename.txt') 
You can also tell Python exactly where the file is on your computer, regardless of where the program that’s being executed is stored. This is called an absolute file path. You can use an absolute path if a relative path doesn’t work. For instance, if you’ve put text_files in some folder other than python_work, then just passing Path the path 'text_files/filename.txt' won’t work because Python will only look for that location inside python_work. You’ll need to write out an absolute path to clarify where you want Python to look. Absolute paths are usually longer than relative paths, because they start at your system’s root folder: 
path = Path('/home/eric/data_files/text_files/filename.txt') 
Using absolute paths, you can read files from any location on your system. For now it’s easiest to store files in the same directory as your program files, or in a folder such as text_files within the directory that stores your program files. Note Windows systems use a backslash (\) instead of a forward slash (/) when displaying file paths, but you should use forward slashes in your code, even on Windows. The pathlib library will automatically use the correct representation of the path when it interacts with your system, or any user’s system.
Accessing a File’s Lines
You can use the splitlines() method to turn a long string into a set of lines, and then use a for loop to examine each line from a file, one at a time:
file_reader.py 
from pathlib import Path
path = Path('pi_digits.txt')
❶ contents = path.read_text()

❷ lines = contents.splitlines()
for line in lines:
    print(line)

Writing to a File 
One of the simplest ways to save data is to write it to a file. When you write text to a file, the output will still be available after you close the terminal containing your program’s output. You can examine output after a program finishes running, and you can share the output files with others as well. You can also write programs that read the text back into memory and work with it again later. Writing a Single Line Once you have a path defined, you can write to a file using the write_text() method. To see how this works, let’s write a simple message and store it in a file instead of printing it to the screen: 
write_message.py 
from pathlib import Path
path = Path('programming.txt')                   
path.write_text("I love programming.")  #write_text is a method in Path class.

The write_text() method takes a single argument: the string that you want to write to the file. This program has no terminal output, but if you open the file programming.txt, you’ll see one line: 
programming.txt
I love programming. This file behaves like any other file on your computer. You can open it, write new text in it, copy from it, paste to it, and so forth. Note Python can only write strings to a text file. If you want to store numerical data in a text file, you’ll have to convert the data to string format first using the str() function. 
Writing Multiple Lines The write_text() method does a few things behind the scenes. If the file that path points to doesn’t exist, it creates that file. Also, after writing the string to the file, it makes sure the file is closed properly. Files that aren’t closed properly can lead to missing or corrupted data.
To write more than one line to a file, you need to build a string containing the entire contents of the file, and then call write_text() with that string. Let’s write several lines to the programming.txt file: 
from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents) 
We define a variable called contents that will hold the entire contents of the file. On the next line, we use the += operator to add to this string. You can do this as many times as you need, to build strings of any length. In this case we include newline characters at the end of each line, to make sure each statement appears on its own line.
If you run this and then open programming.txt, you’ll see each of these lines in the text file: I love programming.
I love creating new games.
I also love working with data. You can also use spaces, tab characters, and blank lines to format your output, just as you’ve been doing with terminal-based output. There’s no limit to the length of your strings, and this is how many computer-generated documents are created. Note Be careful when calling write_text() on a path object. If the file already exists, write_text() will erase the current contents of the file and write new contents to the file. Later in this chapter, you’ll learn to check whether a file exists using pathlib.

Exceptions 
Python uses special objects called exceptions to manage errors that arise during a program’s execution. Whenever an error occurs that makes Python unsure of what to do next, it creates an exception object. If you write code that handles the exception, the program will continue running. If you don’t handle the exception, the program will halt and show a traceback, which includes a report of the exception that was raised. Exceptions are handled with try-except blocks. A try-except block asks Python to do something, but it also tells Python what to do if an exception is raised. When you use try-except blocks, your programs will continue running even if things start to go wrong. Instead of tracebacks, which can be confusing for users to read, users will see friendly error messages that you’ve written. 
Handling the ZeroDivisionError Exception 
Let’s look at a simple error that causes Python to raise an exception. You probably know that it’s impossible to divide a number by zero, but let’s ask Python to do it anyway: 
division_calculator.py 
print(5/0)
Python can’t do this, so we get a traceback: Traceback (most recent call last):
  File "division_calculator.py", line 1, in <module>
    print(5/0)
          ~^~
❶ ZeroDivisionError: division by zero 
The error reported in the traceback, ZeroDivisionError, is an exception object ❶. Python creates this kind of object in response to a situation where it can’t do what we ask it to. When this happens, Python stops the program and tells us the kind of exception that was raised. We can use this information to modify our program. We’ll tell Python what to do when this kind of exception occurs; that way, if it happens again, we’ll be prepared. 

Using try-except Blocks 
When you think an error may occur, you can write a try-except block to handle the exception that might be raised. You tell Python to try running some code, and you tell it what to do if the code results in a particular kind of exception. Here’s what a try-except block for handling the ZeroDivisionError exception looks like: 
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!") 

Let’s look at an example where catching an error can allow a program to continue running. 
Using Exceptions to Prevent Crashes 
Handling errors correctly is especially important when the program has more work to do after the error occurs. This happens often in programs that prompt users for input. If the program responds to invalid input appropriately, it can prompt for more valid input instead of crashing. Let’s create a simple calculator that does only division:
division_calculator.py print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
❶     first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
❷     second_number = input("Second number: ")
    if second_number == 'q':
        break
❸     answer = int(first_number) / int(second_number)
    print(answer) This program prompts the user to input a first_number ❶ and, if the user does not enter q to quit, a second_number ❷. We then divide these two numbers to get an answer ❸. This program does nothing to handle errors, so asking it to divide by zero causes it to crash: Give me two numbers, and I'll divide them.
Enter 'q' to quit.
First number: 5
Second number: 0
Traceback (most recent call last):
  File "division_calculator.py", line 11, in <module>
    answer = int(first_number) / int(second_number)
             ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~
ZeroDivisionError: division by zero It’s bad that the program crashed, but it’s also not a good idea to let users see tracebacks. Nontechnical users will be confused by them, and in a malicious setting, attackers will learn more than you want them to. For example, they’ll know the name of your program file, and they’ll see a part of your code that isn’t working properly. A skilled attacker can sometimes use this information to determine which kind of attacks to use against your code. The else Block We can make this program more error resistant by wrapping the line that might produce errors in a try-except block. The error occurs on the line that performs the division, so that’s where we’ll put the try-except block. This example also includes an else block. Any code that depends on the try block executing successfully goes in the else block: --snip--
while True:
    --snip--
    if second_number == 'q':
        break
❶     try:
        answer = int(first_number) / int(second_number)
❷     except ZeroDivisionError:
        print("You can't divide by 0!")
❸     else:
        print(answer) We ask Python to try to complete the division operation in a try block ❶, which includes only the code that might cause an error. Any code that depends on the try block succeeding is added to the else block. In this case, if the division operation is successful, we use the else block to print the result ❸. The except block tells Python how to respond when a ZeroDivisionError arises ❷. If the try block doesn’t succeed because of a division-by-zero error, we print a friendly message telling the user how to avoid this kind of error. The program continues to run, and the user never sees a traceback: Give me two numbers, and I'll divide them.
Enter 'q' to quit.

First number: 5
Second number: 0
You can't divide by 0!

First number: 5
Second number: 2
2.5

First number: q
The only code that should go in a try block is code that might cause an exception to be raised. Sometimes you’ll have additional code that should run only if the try block was successful; this code goes in the else block. The except block tells Python what to do in case a certain exception arises when it tries to run the code in the try block. By anticipating likely sources of errors, you can write robust programs that continue to run even when they encounter invalid data and missing resources. Your code will be resistant to innocent user mistakes and malicious attacks. 

Handling the FileNotFoundError Exception 
One common issue when working with files is handling missing files. The file you’re looking for might be in a different location, the filename might be misspelled, or the file might not exist at all. You can handle all of these situations with a try-except block.
Let’s try to read a file that doesn’t exist. The following program tries to read in the contents of Alice in Wonderland, but I haven’t saved the file alice.txt in the same directory as alice.py: 
alice.py from pathlib import Path

path = Path('alice.txt')
contents = path.read_text(encoding='utf-8') Note that we’re using read_text() in a slightly different way here than what you saw earlier. The encoding argument is needed when your system’s default encoding doesn’t match the encoding of the file that’s being read. This is most likely to happen when reading from a file that wasn’t created on your system. Python can’t read from a missing file, so it raises an exception:
Traceback (most recent call last):
❶   File "alice.py", line 4, in <module>
❷     contents = path.read_text(encoding='utf-8')
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/.../pathlib.py", line 1056, in read_text
    with self.open(mode='r', encoding=encoding, errors=errors) as f:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/.../pathlib.py", line 1042, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
❸ FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt' This is a longer traceback than the ones we’ve seen previously, so let’s look at how you can make sense of more complex tracebacks. It’s often best to start at the very end of the traceback. On the last line, we can see that a FileNotFoundError exception was raised ❸. This is important because it tells us
what kind of exception to use in the except block that we’ll write. Looking back near the beginning of the traceback ❶, we can see that the error occurred at line 4 in the file alice.py. The next line shows the line of code that caused the error ❷. The rest of the traceback shows some code from the libraries that are involved in opening and reading from files. You don’t usually need to read through or understand all of these lines in a traceback. To handle the error that’s being raised, the try block will begin with the line that was identified as problematic in the traceback. In our example, this is the line that contains read_text(): 
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
❶ except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")

Analyzing Text 
You can analyze text files containing entire books.
Let’s pull in the text of Alice in Wonderland and try to count the number of words in the text. To do this, we’ll use the string method split(), which by default splits a string wherever it finds any whitespace:
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate number of words in the file:
❶     words = contents.split()  # .split() method built into python creates a list [] looks at whitespace to consider parts of string a word and uses word as value in list
❷     num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
Working with Multiple Files
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 
        'little_women.txt']
for filename in filenames:
❶     path = Path(filename)
    count_words(path)

Failing Silently
In the previous example, we informed our users that one of the files was unavailable. But you don’t need to report every exception you catch. Sometimes, you’ll want the program to fail silently when an exception occurs and continue on as if nothing happened. To make a program fail silently, you write a try block as usual, but you explicitly tell Python to do nothing in the except block. Python has a pass statement that tells it to do nothing in a block: def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        --snip—
except FileNotFoundError:
        pass
    else:
        --snip—
The only difference between this listing and the previous one is the pass statement in the except block. Now when a FileNotFoundError is raised, the code in the except block runs, but nothing happens. No traceback is produced, and there’s no output in response to the error that was raised. Users see the word counts for each file that exists, but they don’t see any indication that a file wasn’t found:
The pass statement also acts as a placeholder. It’s a reminder that you’re choosing to do nothing at a specific point in your program’s execution and that you might want to do something there later.

Storing Data Many of your programs will ask users to input certain kinds of information. You might allow users to store preferences in a game or provide data for a visualization. Whatever the focus of your program is, you’ll store the information users provide in data structures such as lists and dictionaries. When users close a program, you’ll almost always want to save the information they entered. A simple way to do this involves storing your data using the json module.
The json module allows you to convert simple Python data structures into JSON-formatted strings, and then load the data from that file the next time the program runs. You can also use json to share data between different Python programs. Even better, the JSON data format is not specific to Python, so you can share data you store in the JSON format with people who work in many other programming languages. It’s a useful and portable format, and it’s easy to learn. Note The JSON (JavaScript Object Notation) format was originally developed for JavaScript. However, it has since become a common format used by many languages, including Python. Using json.dumps() and json.loads() Let’s write a short program that stores a set of numbers and another program that reads these numbers back into memory. The first program will use json.dumps() to store the set of numbers, and the second program will use json.loads(). The json.dumps() function takes one argument: a piece of data that should be converted to the JSON format. The function returns a string, which we can then write to a data file: 
number_writer.py 
from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

❶ path = Path('numbers.json') # File
❷ contents = json.dumps(numbers)  
path.write_text(contents) 
We first import the json module, and then create a list of numbers to work with. Then we choose a filename in which to store the list of numbers ❶. It’s customary to use the file extension .json to indicate that the data in the file is stored in the JSON format. Next, we use the json.dumps() ❷ function to generate a string containing the JSON representation of the data we’re working with. Once we have this string, we write it to the file using the same write_text() method we used earlier. This program has no output, but let’s open the file numbers.json and look at it. The data is stored in a format that looks just like Python: [2, 3, 5, 7, 11, 13] Now we’ll write a separate program that uses json.loads() to read the list back into memory: number_reader.py from pathlib import Path
import json
❶ path = Path('numbers.json')
❷ contents = path.read_text()
❸ numbers = json.loads(contents)
print(numbers) 
We make sure to read from the same file we wrote to ❶. Since the data file is just a text file with specific formatting, we can read it with the read_text() method ❷. We then pass the contents of the file to json.loads() ❸. This function takes in a JSON-formatted string and returns a Python object (in this case, a list), which we assign to numbers. Finally, we print the recovered list of numbers and see that it’s the same list created in number_writer.py: [2, 3, 5, 7, 11, 13] This is a simple way to share data between two programs 

Refactoring Often, you’ll come to a point where your code will work, but you’ll recognize that you could improve the code by breaking it up into a series of functions that have specific jobs. This process is called refactoring. Refactoring makes your code cleaner, easier to understand, and easier to extend.

.read_text() opens the path in text mode and returns the contents as a string.
.read_bytes() opens the path in binary mode and returns the contents as a byte string.
.write_text() opens the path and writes string data to it.
.write_bytes() opens the path in binary mode and writes data to it.
