#  HW: Introduction to Functions

**Purpose:** Learn how to create and use functions.

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/04_intro_functions/(Starter_Workbook)_HW_Intro_Functions.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "(Your_Name)_HW_Intro_Functions".

In this assignment, you will be calculating the efficiency of cutting rebar from stock lengths and the wasted material. 
You will 
create functions to perform the calculations and print the results.

---

#### Code Block 1

1. In the first code block, define a function called optimize_rebar that takes two parameters, the length of the cut "cut_lengths" and the length of the stock, "stock_length".
2. We are going to create a new variable called total cut that will be the sum of all the cut lengths.
3. In this problem we are going to be pulling knowledge from our previous if statement lessons. Your function is going 
   to have two if statements. The first if statement is going to check to see if the stock length is greater than or 
   equal to the sum of the 
   cut lengths. 
4. If the stock length is greater than or equal to the sum of the cut lengths, then we can create a new variable 
   called wasted_length that is the difference between the stock length and the sum of the cut lengths.
5. If the stock length is less than the sum of the cut lengths, then we cannot cut all the lengths from the stock. 
   In this case, we will set wasted_length to be equal to 0.
4. The second if statement will check to see if the stock length is greater than 0.
5. If the stock length is greater than 0, then we can create a new variable called efficiency that is the ratio of 
   the sum of the cut lengths to the stock length (sum(cut_lengths) / stock_length).
6. If the stock length is less than or equal to 0, then we cannot calculate efficiency. In this case, we will set 
   efficiency to be equal to 0.
7. Finally, return the waste and efficiency from the function.

## Code Block 2 - Defining Functions
1. Define a function called print_results that takes two parameters: cut_lengths and stock_length.
2. Take waste and efficiency and set them equal to the return values from optimize_rebar(cut_lengths, stock_length).
3. make a print function that prints the Rebar Cut Lengths, the Total Stock Length, the Wasted Length, and the 
   Efficiency as a percentage (efficiency * 100).

## Code Block 3 - Calling Functions
1. To test out your code try calling the print_results function with the following values:
   - cut_lengths = [10, 15, 7, 8]
   - stock_lengths = 50
   - print_results(cut_lengths, stock_lengths)
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
