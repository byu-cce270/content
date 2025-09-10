# In-Class Exercise: Lookups, Match, and IF Functions

---

We will practice using Lookups, Match, and IF functions is several real-world scenarios. For this exercise, open the in-class workbook, make a copy, and follow the instructions.
You can find the in-class workbook here: [(Starter-Workbook)-Class-Lookups-Match-IF.xlsx](%28Starter-Workbook%29-Class-Lookups-Match-IF.xlsx)

Be sure to rename it something like “(Your-Name)-Class-Lookups-Match-IF”.

In this workbook, there are 5 sheets.

- **Project Budget** - Used for Exercise 1. 
- **Materials** - Data used for Exercise 1.
- **Employee Work Hours** - Used for Exercise 2.
- **Concrete Price Estimator** - Used for Exercise 3.
- **School Left** - Used for Exercise 4.

---

## Exercise 1 - Material Cost & Availability

This sheet contains two tables: one with material costs and one with material availability. We will use the VLOOKUP functions to find the correct unit cost and available quantities for each material in the Project Budget sheet. We will also use Data Validation to ensure that the material names are correct and that the material quantities are positive numbers.

1. Navigate to the **Project Budget** sheet

2. Apply dropdown (from a range) data validation to cells **B2:B30** that references cells **A4:A12** on the **Materials** sheet

3. Fix the error in the **Project Budget** sheet that the data validation detected

4. Apply data validation to cells **C2:C30** that ensures the material quantities are positive numbers

5. In column **D**, use the VLOOKUP function to find the correct unit cost for each row from the table in the **Materials** sheet

6. In column **E**, multiply the material quantities and unit costs to get the total price for each row

7. Look at the SUMIF() formula in the cells in column **H**. This finds the total materials used in column **C** for each material type (This formula is already done for you).

8. In column **I**, use the VLOOKUP function to find the available quantities for material from the table in the **Materials** sheet

9. In column **J**, use the difference in columns **H** and **I** to find the remaining material quantities. Note that we have conditional formatting on to highlight items that are out of stock

---

## Exercise 2 - Employee Work Hours

This sheet contains hours worked each month for a set of employees. Our objective is a combination of VLOOKUP and MATCH to find numbers in this table.

1. Note the layout of the table on the top. Each row represents a month and each column represents an employee. The numbers are hours worked each month by the employee

2. In the table below, use the VLOOKUP to find the hours worked in the month specified in column **B**. Embed the MATCH function inside the VLOOKUP function to determine what column to use based on the employee name in column **C**. Enter your formula in **D20:D33**

3. Add a function in D35 to compute the total hours worked on this project

---

## Exercise 3 - Concrete Price Estimator

The following exercise is based on the IF/IFS statements we have just covered.

1. Navigate to the Concrete Price Estimator sheet

2. Solve for the total cubic volume (cell E16)

3. Write an IFS statement in E18 to give the price per cubic foot based on the volume

4. Solve for the total price (cell E19)

5. Try adjusting the lengths of the concrete to see if it changes the price per cubic foot and total price correctly

---

## Exercise 4 - Number of School Years Left

Use IF statements and user inputs/selections to determine how many years that the user has left to finish school. Keep in mind, this is probably not correct.

**Instructions**

1. Navigate to the School Left sheet

2. Fill in the criteria in the yellow cells (C9, C11, C13, C15, F17, C19). These cells have a dropdown menu to select from. You can select the cell and then click on the arrow that appears to the right of the cell to see the dropdown menu. (This is made using Data Validation, which we will cover next class)

3. Write an IF/IFS function under Years (Column I) that is dependent on the criteria and conditions given in column J.

4. Add up the total in I23 to determine how many years of school you have left.

---
			
## Turning in/Rubric

**_REMINDER_** - For this class, **you will only turn in the links to your Excel files**. You will get a 0 for this assignment if you turn in an Excel file or a link that is not shareable. 

1. On the top right, click the share button --> share --> settings
2. Click "anyone" at the top, then underneath "More settings", change "can view" to "can edit". Then click apply. 
3. Copy the link, then turn it into Learning Suite in the feedback box for that assignment.

**Rubric:**

|                      Item                      | Points Possible |
|:----------------------------------------------:|:---------------:|
| <div style="text-align: right">**Total**</div> |        5        |

---

The following is not a part of the rubric, but specifies how you can lose points. For example: if you fail to share your link correctly.

| **Reasons for Points Lost** |    **Amount**     |  
|:---------------------------:|:-----------------:|
|   Link shared incorrectly   |       -10%        |
|  Turned in late (per week)  | -10% (up to -50%) |
