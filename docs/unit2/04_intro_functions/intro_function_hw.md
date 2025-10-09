#  HW: Introduction to Functions

**Purpose:** Learn how to create and use functions.

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/04_intro_functions/(Starter_Workbook)_HW_Intro_Functions.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "(Your_Name)_HW_Intro_Functions".


Rebar is often delivered in standard lengths, such as 20 ft or 60 ft. When a contractor needs to cut rebar to 
specific lengths for a project, they want to minimize waste and maximize efficiency. Being able to model and 
optimize this process can lead to significant cost savings, more sustainable construction practices, and improved 
construction efficiency. 

In this assignment, you will be in charge of a concrete construction project. You need to know how much rebar 
you need to order for your project. You will create two functions, the first will calculate the waste and 
efficiency of 
cutting rebar from standard lengths, and the second will be an optimization of the rebar cutting process.

---

## Code Block 1 - Defining Functions

1. In the first code block, you're going to create a function "analyze_rebar", 
   that takes two 
   parameters, the length of the 
   cut, "cut_length" and the length of the stock, "stock_length." The cut_length will be a list of the lengths that 
   your company needs to cut. The stock_length will be the length of the rebar that you are cutting from (like 20ft 
   or 60ft). We need 
   this function to calculate three things: the amount of wasted material, the efficiency of the cuts, and the 
   number 
   of stock.
2. Your function should loop through the cut_length list and calculate how many pieces of stock you need to buy, 
   how much waste you will have, and the efficiency of the process.
3. Remember that if the stock length is less than the sum of all cut lengths, then you cannot cut all the lengths from 
   the 
   stock. In this case, the wasted material will be 0, and the efficiency will also be 0.
4. Return the wasted material, the efficiency, and the number of stock from the function.

## Code Block 2 - Optimization Function

1. In the second code block, you will create a function called optimize rebar that takes three parameters: 
   cut_length, min_stock_length, and max_stock_length.
2. The function will loop through all the stock lengths from min_stock_length to 
   max_stock_length and call the analyze_rebar function for each stock length. It will start with the min_stock_length
    and go up to the max_stock_length, incrementing by 1 each time.
3. As you loop through the stock lengths, you will call the analyze_rebar function and get the waste and efficiency for 
   each stock length.
4. The function will keep track of the stock length that gives the least waste and the highest efficiency, and return 
   those values at the end of the function.


## Code Block 3 - Calling Functions
In this code block you will create a function that prints the results of the analyze_rebar and the results 
of the optimize_rebar functions.
It will 
call 
the function 
and set the waste and efficiency variables equal to the return values from the analyze_rebar function. It will also 
print the results in a readable format.

1. Define a function called print_results that takes two parameters: cut_length and stock_length.
2. Call the function you created in Code Block 1, and retrieve the waste and efficiency values.
3. Create a print function that prints the Rebar Cut Lengths, the Total Stock Length, the Wasted Length, and the 
   Efficiency as a percentage.

## Code Block 3 - Calling Functions
1. To test out your code try calling the print_results function with the following values:
   - cut_length = [10, 15, 7, 8]
   - stock_length = 50
You should get the following output:
```
Waste: 10 ft
Efficiency: 80.0%
```
# Turning In/Rubric

Turn on sharing and editing. Turn in the link to the Learning Suite feedback box

|                    **Item**                    | **Amount** |  
|:----------------------------------------------:|:----------:|
|  optimize_rebar function is defined correctly  |     4      |
|     The function includes 2 if statements      |     4      |
|         waste is calculated correctly          |     3      |
|       efficiency is calculated correctly       |     3      |
|       print_results is defined correctly       |     4      |
|  print_results calls function optimize_rebar   |     4      |
|        Prints the correct rebar lengths        |     2      |
|         Prints the total stock lengths         |     2      |
|        Prints the total wasted material        |     2      |
|     Prints the total efficiency in percent     |     2      |
| <div style="text-align: right">**Total**</div> |   **30**   |

The following is not part of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                      **Reasons for Points Lost**                         | **Amount** |  
|:------------------------------------------------------------------------:|:----------:|
|  No comments explaining why AI is used and what its provided code does   |     2-3    |
|                       Link shared incorrectly                            |      3     |
