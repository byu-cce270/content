# In-Class Exercise: PivotTables and Goal Seek

---

These exercises introduce **Data Validation**, **Goal Seek**, and **PivotTables**. Download the in-class workbook here: [(Starter-Workbook)-Class-Pivot-GoalSeek-DataV.xlsx](%28Starter-Workbook%29-Class-Pivot-GoalSeek-DataV.xlsx)

The workbook contains five worksheets: **Data Validation** for Exercise 1, **Brickmaking Business** for Exercise 2, **Data** and **Pivot Table** for Exercise 3, and **credits** for the data source. The **Data** worksheet contains the employee source data.

For a reminder about cell, range, absolute, or named references, see [Cells and Formulas](../../resources/excel_review/basic_excel_review.md).

---

## Exercise 1 - Data Validation

1. Navigate to the **Data Validation** worksheet.
2. Open **Data > Data Validation** and enter the following fields for each range:

   | Cells | Allow | Data | Value or Source |
   |:------|:------|:-----|:----------------|
   | `A11:A23` | Whole number | greater than | Minimum: `0` |
   | `B11:B23` | List | — | Source: `=$B$25:$B$31` |
   | `C11:C23` | Date | less than | End date: `=TODAY()` |
   | `D11:D23` | Decimal | between | Minimum: `0`; Maximum: `1` |

3. For each entry range, add an **Input Message** that briefly describes the required value.
4. For each entry range, add a descriptive **Error Alert** that helps the user correct an invalid value. Use the **Stop** style so Excel rejects invalid entries.
5. Test every rule by entering at least one valid value and one invalid value. Confirm that valid values are accepted and invalid values display the intended alert. Leave valid values in the cells when finished.

--- 

## Exercise 2 - Brickmaking Business

1. Navigate to the **Brickmaking Business** worksheet.
2. Enter formulas for:
   - **Total Expense (`B8`):** fixed expense plus the variable expense for the number of bricks sold.
   - **Total Revenue (`B9`):** selling price per brick multiplied by the number of bricks sold.
   - **Profit (`B10`):** total revenue minus total expense.
3. Use Goal Seek to determine how many bricks must be sold to earn a profit of $100,000:
   - **Set Cell:** `B10`
   - **To Value:** `100000`
   - **By Changing Cell:** `B7`
4. Accept the Goal Seek result and leave the calculated number of bricks in `B7`.

---

## Exercise 3 - Employee Data

1. Create a PivotTable using `Data!A1:P1001`, which means cells `A1` through `P1001` on the **Data** worksheet. In the **Create PivotTable** dialog, verify this source in **Table/Range**, select **Existing Worksheet**, and set **Location** to `'Pivot Table'!A8`. Excel may add dollar signs to either reference; for example, `Data!$A$1:$P$1001` identifies the same source cells.
2. Place **Job Title** in **Rows**.
3. Place **EEID** in **Values** and use **Value Field Settings** to summarize it by **Count**.
4. Place **Annual Salary** in **Values**, use **Value Field Settings** to summarize it by **Average**, and use **Number Format** in that dialog to display the results as currency.
5. Place **Department** below **Job Title** in **Rows** and examine the nested summary.
6. Move **Department** from **Rows** to **Columns** and compare the new layout with the nested summary.
7. In the labeled response box on the **Pivot Table** worksheet, type one concise observation about the distribution of employees or average salaries. Base the observation on your PivotTable results.

---

## Turning in/Rubric

**_REMINDER_** - For this class, **you will upload your Excel file directly to Learning Suite**. Make sure the file you upload is for the correct assignment and contains your finished work.

1. Make sure your work is saved, then close the workbook so that all of your changes are written to the file.
2. Go to the assignment in Learning Suite and upload your `.xlsx` file as an attachment.
3. Double-check that the file you uploaded is the one that contains your completed work.

In-class assignment scores are based on valid effort and 
   completion.

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
