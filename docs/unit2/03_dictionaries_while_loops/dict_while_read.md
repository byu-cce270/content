#  Reading: Dictionaries and While Loops

---

# Pre Class Reading Assignment

On the O'Reilly's website read Chapter 6 in _Python Crash Course, 3rd Edition_  and Chapter 7, the section on "How 
the input() Function Works" and "Introducing while Loops." Don't bother with the other sections in Chapter 7.

Here is a direct link to the readings:</br>
[PCC Chapter 6: Dictionaries](https://learning.oreilly.com/library/view/python-crash-course/9781098156664/c06.xhtml){:target="_blank"}</br>
[PCC Chapter 7: User Input and While Loops](https://learning.oreilly.com/library/view/python-crash-course/9781098156664/c07.xhtml){:target="_blank"}

Remember that you will have to sign in to you free account that you created earlier.

## Things to Look Out For in Dictionaries
- Dictionaries use braces {} as opposed to lists which use square brackets []
- Keys and values are separated by colons, and key-value pairs are separated by commas
- A dictionary's keys cannot be lists, but its values can be

## Things to Look out For in Input/While Loops
- What is the input statement used for? 
- How do you format a prompt question if it doesn't fit on its initial line. 
- int?
- What is the difference between for loops and while loops?
- How would you code a stopping point if you wanted to stop the input program?

---

# Pre-Class Quiz Challenge
In a Colab notebook, complete Problem 6-5 found in chapter 6 of the textbook. Submit a link to the completed problem in your Pre-Class Quiz.

![preclasschallenge.png](images/preclasschallenge.png)

In this activity, you will create and work with a dictionary of pizza toppings, use loops to display information, and allow the user to add new toppings through input until they type "quit". Open the provided Google Colab notebook, follow the step-by-step comments, and fill in the missing code. When finished, run your program to check that it prints sentences about toppings, lists the keys and values separately, accepts new toppings, and displays the updated list at the end.

 Pizza Toppings Dictionary & While Loops
 In this activity, you'll practice:
 - Creating and modifying dictionaries
 - Looping through keys, values, and key-value pairs
 - Taking user input with a while loop

 Step 1: Create a dictionary called 'toppings' with at least
 three pizza toppings as keys and a short description as values.
 Example: 'pepperoni': 'spicy slices of cured meat'

toppings = {
     📝 Your code here
}

 Step 2: Use a for loop to print a sentence about each topping.
 Example: "Pepperoni is spicy slices of cured meat."

 📝 Your code here


 Step 3: Use a for loop to print just the topping names (keys).

 📝 Your code here


 Step 4: Use a for loop to print just the topping descriptions (values).

 📝 Your code here


 Step 5: Ask the user to add their own toppings in a while loop.
 Keep asking until they type 'quit'.
 For each new topping, store it in the dictionary with the value "custom topping"
 and print a message like "We'll add Mushrooms to your pizza."

 📝 Your code here


 Step 6: After the loop ends, print the final list of toppings (keys only).

 📝 Your code here

