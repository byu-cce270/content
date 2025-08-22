# HW: IF Statements
---
**Purpose:** 
- Learn how to use IF, ELIF, and ELSE statements to analyze inputs and lists to determine a desired result.
- Practice using if statements with for loops and lists.

---
## Part 1

**Objective**: Create a code that can solve the determinacy of any given truss when given the correct inputs. Determinacy is a Statics principle that helps us know whether or not we can solve the forces in a given system using statics equations.

Here is an example of a truss. The blue lines are the members, the joints are the white circles where the members meet, and the red arrows are the reaction forces.:

![Warren-Truss2.png](images/Warren-Truss2.png)
_(image from [www.engineeringskills.com](https://www.engineeringskills.com/posts/truss-analysis-using-method-of-joints-and-sections))_

For this example, a student has given you a list of trusses he needs to solve for in his statics class. Because of your charitable heart, and your superb coding skills, you have agreed to help him.

### Steps

1. Open this Colab notebook and title it with your name: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/02_if_statements/(Starter_Workbook)_HW_If_Statements.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Go to the "Part 1 - Truss Determinacy Solver" code block. Starting in line 2, create 3 different input statements using colab forms 
   to ask the user for the following:
    - The number of joints in the truss. (Must be an integer)
    - The number of members in the truss. (Must be be an integer)
    - The number of reaction forces acting on the truss. (Must be an integer)
   
3. Write IF, ELIF, and ElSE statements on the next line under the "Write If statements here" line for the following 
   scenarios. 

  | Equation                                                | Result                   |
   |---------------------------------------------------------|--------------------------|
   | # of members + # of reaction forces = 2 * (# of joints) | Statically determinate   |
   | # of members + # of reaction forces > 2 * (# of joints) | Statically Indeterminate |
   | # of members + # of reaction forces < 2 * (# of joints) | Unstable                 |

4. Have your code print the result. For example, if my truss had more joints than reaction forces + my members, then 
   my code would print "truss is statically unstable"

5. Test your code with the following scenarios:


| Scenario # | Joints | Members | Reaction Forces | Result                   |
|------------|--------|---------|-----------------|--------------------------|
| 1          | 3      | 3       | 3               | Statically determinate   |
| 2          | 4      | 6       | 3               | Statically indeterminate |
| 3          | 8      | 9       | 4               | Unstable                 |

## Part 2

**Objective**:  You are helping a company count the orders of materials it has. They have given you the list and want you to count it.

### Steps
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

|                 If Statements                  | Points Possible |
|:----------------------------------------------:|:---------------:|
|     Part 1 - Correct value for scenario 1      |        5        |
|     Part 1 - Correct value for scenario 2      |        5        |
|     Part 1 - Correct value for scenario 3      |        5        |
|        Part 2 - Correct value for wood         |        3        |
|        Part 2 - Correct value for steel        |        3        |
|        Part 2- Correct value for brick         |        3        |
|        Part 2 - Correct value for glass        |        3        |
|       Part 2- Correct value for concrete       |        3        |
| <div style="text-align: right">**Total**</div> |       30        |

---

The following is not a part of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                       **Reasons for Points Lost**                       |    **Amount**     |  
|:-----------------------------------------------------------------------:|:-----------------:|
|                         Link shared incorrectly                         |       -10%        |
|                        Turned in late (per week)                        | -10% (up to -50%) |
| No comments explaining where AI is used and what its provided code does |       -10%        |

