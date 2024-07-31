#  HW: Dictionaries

**Purpose:** Learn how to create a dictionary and how to call information from it

## Instructions
1. First, make a copy of the starter sheet here:
   [Starter Sheet- HW IF Statements & Goal Seek](https://colab.research.google.com/drive/118eLrrkwC5i3f_dR_WrOxBOsVSKCbwzY)
2. Rename is something like "[Your Name] HW 2.4 - Dictionaries"

---

#### Part 1
3. In the first code block, make a dictionary called MaterialsDictionary. Inside of this, use the following keys and their corresponding values to populate the dictionary:

      Key         |             Value
      ----------- | ------------------------------------
      "Guide"     |  ["$ per ton","$ ship ton per mile"] 
      “Steel”     |  [700,5] 
      “Cement”    |  [130,2]
      "Lumber"    |  [34,4]
      "Glass"     |  [50,15]

---

#### Part 2
4. The existing function has two parameters: a dictionary (titled MaterialsDictionary) and the number of different types of materials there are in the dictionary (amountmat)
5. Write a **for-loop** that will iterate as many times as there are different types of materials (at the very end, it should loop 4 times)
**Hint**: Use the "amountmat" variable in your for-loop statement
6. In the loop, use three input statements that:
   - Ask what material the user wants to buy
   - Ask how much of that material the user wants to buy
   - Ask how far the material will be shipped
The input statements should create three different variables with names related to their prompts
7. Create a variable called "cost" that references the dictionary and pulls the value related to whatever material is input by the user
8. Finally, multiply the cost of the material and its amount and add this to the cost of shipping the material times the distance. Add this to the total variable
9. Run all the cells and then test the function using this table:
    
      Key         |   Value   |  Distance
      ----------- | --------- | ----------
      “Steel”     |  [700,5]  |    90
      “Cement”    |  [130,2]  |    90
      "Lumber"    |  [34,4]   |    90
      "Glass"     |  [50,15]  |    90

  Your total should come out to **$5574**

10. Turn on sharing and editing. Turn in the link to the Learning Suite feedback box!
