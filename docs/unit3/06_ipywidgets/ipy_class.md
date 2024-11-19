# In Class Excersise: ipywidgets

In this class exercise, we will learn how to use ipywidgets to create interactive widgets in Google Colab and Jupyter notebooks. We will create a simple interactive widgets to demonstrate the basic functionality of ipywidgets and see the different types of widgets available.

To begin, create a copy of the "Starter_Sheet_In_Class_Workbook-ipywidgets": 

Then rename it something like, '**yourname_In_Class_Workbook_ipywidgets.ipynb'** and follow the follow instructions below. 

# Instructions

## Part 1: Basic HTML, more comments, and getting started

A lot of widgets use HTML for creating text and displaying images. If you click into the text box, you can see some example HTML text code showing different text styles and images. The following code block show another kind of comment that will print as a part of your code.

1. Find the code block titled "Imports" import the library for using ipywidgets.

<details>
<summary><b>Hint</b></summary>
    
    ```python
    !pip install ipywidgets
    import ipywidgets as widgets
    ```

</details>

For the remainder of our work, we don't have to keep installing ipywidgets because it is already in the system now.

2. In the code block titled "Input Text Box", create a text box that will allow the user to input their Favorite Food. Try having the text box have a placeholder and a description.

   - Try to print out the widget. Notice that the widget doesn't display. 
   - Now display the widget using the display() function.

3. In the code block titled "Text Box Value", write a print statement to print out the value of the text box