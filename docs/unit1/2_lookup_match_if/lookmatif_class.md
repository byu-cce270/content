# In-Class Exercise: Lookups, Match, and IF Functions

---

We will practice using VLOOKUP, MATCH, IF, and IFS in several real-world scenarios. For this exercise, open the in-class workbook, make a copy, and follow the instructions.
You can find the in-class workbook here: [(Starter-Workbook)-Class-Lookups-Match-IF.xlsx](%28Starter-Workbook%29-Class-Lookups-Match-IF.xlsx)

Need a reminder about cell, range, cross-sheet, or absolute references? See [Cells and Formulas](../../resources/excel_review/basic_excel_review.md).

This workbook contains six worksheets.

- **Project Budget** - Used for Exercise 1. 
- **Materials** - Data used for Exercise 1.
- **Employee Work Hours** - Used for Exercise 2.
- **Concrete Price Estimator** - Used for Exercise 3.
- **School Left** - Used for Exercise 4.
- **School Dropdown** - Contains the lists used by the dropdown menus in Exercise 4.

---

## Exercise 1 - Material Cost & Availability

The **Materials** worksheet contains lookup ranges for material costs and available quantities. We will use VLOOKUP to return those values to the **Project Budget** worksheet. A dropdown list for material names has already been provided using Data Validation; you will learn how to create dropdown lists in a later lesson.

1. Navigate to the **Project Budget** worksheet.

2. In `D2`, use VLOOKUP with an exact match (`range_lookup = FALSE`) to find the correct unit cost for the material in `B2`. Use `Materials!$A$4:$D$12` as the lookup range and return its third column. Fill the formula through `D30`.

3. In `E2`, multiply the material quantity in `C2` by the unit cost in `D2`, then fill the formula through `E30`.

4. Look at the `SUMIF` formulas in column **H**. These formulas find the total quantity used in column **C** for each material type. The formulas are already provided.

5. In `I2`, use VLOOKUP with an exact match (`range_lookup = FALSE`) to find the available quantity for the material in `G2`. Use the same `Materials!$A$4:$D$12` lookup range, but return its fourth column. Fill the formula through `I10`.

6. In `J2`, subtract the total used in `H2` from the available quantity in `I2`, then fill the formula through `J10`. Conditional formatting highlights items that are out of stock.

7. One material name intentionally contains a data-quality problem that causes an exact lookup to return `#N/A`. Find and correct the inconsistent entry, then confirm that the lookup and material totals update correctly.

<details>
<summary><b>Hint: Exact text does not match</b></summary>

Excel treats spaces as characters. The entry `Clay ` contains a trailing space and does not exactly match `Clay` in the Materials worksheet. Remove the trailing space from the Project Budget entry. Do not hide the mismatch with an approximate lookup or `IFERROR`.
</details>

<!-- Instructor note: The trailing space in 'Project Budget'!B5 is intentional. Use it to discuss data cleaning and why exact text lookups can return #N/A. Students should remove the trailing space. -->

---

## Exercise 2 - Employee Work Hours

This worksheet contains hours worked each month for a set of employees. Our objective is to combine VLOOKUP and MATCH to find values in a two-dimensional lookup range.

1. Note the layout of the lookup range in `$A$4:$H$16`. Each row represents a month and each employee has a column. The values are the hours worked each month by that employee.

2. In `D20`, use VLOOKUP with an exact match (`range_lookup = FALSE`) to find the hours worked in the month listed in `B20`. Use `$A$4:$H$16` as the VLOOKUP range. Nest MATCH with an exact match (`match_type = 0`) to locate the employee in `C20` within the header range `$A$4:$H$4`. Because both ranges begin in column A, the MATCH position is also the correct VLOOKUP column index. Fill the formula through `D33`.

3. Add a function in D35 to compute the total hours worked on this project

---

## Exercise 3 - Concrete Price Estimator

The following exercise is based on the IF and IFS functions we have just covered.

1. Navigate to the **Concrete Price Estimator** worksheet.

2. Calculate the volume of each item in `E11:E13`, then calculate the total cubic volume in `E16`.

3. Write an IFS formula in E18 to return the price per cubic foot based on the total volume:

   - Less than 400 ft³: $5.25 per ft³
   - At least 400 ft³ but less than 5,000 ft³: $4.30 per ft³
   - At least 5,000 ft³: $3.00 per ft³

4. Multiply the total volume by the price per cubic foot to calculate the total price in `E19`.

5. Try adjusting the lengths of the concrete to see if it changes the price per cubic foot and total price correctly

---

## Exercise 4 - Number of School Years Left

Use IF or IFS formulas and user selections to create an illustrative estimate of the number of years a student has left to finish school. The result is only a simplified example for practicing conditional logic.

**Instructions**

1. Navigate to the **School Left** worksheet.

2. Fill in the criteria in the yellow cells (`C9`, `C11`, `C13`, `C15`, `F17`, and `C19`). These cells have dropdown menus that were created with Data Validation. You will learn how to create them in a later lesson.

3. Write an IF or IFS formula in each applicable **Years** cell (`I9`, `I11`, `I13`, `I15`, `I17`, and `I19`) based on the student selections and the conditions in column **J**.

4. Add up the total in I23 to determine how many years of school you have left.

---
			
## Turning in/Rubric

**_REMINDER_** - For this class, **you will upload your Excel file directly to Learning Suite**. Make sure the file you upload is for the correct assignment and contains your finished work.

1. Make sure your work is saved, then close the workbook so that all of your changes are written to the file.
2. Go to the assignment in Learning Suite and upload your `.xlsx` file as an attachment.
3. Double-check that the file you uploaded is the one that contains your completed work.

**Rubric:**

|                      Item                      | Points Possible |
|:----------------------------------------------:|:---------------:|
| <div style="text-align: right">**Total**</div> |        5        |

---

The following is not a part of the rubric, but specifies how you can lose points. For example: if you fail to upload your file correctly.

| **Reasons for Points Lost** |    **Amount**     |  
|:---------------------------:|:-----------------:|
|  File uploaded incorrectly  |       -10%        |
|  Turned in late (per week)  | -10% (up to -50%) |
