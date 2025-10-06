#  HW: Introduction to Functions

**Purpose:** Learn how to create and use functions.

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/04_intro_functions/(Starter_Workbook)_HW_Intro_Functions.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "(Your_Name)_HW_Intro_Functions".

Rebar is often delivered in standard lengths, such as 20 ft or 60 ft. When a contractor needs to cut rebar to 
specific lengths for a project, they want to minimize waste and maximize efficiency. Being able to model and 
optimize this process can lead to significant cost savings, more sustainable construction practices, and improve 
construction efficiency. In this assignment, you will create a function that calculates the waste and efficiency of 
cutting rebar from standard lengths.



---

#### Code Block 1

1. In the first code block, define a function called "optimize_rebar" that takes two parameters, the length of the 
   cut, "cut_length" and the length of the stock, "stock_length".
2. We need to know the total amount that is required, so we are going to create a new variable called 
   "total_cut" that 
   will be the sum of all the 
   cut lengths.
3. Your function is going 
   to have two if statements. The first if statement is going to check to see if the stock length is greater than 
   the total cut length.
4. If the stock length is greater than the sum of the cut lengths, then we can create a new variable that is the 
   difference between the stock length and the total cut. This variable will be the amount of wasted material.
5. If the stock length is less than the total cut, then we cannot cut all the lengths from the stock. In this case, 
   the wasted material will be 0.
6. The second if statement will check to see if the stock length is greater than 0. 
7. If the stock length is greater than 0, then we can create a new variable called efficiency that is the ratio of 
   the total cut to the stock length.
8. If the stock length is less than or equal to 0, then we cannot calculate efficiency. In this case, we will set 
   efficiency to be equal to 0.
9. Finally, return the variables waste and efficiency from the function.

## Code Block 2 - Defining Functions
In this code block you will create a function that prints the results of the optimization. It will call the function 
and set the waste and efficiency variables equal to the return values from the optimize_rebar function. It will also 
print the results in a readable format.

1. Define a function called print_results that takes two parameters: cut_length and stock_length.
2. Take waste and efficiency and set them equal to the return values from optimize_rebar(cut_length, stock_length). 
   This will call the function you created in Code Block 1.
3. Create a print function that prints the Rebar Cut Lengths, the Total Stock Length, the Wasted Length, and the 
   Efficiency as a percentage.

## Code Block 3 - Calling Functions
1. To test out your code try calling the print_results function with the following values:
   - cut_length = [10, 15, 7, 8]
   - stock_length = 50
   - print_results(cut_length, stock_length)
You should get the following output:
```
Waste: 10 ft
Efficiency: 80.0%
```
# Turning In/Rubric

Turn on sharing and editing. Turn in the link to the Learning Suite feedback box

|                            **Item**                             | **Amount** |  
|:---------------------------------------------------------------:|:----------:|
|               getCuFt function is defined correctly             |     4      |
|             cuftToCuyd function is defined correctly            |     4      |
|              volToTon function is defined correctly             |     4      |
|          getCostofGravel function is defined correctly          |     4      |
|      The forms and related variables are properly created       |     2      |
|               All functions are called correctly and used markdown               |     7      |
|             All print statements created correctly              |     5      |
|         <div style="text-align: right">**Total**</div>          |   **30**   |

The following is not part of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                      **Reasons for Points Lost**                         | **Amount** |  
|:------------------------------------------------------------------------:|:----------:|
|  No comments explaining why AI is used and what its provided code does   |     2-3    |
|                       Link shared incorrectly                            |      3     |
