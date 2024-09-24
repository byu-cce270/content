
#  Reading: Lookups, Match, Data Validation

---
# Pre Class Reading Assignment

There will be 3 short reading assignment before the next class. It will be on Lookups (specifically vlookup), Match, and Data Validation.

 [VLOOKUP](https://www.benlcollins.com/spreadsheets/vlookup-function/){:target="_blank"} - **Read Until** you get the the heading "VLOOKUP function template"
 
 [MATCH](https://blog.sheetgo.com/google-sheets-formulas/match-formula-google-sheets/){:target="_blank"} - **Read Until** you get the the heading "How to use the INDEX MATCH function combination"

 [Data Validations](https://unito.io/blog/data-validation-google-sheets/){:target="_blank"}
 

## Thing to look out for and think about
- Look for the differances in the function syntax between the VLOOKUP and MATCH.
- Think about how using Data Validations can help minimize errors in your formulas


---

# Pre-Class Quiz Challenge

## Instructions
1. First make a copy of the starter sheet here: [Starter Sheet Pre - Lookups, Match, Data Validation](https://docs.google.com/spreadsheets/d/1uMdVl5TzfQAnsSvh1fv3kuw2ci_jPpJNpaVRDbW3EH8/edit?usp=sharing){:target="_blank"}
2. Using Data Validations, add dropdowns in cells B2 to B25 for all the different types of services. (Tree Removal, Sidewalk Replacement, Siding Replacement, Gutter Cleaning, Gutter Replacement, Grass Removal, and Grass Replacement)
3. Now add dropdowns in cells D2 to D25 for the level of each service can recieve (Full, Partial, and Finishing)
4. In cells E2 to E25 use the Vlookup and Match functions to correctly give a quote for the service and type that the customer would like mulitplied by the quantity.

Look below for a solution to see if you did it correctly and for some hints. (Click on the **bold** words to see the hints)

<details>
<summary><b>Solution</b></summary>

For any customer with the Service: "Sidewalk Replacement", Quantity: "10", and Type: "Full", the cost should be $1,890.

</details>


<details>
<summary><b>Hint 1: Function Syntax</b></summary>

Column B - Search Key
Column C - Multipy the total of your VLOOKUP and Match Function at the end
Column D - Search Key for the Index or MATCH Function

</details>


<details>
<summary><b>Hint 2: N/A Errors</b></summary>

If you are getting a lot of N/As maybe your is_sorted on your Vlookup is not correct or your search type for match is incorrect. Look over the preclass readings for help

</details>


<details>
<summary><b>Hint 3: N/A Errors Part 2</b></summary>
  
Make the is_sorted false and the search type 0

</details>

