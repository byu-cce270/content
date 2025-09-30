#  HW: Introduction to Functions

**Purpose:** Learn how to create and use functions.

## Instructions

1. First, make a copy of the starter sheet here:
<a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/04_intro_functions/(Starter_Workbook)_Class_Intro_Functions.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "[Your Name]Functions_(Part 1)_homework.ipynb"

In this assignment, you will be creating functions that calculate the total area, volume, weight, and cost of different gravel types for a landscaping project.

---

#### Part 1

1. In the first code block, define a function called **get_cubic_ft** with two input parameters, **area_ft** and **depth_in**, which is the area of the gravel in feet and the depth of the gravel in inches, respectively. Within the function, calculate the volume of the gravel in cubic feet using the given parameters (remember: you will need to convert the depth from inches into feet), then return it using the return statement
2. On a new line within the code block, define a function called **cuft_to_cuyd** with one input parameter: **cubic_ft**, which is the volume of gravel in cubic feet. Within the function, calculate the volume of the gravel in cubic yards, then return it. (To find cuyd you must divide cubic_ft by 27)
3. On a new line within the code block, define a function called **vol_to_ton** with one input parameter, **vol_yds**, which is the volume of the gravel in cubic yards. Within the function, calculate the tonnage of the gravel (1 cubic yard of gravel weighs about 1.4 tons), then return it
4. On a new line within the code block, define a function called **get_gravel_cost** with two input parameters, **gravel_dict** and **gravel**, which is a dictionary of gravel types/costs and the type of gravel, respectively. Within the function, create a variable called **cost** that pulls the cost associated with the gravel type from the dictionary
5. Go back and before each code use markdown and explain the function of each code that you created. 
    <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Hint**: You will use both parameters to correctly pull the cost</br>

---

#### Part 2

1. In the second code block, make a dictionary called **gravel_costs**. Use the following keys and their corresponding 
   values to 
   populate the dictionary:

   | Key              | Value |
   |------------------|-------|
   | "Gunsmoke"       | 70    |                               
   | “Santa Fe”       | 72    |                       
   | “Desert Rose”    | 80    |                        
   | "Glacier Cobble" | 100   |                           
   | "Arctic Pebbles" | 100   |
   | "Canadian Blend" | 115   |                           
   | "Rainbow Beach"  | 160   |                      

2. On a new line within the code block, print the **gravel_cost** dictionary and then create the following (input) form fields:

   | Variable Name |                     Form Field Placeholder                  | Variable Type |
   |:-------------:|:-----------------------------------------------------------:|:-------------:|
   |    gravel     |          Asks what gravel type the user wants to buy        |    string     |
   |       d       |         Asks what the depth of the gravel is in inches      |    integer    |

3. On a new line within the code block, create a variable that calls the function **get_area** with arguments x_list and y_list in that order - this will calculate the area of the gravel in square feet.
4. On a new line within the code block, create a variable that calls the function **get_cubic_ft** with the area and the depth as its arguments in that order - this will calculate the volume of the gravel in cubic feet.
5. On a new line within the code block, create a variable that calls the function **cuft_to_cuyd** with the volume in cubic feet as its argument - this will calculate the volume of the gravel in cubic yards.
6. On a new line within the code block, create a variable that calls the function **vol_to_ton** with the volume in cubic yards as its argument - this will calculate the tonnage of the gravel.
7. On a new line within the code block, create a variable that calls the function **get_gravel_cost** with the dictionary and gravel type as its arguments, and multiplies the value returned by that function by the tonnage of gravel. This will calculate the total cost of the gravel.
8. Use five separate print statements that print the area of the gravel, depth of the gravel, volume of the gravel, tons of gravel, and cost of the gravel
9. Run all the cells, then input **Rainbow Beach** as the gravel type and **3** for depth in the form fields. If 
   done correctly, the total should come out to be **$9126**.

---

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

The following is not apart of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                      **Reasons for Points Lost**                         | **Amount** |  
|:------------------------------------------------------------------------:|:----------:|
|  No comments explaining why AI is used and what its provided code does   |     2-3    |
|                       Link shared incorrectly                            |      3     |
