# HW: IF Statements
---
**Purpose:** 
- Learn how to use IF, ELIF, and ELSE statements to analyze inputs and lists to determine a desired result.
- Practice using if statements with for loops and lists.
- Practice commenting code to help another users understand the purpose and function of what we are writing.

---
## Part 1
### Objective: Create a code that can, when given the correct inputs, solve the determinacy of any given truss. Determinacy is a Statics principle that helps us know whether or not we can solve the forces in a given system using statics equations.

**INSERT PICTURE HERE OF TRUSS**

For this example, a student has given you a list of trusses he needs to solve for in his statics class. Because of your charitable heart, and your superb coding skills, you have agreed to help him.

### Steps
1. Open this Colab note book and title it with your name
2. Go to the part 1 code block.
3. On line 1, create a varbale with the name "trusses" that uses an input statement that will ask the user how many trusses they would like to solve for. Use the int() function to make sure that this varlable will only have integer values.
4. On line 4, write a for loop that will run for the exact amount of times the user inputs in your "trusses" variable. HINT: Use the range() function with your variable "trusses". Reffer back to textbook chapter 4 for examples of the range function
