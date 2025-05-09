# In-Class Exercise: Lookups, Match, and Data Validation

We will practice using Lookups, Match, and Data Validation in two real-world scenarios. 

## Exercise 1 - Material Cost & Availability

For this exercise, we will use the Material Cost & Availability starter sheet. This sheet contains two tables: one with material costs and one with material availability. We will use the VLOOKUP functions to find the correct unit cost and available quantities for each material in the Project Budget sheet. We will also use Data Validation to ensure that the material names are correct and that the material quantities are positive numbers.

You can find the **Material Cost & Availability** starter sheet here: [Lookups and Data Validation Starter Sheet](https://docs.google.com/spreadsheets/d/1d05uBVdjckpeUPTVWy4s4ekUqRCkoLP78nDcNvu1nwQ/edit?gid=1293153190#gid=1293153190){:target="_blank"}

**Instructions**

  1. Navigate to the **Project Budget** sheet.
  2. Apply dropdown (from a range) data validation to cells **B2:B30** that references cells **A4:A12** on the **Materials** sheet.
  3. Fix the error in the **Project Budget** sheet that the data validation detected.
  4. Apply data validation to cells **C2:C30** that ensures the material quantities are positive numbers.
  5. In column **D**, use the VLOOKUP function to find the correct unit cost for each row from the table in the **Materials** sheet.
  6. In column **E**, multiply the material quantities and unit costs to get the total price for each row.
7. Look at the SUMIFS() formula in the cells in column **H**. This finds the total materials used in column **C** for each material type.
  7. In column **I**, use the VLOOKUP function to find the available quantities for material from the table in the **Materials** sheet.
  8. In column **J**, use the difference in columns **H** and **I** to find the remaining material quantities. Note that we have conditional formattting on to highlight items tha are out of stock.

## Exercise 2 - Employee Work Hours

For this exercise, we will use the Employee Work Hours starter sheet. This sheet contains hours worked each month for a set of employees. Our objective is a combination of VLOOKUP and MATCH to find numbers in this table.

You can find the **Employee Work Hours** starter sheet here: [Lookups and Match Starter Sheet](https://docs.google.com/spreadsheets/d/1XECW9PeMxbtcPXn8hC6sYhXjaQyJ89srCxFyrmzaRwA/edit?gid=0#gid=0){:target="_blank"}

**Instructions**

1. Note the layout of the table on the top. Each row represents a month and each column represents an employee. The numbers are hours worked each month by the employee.
2. In the table below, use the VLOOKUP to find the hours worked in the month specified in column **B**. Embed the MATCH function inside the VLOOKUP function to determine what column to use based on the employee name in column **C**. Enter your formula in **D20:D33**.

## Turning in/Rubric
Turn sharing and editing on, then submit the links to Learning Suite in the feedback box for each exercise. In-class assignment scores are based on valid effort and completion.
