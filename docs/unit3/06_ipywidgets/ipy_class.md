# In Class Excersise: ipywidgets

In this class exercise, we will learn how to use ipywidgets to create interactive widgets in Google Colab and Jupyter notebooks. We will create a simple interactive widgets to demonstrate the basic functionality of ipywidgets and see the different types of widgets available.

To begin, create a copy of the "Starter_Sheet_In_Class_Workbook-ipywidgets": 

Then rename it something like, '**yourname_In_Class_Workbook_ipywidgets.ipynb'** and follow the follow instructions below. 

## Instructions

### Part 1: Basic HTML, more comments, and getting started

A lot of widgets use HTML for creating text and displaying images. If you click into the text box, you can see some example HTML text code showing different text styles and images. The following code block show another kind of comment that will print as a part of your code.

1. Find the code block titled "Imports" import the library for using ipywidgets.

<details>
   <summary><b>Hint</b></summary>
   <div style="margin-left: 20px;">
      <pre><code>
         import ipywidgets as widgets
      </code></pre>
   </div>
</details>

<br> For the remainder of our work, we don't have to keep installing ipywidgets because it is already in the system now.

2. In the code block titled "Input Text Box", create a text box that will allow the user to input their Favorite Food. Try having the text box have a placeholder and a description.

      - Try to print out the widget. Notice that the widget doesn't display. 
      - Now display the widget using the display() function.

3. In the code block titled "Text Box Value", write a print statement to print out the value of the text box


### Part 2: Buttons

In this part, we will create a button that will print out a message when clicked.

1. In the code block titled "Basic Button", create a button with the following. Then display the button.

      - A description 
      - A style or color
      - A tooltip

2. In the code block titled "callMeAl function", you will find a function that will print out a message when a function is called. Run this code block to put the function in the memory to use later. Try changing your name the name where the function is called to your name. 

3. In the code block titled "Button Click", create a button that will call the function when clicked. Create a new button. Be sure to change the description to something that makes sense and add some color. Make sure to display the button. Now we need to create a function that will capture the click event. Finally, we need to assign the function to the "on_click" event of the button. 

<details>
   <summary><b>Hint</b></summary>
   <div style="margin-left: 20px;">
      Your function should have parameter, call the function, and print it.
   </div>
</details>
<br>

4. In the code block titled "Free Complement Button", create a button with a fun description, color, and tooltip. Then create a function that will print out a complement when the button is clicked. You should only need 1 function for this. Then try it. 

<details>
   <summary><b>Hint</b></summary>
   <div style="margin-left: 20px;">
      Try writing the code from scratch, but if needed, you can use the code from the previous example.
   </div>
</details>
<br>


### Part 3: Accepting Text Input

In this part, the first two code blocks are an example code you can reference to create a text box that will accept text input and a button that will print something based off the input.

1. In the code block titled "Modified Compliment Button", create a text box that will accept text input. Then create a new button that will print out a complement based off the text input.

<details>
   <summary><b>Hint</b></summary>
   <div style="margin-left: 20px;">
      Try writing the code from scratch, but if needed, you can use the code from the previous example.
   </div>
</details>
<br>


### Part 4: Side Note on the Random Module

In this part, we will learn how to use the random module to generate random numbers. To start, go the code block titled "Imports" at the top of the notebook and import the random module.

1. In the code block titled "Intro to Random", create a variable and set it equal to random.random(). This creates a random number between 0 and 1. Then print out the variable. Then try running the code block a few times to see the different numbers that are generated. Then write a new variable and set it equal to random.random() * 100. This will create a random number between 0 and 100. Print out the variable. We could also make the number an integer by using the int() function. Notice how everytime you run the code block, the number changes.

2. In the code block titled "randrange", create a variable and set it equal to random.randrange(100). This will create a random number between 1 and 100. Print out the variable. Then try running the code block a few times to see the different numbers that are generated. It's kind of like "randbetween" in Google Sheets. if you specify only one parameter to the function, it will give you a random integer from 0 to the number you specify in parentheses.

3. With the random function, you can select not just numbers, but also items from a list.In the code block titled "Multiple Random Choices", you will find a list of names called "myList". 
      - Create a variable and use the choice method to select a random name from the list. Print out the variable.
      - The Choices method has a few optional parameters that you can use to select multiple items from the list. You can see the different parameter options here: [Random Choices() Method](https://www.w3schools.com/python/ref_random_choices.asp){:target="_blank"} Try using the parameter "k" to select 3 random names from the list. Print out the variable.
      - A similar method is the sample method. The sample method will return a list of unique items from the list. Create a variable and use the sample method to select 3 random names from the list. Print out the variable.

    Try running the code block a few times to see the different names that are generated for each of the 3 variables created. You should see duplicates in the second print statement, but not the third one.


### Part 5: Common Widget Examples

Nothing needs to be done here, but this is a good reference for the different types of widgets that are available.



## Turning in/Rubric
Turn sharing and editing on, then submit the link to Learning Suite in the feedback box. In-class assignment scores are based on valid effort and completion.
