# HW: IF Statements
---
**Purpose:** 
- Learn how to use IF, ELIF, and ELSE statements to analyze inputs and lists to determine a desired result.
- Practice using if statements with for loops and lists.

---
## Part 1
### Objective: Create a code that can, when given the correct inputs, solve the determinacy of any given truss. Determinacy is a Statics principle that helps us know whether or not we can solve the forces in a given system using statics equations.

Here is an example of a truss labeled with the joints, reaction forces, and members:

![TRUSS_ANALYSES.png](images/TRUSS_ANALYSES.png)

For this example, a student has given you a list of trusses he needs to solve for in his statics class. Because of your charitable heart, and your superb coding skills, you have agreed to help him.

### Steps
1. Open this Colab notebook and title it with your name: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/2_4_%5Byour_name%5D_IF_Statements_.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
2. Go to the "Part 1 - Truss Determinacy Solver" code block
3. Starting in line 2, create 3 different input statements to ask the user for the following:
  - The number of joints in the truss. (Must be a whole number)
  - The number of members in the truss
5. On line 4, write a for loop that will run for the exact amount of times the user inputs in your "trusses" variable. HINT: Use the range() function with your variable "trusses". Refer back to textbook chapter 4 for examples of the range function
