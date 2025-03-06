
# HW: Gspread
---
**Purpose:** 
- Learn how to connect read data from a google sheet to manipulate in Python and update into your google sheet.
- Practice using functions and loops with gspread.

---
## Part 1

**Objective**: Create a code that will analyze the different subcontractor bids given to you for the drywall and concrete scopes. Choose a subcontractor bid based on your analysis. 

For this example, you have been given bids that were submitted for a job and it is your job as the project manager to determine which bid you will choose. 

### Steps
1. Open this Colab notebook and title it with your name: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/03_if_statements/%5Byour_name%5D_if_statements_hw.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
2. Go to the "Imports" code block. Write the proper code to import gspread and authentiate yourself.
3. Create a copy of the following worksheet and open it by url in the same code block. 
4.
5. Starting in line 2, create 3 different input statements using colab forms 
   to ask the user for the following:
    - The number of joints in the truss. (Must be an integer)
    - The number of members in the truss. (Must be be an integer)
    - The number of reaction forces acting on the truss. (Must be an integer)
6. Write IF, ELIF, and ElSE statements on the next line under the "Write If statements here" line for the following 
   scenarios. 

  | Equation      | Result                                |
   |----------|--------------------------------------|
   | # of members + # of reaction forces = 2 * (# of joints) | Statically determinate |
   | # of members + # of reaction forces > 2 * (# of joints) | Statically Indeterminate |
   | # of members + # of reaction forces < 2 * (# of joints) | Unstable |

4. Have your code print the result. For example, if my truss had more joints than reaction forces + my members, then 
   my code would print "truss is statically unstable"
5. Test your code with the following scenarios:


| Scenario # | Joints | Members | Reaction Forces | Result |
|------------|--------|---------|-----------------|--------|
| 1          | 3      | 3       | 3               | Statically determinate |
| 2          | 4      | 6       | 3               | Statically indeterminate |
| 3          | 8      | 9       | 4               | Unstable |

##Part 2

**Objective**:  You are helping a company count the orders of materials it has. They have given you the list and want you to count it.

###Steps
1. Under the line "main for loop", create a for loop that will go through each order in the given "orders " list.
2. In the next line, create a for loop that will read each item in the "Total_order" list.
3. Now, create a 3rd loop that loops through the totals  if the material from the "order" list is equal to the item in the "Total_order" list, then add 1 to the item total.
    - EX: If steel is in the "order" list and "total_orders" list, then the value for steel in the "total_orders" list should increase by 1 for each occurrence of steel. This should be the same for wood and brick.
4. Write a loop to print each of the final values for wood, brick, steel, glass, and concrete. Here are the final values that you should get:
    - 14 orders of wood
    - 10 orders of brick
    - 8 orders of steel
    - 12 orders of glass
    - 6 orders of concrete

---

**Turn sharing and editing on. Turn in the link to Learning Suite in the feedback box**

---

**Rubric:**

|                                               If Statements                                                     | Points Possible |
|:-------------------------------------------------------------------------------------------------------:|:---------------:|
|                         Part 1 - Correct value for scenario 1                                           |        5        |
|                          Part 1 - Correct value for scenario 2                                          |        5        |
|                          Part 1 - Correct value for scenario 3                                          |        5        |
|                           Part 2 - Correct value for wood                                               |        3        |
|                            Part 2 - Correct value for steel                                             |        3        |
|                               Part 2- Correct value for brick                                           |        3        |
|                            Part 2 - Correct value for glass                                             |        3        |
|                               Part 2- Correct value for concrete                                        |        3        |
|                             <div style="text-align: right">**Total**</div>                              |       30        |

The following is not apart of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                      **Reasons for Points Lost**                      | **Amount** |  
|:---------------------------------------------------------------------:|:----------:|
| No comments explaining why AI is used and what its provided code does |    2-3     |
|                        Link shared incorrectly                        |     3      |
|       Turned in late. 10% or 3 points for every week it's late.       |    3-15    |
