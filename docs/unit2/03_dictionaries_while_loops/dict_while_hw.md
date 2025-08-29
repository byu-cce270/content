#  HW: Dictionaries, input statements, and while loops

**Purpose:** Learn how to create a dictionary and how to call information from it.

## Instructions

First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/03_dictionaries_while_loops/dictionaries_hw.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Rename it something like "[Your Name]dictionaries_while_loops_input.ipynb"

In this assignment, you will be creating a dictionary and using it to calculate the cost of materials and shipping. The dictionary will contain the cost of each material per ton and the cost to ship each material per mile. You will then use this dictionary to calculate the total cost of a shipment of materials.

---

## Part 1 - Dictionary Creation

1. In the first code block, make a dictionary called MaterialsDictionary. Use the following keys and their 
corresponding values to populate the dictionary:

   | Key      | Value                                |
   |----------|--------------------------------------|
   | "Guide"  | ["$ per ton","$ ship ton per mile"]  |
   | “Steel”  | [700,5]                              |
   | “Cement” | [130,2]                              |
   | "Lumber" | [34,4]                               |
   | "Glass"  | [50,15]                              |

---

## Part 2 - Function Definition

2. In the second code block, you will write the code for a function called "invoice_calc" that will calculate the 
total cost of a shipment of materials. 
3. The function will take two parameters: a dictionary (titled MaterialsDictionary) and the number of different 
types of materials there are in the dictionary (amountmat). The function will return the total cost of the shipment. The structure of the function is already set up for you.

---

## Part 3 - For Loop

4. In the function (where it says "Write the first for loop starting here"), write a for-loop that loops through the 
keys and values of the MaterialsDictionary. Make sure that you start writing your code with at least one indentation since it is within a function.

5. In the for-loop, use an if statement to ensure that the key is **not** equal to "Guide." Then print a sentence 
saying how much each material costs per ton and how much they cost to ship.

---

## Part 4 - While Loop

6. In the function where it says "Write the while-loop starting here," write a while-loop that will iterate as many 
   times as there are different types of materials, asking how many tons they want and how many miles it will be 
   shipped.
    <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Hint**: Use the "amountmat" variable in your while-loop 
   statement.</br>
7. In the new while-loop, create the following input statements:

   | Variable Name |                            Prompt                           | Variable Type |
   |:-------------:|:-----------------------------------------------------------:|:-------------:|
   |    material   |            Asks what material the user wants to buy         |    string     |
   |    quantity   | Asks how much of that material the user wants to buy in tons|     float     |
   |    distance   |      Asks how far the material will be shipped in miles     |     float     |

8. Still inside the while loop, create a variable called "cost" that references the dictionary and pulls the value 
   related to whatever material is input by the user.
9. Still in the loop, add the cost of the material multiplied by its quantity to the cost of shipping the material 
   multiplied by its distance. Add this to the variable "total" that was already included in the function.
   <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Hint**: Use the += operator when adding the costs to the total. </br>
10. Run all the cells and then test the function using this table:
    
   | Material | Amount | Distance |
   |----------|--------|----------|
   | “Steel”  | 4      | 90       |
   | “Cement” | 1      | 90       |
   | "Lumber" | 6      | 90       |
   | "Glass"  | 2      | 90       |

   Your total should come out to be **$5574**

---

## Turning In/Rubric

Turn on sharing and editing. Turn in the link to the Learning Suite feedback box

|                            **Item**                             | **Amount** |  
|:---------------------------------------------------------------:|:----------:|
|               The dictionary is properly created                |     2      |
|             The first for loop is defined correctly             |     4      |
|               The while loop is defined correctly               |     4      |
| The input statements and related variables are properly created |     4      |
|     The "cost" variable is pulled from dictionary correctly     |     4      |
|                The total is calculated correctly                |     6      |
|    The function prints every material and its related price     |     4      |
|                      The total is returned                      |     2      |
|         <div style="text-align: right">**Total**</div>          |   **30**   |

The following is not a part of the rubric, but specifies how you can lose points. For example: if you do not explain 
your code when using AI to help you create it or fail to share your link correctly.

|                       **Reasons for Points Lost**                       |    **Amount**     |  
|:-----------------------------------------------------------------------:|:-----------------:|
|                         Link shared incorrectly                         |       -10%        |
|                        Turned in late (per week)                        | -10% (up to -50%) |
| No comments explaining where AI is used and what its provided code does |       -10%        |
