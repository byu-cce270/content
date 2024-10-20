#  HW: Functions (Part 1)

**Purpose:** Learn how to create and use functions.

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/06a_functions/functions1_hw.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "[Your Name] HW 2.6a - Functions (Part 1)"

In this assignment, you will be creating functions that calculate the total area, volume, weight, and cost of different gravel types for a landscaping project.

---

#### Part 1

1. In the first code block, define a function called "getCuFt" with two input parameters, "areaFt" and "depthIn", which is the area of the gravel in feet and the depth of the gravel in inches, respectively
2. Within the function, calculate the volume of the gravel in cubic feet using the given parameters (remember: you will need to convert the depth from inches into feet), then return it using the return statement
4. On a new line within the code block, define a function called "cuftToCuyd" with one input parameter: "cubicFeet", which is the volume of gravel in cubic feet
5. Within the function, calculate the volume of the gravel in cubic yards, then return it
6. On a new line within the code block, define a function called "volToTon" with one input parameter, "volYards", which is the volume of the gravel in cubic yards
7. Within the function, calculate the tonnage of the gravel (1 cubic yard of gravel weighs about 1.4 tons), then return it
8. On a new line within the code block, define a function called "getCostofGravel" with two input parameters, "dictionary" and "Gravel", which is a dictionary of gravel types/costs and the type of gravel, respectively
9. Within the function, create a variable called "cost" that pulls the cost associated with the gravel type from the dictionary
    <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Hint**: You will use both parameters to correctly pull the cost</br>

---

#### Part 2

1. In the second code block, make a dictionary called gravelCosts. Use the following keys and their corresponding values to populate the dictionary:

   | Key              | Value |
   |------------------|-------|
   | "Gunsmoke"       | 70    |                               
   | “Santa Fe”       | 72    |                       
   | “Desert Rose”    | 80    |                        
   | "Glacier Cobble" | 100   |                           
   | "Arctic Pebbles" | 100   |
   | "Canadian Blend" | 115   |                           
   | "Rainbow Beach"  | 160   |                      

2. On a new line within the code block, create the following input statements:

   | Variable Name |                            Prompt                           | Variable Type |
   |:-------------:|:-----------------------------------------------------------:|:-------------:|
   |    Gravel     |          Asks what gravel type the user wants to buy        |    string     |
   |       D       |         Asks what the depth of the gravel is in inches      |    integer    |

3. On a new line within the code block, create a variable that calls the function "getArea" with arguments "xList" and "yList" in that order - this will calculate the area of the gravel in square feet
4. On a new line within the code block, create a variable that calls the function "getCuFt" with the area and the depth as its arguments in that order - this will calculate the volume of the gravel in cubic feet
5. On a new line within the code block, create a variable that calls the function "cuftToCuyd" with the cubic feet as its argument - this will calculate the volume of the gravel in cubic yards
6. On a new line within the code block, create a variable that calls the function "volToTon" with the volume in cubic yards as its argument - this will calculate the tonnage of the gravel
7. On a new line within the code block, create a variable that calls the function "getCostOfGravel" with the dictionary and gravel type as its arguments, and multiplies that function by the tonnage of gravel. This will calculate the total cost of the gravel
8. Use five separate print statements that print the area of the gravel, depth of the gravel, volume of the gravel, tons of gravel, and cost of the gravel
9. Run all the cells, then input "Rainbow Beach" as the gravel type and "3" for depth (do not include quotations). If done correctly, the total should come out to be **$9126**

---

# Turning In/Rubric

Turn on sharing and editing. Turn in the link to the Learning Suite feedback box

|                            **Item**                             | **Amount** |  
|:---------------------------------------------------------------:|:----------:|
|               getCuFt function is defined correctly             |     4      |
|             cuftToCuyd function is defined correctly            |     4      |
|              volToTon function is defined correctly             |     4      |
|          getCostofGravel function is defined correctly          |     4      |
| The input statements and related variables are properly created |     2      |
|               All functions are called correctly                |     7      |
|             All print statements created correctly              |     5      |
|         <div style="text-align: right">**Total**</div>          |   **30**   |
