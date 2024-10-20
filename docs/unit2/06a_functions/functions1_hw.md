#  HW: Functions (Part 1)

**Purpose:** Learn how to create and use functions.

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/04_dictionaries/dictionaries_hw.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "[Your Name] HW 2.6a - Functions (Part 1)"

In this assignment, you will be creating functions that calculate the total area, volume, weight, and cost of different gravel types for a landscaping project.

---

#### Part 1

1. In the first code block, define a function called "getCuFt" with two input parameters, "areaFt" and "depthIn", which is the area of the gravel in feet and the depth of the gravel in inches respectively
2. Within the function, calculate the volume of the gravel in cubic feet using the given parameters (remember: you will need to convert the depth from inches into feet), then return it using the return statement
4. On a new line within the code block, define a function called "cuftToCuyd" with one input parameter: "cubicFeet", which is the volume of gravel in cubic feet
5. Within the function, calculate the volume of the gravel in cubic yards, then return it
6. On a new line within the code block, define a function called "volToTon" with one input parameter, "volYards", which is the volume of the gravel in cubic yards
7. Within the function, calculate the tonnage of the gravel (1 cubic yard of gravel weighs about 1.4 tons), then return it
8. On a new line within the code block, define a function called "getCostofGravel" that 

---

#### Part 2

In the second code block, you will write the code for a function called "invoice_calc" that will calculate the total cost of a shipment of materials. The function will take two parameters: a dictionary and the number of different types of materials there are in the dictionary. The function will return the total cost of the shipment. The structure of the function is already set up for you.

1. The existing function has two parameters: a dictionary (titled MaterialsDictionary) and the number of different types of materials there are in the dictionary (amountmat)
2. In the function (where it says "Write the first for-loop starting here"), write a for-loop that loops through the keys and values of the MaterialsDictionary. Make sure that you start writing your code with at least one indentation since it is within a function.
3. In the for-loop, use an if statement to ensure that the key is **not** equal to "Guide." Then print a sentence saying how much each material costs per ton and how much they cost to ship.
5. In the function (where it says "Write the second for-loop starting here"), write a second for-loop that will iterate as many times as there are different types of materials
    <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Hint**: Use the "amountmat" variable in your for-loop statement</br>
6. In the new for-loop, create the following input statements:

   | Variable Name |                            Prompt                           | Variable Type |
   |:-------------:|:-----------------------------------------------------------:|:-------------:|
   |    material   |            Asks what material the user wants to buy         |    string     |
   |    quantity   | Asks how much of that material the user wants to buy in tons|     float     |
   |    distance   |      Asks how far the material will be shipped in miles     |     float     |

7. Still in the loop, create a variable called "cost" that references the dictionary and pulls the value related to whatever material is input by the user
8. Still in the loop, add the cost of the material multiplied by its quantity to the cost of shipping the material multiplied by its distance. Add this to the variable "total" that was already included in the function
   <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Hint**: Use the += operator when adding the costs to the total </br>
9. Run all the cells and then test the function using this table:
    
   | Material | Amount | Distance |
   |----------|--------|----------|
   | “Steel”  | 4      | 90       |
   | “Cement” | 1      | 90       |
   | "Lumber" | 6      | 90       |
   | "Glass"  | 2      | 90       |

   Your total should come out to be **$5574**

---

# Turning In/Rubric

Turn on sharing and editing. Turn in the link to the Learning Suite feedback box

|                            **Item**                             | **Amount** |  
|:---------------------------------------------------------------:|:----------:|
|               The dictionary is properly created                |     2      |
|             The first for loop is defined correctly             |     4      |
|             The second for loop is defined correctly            |     4      |
| The input statements and related variables are properly created |     4      |
|      The "cost" variable is pulled from dictionary correctly    |     4      |
|                  The total is calculated correctly              |     6      |
|    The function prints every material and its related price     |     4      |
|                      The total is returned                      |     2      |
|         <div style="text-align: right">**Total**</div>          |   **30**   |
