# Unit 2 Midterm Exam Study Guide

This study guide is designed to help you review and prepare for the Unit 2 Midterm Exam in CCE 270. It includes a summary of core concepts, a practice quiz with answers, and a glossary of key terms.

!!! Note
    This study guide is not exhaustive. Be sure to review the course reading content, in-class exercises, homework assignments, and any additional materials provided by your instructor.

## Core Concepts Summary

This section provides a detailed summary of the key concepts, procedures, and functions covered in the course materials.

### Chapter 2: Variables and Simple Data Types

This chapter introduces the fundamental building blocks of Python programming, including variables, data types, and basic operations.

* **Variables**: Labels that store values with associated names.
    * Naming rules: letters, numbers, underscores; cannot start with a number; no spaces; avoid Python keywords.
    * Best practices: short, descriptive, lowercase names.
* **Strings (Text Data)**: A series of characters enclosed in single or double quotes.
    * Case Manipulation: **title()**, **upper()**, **lower()**.
    * **f-strings**: Embedding variable values within strings using **f"{variable}"**.
    * **Whitespace**: Nonprinting characters like spaces, tabs (**\t**), and newlines (**\n**).
    * Stripping Whitespace: **rstrip()**, **lstrip()**, **strip()**.
    * Removing Prefixes/Suffixes: **removeprefix()**, **removesuffix()**.
* **Numbers**: Python supports integers and floating-point numbers for mathematical operations.
    * **Integers**: Whole numbers. Operations include addition (**+**), subtraction (**-**), multiplication (**\***), division (**/**), and exponents (**\*\***).
    * **Floats**: Numbers with a decimal point. Division of any two numbers always results in a float.
    * Underscores in Numbers: Using underscores for readability in long numbers (e.g., 14_000_000_000).
* **Data Structures & Assignment**: Techniques for assigning values to variables.
    * **Multiple Assignment**: Assigning values to multiple variables in one line (e.g., x, y, z = 0, 0, 0).
    * **Constants**: Variables intended to remain unchanged, indicated by all-caps names (e.g., MAX_CONNECTIONS).
* **Code Structure & Readability**: Best practices for writing clean, maintainable code.
    * **Comments**: Notes in plain language ignored by the interpreter, starting with a hash mark (**#**).
    * **The Zen of Python**: A set of principles for writing good Python code, accessed with **import this**. Key ideas include "Simple is better than complex" and "Readability counts."
* **Errors**: Common errors encountered when working with variables and data types.
    * **NameError**: Occurs when using a variable that has not been defined or is misspelled.
    * **SyntaxError**: Occurs when Python does not recognize a section of the program as valid code.

### Chapter 3: Introducing Lists

This chapter covers Python lists, which are versatile data structures for storing collections of items.

* **What is a List?**: A collection of items in a particular order.
    * Defined with square brackets (**[]**), with elements separated by commas.
* **Accessing Elements**: Retrieving specific items from a list using their position.
    * **Index**: Accessing an element by its position. Indexing starts at **0**.
    * Accessing the last element: Using index **-1**.
* **Modifying, Adding, and Removing Elements**: Methods for changing list contents.
    * Modifying: Changing an element's value using its index (e.g., **my_list[0] = 'new_value'**).
    * Adding Elements:
        * **append()**: Adds an element to the end of the list.
        * **insert()**: Adds an element at a specific position.
    * Removing Elements:
        * **del** statement: Removes an element at a known index.
        * **pop()**: Removes the last item from a list but allows you to work with it. Can also pop from any position (**pop(index)**).
        * **remove()**: Removes the first occurrence of a specific value.
* **Organizing a List**: Methods and functions for sorting and rearranging lists.
    * Permanent Sorting: **sort()** method changes the list's order permanently. Can be sorted in reverse with **sort(reverse=True)**.
    * Temporary Sorting: **sorted()** function returns a sorted copy of the list, leaving the original unchanged.
    * Reversing Order: **reverse()** method reverses the list's order permanently.
    * Finding Length: **len()** function returns the number of items in a list.
* **Errors**: Common errors when working with lists.
    * **IndexError**: Occurs when trying to access an index that is outside the range of the list.

### Chapter 4: Working with Lists

This chapter explores advanced list operations including iteration, numerical lists, slicing, and Python coding style conventions.

* **Looping**: Using **for** loops to iterate through list items.
    * **for loop**: Iterates through each item in a list, performing the same action on each one.
    * **Indentation**: Python uses indentation to determine which lines of code are inside the loop. Forgetting to indent, indenting unnecessarily, or indenting extra lines can lead to errors or unexpected behavior.
    * **Colon (:**): Required at the end of the **for** statement.
* **Numerical Lists**: Creating and working with lists of numbers.
    * **range()** function: Generates a series of numbers. **range(1, 5)** generates numbers 1, 2, 3, 4. Can accept a third "step" argument.
    * **list()** function: Converts the output of **range()** into a list.
    * Simple Statistics: **min()**, **max()**, **sum()** functions for lists of numbers.
    * **List Comprehensions**: A concise way to create lists (e.g., **squares = [value\*\*2 for value in range(1, 11)]**).
* **Working with Parts of a List**: Techniques for accessing and copying portions of lists.
    * **Slice**: A specific group of items in a list (e.g., **players[0:3]**).
    * Slicing syntax omits the item at the second index.
    * Omitting the first index (**[:4]**) starts from the beginning. Omitting the second (**[2:]**) goes to the end.
    * Copying a List: Use a slice with no indices (**[:]**) to create a copy. Assigning a list without a slice (**friend_foods = my_foods**) makes both variables point to the same list.
* **Tuples**: Immutable sequences that cannot be modified after creation.
    * An immutable (unchangeable) list.
    * Defined with parentheses **()**) instead of square brackets.
    * Values cannot be changed after definition, but the variable holding the tuple can be reassigned to a new tuple.
* **Code Styling (PEP 8)**: Python's style guide for writing clean, readable code.
    * Indentation: Use four spaces per level.
    * Line Length: Keep lines under 80 characters.
    * Blank Lines: Use to group parts of the program visually without being excessive.

### Chapter 5: if Statements

This chapter covers conditional logic in Python, allowing programs to make decisions based on different conditions.

* **Conditional Tests**: Expressions that evaluate to **True** or **False**.
    * An expression that evaluates to **True** or **False**.
    * Equality: **==** (case-sensitive).
    * Inequality: **!=**.
    * Numerical Comparisons: **<**, **<=**, **>**, **>=**.
    * Checking Multiple Conditions:
        * **and**: Both conditions must be **True**.
        * **or**: At least one condition must be **True**.
    * Checking for Values in a List:
        * **in**: Checks if a value is present in a list.
        * **not in**: Checks if a value is not present in a list.
    * **Boolean Expressions**: Another name for a conditional test, with values **True** or **False**.
* **if Statements**: Controlling program flow based on conditions.
    * **if**: Executes a block of code if a condition is **True**.
    * **if-else**: Executes one block if the condition is **True** and another if it is **False**.
    * **if-elif-else chain**: Tests a series of conditions in order. It executes the code for the first test that passes and skips the rest.
    * Multiple **if** statements: Use a series of independent **if** statements if you need to check all conditions and potentially run more than one block of code.
* **Using if Statements with Lists**: Applying conditional logic when working with lists.
    * Checking for special items within a **for** loop.
    * Checking if a list is empty. An empty list evaluates to **False** in a conditional test.
    * Comparing items between two lists (e.g., checking requested toppings against available toppings).

### Chapter 6: Dictionaries

This chapter introduces dictionaries, Python's most powerful data structure for storing related information in key-value pairs.

* **What is a Dictionary?**: A collection of key-value pairs where each key is connected to a value.
    * A collection of key-value pairs. Each key is connected to a value.
    * Defined with braces (**{}**), with key-value pairs separated by commas (e.g., **'key': 'value'**).
* **Working with Dictionaries**: Methods for accessing, adding, modifying, and removing data.
    * Accessing Values: Use the key in square brackets (e.g., **alien_0['color']**).
    * **.get()** method: Accesses a value but can provide a default value if the key does not exist, avoiding a **KeyError**.
    * Adding New Key-Value Pairs: **dictionary_name['new_key'] = 'new_value'**.
    * Modifying Values: Reassign a value to an existing key.
    * Removing Key-Value Pairs: Use the **del** statement (e.g., **del alien_0['points']**).
* **Looping Through Dictionaries**: Techniques for iterating through keys, values, or both.
    * All Key-Value Pairs: Use the **.items()** method (e.g., **for key, value in user_0.items():**).
    * All Keys: Use the **.keys()** method or loop directly over the dictionary (e.g., **for name in favorite_languages.keys():**).
    * All Values: Use the **.values()** method.
    * Looping in Order: Use **sorted()** on the keys to loop through a dictionary alphabetically.
* **Sets**: A collection where each item must be unique.
    * A collection where each item must be unique.
    * Created with **set()** or with braces **{}** (e.g., **languages = {'python', 'rust'}**).
    * Useful for finding unique values from a dictionary's values.
* **Nesting**: Storing complex data structures within dictionaries and lists.
    * A List of Dictionaries: Store multiple dictionaries in a single list.
    * A List in a Dictionary: Store a list as a value for a key in a dictionary.
    * A Dictionary in a Dictionary: Store a dictionary as a value for a key in another dictionary.

### Chapter 7: User Input and while Loops

This chapter covers how to accept user input and use while loops to repeat code as long as certain conditions are met.

* **User Input**: Getting data from users during program execution.
    * **input()** function: Pauses the program and waits for the user to enter text.
    * The **input()** function always interprets user input as a string.
    * **int()** function: Converts a string representation of a number to an integer for numerical comparisons or calculations.
* **while Loops**: Repeating code as long as a condition remains **True**.
    * Runs a block of code as long as a certain condition is **True**.
    * **Flag**: A variable (usually a boolean) that acts as a signal to control the loop's execution. The loop runs while the flag is **True**.
    * **break** statement: Exits a loop immediately, regardless of the conditional test.
    * **continue** statement: Skips the rest of the current iteration and returns to the beginning of the loop.
    * **Infinite Loops**: A loop that never ends because its condition always remains **True**. Can be stopped with **CTRL-C**.
* **Using while Loops with Lists and Dictionaries**: Applying **while** loops to modify collections.
    * Modifying a list while iterating through it (e.g., moving items from one list to another).
    * Removing all instances of a specific value from a list.
    * Filling a dictionary with user input.

### Chapter 8: Functions

This chapter teaches how to write functions, which are named blocks of code designed to perform specific tasks, making programs more organized and reusable.

* **Defining and Calling a Function**: Creating and executing custom functions.
    * **def** keyword: Used to define a function.
    * Function Name: Followed by parentheses **()**.
    * Function Body: Indented block of code that performs a specific job.
    * **Docstring**: A comment in triple quotes that describes the function's purpose.
    * Function Call: Executes the code inside the function.
* **Passing Arguments**: Providing data to functions for processing.
    * **Parameter**: A variable in the function definition.
    * **Argument**: A value passed to the function when it is called.
    * **Positional Arguments**: Arguments matched to parameters based on their order.
    * **Keyword Arguments**: Name-value pairs passed to a function, where order does not matter (e.g., **describe_pet(pet_name='harry', animal_type='hamster')**).
    * **Default Values**: Assigning a default value to a parameter in the function definition. Parameters with default values must come after those without.
* **Return Values**: Sending data back from a function to the calling code.
    * **return** statement: Takes a value from inside a function and sends it back to the line that called it.
    * Optional Arguments: Can be handled by giving a parameter a default value (like an empty string or **None**).
    * Functions can return any data type, including lists and dictionaries.
* **Working with Collections**: Passing lists and dictionaries to functions.
    * Passing a List: A function can modify a list passed to it. The changes are permanent.
    * Preventing Modification: Pass a copy of the list using slice notation (**[:]**) to prevent the original from being changed.
* **Arbitrary Arguments**: Accepting a variable number of arguments.
    * **Arbitrary Positional Arguments (\*args)**: Collects multiple positional arguments into a tuple (e.g., **def make_pizza(\*toppings):**). Must be the last positional parameter.
    * **Arbitrary Keyword Arguments (\*\*kwargs)**: Collects multiple keyword arguments into a dictionary (e.g., **def build_profile(first, last, \*\*user_info):**). Must be the final parameter.
* **Modules**: Organizing functions in separate files for reuse.
    * Storing functions in a separate **.py** file to be imported into another program.
    * **import module_name**: Imports the entire module. Functions are called with **module_name.function_name()**.
    * **from module_name import function_name**: Imports a specific function, which can then be called by name.
    * **Aliases**: Using **as** to give a function or module a shorter nickname (e.g., **import pizza as p** or **from pizza import make_pizza as mp**).
    * **from module_name import \***: Imports all functions from a module. Not generally recommended as it can cause name conflicts.




---


## Midterm Practice Quiz

Sample questions to help you prepare for the midterm exam. Answers are provided at the end of the quiz.

**True/False Questions**

1. Variable names in Python can start with a number.
2. The **title()** string method capitalizes the first letter of every word in a string.
3. When you divide any two numbers in Python, the result is always a **float**.
4. The **del** statement allows you to use the value of an item after you remove it from a list.
5. The **sorted()** function permanently changes the order of a list.
6. A **tuple** is a mutable collection of items, meaning its elements can be changed after it is created.
7. The **range(1, 5)** function generates the numbers 1, 2, 3, 4, 5.
8. In a conditional test, **and** requires both conditions to be true for the entire expression to be true.
9. An **if-elif-else** chain will execute all blocks of code for which the condition is **True**.
10. Dictionaries store items in a specific order, which is the order they were added.
11. To access a value in a dictionary, you must use its index number, just like in a list.
12. The **input()** function automatically interprets numerical input as an integer.
13. A **while True:** loop will run forever unless it encounters a **break** statement.
14. An argument is a piece of information that is passed from a function call to a function.
15. The **import module_name as mn** syntax imports only one function from the module.

**Multiple Choice Questions**

1. Which of the following is a valid Python variable name?<br>
a) 1st_message<br>
b) greeting message<br>
c) greeting_message<br>
d) print
2. What is the output of **print("Hello\tWorld")**?<br>
a) Hello World<br>
b) HelloWorld<br>
c) Hello  World (with a tab space)<br>
d) Hello\tWorld
3. Which method removes whitespace from both the left and right sides of a string?<br>
a) lstrip()<br>
b) rstrip()<br>
c) strip()<br>
d) clean()
4. What is the result of the expression **(2 + 3) \* 4**?<br>
a) 14<br>
b) 20<br>
c) 9<br>
d) 11
5. How do you access the third element in a list named **bicycles**?<br>
a) bicycles[3]<br>
b) bicycles[2]<br>
c) bicycles.get(3)<br>
d) bicycles.third()
6. Which method adds a new element to the end of a list?<br>
a) insert()<br>
b) add()<br>
c) append()<br>
d) push()
7. Which method removes the last item from a list and returns it?<br>
a) remove()<br>
b) del<br>
c) pop()<br>
d) strip()
8. What is the correct syntax for making a copy of a list named **my_list**?<br>
a) new_list = my_list<br>
b) new_list = my_list[:]<br>
c) new_list = copy(my_list)<br>
d) new_list = list(my_list)
9. What symbol is used to define a **tuple**?<br>
a) [] (Square Brackets)<br>
b) {} (Braces)<br>
c) () (Parentheses)<br>
d) <> (Angle Brackets)
10. Which of the following correctly creates a list of numbers from 2 to 10, counting by twos?<br>
a) list(range(2, 10, 2))<br>
b) list(range(2, 11, 2))<br>
c) list(range(2, 12, 2))<br>
d) list(range(1, 10, 2))
11. What is the output of **print(players[-1])** if **players = ['charles', 'martina', 'michael']**?<br>
a) 'charles'<br>
b) 'martina'<br>
c) 'michael'<br>
d) IndexError
12. In Python, what symbol represents the equality operator?<br>
a) =<br>
b) ==<br>
c) !=<br>
d) is
13. What keyword allows you to check if a value is present in a list?<br>
a) has<br>
b) contains<br>
c) is<br>
d) in
14. What does a boolean expression evaluate to?<br>
a) A string or a number<br>
b) True or False<br>
c) A list or a tuple<br>
d) Yes or No
15. If you want to run a specific block of code only when an **if** condition is false, which statement should you use?<br>
a) elif<br>
b) else<br>
c) except<br>
d) not if
16. What is the correct way to define a dictionary?<br>
a) my_dict = ['key': 'value']<br>
b) my_dict = ('key', 'value')<br>
c) my_dict = {'key': 'value'}<br>
d) my_dict = {'key' = 'value'}
17. Which method is used to loop through both the keys and values of a dictionary?<br>
a) .keys()<br>
b) .values()<br>
c) .items()<br>
d) .pairs()
18. What does the **get()** method do for a dictionary?<br>
a) It retrieves a value for a key but returns a default value instead of an error if the key doesn't exist.<br>
b) It gets the first item in the dictionary.<br>
c) It creates a new key-value pair.<br>
d) It permanently removes a key-value pair.
19. A collection in which each item must be unique is called a:<br>
a) List<br>
b) Dictionary<br>
c) Set<br>
d) Tuple
20. What function is used to get input from a user?<br>
a) get()<br>
b) read()<br>
c) prompt()<br>
d) input()
21. The **input()** function returns data of what type?<br>
a) Integer<br>
b) String<br>
c) Float<br>
d) Boolean
22. What is the modulo operator **%** used for?<br>
a) Percentage calculation<br>
b) Division<br>
c) Returning the remainder of a division<br>
d) Exponents
23. Which statement will immediately exit the current loop?<br>
a) continue<br>
b) exit<br>
c) stop<br>
d) break
24. In a function definition **def my_func(name):**, what is **name**?<br>
a) An argument<br>
b) A parameter<br>
c) A variable<br>
d) A return value
25. What is the purpose of a **return** statement in a function?<br>
a) To print a value to the screen.<br>
b) To stop the execution of the program.<br>
c) To send a value back to the line that called the function.<br>
d) To define the function's parameters.
26. To make a parameter optional in a function, you should provide it with a:<br>
a) Keyword argument<br>
b) Positional argument<br>
c) Default value<br>
d) Return value
27. Which syntax correctly collects an arbitrary number of positional arguments into a tuple?<br>
a) \*\*kwargs<br>
b) &args<br>
c) \*args<br>
d) @args
28. Which syntax correctly collects an arbitrary number of keyword arguments into a dictionary?<br>
a) \*\*kwargs<br>
b) \*args<br>
c) &kwargs<br>
d) dict()
29. A separate **.py** file that contains functions to be used in another program is called a:<br>
a) Script<br>
b) Library<br>
c) Module<br>
d) Package
30. Which import statement would allow you to call the function **make_pizza()** from the **pizza** module by using the alias **mp()**?<br>
a) import pizza as mp<br>
b) import pizza.make_pizza as mp<br>
c) from pizza import make_pizza as mp<br>
d) from pizza import \* as mp

**Short Answer Questions**

1. What is a variable in Python and why is it useful?
2. What is the difference between an **integer** and a **float**?
3. Write an **f-string** to print the value of a variable **name** in title case.
4. What is the purpose of the hash mark (**#**) in Python code?
5. What are the two main differences between a **list** and a **tuple**?
6. Explain what an **IndexError** is and provide a simple code example that would cause one.
7. Write a **list comprehension** that creates a list of the first 5 cubed numbers (1, 8, 27, 64, 125).
8. What is the difference between **list.sort()** and the **sorted()** function?
9. Explain the difference between **=** and **==**.
10. When should you use a series of **if** statements versus an **if-elif-else** chain?
11. What is a **key-value pair** in a dictionary?
12. How do you remove a key-value pair from a dictionary? Provide the line of code.
13. What is **nesting** in the context of Python data structures?
14. Why is it necessary to use **int()** on the result of **input()** when you want to perform a numerical calculation?
15. What is a "flag" in the context of a **while** loop?
16. What is the difference between the **break** and **continue** statements inside a loop?
17. In the function call **describe_pet(animal_type='dog', pet_name='willie')**, what type of arguments are being used?
18. What does it mean to provide a "default value" for a parameter in a function?
19. What is the purpose of a **docstring** in a function?
20. What is the syntax for importing an entire module named **printing_functions** and giving it the alias **pf**?




---


**Answer Key**

**True/False Answers**

1. False. Variable names must start with a letter or an underscore.
2. True.
3. True.
4. False. The del statement removes the item permanently without returning it. pop() returns the item.
5. False. sorted() returns a sorted copy of the list, leaving the original unchanged. sort() permanently changes the list.
6. False. A tuple is immutable, meaning its elements cannot be changed.
7. False. range(1, 5) generates numbers 1, 2, 3, 4. It stops before the end value.
8. True.
9. False. It only executes the first block whose condition is True and then skips the rest.
10. True. Since Python 3.7, dictionaries retain their insertion order.
11. False. You must use its key.
12. False. It interprets all input as a string.
13. True.
14. True.
15. False. This syntax imports the entire module and gives the module an alias, not just one function.

**Multiple Choice Answers**

1. c) **greeting_message**
2. c) Hello  World (with a tab space)
3. c) **strip()**
4. b) 20
5. b) **bicycles[2]** (Because indexing starts at 0)
6. c) **append()**
7. c) **pop()**
8. b) **new_list = my_list[:]**
9. c) **()** (Parentheses)
10. b) **list(range(2, 11, 2))** (Stops before 11, so 10 is included)
11. c) **'michael'**
12. b) **==**
13. d) **in**
14. b) **True** or **False**
15. b) **else**
16. c) **my_dict = {'key': 'value'}**
17. c) **.items()**
18. a) It retrieves a value for a key but returns a default value instead of an error if the key doesn't exist.
19. c) **Set**
20. d) **input()**
21. b) **String**
22. c) Returning the remainder of a division
23. d) **break**
24. b) A parameter
25. c) To send a value back to the line that called the function.
26. c) Default value
27. c) **\*args**
28. a) **\*\*kwargs**
29. c) **Module**
30. c) **from pizza import make_pizza as mp**

**Short Answer Answers**

1. A variable is a label or a name that you assign to a value. It's useful because it allows you to store information and refer to it later in the program using a descriptive name.
2. An **integer** is a whole number (e.g., 5, -10, 0), while a **float** is a number with a decimal point (e.g., 5.0, -10.25).
3. **print(f"Hello, {name.title()}!")**
4. The hash mark (**#**) indicates that the rest of the line is a **comment**, which is ignored by the Python interpreter.
5. A **list** is mutable (its contents can be changed) and is defined with square brackets **[]**. A **tuple** is immutable (its contents cannot be changed) and is defined with parentheses **()**.
6. An **IndexError** occurs when you try to access an item in a list at an index that doesn't exist. Example: **my_list = [1, 2]; print(my_list[2])**.
7. **cubes = [value\*\*3 for value in range(1, 6)]**
8. **list.sort()** permanently modifies the list in place and does not return a value. **sorted(list)** returns a new, sorted list and leaves the original list unchanged.
9. **=** is the assignment operator, used to assign a value to a variable. **==** is the equality operator, used to check if two values are equal.
10. Use a series of **if** statements when you want to check multiple conditions and potentially execute more than one block of code. Use an **if-elif-else** chain when you only want one block of code to run (the first one whose condition is met).
11. A **key-value pair** is a set of two associated values in a dictionary. The key is a unique identifier, and the value is the data connected to that key.
12. Use the **del** statement: **del my_dictionary['key_to_remove']**.
13. **Nesting** is storing a data structure inside another data structure, such as a list of dictionaries, a list inside a dictionary, or a dictionary inside another dictionary.
14. The **input()** function returns a string. If you want to use that input in a numerical context (like a math operation or comparison), you must first convert the string to a number using **int()** (for integers) or **float()**.
15. A **flag** is a variable, typically boolean (**True**/**False**), that is used to control whether a **while** loop continues to run. The loop continues as long as the flag's condition is met (e.g., **while active:**).
16. **break** exits the loop entirely. **continue** stops the current iteration and immediately jumps back to the beginning of the loop for the next iteration.
17. **Keyword arguments**.
18. It means you assign a value to a parameter in the function's definition, which will be used if no argument is provided for that parameter during the function call.
19. A **docstring** is a multi-line string immediately following a function's definition that explains what the function does. It helps with documentation.
20. **import printing_functions as pf**




---


## Glossary of Key Terms

| Term | Definition |
| :--- | :--- |
| **Argument** | A piece of information that is passed from a function call to a function. |
| **Boolean Expression** | Another name for a conditional test. A Boolean value is either True or False. |
| **Comment** | Notes in your spoken language, within your programs. In Python, a comment begins with a hash mark (#). |
| **Conditional Test** | An expression at the heart of every if statement that can be evaluated as True or False. |
| **Constant** | A variable whose value stays the same throughout the life of a program. Indicated in Python with all capital letters. |
| **Dictionary** | A collection of key-value pairs. Each key is connected to a value. Wrapped in braces ({}).  |
| **Docstring** | A comment that describes what a function does. Appears immediately after the function definition. |
| **f-string** | A string that allows you to embed variables by placing the letter f before the opening quote and putting variable names in braces ({}). |
| **Flag** | A variable that acts as a signal to the program, often used to determine if a while loop should continue running. |
| **Float** | Any number with a decimal point. |
| **Function** | A named block of code designed to do one specific job. Defined with the def keyword. |
| **Index** | The position of an item in a list. In Python, indexing starts at 0. |
| **Integer** | A whole number, without a decimal point. |
| **Key-Value Pair** | A set of values associated with each other in a dictionary. |
| **Keyword Argument** | A name-value pair that you pass to a function. Order does not matter. |
| **List** | A collection of items in a particular order. It is mutable and defined with square brackets ([]). |
| **List Comprehension** | A concise syntax that combines a for loop and the creation of new elements into one line to generate a list. |
| **Loop** | A control flow statement that allows code to be executed repeatedly. Examples are for and while loops. |
| **Method** | An action that Python can perform on a piece of data. It is called using dot notation (e.g., name.title()). |
| **Module** | A file ending in .py that contains code (like functions) you want to import into your program. |
| **Nesting** | Storing a collection of items (like a list or dictionary) inside another collection. |
| **Parameter** | A piece of information the function needs to do its job, specified in the function's definition. |
| **Positional Argument** | An argument passed to a function that is matched with a parameter based on its order. |
| **Return Value** | The value a function returns to the line that called it, using the return statement. |
| **Set** | A collection in which each item must be unique. Defined with braces ({}). |
| **Slice** | A specific group of items in a list. |
| **String** | A series of characters. Anything inside quotes is considered a string. |
| **Syntax Highlighting** | A text editor feature that displays different parts of a program in different colors to help distinguish code elements. |
| **Tuple** | An immutable (unchangeable) list. Defined with parentheses (()). |
| **Variable** | A label connected to a value, used to represent data in a program. |
| **Whitespace** | Any nonprinting character, such as spaces, tabs, and end-of-line symbols. |
