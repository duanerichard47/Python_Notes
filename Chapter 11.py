Chapter 11 Testing Your Code
When you write a function or a class, you can also write tests for that code. Testing proves that your code works as it’s supposed to in response to all the kinds of input it’s designed to receive.
In this chapter, you’ll learn to test your code using pytest. The pytest library is a collection of tools that will help you write your first tests quickly and simply, while supporting your tests as they grow in complexity along with your projects. Python doesn’t include pytest by default, so you’ll learn to install external libraries. Knowing how to install external libraries will make a wide variety of well-designed code available to you. These libraries will expand the kinds of projects you can work on immensely.
Installing pytest with pip 
While Python includes a lot of functionality in the standard library, Python developers also depend heavily on third-party packages. A third-party package is a library that’s developed outside the core Python language. Some popular third-party libraries are eventually adopted into the standard library, and end up being included in most Python installations from that point forward. This happens most often with libraries that are unlikely to change much once they’ve had their initial bugs worked out. These kinds of libraries can evolve at the same pace as the overall language. Many packages, however, are kept out of the standard library so they can be developed on a timeline independent of the language itself. These packages tend to be updated more frequently than they would be if they were tied to Python’s development schedule. This is true of pytest and most of the libraries we’ll use in the second half of this book. You shouldn’t blindly trust every third-party package, but you also shouldn’t be put off by the fact that a lot of important functionality is implemented through such packages. 
Updating pip 
Python includes a tool called pip that’s used to install third-party packages. Because pip helps install packages from external resources, it’s updated often to address potential security issues. So, we’ll start by updating pip.
Open a new terminal window and issue the following command:
 $ python -m pip install --upgrade pip

The first part of this command, python -m pip, tells Python to run the module pip. The second part, install --upgrade, tells pip to update a package that’s already been installed. The last part, pip, specifies which third-party package should be updated.
You can use this command to update any third-party package installed on your system: 
$ python -m pip install --upgrade package_name
Installing pytest 
Now that pip is up to date, we can install pytest: 
$ python -m pip install --user pytest
We’re still using the core command pip install, without the --upgrade flag this time. Instead, we’re using the --user flag, which tells Python to install this package for the current user only. 
You can use this command to install many third-party packages: 
$ python -m pip install --user package_name
Note If you have any difficulty running this command, try running the same command without the --user flag.
Python application>pip already installed part of Python app and is used as secure way to install 3rd party add ons Like Google play does 	
Testing a Function
To learn about testing, we need code to test. Here’s a simple function that takes in a first and last name, and returns a neatly formatted full name: 
name_function.py
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title() 
The function get_formatted_name() combines the first and last name with a space in between to complete a full name, and then capitalizes and returns the full name. To check that get_formatted_name() works, let’s make a program that uses this function. The program names.py lets users enter a first and last name, and see a neatly formatted full name: 
names.py 
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.") 

This program imports get_formatted_name() from name_function.py. The user can enter a series of first and last names and see the formatted full names that are generated: 
Enter 'q' at any time to quit.

Please give me a first name: janis
Please give me a last name: joplin
       Neatly formatted name: Janis Joplin.

Please give me a first name: bob
Please give me a last name: dylan
        Neatly formatted name: Bob Dylan.

Please give me a first name: q
We can see that the names generated here are correct. But say we want to modify get_formatted_name() so it can also handle middle names. As we do so, we want to make sure we don’t break the way the function handles names that have only a first and last name. We could test our code by running names.py and entering a name like Janis Joplin every time we modify get_formatted_name(), but that would become tedious. Fortunately, pytest provides an efficient way to automate the testing of a function’s output. If we automate the testing of get_formatted_name(), we can always be confident that the function will work when given the kinds of names we’ve written tests for. 
Unit Tests and Test Cases 
There is a wide variety of approaches to testing software. One of the simplest kinds of test is a unit test. A unit test verifies that one specific aspect of a function’s behavior is correct. A test case is a collection of unit tests that together prove that a function behaves as it’s supposed to, within the full range of situations you expect it to handle. A good test case considers all the possible kinds of input a function could receive and includes tests to represent each of these situations. A test case with full coverage includes a full range of unit tests covering all the possible ways you can use a function. Achieving full coverage on a large project can be daunting. It’s often good enough to write tests for your code’s critical behaviors and then aim for full coverage only if the project starts to see widespread use.
A Passing Test
With pytest, writing your first unit test is pretty straightforward. We’ll write a single test function. The test function will call the function we’re testing, and we’ll make an assertion about the value that’s returned. If our assertion is correct, the test will pass; if the assertion is incorrect, the test will fail.
Here’s the first test of the function get_formatted_name():
test_name_function.py 
from name_function import get_formatted_name

❶ def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
❷     formatted_name = get_formatted_name('janis', 'joplin')
❸     assert formatted_name == 'Janis Joplin'
Before we run the test, let’s take a closer look at this function. The name of a test file is important; it must start with test_. When we ask pytest to run the tests we’ve written, it will look for any file that begins with test_, and run all of the tests it finds in that file. In the test file, we first import the function that we want to test: get_formatted_name(). Then we define a test function: in this case, test_first_last_name() ❶. This is a longer function name than we’ve been using, for a good reason. First, test functions need to start with the word test, followed by an underscore. Any function that starts with test_ will be discovered by pytest, and will be run as part of the testing process. Also, test names should be longer and more descriptive than a typical function name. You’ll never call the function yourself; pytest will find the function and run it for you. Test function names should be long enough that if you see the function name in a test report, you’ll have a good sense of what behavior was being tested. Next, we call the function we’re testing ❷. Here we call get_formatted_name() with the arguments 'janis' and 'joplin', just like we used when we ran names.py. We assign the return value of this function to formatted_name. Finally, we make an assertion ❸. An assertion is a claim about a condition. Here we’re claiming that the value of formatted_name should be 'Janis Joplin'.
Running a Test
If you run the file test_name_function.py directly, you won’t get any output because we never called the test function. Instead, we’ll have pytest run the test file for us. To do this, open a terminal window and navigate to the folder that contains the test file. If you’re using VS Code, you can open the folder containing the test file and use the terminal that’s embedded in the editor window. In the terminal window, enter the command pytest. Here’s what you should see: $ pytest
========================= test session starts =========================
❶ platform darwin -- Python 3.x.x, pytest-7.x.x, pluggy-1.x.x
❷ rootdir: /.../python_work/chapter_11
❸ collected 1 item

❹ test_name_function.py .                                          [100%]
========================== 1 passed in 0.00s ========================== Let’s try to make sense of this output. First of all, we see some information about the system the test is running on ❶. I’m testing this on a macOS system, so you may see some different output here. Most importantly, we can see which versions of Python, pytest, and other packages are being used to run the test. Next, we see the directory where the test is being run from ❷: in my case, python_work/chapter_11. We can see that pytest found one test to run ❸, and we can see the test file that’s being run ❹. The single dot after the name of the file tells us that a single test passed, and the 100% makes it clear that all of the tests have been run. A large project can have hundreds or thousands of tests, and the dots and percentage-complete indicator can be helpful in monitoring the overall progress of the test run.
The last line tells us that one test passed, and it took less than 0.01 seconds to run the test. This output indicates that the function get_formatted_name() will always work for names that have a first and last name, unless we modify the function. When we modify get_formatted_name(), we can run this test again. If the test passes, we know the function will still work for names like Janis Joplin.
Note If you’re not sure how to navigate to the right location in the terminal, see “Running Python Programs from a Terminal” on page 11. Also, if you see a message that the pytest command was not found, use the command python -m pytest instead.
A Failing Test
What does a failing test look like? Let’s modify get_formatted_name() so it can handle middle names, but let’s do so in a way that breaks the function for names with just a first and last name, like Janis Joplin. Here’s a new version of get_formatted_name() that requires a middle name argument:
name_function.py
def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()
This version should work for people with middle names, but when we test it, we see that we’ve broken the function for people with just a first and last name. This time, running pytest gives the following output: $ pytest
========================= test session starts =======
==================
--snip--
❶ test_name_function.py F                                          [100%]
❷ ============================== FAILURES ===============================
❸ ________________________ test_first_last_name _________________________
    def test_first_last_name():
        """Do names like 'Janis Joplin' work?"""
❹ >       formatted_name = get_formatted_name('janis', 'joplin')
❺ E       TypeError: get_formatted_name() missing 1 required positional
            argument: 'last'

test_name_function.py:5: TypeError
======================= short test summary info =======================
FAILED test_name_function.py::test_first_last_name - TypeError:
    get_formatted_name() missing 1 required positional argument: 'last'
========================== 1 failed in 0.04s ==========================
There’s a lot of information here because there’s a lot you might need to know when a test fails. The first item of note in the output is a single F ❶, which tells us that one test failed. We then see a section that focuses on FAILURES ❷, because failed tests are usually the most important thing to focus on in a test run. Next, we see that test_first_last_name() was the test function that failed ❸. An angle bracket ❹ indicates the line of code that caused the test to fail. The E on the next line ❺ shows the actual error that caused the failure: a TypeError due to a missing required positional argument, last. The most important information is repeated in a shorter summary at the end, so when you’re running many tests, you can get a quick sense of which tests failed and why.
Responding to a Failed Test
What do you do when a test fails? Assuming you’re checking the right conditions, a passing test means the function is behaving correctly and a failing test
means there’s an error in the new code you wrote. So when a test fails, don’t change the test. If you do, your tests might pass, but any code that calls your function like the test does will suddenly stop working. Instead, fix the code that’s causing the test to fail. Examine the changes you just made to the function, and figure out how those changes broke the desired behavior. In this case, get_formatted_name() used to require only two parameters: a first name and a last name. Now it requires a first name, middle name, and last name. The addition of that mandatory middle name parameter broke the original behavior of get_formatted_name(). The best option here is to make the middle name optional. Once we do, our test for names like Janis Joplin should pass again, and we should be able to accept middle names as well. Let’s modify get_formatted_name() so middle names are optional and then run the test case again. If it passes, we’ll move on to making sure the function handles middle names properly.
To make middle names optional, we move the parameter middle to the end of the parameter list in the function definition and give it an empty default value. We also add an if test that builds the full name properly, depending on whether a middle name is provided:
name_function.py 
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
In this new version of get_formatted_name(), the middle name is optional. If a middle name is passed to the function, the full name will contain a first, middle, and last name. Otherwise, the full name will consist of just a first and last name. Now the function should work for both kinds of names. To find out if the function still works for names like Janis Joplin, let’s run the test again: $ pytest
========================= test session starts =========================
--snip--
test_name_function.py .                                       [100%]
========================== 1 passed in 0.00s ==========================
 The test passes now. This is ideal; it means the function works for names like Janis Joplin again, without us having to test the function manually. Fixing our function was easier because the failed test helped us identify how the new code broke existing behavior.
Adding New Tests 
Now that we know get_formatted_name() works for simple names again, let’s write a second test for people who include a middle name. We do this by adding another test function to the file test_name_function.py: 
test_name_function.py 
from name_function import get_formatted_name

def test_first_last_name():
    --snip--

def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
❶     formatted_name = get_formatted_name(
        'wolfgang', 'mozart', 'amadeus')
❷     assert formatted_name == 'Wolfgang Amadeus Mozart' 
We name this new function test_first_last_middle_name(). The function name must start with test_ so the function runs automatically when we run pytest. We name the function to make it clear which behavior of get_formatted_name() we’re testing. As a result, if the test fails, we’ll know right away what kinds of names are affected.
To test the function, we call get_formatted_name() with a first, last, and middle name ❶, and then we make an assertion ❷ that the returned full name matches the full name (first, middle, and last) that we expect. When we run pytest again, both tests pass: $ pytest
========================= test session starts =========================
--snip--
collected 2 items

❶ test_name_function.py ..                                         [100%]
========================== 2 passed in 0.01s ========================== The two dots ❶ indicate that two tests passed, which is also clear from the last line of output. This is great! We now know that the function still works for names like Janis Joplin, and we can be confident that it will work for names like Wolfgang Amadeus Mozart as well.
Testing a Class
 In the first part of this chapter, you wrote tests for a single function. Now you’ll write tests for a class. You’ll use classes in many of your own programs, so it’s helpful to be able to prove that your classes work correctly. If you have passing tests for a class you’re working on, you can be confident that improvements you make to the class won’t accidentally break its current behavior.
A Variety of Assertions So far, you’ve seen just one kind of assertion: a claim that a string has a specific value. When writing a test, you can make any claim that can be expressed as a conditional statement. If the condition is True as expected, your assumption about how that part of your program behaves will be confirmed; you can be confident that no errors exist. If the condition you assume is True is actually False, the test will fail and you’ll know there’s an issue to resolve. Table 11-1 shows some of the most useful kinds of assertions you can include in your initial tests. Table 11-1: Commonly Used Assertion Statements in Tests Assertion Claim assert a == b Assert that two values are equal. assert a != b Assert that two values are not equal. assert a Assert that a evaluates to True.
assert not a Assert that a evaluates to False. assert element in list Assert that an element is in a list. assert element not in list Assert that an element is not in a list. These are just a few examples; anything that can be expressed as a conditional statement can be included in a test. A Class to Test Testing a class is similar to testing a function, because much of the work involves testing the behavior of the methods in the class. However, there are a few differences, so let’s write a class to test. Consider a class that helps administer anonymous surveys: survey.py class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

❶
❶     def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

❷     def show_question(self):
        """Show the survey question."""
        print(self.question)

❸     def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

❹     def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}") 
This class starts with a survey question that you provide ❶ and includes an empty list to store responses. The class has methods to print the survey question ❷, add a new response to the response list ❸, and print all the responses stored in the list ❹. To create an instance from this class, all you have to provide is a question. Once you have an instance representing a particular survey, you display the survey question with show_question(), store a response using store_response(), and show results with show_results(). To show that the AnonymousSurvey class works, let’s write a program that uses the class: language_survey.py from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
language_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results() This program defines a question ("What language did you first learn to speak?") and creates an AnonymousSurvey object with that question. The program calls show_question() to display the question and then prompts for responses. Each response is stored as it is received. When all responses have been entered (the user inputs q to quit), show_results() prints the survey results: What language did you first learn to speak?
Enter 'q' at any time to quit.

Language: English
Language: Spanish
Language: English
Language: Mandarin
Language: q

Thank you to everyone who participated in the survey!
Survey results:
- English
- Spanish
- English
- Mandarin This class works for a simple anonymous survey, but say we want to improve AnonymousSurvey and the module it’s in, survey. We could allow each user to enter more than one response, we could write a method to list only unique responses and to report how many times each response was given, or we could even write another class to manage non-anonymous surveys. Implementing such changes would risk affecting the current behavior of the class AnonymousSurvey. For example, it’s possible that while trying to allow each user to enter multiple responses, we could accidentally change how single responses are handled. To ensure we don’t break existing behavior as we develop this module, we can write tests for the class. Testing the AnonymousSurvey Class Let’s write a test that verifies one aspect of the way AnonymousSurvey behaves. We’ll write a test to verify that a single response to the survey question is stored properly: test_survey.py from survey import AnonymousSurvey

❶ def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
❷     language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
❸     assert 'English' in language_survey.responses
 We start by importing the class we want to test, AnonymousSurvey. The first test function will verify that when we store a response to the survey question, the response will end up in the survey’s list of responses. A good descriptive name for this function is test_store_single_response() ❶. If this test fails, we’ll know from the function name in the test summary that there was a problem storing a single response to the survey. To test the behavior of a class, we need to make an instance of the class. We create an instance called language_survey ❷ with the question "What language did you first learn to speak?" We store a single response, English, using the store_response() method. Then we verify that the response was stored correctly by asserting that English is in the list language_survey.responses ❸. By default, running the command pytest with no arguments will run all the tests that pytest discovers in the current directory. To focus on the tests in one file, pass the name of the test file you want to run. Here we’ll run just the one test we wrote for AnonymousSurvey:
$ pytest test_survey.py
========================= test session starts =========================
--snip--
test_survey.py .                                                 [100%]
========================== 1 passed in 0.01s ========================== This is a good start, but a survey is useful only if it generates more than one response. Let’s verify that three responses can be stored correctly. To do this, we add another method to TestAnonymousSurvey:
 from survey import AnonymousSurvey

def test_store_single_response():
    --snip--

def test_store_three_responses():
    """Test that three individual responses are stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
❶     responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

❷     for response in responses:
        assert response in language_survey.responses We call the new function test_store_three_responses(). We create a survey object just like we did in test_store_single_response(). We define a list containing three different responses ❶, and then we call store_response() for each of these responses. Once the responses have been stored, we write another loop and assert that each response is now in language_survey.responses ❷. When we run the test file again, both tests (for a single response and for three responses) pass: $ pytest test_survey.py
========================= test session starts =========================
--snip--
test_survey.py ..                                                [100%]
========================== 2 passed in 0.01s ========================== This works perfectly. However, these tests are a bit repetitive, so we’ll use another feature of pytest to make them more efficient. Using Fixtures In test_survey.py, we created a new instance of AnonymousSurvey in each test function. This is fine in the short example we’re working with, but in a real-world project with tens or hundreds of tests, this would be problematic. In testing, a fixture helps set up a test environment. Often, this means creating a resource that’s used by more than one test. We create a fixture in pytest by writing a function with the decorator @pytest.fixture. A decorator is a directive placed just before a function definition; Python applies this directive to the function before it runs, to alter how the function code behaves. Don’t worry if this sounds complicated; you can start to use decorators from third-party packages before learning to write them yourself. Let’s use a fixture to create a single survey instance that can be used in both test functions in
 test_survey.py: 
import pytest
from survey import AnonymousSurvey
❶ @pytest.fixture
❷ def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

❸ def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
❹     language_survey.store_response('English')
    assert 'English' in language_survey.responses

❺ def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
❻         language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
 We need to import pytest now, because we’re using a decorator that’s defined in pytest. We apply the @pytest.fixture decorator ❶ to the new function language_survey() ❷. This function builds an AnonymousSurvey object and returns the new survey. Notice that the definitions of both test functions have changed ❸ ❺; each test function now has a parameter called language_survey. When a parameter in a test function matches the name of a function with the @pytest.fixture decorator, the fixture will be run automatically and the return value will be passed to the test function. In this example, the function language_survey() supplies both test_store_single_response() and test_store_three_responses() with a language_survey instance. There’s no new code in either of the test functions, but notice that two lines have been removed from each function ❹ ❻: the line that defined a question and the line that created an AnonymousSurvey object. When we run the test file again, both tests still pass. These tests would be particularly useful when trying to expand AnonymousSurvey to handle multiple responses for each person. After modifying the code to accept multiple responses, you could run these tests and make sure you haven’t affected the ability to store a single response or a series of individual responses. The structure above will almost certainly look complicated; it contains some of the most abstract code you’ve seen so far. You don’t need to use fixtures right away; it’s better to write tests that have a lot of repetitive code than to write no tests at all. Just know that when you’ve written enough tests that the repetition is getting in the way, there’s a well-established way to deal with the repetition. Also, fixtures in simple examples like this one don’t really make the code any shorter or simpler to follow. But in projects with many tests, or in situations where it takes many lines to build a resource that’s used in multiple tests, fixtures can drastically improve your test code. When you want to write a fixture, write a function that generates the resource that’s used by multiple test functions. Add the @pytest.fixture decorator to the new function, and add the name of this function as a parameter for each test function that uses this resource. Your tests will be shorter and easier to write and maintain from that point forward.
Wrap function or method in test_ function. Can  pass instance or  into this function.  Call function or method entering made up arguments.  Have one line assert  to test boolean expression that contains return value or result variable is true. 

