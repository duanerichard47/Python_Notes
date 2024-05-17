Chapter 7
Input() - input function. When called will allow string input from terminal. Prompt message is in () to instruct user. Input always originally a string. Sometime this won’t work in code editor and have to run it in terminal.
While loop.
The for loop takes a collection of items and executes a block of code once for each item in the collection. In contrast, the while loop runs as long as, or while, a certain condition is true.

For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active. This variable, called a flag, acts as a signal to the program.
Active=True
While active:

To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the break statement.

while True:

city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

Note You can use the break statement in any of Python’s loops. For example, you could use break to quit a for loop that’s working through a list or a dictionary.

Using continue in a Loop Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue statement to return to the beginning of the loop, based on the result of a conditional test.

current_number = 0
while current_number < 10:

❶     current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
If your program gets stuck in an infinite loop, press CTRL-C or just close the terminal window displaying your program’s output.
