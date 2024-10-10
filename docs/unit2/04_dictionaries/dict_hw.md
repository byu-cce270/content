#  HW: Dictionaries

**Purpose:** Learn how to create a dictionary and how to call information from it.

## Instructions
1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/04_dictionaries/Starter_Sheet_HW_Dictionaries.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "[Your Name] HW 2.5 - Dictionaries"

---

#### Part 1
1. In the first code block, make a dictionary called MaterialsDictionary. Inside of this, use the following keys and their corresponding values to populate the dictionary:

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
2. In the function, write a **for-loop** that loops through the keys and values of the MaterialsDictionary. 
3. In the for-loop, create an if statement that passes the loop every time the key is equal to "Guide"
4. In the for-loop, create an else statement that prints a sentence saying how much each material costs per ton and how much they cost to ship.
5. Write a for-loop that will iterate as many times as there are different types of materials (at the very end, it should loop 4 times)
    <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Hint**: Use the "amountmat" variable in your for-loop statement</br>
6. In the loop, use three input statements that:
   
      - Ask what material the user wants to buy
      - Ask how much of that material the user wants to buy
      - Ask how far the material will be shipped
     
      The input statements should create three different variables with appropriate names related to their prompts. Make sure the variables are the correct data type (i.e. material should be a string, material quantity and distance should be floats/integers)

7. Create a variable called "cost" that references the dictionary and pulls the value related to whatever material is input by the user
8. Finally, multiply the cost of the material and its quantity and add this to the cost of shipping the material times the distance. Add this to the total variable
9. Run all the cells and then test the function using this table:
    
   | Material | Amount | Distance |
   |----------|--------|----------|
   | “Steel”  | 4      | 90       |
   | “Cement” | 1      | 90       |
   | "Lumber" | 6      | 90       |
   | "Glass"  | 2      | 90       |

   Your total should come out to **$5574**

---

# Turning In/Rubric

Turn on sharing and editing. Turn in the link to the Learning Suite feedback box

|                            **Item**                             | **Amount** |  
|:---------------------------------------------------------------:|:----------:|
|               The dictionary is properly created                |     5      |
|                The for loop is defined correctly                |     6      |
| The input statements and related variables are properly created |     6      |
|     The information is taken from the dictionary correctly      |     4      |
|             The total cost is calculated correctly              |     5      |
|                      The total is returned                      |     2      |
|         <div style="text-align: right">**Total**</div>          |   **30**   |
