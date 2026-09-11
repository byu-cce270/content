# In-Class Exercise: Graphing and Solver

We will practice selecting charts and using Goal Seek and Solver in Excel. The data are an expanded version of the pre-class construction surplus store. Before starting, review [Cells and Formulas](../../resources/excel_review/basic_excel_review.md) if you need a reminder about worksheets, ranges, or cell references.

Download the [(Starter-Workbook)-Class-Graphing-and-Solver.xlsx](%28Starter-Workbook%29-Class-Graphing-and-Solver.xlsx) workbook.

---
## Exercise #1—Graphing Sales Data

The `Construction_Sales` worksheet contains individual sales records. Use the Excel table `Table1` as the source for the PivotTables. The equivalent worksheet range is `Construction_Sales!A1:M1001`.

Create each chart on its own **chart sheet** and give it a descriptive title. Charts with axes should have axis titles and units where applicable. Use a legend only when it helps identify multiple series; for the pie chart, identify categories with a legend or data labels.

1. **Sales by product:** Create a PivotTable with `Product` in **Rows** and `Total Sales` in **Values**, summarized by **Sum**. Create a pie chart showing each product's share of total sales.
2. **Units sold and revenue:** Create an **XY Scatter—Markers Only** chart directly from `Table1`. Use `Units Sold` for the horizontal (x) axis and `Total Sales` for the vertical (y) axis. Are higher quantities associated with higher total sales? The chart shows association, not necessarily causation.
3. **Sales by region:** Create a PivotTable with `Region` in **Rows** and `Total Sales` in **Values**, summarized by **Sum**. Create a bar chart comparing total sales among regions.
4. **Monthly sales:** Create a PivotTable with `Date` in **Rows** and `Total Sales` in **Values**, summarized by **Sum**. In the PivotTable, group the Date field by **Years** and **Months**. Do not use the separate `Month Start` column for this exercise. Filter out September 2026 because it is an incomplete month, then create a line chart of monthly total sales and add a trendline.

The purpose is to practice matching a chart to a question. You may experiment with colors and styles, but prioritize accurate data, readable labels, and an appropriate chart type.

---
## Exercise #2—Using Goal Seek and Solver

Navigate to the `Polynomial_Solver` worksheet. This worksheet evaluates a polynomial of the form

> $y=ax^4+bx^3+cx^2+dx+e$

The coefficients $a$ through $e$ are in `C11:C15`. With the supplied coefficients, the equation is

> $y=x^4-3x^2+0.6$

### Graphing the Polynomial

Create an **XY Scatter—Smooth Lines** chart from `B17:C38`, using column B for x-values and column C for y-values. Add a descriptive title and axis titles. Use the chart to estimate the locations of the four x-axis crossings before using a numerical tool.

### Finding Four Roots with Goal Seek

The trial x-value is in `F12`, and the corresponding y-value is calculated in `F13`. Use Goal Seek four times:

- **Set cell:** `F13`
- **To value:** `0`
- **By changing cell:** `F12`

Before each run, enter a different starting estimate in `F12` near one of the four crossings visible on your chart. Record each root in the labeled answer area.

<details>
<summary><b>Hint: Why are different starting estimates needed?</b></summary>

The equation has several valid roots. Goal Seek normally returns a solution near the starting estimate, so use the graph to choose one starting value near each crossing.

</details>

### Finding Two Minima with Solver

Use Solver to find the minimum on each side of the y-axis. For both runs:

- **Set Objective:** `F13`
- Select **Min**.
- **By Changing Variable Cell:** `F12`
- Use the **GRG Nonlinear** solving method.

For the negative-side minimum, constrain `F12` to the interval $-2\leq x\leq0$ and start with a negative estimate. For the positive-side minimum, constrain `F12` to $0\leq x\leq2$ and start with a positive estimate. Record both x- and y-values in the labeled answer area.

The bounds tell Solver which local minimum to find. After each run, confirm that the returned x-value satisfies the constraints and that substituting it into the polynomial produces the reported y-value.

<details>
<summary><b>Optional extension: Find the central maximum</b></summary>

Use Solver to **maximize** `F13` by changing `F12`, with $-1\leq x\leq1$ and a starting estimate near zero. Record the result in the labeled answer area.

</details>

---

## Turning in/Rubric

**_REMINDER_** - For this class, **you will upload your Excel file directly to Learning Suite**. Make sure the file you upload is for the correct assignment and contains your finished work.

1. Make sure your work is saved, then close the workbook so that all of your changes are written to the file.
2. Go to the assignment in Learning Suite and upload your `.xlsx` file as an attachment.
3. Double-check that the file you uploaded is the one that contains your completed work.

---

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
