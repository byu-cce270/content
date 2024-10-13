#  HW: Dictionaries

**Purpose:** Learn how to create a dictionary and how to call information from it.

## Instructions
1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/04_dictionaries/dictionaries_hw.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "[Your Name] HW 2.5 - Dictionaries"

---

#### Part 1
1. In the first code block, make a dictionary called MaterialsDictionary. Use the following keys and their corresponding values to populate the dictionary:

   | Key      | Value                                |
   |----------|--------------------------------------|
   | "Guide"  | ["$ per ton","$ ship ton per mile"]  |
   | “Steel”  | [700,5]                              |
   | “Cement” | [130,2]                              |
   | "Lumber" | [34,4]                               |
   | "Glass"  | [50,15]                              |

---

#### Part 2
1. The existing function has two parameters: a dictionary (titled MaterialsDictionary) and the number of different types of materials there are in the dictionary (amountmat)
2. In the function (where it says "Write the first for-loop starting here"), write a for-loop that loops through the keys and values of the MaterialsDictionary. 
3. In the for-loop, create an if statement that skips the loop when the key is equal to "Guide."
   <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Hint**: Use the "continue" statement in your for-loop</br>
4. In the for-loop, create an else statement that prints a sentence saying how much each material costs per ton and how much they cost to ship.
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
