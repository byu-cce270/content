#  HW: Introduction to Functions

**Purpose:** Learn how to create and use functions.

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/04_intro_functions/(Starter_Workbook)_HW_Intro_Functions.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "(Your_Name)_HW_Intro_Functions".

In this assignment, you will be creating functions that calculate the total area, volume, weight, and cost of different gravel types for a landscaping project.

---

#### Part 1

1. In the first code block, define a function called optimize_rebar that takes two parameters, the length of the cut "cut_lengths" and the length of the stock, "stock_length".
2. Your function should include an input function for the cut_lengths, which will be a list of rebar lengths (in feet or inches) that are needed for the project. 
3. The function should calculate how much rebar is used from the stock, how much is wasted, and the efficiency (percent of stock length used).
4. The function should return the efficiency as a decimal (e.g., 0.75 for 75% efficiency).
5. define a variable called print_results(cut_lengths, stock_length). This function should call the optimize_rebar function and prints what lengths were cut, how much rebar was wasted, and the efficiency in percentage.

## Code Block 2 - Calling Functions
1. Create a list of cut lengths, e.g. 
python 

cuts = [10, 15, 7, 8](in ft)
2. Define the stock length, e.g. stock = 40.
3. Call print_results(cuts, stock) to display the results.
4. Try running your program again with a different stock length or cut lengths and see how the efficiency changes.
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
