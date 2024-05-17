Chapter 2
When you run the file hello_world.py, the ending .py indicates that the file is a Python program. Your editor then runs the file through the Python interpreter, which reads through the program and determines what each word in the program means. For example, when the interpreter sees the word print followed by parentheses, it prints to the screen whatever is inside the parentheses.

Variable – is assigned a value. Place in memory is carved out. Variable name points to space in memory. Value is what is stored in memory.
String – 
	Print(Variable.title()) – Capitalizes string. Methods act on variables.If information is needed for the method to work it is entered in the ().
		.upper() – Changes all string characters to uppercase.  
.lower()- Changes all string characters to lowercase
full_name = f”{first_name} {last_name}”, print(full_name)  ,  f-string. F is for format. To insert a variable’s value into a string. Python will replace each variable with its value when the string is displayed. Can use with string literal.
Whitespace = print(“\tPython”) – prints out a tab space. Creates white space.
Newline = print(“Languages:\nPython\nC\nJavaScript”) 
Remove white space= ❶ >>> favorite_language = ' python ' , ❷ >>> print(favorite_language.rstrip())   > output: ' python' , ❸ >>>print( favorite_language.lstrip())   > output: 'python ' ❹ , >>> print(favorite_language.strip())   > output:'python'
		Removing Pre-fix = >>> nostarch_url = 'https://nostarch.com',    >>> print( nostarch_url.removeprefix('https://')),   >> output  > 'nostarch.com'
Numbers –
	Floats = >>> 0.2 + 0.1 = 0.30000000000000004
	Large numbers = written with underscores  14_000_000_000
	Multiple assignments =  x,y,z = 0,0,0
	Constants = MAX_CONNECTIONS = 5000
Comments -  #, “””   sssss”””, ‘’’ sssss’’’
None- The None keyword is used to define a null value, or no value at all.
None is not the same as 0, False, or an empty string. None is a class prdata type of its own (NoneType) and only None can be None.

You can use escape sequences in f-strings to include special characters, such as quotation marks, in your string. An escape sequence is a sequence of characters that begins with a backslash (\) and is followed by a letter or symbol.
