#  HW: Dictionaries and While Loops

**Purpose:** Learn how to create a dictionary and how to call information from it.

---

## Getting Started

Create a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/03_dictionaries_while_loops/(Starter_Workbook)_HW_Dict_While.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Rename it something like "(Your_Name)_HW_Dict_While.ipynb".

---

## Part 1 - Dictionary Creation

In this assignment, you will be creating a dictionary and using it to calculate the cost of materials and shipping. The dictionary will contain the cost of each material per ton and the cost to ship each material per mile. You will then use this dictionary to calculate the total cost of a shipment of materials.

1. In the first code block, make a dictionary called MaterialsDictionary. Use the following keys and their 
corresponding values to populate the dictionary:

   | Key      | Value                            |
   |----------|----------------------------------|
   | "Guide"  | ["$ per ton","$ ship per mile"]  |
   | “Steel”  | [700,5]                          |
   | “Cement” | [130,2]                          |
   | "Lumber" | [34,4]                           |
   | "Glass"  | [50,15]                          |

---

## Part 2 - Function Definition

2. In the second code block, you will write the code for a function called "invoice_calc" that will calculate the 
total cost of a shipment of materials. 
3. The function will take two parameters: a dictionary (titled MaterialsDictionary that you made above) and the number of different materials that 
   the user has requested to buy (a variable titled `amountmat`). The function will return the total 
   cost of the shipment. The structure of the function is already set up for you.

---

## Part 3 - For Loop

4. In the function (where it says "Write the first for loop starting here"), write a for loop that loops through the 
materials in the MaterialsDictionary. Make sure that you start writing your code with at least one indentation since 
   it is within a function.

5. In the for loop, use an if statement to ensure that the key is **not** equal to "Guide." Create two variables 
   that you will reference in a print statement. One variable should reference the cost per ton value in the 
   dictionary, and the second variable should reference the $ ship ton per mile. Create a print statement that 
   loops through each material and states how much each material costs per ton and how much it costs to ship.

---

## Part 4 - While Loop


6. In the function where it says "Write the while loop starting here," write a while loop that will iterate however 
   many items the user ordered, asking:  
    1) what material,  
    2) how many tons,  
    3) how many miles it will be shipped.  

!!! hint
    In the table below we provide some guidance for the input statements. You need to convert any numbers entered to `float` variable type, as any input to an input statement assumes everything is a string.
  




7. Create an if statement that checks if the user has inputted a valid material. If the material is not in the 
   dictionary, print a message that says "Material not found. Please enter a valid material." and use the 
   continue statement to skip to the next iteration of the loop. Make sure the count does not increase if the 
   material is not found.
7. In the while loop, create the following input statements:

   | Variable Name |                            Prompt                           | Variable Type |
   |:-------------:|:-----------------------------------------------------------:|:-------------:|
   |    material   |            Asks what material the user wants to buy         |    string     |
   |    quantity   | Asks how much of that material the user wants to buy in tons|     float     |
   |    distance   |      Asks how far the material will be shipped in miles     |     float     |

!!!Hint
      Use the `.capitalize()` function so that you don't have to worry about capitalization problems with your materials! </br>

9. Still in the loop, add the cost of the material multiplied by its quantity to the cost of shipping the material 
   multiplied by its distance. Store this in a variable that represents the item cost.
10. Add each item cost to the variable "total" that was already included in the function.

!!! hint 
    Use the `+="` operator when adding the costs to the total. 

11. Make sure that the `amountmat` variable is decreased by 1 at the end of each iteration of the while loop so that the loop will 
   eventually stop according to how many items the user wants to order.
10. Run all the cells and then test the function using this table:
    
   | Material | Amount | Distance |
   |----------|--------|----------|
   | “Steel”  | 4      | 90       |
   | “Cement” | 1      | 90       |
   | "Lumber" | 6      | 90       |
   | "Glass"  | 2      | 90       |

   Your total should come out to be **$5574**

---

## Turning in/Rubric

**_REMINDER_** - For this class, **you will only turn in the links to your colab notebooks**. You will get a 0 for this assignment if you turn in a python file or a link that is not correct, wrong assignment, or does not give editor permission.

**Rubric:**

|                            **Item**                             | **Amount** |  
|:---------------------------------------------------------------:|:----------:|
|               The dictionary is properly created                |     2      |
|             The first for loop is defined correctly             |     4      |
|               The while loop is defined correctly               |     4      |
| The input statements and related variables are created properly |     4      |
|     The "cost" variable is pulled from dictionary correctly     |     4      |
|                The total is calculated correctly                |     6      |
|    The function prints every material and its related price     |     4      |
|                      The total is returned                      |     2      |
|         <div style="text-align: right">**Total**</div>          |   **30**   |

---

The following is not a part of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                       **Reasons for Points Lost**                       |    **Amount**     |  
|:-----------------------------------------------------------------------:|:-----------------:|
|                         Link shared incorrectly                         |       -10%        |
|                        Turned in late (per week)                        | -10% (up to -50%) |
| No comments explaining where AI is used and what its provided code does |       -50%        |
