# Unit 1 Midterm Exam Study Guide

This study guide is designed to help you review and prepare for the Unit 1 Midterm Exam in CCE 270. It includes a summary of core concepts, a practice quiz with answers, and a glossary of key terms.

!!! Note
    This study guide is not exhaustive. Be sure to review the course reading content, in-class exercises, homework assignments, and any additional materials provided by your instructor.

## Core Concepts Summary

This section provides a detailed summary of the key concepts, procedures, and functions covered in the course materials.

### 1.0 - A Tour of Class Resources

This module focuses on the foundational procedures for managing and submitting coursework for the CCE 270 class.

* File Management: Students create a single folder on their computer (e.g., "CCE 270") and keep every class file in it. This practice is crucial for managing the numerous files that will be downloaded and worked on throughout the course.
* Assignment Submission Process:
    * Excel assignments are submitted by uploading the Excel (.xlsx) file itself to Learning Suite.
    * Uploading the wrong file, or a file that is not an Excel workbook, will cost points.
* Uploading an Assignment Correctly:<br>
    1. Save your work and close the workbook so all changes are written to the file.<br>
    2. Go to the assignment in Learning Suite.<br>
    3. Upload the `.xlsx` file as an attachment.<br>
    4. Verify that the uploaded file is the one containing your completed work, not the blank starter workbook.
* Grading and Penalties:
    * Incorrect Upload: A penalty of -10% is applied if the file is not uploaded correctly (e.g., the wrong file, or a file that is not an Excel workbook).
    * Late Submissions: A penalty of -10% per week is applied for late submissions, with a maximum penalty of -50%.
* Class Resources and Communication: Students are expected to know how to find information on the class website, such as TA office hours, and how to use communication tools like Microsoft Teams for homework help.

### 1.1 - Analyzing & Managing Data

This module introduces fundamental Excel tools for making data easier to read, analyze, and understand.

* Conditional Formatting: This feature formats cells based on specified conditions, making it easier to highlight important data points.
    * Common Uses: Highlighting cells with specific values (text, numbers, dates), values above/below a threshold, duplicates, blanks, or errors. Visual aids include data bars, color scales, and icon sets.
    * Application Process:<br>
        1. Select the desired range of cells.<br>
        2. On the Home tab, select Conditional Formatting.<br>
        3. Choose a rule type (e.g., Highlight Cells Rules, Top/Bottom Rules) or create a "New Rule".<br>
        4. In the dialog box, set the conditions (e.g., "Text that contains", ">=5", ">=A1").<br>
        5. Choose a preset format or create a "Custom Format" (font, border, fill).
    * Rule Management: Multiple rules can be applied to the same range. The order of rules matters, as the first true rule takes precedence. Rules can be edited, deleted, or copied using the Conditional Formatting Rules Manager and Paste Special (Formats).
* Filtering Data: This feature allows users to display only the data that meets certain criteria, hiding the rest.
    * Application Process:<br>
        1. Select the columns to be filtered.<br>
        2. Go to Data > Filter, or on the Home tab select Sort & Filter > Filter. (Shortcut: Ctrl + Shift + L on Windows; Command + Shift + F or Ctrl + Shift + L on Mac.)<br>
        3. Click the filter arrow in the header of the column to open the filter menu.
    * Filter Types: Users can filter by specific values, numbers (e.g., "Greater Than", "Between"), dates, or cell color.
    * Identifying Filters: A filter icon in the column header indicates an active filter. Row numbers will also appear non-sequential, indicating hidden rows. Filters can be cleared individually or all at once.
    * Filtering hides rows; it never deletes them.
* Excel Tables: A Table is a range that Excel manages as a single object, with tools for sorting, filtering, formatting, and formulas built in.
    * Creating a Table: Select a cell in the data, then Home > Format as Table (shortcut Ctrl + T on Windows). Confirm the range and check **My table has headers** so Excel keeps your headings instead of substituting Column1, Column2, and so on.
    * Benefits: Filter and sort buttons appear automatically; banded rows improve readability; formatting and formulas extend to new rows; columns can be referenced by name; an optional Total Row summarizes the data.
    * Table Design Tab: Appears when a cell inside the Table is selected (labeled **Table** on some Mac versions). Use it to change the style, toggle banded rows, show or hide filter buttons, add a Total Row, resize the Table, and give the Table a descriptive name in place of the default `Table1`.
    * Total Row: Table Design > Total Row adds a row at the bottom that can calculate Sum, Average, Count, Minimum, or Maximum. The result reflects only the visible rows, so it updates when the Table is filtered.
    * Structured References: A formula can refer to a named Table column, such as `EquipmentCheckout[Days Checked Out]`, instead of a cell range such as `F2:F30`.
* Filters versus Tables: A Table does not replace filtering; it organizes the data and adds filter controls automatically.
    * Use filters on a normal range for a quick, temporary review.
    * Use an Excel Table for a spreadsheet that will be updated or reused over time.
    * Always include every related column in the filtered range or Table. Leaving a column out allows sorting to rearrange the included columns while the excluded column stays put, which mismatches values across records.
* Common Functions for Data Analysis:

| Function | Syntax | Purpose |
| :--- | :--- | :--- |
| Sum | =SUM(arguments) | Adds all arguments together. |
| Average | =AVERAGE(arguments) | Averages all arguments. |
| Max | =MAX(arguments) | Returns the highest number from the arguments. |
| Min | =MIN(arguments) | Returns the lowest number from the arguments. |
| Standard Deviation | =STDEV(arguments) | Returns the sample standard deviation. **Use STDEV for the activities and homework in this topic.** |
| Mode | =MODE(arguments) | Returns the most frequently occurring number in the arguments. |
| Median | =MEDIAN(arguments) | Returns the median (middle value) of the arguments. |

!!! note "STDEV.S and STDEV.P"
    Excel may list `STDEV.S` and `STDEV.P` ahead of `STDEV` when you search. `STDEV.S` is the current function for a sample and gives the same kind of result as `STDEV`. `STDEV.P` is for data that represent an entire population. This topic uses `STDEV`.

* Naming a Cell: Select the cell, click the Name Box to the left of the formula bar, type a name with no spaces (such as `con_fac`), and press Enter. The name can then be used in formulas, as in `=C4*con_fac`. Named cells make formulas easier to read and act as fixed references by default.
* Freezing Rows and Columns: Keeps headings visible while the rest of the data scrolls.
    * View > Freeze Panes > Freeze Top Row, or Freeze First Column.
    * For a custom split, select the cell just below the rows and just right of the columns you want to keep visible, then View > Freeze Panes > Freeze Panes. Selecting C3 freezes rows 1-2 and columns A-B.
    * View > Freeze Panes > Unfreeze Panes removes the split.

### 1.2 - Lookups, Match, and IF Functions

This module covers powerful functions for automating calculations and data retrieval in large datasets.

* VLOOKUP / HLOOKUP Functions: These functions look up values in a table. VLOOKUP searches vertically (down columns), while HLOOKUP searches horizontally (across rows).
    * VLOOKUP Syntax: =VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])
    * Parameters:
        * lookup_value: The value to find in the first column of the table_array.
        * table_array: The table of data to search within. Often an absolute reference (e.g., $B$5:$C$10).
        * col_index_num: The column number within the table_array from which to return a value.
        * [range_lookup]: A logical value. FALSE for an exact match. TRUE (or omitted) for an approximate match.
    * Exact vs. Approximate Match:
        * FALSE (Exact Match): Finds the exact lookup_value.
        * TRUE (Approximate Match): Finds the largest value that is less than or equal to the lookup_value. Requires the first column of the table_array to be sorted in ascending order. It is strongly recommended to always specify TRUE or FALSE to avoid unintended errors.
* MATCH Function: Returns the relative position (index number) of an item within a range of cells.
    * Syntax: =MATCH(lookup_value, lookup_array, [match_type])
    * Parameters:
        * lookup_value: The value to find.
        * lookup_array: The range of cells to search.
        * [match_type]:
            * 1 (or omitted): Finds the largest value less than or equal to lookup_value (requires ascending sort).
            * 0: Finds the first value that is exactly equal to lookup_value.
            * -1: Finds the smallest value greater than or equal to lookup_value (requires descending sort).
    * Use with VLOOKUP: MATCH can be nested within VLOOKUP's col_index_num argument to create a dynamic two-dimensional lookup.
* IF / IFS Functions: These functions perform logical comparisons.
    * IF Statement: Compares two values and returns one result if the condition is true, and another if it is false.
        * Syntax: =IF(logical_expression, value_if_true, value_if_false)
        * logical_expression: A condition that evaluates to TRUE or FALSE (e.g., A1 > 75, B2 = "Concrete").
    * IFS Statement: Allows for multiple conditional statements within one function. It tests conditions in order and returns the value for the first condition that is found to be true.
        * Syntax: =IFS(logical_expression1, value_if_true1, [logical_expression2, value_if_true2], ...)
    * Nested IF Compared with IFS: Several outcomes can be handled either way. These two formulas assign the same letter grade:
        * Nested IF: `=IF(E2>=90,"A",IF(E2>=80,"B",IF(E2>=70,"C",IF(E2>=60,"D","F"))))`
        * IFS: `=IFS(E2>=90,"A",E2>=80,"B",E2>=70,"C",E2>=60,"D",TRUE,"F")`
        * Both work, but IFS is usually easier to read and revise when there are many outcomes. In both, order the conditions from the highest threshold to the lowest. A final `TRUE` condition in IFS acts as the catch-all.
* Useful Shortcuts:

| Task | Windows | Mac |
| :--- | :--- | :--- |
| Cycle through relative, absolute, and mixed references while editing a formula | F4 | Command+T or F4 |
| Jump to the edge of the current data region | Ctrl+Arrow | Command+Arrow |

    F4 is especially useful for locking a lookup range before filling a formula down a column.

### 1.3 - Pivot Tables, Goal Seek, and Data Validation

This module explores tools for summarizing data, controlling data entry, and automating problem-solving.

* Data Validation: A feature that controls the type of data that can be entered into a cell, preventing errors.
    * Purpose: To ensure data is appropriate for its context (e.g., only positive numbers, dates within a range, items from a list).
    * Setup:<br>
        1. Select the cell(s).<br>
        2. Go to Data > Data Validation.<br>
        3. In the criteria box, set the rules (e.g., "Whole number", "Date", "List").<br>
        4. For a list, you can type the items or reference a range of cells to create a drop-down menu.<br>
        5. Set output options, such as showing a warning or rejecting invalid data.
* Pivot Tables: A tool used to summarize, analyze, and see relationships in large datasets by reorganizing columns and rows.
    * Creation:<br>
        1. Select the entire data set.<br>
        2. Go to Insert > Pivot Table.<br>
        3. Choose to place the table in a new or existing worksheet.
    * Pivot Table Editor: This panel is used to configure the table.
        * Filters: Filter the entire dataset based on a field.
        * Columns: Creates column headers from a field's unique values.
        * Rows: Creates row labels from a field's unique values.
        * Values: The field(s) to be summarized (e.g., by Sum, Count, Average, Min, Max).
* Goal Seek: An automated trial-and-error tool that finds the specific input value needed to achieve a desired result in a formula.
    * Location: Data > What-If Analysis > Goal Seek.
    * Inputs:<br>
        1. Set Cell: The cell containing the formula whose result you want to change.<br>
        2. To Value: The desired result or target value for the formula.<br>
        3. By Changing Cell: The single input cell that Goal Seek can adjust to reach the target value.

### 1.4 - Graphing and Numerical Solver

This module covers data visualization through charts and optimization using the Solver add-in.

* Choosing a Chart: Match the chart to the question you are asking. Recommended Charts can suggest options, but you decide whether a suggestion represents the data correctly.

| Question | Recommended chart |
| :--- | :--- |
| How do values compare across categories? | Bar or column |
| How does a value change over ordered time periods? | Line |
| How are two numerical variables related? | XY scatter |
| How is one total divided among a few categories? | Pie, used sparingly |

* Bar and column charts perform the same basic comparison. Bars are horizontal and work well with long category names; columns are vertical. A pie chart is appropriate only when the slices are genuine parts of one meaningful whole.
* Line Chart versus XY Scatter: These can look nearly identical, especially when both connect their points. The difference is how Excel treats the horizontal axis.

| Feature | Line chart | XY scatter chart |
| :--- | :--- | :--- |
| Horizontal axis | Category or date/time axis | Numerical value axis |
| Point spacing | Based on categories or time units | Based on the actual x-values |
| Typical purpose | Show a trend over ordered periods | Examine a relationship between two numerical variables |
| Example | Monthly streamflow | Applied load versus beam deflection |

* Practical default: when both x and y are measured quantitative values, an XY scatter chart is nearly always correct, and this is the usual case for engineering data. Use a line chart when the horizontal values are ordered categories and connecting them represents a meaningful sequence. Category labels can be numbers and still be categories, such as Test 1, Test 2, Test 3. For unordered categories, use a bar or column chart rather than connecting points with a line.
* Creating and Editing a Chart: Highlight the data, then Insert > Chart. Use the Chart Design tab to add elements (titles, axis labels, legends), change the data source, switch rows and columns, and apply styles.
* Useful Chart Shortcuts:

| Action | Windows | Mac |
| :--- | :--- | :--- |
| Create an embedded chart from selected data | Alt+F1 | Insert > Recommended Charts |
| Create a chart sheet | F11 | F11 or Fn+F11 |
| Format the selected chart element | Ctrl+1 | Command+1 |

* Goal Seek versus Solver: Both change inputs and recalculate formulas, but they answer different questions.

| Feature | Goal Seek | Solver |
| :--- | :--- | :--- |
| Purpose | Make one formula reach one target value | Reach a target, maximize, or minimize an objective |
| Changing cells | One | One or more |
| Constraints | No | Yes |
| Typical question | What input makes the result equal 50? | What feasible design produces the best result? |

* Solver requires desktop Excel. The standard Solver add-in does not work in Excel for the web or on mobile versions.
* Enabling Solver: It is not enabled by default.
    * Windows: File > Options > Add-ins; beside Manage select Excel Add-ins, then Go; check Solver Add-in, then OK.
    * Mac: Tools > Excel Add-ins; check Solver Add-in, then OK.
    * Solver then appears on the Data tab. This usually needs to be done only once.
* A Solver Model Has Five Parts:<br>
    1. Objective cell: a formula to maximize, minimize, or set to a value.<br>
    2. Changing variable cells: the decisions Solver may change.<br>
    3. Constraints: limits that define feasible solutions (e.g., B9 <= C9, cells are integers, cells >= 0).<br>
    4. Solving method: the algorithm suited to the model.<br>
    5. Validation: a check that the result actually satisfies the formulas and constraints.
* Choosing a Solving Method:
    * Simplex LP: linear models.
    * GRG Nonlinear: smooth nonlinear models.
    * Evolutionary: non-smooth or discontinuous models, including models whose formulas use step functions.
* SUMPRODUCT: Multiplies corresponding values in two ranges and adds the products. It is a compact way to compute a resource total or a weighted contribution in a Solver model.

### 1.5 - Gantt Chart - Project Scheduling and Tracking

This module introduces Gantt charts as a project management tool and the Excel model behind them.

* Gantt Charts: Bar charts that visualize a project schedule, showing when tasks start and finish so progress can be planned, tracked, and communicated.
* What a Basic Gantt Chart Contains:
    * Tasks: the activities required to complete the project.
    * Phases: groups of related tasks.
    * Start dates: when each task is planned to begin.
    * Durations or end dates: how long each task lasts or when it finishes.
    * Dependencies: relationships in which one task depends on another.
    * Assignments: the person or role responsible for each task.
    * Progress: the portion of each task completed.
    * Tasks may run sequentially or in parallel. A milestone is a zero-duration event marking an important deadline or decision.
* Scope of the Excel Model: The workbook records dependencies as text. It does not calculate a dependency network, resource capacity, cost, or critical path; those require dedicated scheduling software.
* Input-Calculation-Output Structure: The workbook separates into three connected parts, and changing an input should update everything downstream.<br>
    1. Inputs: task names, assignments, start dates, work-day durations, and progress.<br>
    2. Calculations: task end dates, phase summaries, and displayed timeline dates.<br>
    3. Outputs: task bars, phase bars, progress bars, weekends, and the current-day marker.
* Excel Dates: Excel stores a date as a serial number. A date format changes how that number is displayed; it does not turn the date into text. Use the original date for calculations and use TEXT only when a text label is needed.
* Functions Used in This Topic:

| Function | What it does | Use in the Gantt chart |
| :--- | :--- | :--- |
| TODAY() | Returns the current date | Marks the current day |
| WEEKDAY(date, return_type) | Converts a date to a weekday number | Aligns the timeline to Monday and identifies weekends |
| TEXT(value, "format") | Converts a value to formatted text | Creates weekday labels |
| LEFT(text, num_chars) | Returns characters from the left of a text string | Shortens weekday labels to one letter |
| WORKDAY(start, days) | Moves by workdays, excluding weekends | Calculates task end dates |
| IF, OR, AND | Test one or more conditions | Leave unused rows blank and control formatting |
| AVERAGE, MIN, MAX | Summarize a range | Calculate phase progress and phase dates |

* Work-day End Dates: A start date that falls Monday through Friday counts as the first workday, so a one-workday task starting Monday also ends Monday. The typical formula is:
    * `=IF(OR(D8="",F8=""),"",WORKDAY(D8,F8-1))`
    * The `OR` test returns a blank when either input is missing. The `F8-1` subtracts one because the start date is already day 1. WORKDAY excludes Saturdays and Sundays, but it does not correct a weekend date entered as the start.
* Named Cells and a Dynamic Timeline: Naming the project-start and display-week cells `project_start` and `display_week` makes the timeline formula readable:
    * `=project_start-WEEKDAY(project_start,3)+(display_week-1)*7`
    * With return type 3, WEEKDAY returns 0 for Monday through 6 for Sunday, so subtracting it moves back to Monday of that week. The final term advances the display seven days per additional week.
* Conditional Formatting and Mixed References: A conditional-formatting rule is written as though it applies to the upper-left cell of its **Applies to** range, and Excel evaluates it for every cell in that range.
    * `H$5` changes columns across the timeline but always reads row 5.
    * `$D7`, `$E7`, and `$F7` stay in their assigned columns but change rows.
    * These mixed references let one rule evaluate every task against every displayed date.
    * The exercise builds separate rules for task bars, phase-summary bars, the current day, and weekends. Separate rules are easier to inspect and debug, and rule order matters when several rules format the same cell.
* Shortcuts Used in This Topic: Save (Ctrl+S / Command+S), Copy and Paste (Ctrl+C, Ctrl+V / Command+C, Command+V), Open Format Cells (Ctrl+1 / Command+1).


---


## Midterm Practice Quiz

Sample questions to help you prepare for the midterm exam. Answers are provided at the end of the quiz.

1. How are Excel assignments turned in for this class?<br>
A. By emailing the workbook to a TA.<br>
B. By uploading the Excel (.xlsx) file to Learning Suite.<br>
C. By printing the workbook and handing it in.<br>
D. By typing your answers into the feedback box.
2. What is the penalty for uploading your assignment incorrectly, such as uploading the blank starter workbook instead of your completed one?<br>
A. -10%.<br>
B. -25%.<br>
C. -50%.<br>
D. There is no penalty.
3. What is the primary purpose of Conditional Formatting in Excel?<br>
A. To perform complex calculations on a range of data.<br>
B. To automatically format cells based on specified rules or conditions.<br>
C. To hide rows that do not meet certain criteria.<br>
D. To create a drop-down list of acceptable values for a cell.
4. If two conditional formatting rules apply to the same cell, how does Excel determine which format to apply?<br>
A. It applies the format from the most recently created rule.<br>
B. It applies the format from the first rule in the list that evaluates to true.<br>
C. It combines the formats from both rules.<br>
D. It prompts the user to choose which rule to apply.
5. Which standard deviation function does this topic tell you to use?<br>
A. =STDEV.P()<br>
B. =STDEV()<br>
C. =VAR()<br>
D. =MEDIAN()
6. When you convert a range into an Excel Table, why should you check "My table has headers"?<br>
A. It sorts the first row alphabetically.<br>
B. It keeps your existing headings instead of replacing them with Column1, Column2, and so on.<br>
C. It freezes the top row automatically.<br>
D. It prevents the Table from expanding when rows are added.
7. A Table's Total Row is set to Average and the Table is then filtered. What does the Total Row show?<br>
A. The average of every row, filtered or not.<br>
B. An error, because filtering breaks the Total Row.<br>
C. The average of only the visible rows.<br>
D. Zero until the filter is cleared.
8. What is `EquipmentCheckout[Days Checked Out]` an example of?<br>
A. An absolute cell reference.<br>
B. A structured reference to the `Days Checked Out` column of the `EquipmentCheckout` Table.<br>
C. A conditional-formatting rule.<br>
D. A formula.
9. You want rows 1-2 and columns A-B to stay visible while you scroll. Which cell do you select before choosing View > Freeze Panes > Freeze Panes?<br>
A. A1<br>
B. B2<br>
C. C3<br>
D. C1
10. What is the effect of naming a cell `con_fac` in the Name Box and then writing `=C4*con_fac`?<br>
A. The formula breaks when copied, because named cells are relative.<br>
B. The name acts as a fixed reference to that cell, and the formula is easier to read.<br>
C. Excel converts C4 into text.<br>
D. The named cell is locked against editing.
11. In the VLOOKUP function, what does the col_index_num argument represent?<br>
A. The number of columns in the lookup table.<br>
B. The column number in the worksheet where the return value is located.<br>
C. The column number within the specified table_array from which to return a value.<br>
D. The number of rows to look down before finding a match.
12. What is the required condition for using VLOOKUP with the range_lookup argument set to TRUE (or omitted)?<br>
A. The entire lookup table must be sorted in ascending order.<br>
B. The first column of the lookup table must be sorted in ascending order.<br>
C. The first column of the lookup table must contain only numbers.<br>
D. The lookup value must be an exact match to a value in the table.
13. What does the MATCH function return?<br>
A. The value from a cell that matches the lookup value.<br>
B. The cell address of the matching value.<br>
C. The relative position (index) of an item in a range.<br>
D. A TRUE or FALSE value indicating if a match was found.
14. Which match_type argument in the MATCH function is used to find an exact match?<br>
A. 1<br>
B. -1<br>
C. TRUE<br>
D. 0
15. What is the primary difference between an IF statement and an IFS statement?<br>
A. IF can handle text, while IFS only handles numbers.<br>
B. IF returns a value, while IFS returns TRUE/FALSE.<br>
C. IF handles one condition, while IFS can handle multiple ordered conditions in a single function.<br>
D. IF is for simple numbers, while IFS is used for lookup operations.
16. While editing a formula, which shortcut cycles a reference through relative, absolute, and mixed forms?<br>
A. Ctrl+Shift+L<br>
B. F4 on Windows, or Command+T on Mac<br>
C. Ctrl+1<br>
D. Alt+F1
17. In the formula =IFS(E2>=90,"A",E2>=80,"B",E2>=70,"C",E2>=60,"D",TRUE,"F"), what is the purpose of the final TRUE?<br>
A. It verifies that the earlier conditions are valid.<br>
B. It acts as a catch-all that returns "F" when no earlier condition is met.<br>
C. It forces Excel to recalculate the formula.<br>
D. It sorts the conditions from highest to lowest.
18. What feature in Excel is used to control the type of data entered into a cell, for example, by creating a drop-down list?<br>
A. Conditional Formatting<br>
B. Filtering<br>
C. Data Validation<br>
D. Pivot Table
19. In the Pivot Table editor, where would you drag the "Region" field if you want to create a row label for each unique region?<br>
A. The Filters section.<br>
B. The Rows section.<br>
C. The Columns section.<br>
D. The Values section.
20. In the Pivot Table editor, where would you drag the "Total Sales" field to calculate the sum of sales for each category?<br>
A. The Filters section.<br>
B. The Rows section.<br>
C. The Values section.<br>
D. The Columns section.
21. Which tool automates a trial-and-error process by changing a single input cell to make a formula cell reach a specific target value?<br>
A. Solver<br>
B. Data Validation<br>
C. Pivot Table<br>
D. Goal Seek
22. What are the three inputs required for Goal Seek?<br>
A. Set Objective, By Changing Cells, Constraints<br>
B. Set Cell, To Value, By Changing Cell<br>
C. Logical Expression, Value if True, Value if False<br>
D. Lookup Value, Table Array, Column Index
23. Which type of chart is best suited for showing trends over a period of time?<br>
A. Pie Chart<br>
B. Bar Chart<br>
C. Bubble Plot<br>
D. Scatter Plot
24. Which chart type is most appropriate for showing the proportion of different categories that make up a whole, such as market share?<br>
A. Line Graph<br>
B. Pie Chart<br>
C. Scatter Plot<br>
D. Column Chart
25. In the Solver parameters, what does the "Set Objective" cell represent?<br>
A. The cell that Solver is allowed to change.<br>
B. The cell containing the formula that you want to optimize (max, min, or set to a value).<br>
C. A cell that contains a constraint for the problem.<br>
D. The cell where the final answer will be displayed.
26. You are plotting measured load against measured beam deflection, and the load values are unevenly spaced. Which chart represents the data correctly?<br>
A. A line chart, because it connects the points.<br>
B. An XY scatter chart, because it places each point at its numerical x-value.<br>
C. A pie chart.<br>
D. A stacked column chart.
27. What is the key difference between a line chart and an XY scatter chart?<br>
A. A line chart cannot display more than one series.<br>
B. A scatter chart cannot connect its points with a line.<br>
C. A line chart treats the horizontal axis as categories or time units, while a scatter chart treats it as numerical values.<br>
D. A scatter chart requires the data to be sorted.
28. What does SUMPRODUCT do in a Solver model?<br>
A. It sorts the products by value.<br>
B. It multiplies corresponding values in two ranges and adds the products.<br>
C. It returns the largest product in a range.<br>
D. It counts how many products exceed a limit.
29. What is a Gantt Chart primarily used for?<br>
A. Analyzing financial data and calculating profit.<br>
B. Visualizing a project schedule, including task durations and timelines.<br>
C. Creating a database of project resources.<br>
D. Performing complex statistical analysis on survey data.
30. In a Gantt chart, what does the length of a horizontal bar typically represent?<br>
A. The budget for the task.<br>
B. The number of people assigned to the task.<br>
C. The duration of the task.<br>
D. The priority level of the task.
31. Which piece of information is essential for creating a basic Gantt chart?<br>
A. A list of tasks, start dates, and durations.<br>
B. The total project budget.<br>
C. The email addresses of all team members.<br>
D. The risk assessment report.
32. Which Excel function is used to return a number representing the day of the week for a specific date?<br>
A. =DAY()<br>
B. =TODAY()<br>
C. =WEEKDAY()<br>
D. =TEXT()
33. What is the purpose of using the TEXT function when creating a Gantt chart in Excel?<br>
A. To extract the first letter of the day of the week.<br>
B. To convert a date into a number.<br>
C. To apply conditional formatting to the chart.<br>
D. To convert the number returned by WEEKDAY() into a text representation like "Mon".
34. In the formula =IF(OR(D8="",F8=""),"",WORKDAY(D8,F8-1)), why is 1 subtracted from the duration in F8?<br>
A. To leave a buffer day at the end of each task.<br>
B. Because the start date already counts as the first workday.<br>
C. Because WORKDAY counts weekends and the subtraction removes one.<br>
D. To convert the duration from calendar days to workdays.
35. What does the WORKDAY function do that a simple date addition does not?<br>
A. It formats the result as a date.<br>
B. It excludes Saturdays and Sundays from the count.<br>
C. It prevents the start date from being edited.<br>
D. It converts the date into text.
36. In a conditional-formatting rule written as =AND($D7<>"",H$5>=$D7), what does the mixed reference H$5 accomplish?<br>
A. It always reads cell H5 no matter which cell is evaluated.<br>
B. It changes columns as Excel moves across the timeline but always reads row 5.<br>
C. It changes rows but always reads column H.<br>
D. It makes the rule apply only to the upper-left cell.
37. How does Excel store a date?<br>
A. As text formatted by the user.<br>
B. As a serial number that a date format displays in a readable way.<br>
C. As a WEEKDAY value from 1 to 7.<br>
D. As a formula that recalculates daily.
38. To apply a filter to a data table, what is the first step?<br>
A. Create a Pivot Table.<br>
B. Select the columns of data you want to add filters to.<br>
C. Use the VLOOKUP function.<br>
D. Enable the Solver Add-in.
39. In the VLOOKUP formula =VLOOKUP(E13, $B$5:$C$10, 2, FALSE), what does the value 2 signify?<br>
A. Return the value from the second worksheet.<br>
B. The lookup table has two rows.<br>
C. An exact match is required.<br>
D. Return the value from the second column of the range $B$5:$C$10.
40. A user wants to create a drop-down list in cell A1 containing the options "Yes", "No", and "Maybe". Which feature should be used?<br>
A. Conditional Formatting with a custom rule.<br>
B. Data Validation set to allow a "List".<br>
C. A Pivot Table with a slicer.<br>
D. An IFS function in cell A1.
41. What is the purpose of using absolute references (e.g., $B$5:$C$10) for the table_array in a VLOOKUP function?<br>
A. To ensure the reference is updated when the formula is copied to other cells.<br>
B. To lock the table reference so it does not change when the formula is copied to other cells.<br>
C. To make the lookup faster.<br>
D. To allow for an approximate match.
42. A scatter plot is the most effective chart type for what purpose?<br>
A. Comparing parts of a whole.<br>
B. Showing the relationship between two numerical variables.<br>
C. Displaying categorical data horizontally.<br>
D. Visualizing the percentages of a set of data.
43. If an IFS statement has multiple conditions that are true for a given cell, which value will it return?<br>
A. The value corresponding to the last true condition.<br>
B. An error message.<br>
C. A combination of all true values.<br>
D. The value corresponding to the first true condition in the sequence.
44. Which function would be used to extract the letter "S" from the text "Sun"?<br>
A. =TEXT("Sun", "d")<br>
B. =LEFT("Sun", 1)<br>
C. =WEEKDAY("Sun")<br>
D. =MATCH("S", "Sun", 0)
45. A user sets up a Pivot Table and drags "Product" to Rows and "Units Sold" to Values. By default, what calculation will the Pivot Table show for "Units Sold"?<br>
A. Count of Units Sold<br>
B. Average of Units Sold<br>
C. Sum of Units Sold<br>
D. Max of Units Sold
46. In Solver, what is the role of a "constraint"?<br>
A. It defines the formula cell to be optimized.<br>
B. It specifies which cells the Solver can change.<br>
C. It sets a rule or limit that the solution must adhere to.<br>
D. It selects the algorithm used for solving.
47. The range_lookup parameter in VLOOKUP is optional. If it is omitted, what value does Excel assume?<br>
A. FALSE<br>
B. TRUE<br>
C. 0<br>
D. An error is returned.
48. To find the "top 10" values in a dataset, which Excel feature would be most direct?<br>
A. A VLOOKUP function.<br>
B. The "Top/Bottom Rules" option within Conditional Formatting or Filtering.<br>
C. The Solver add-in.<br>
D. Creating a Pie Chart.



---


---


**Answer Key**

1. B
2. A
3. B
4. B
5. B
6. B
7. C
8. B
9. C
10. B
11. C
12. B
13. C
14. D
15. C
16. B
17. B
18. C
19. B
20. C
21. D
22. B
23. D
24. B
25. B
26. B
27. C
28. B
29. B
30. C
31. A
32. C
33. D
34. B
35. B
36. B
37. B
38. B
39. D
40. B
41. B
42. B
43. D
44. B
45. C
46. C
47. B
48. B


---


## Glossary of Key Terms

| Term | Definition |
| :--- | :--- |
| **Absolute Reference** | A reference locked with dollar signs (e.g., `$B$5`) so it does not shift when the formula is copied. Press F4 (Command+T on Mac) while editing to cycle reference types. |
| **Banded Rows** | Alternating row shading applied automatically by an Excel Table to make large data sets easier to read. |
| **Conditional Formatting** | A feature in Excel that allows you to format cells based on certain conditions, making data easier to read and highlight. |
| **Data Validation** | A feature that allows you to control the type of data entered into a cell, helping to prevent errors. |
| **Excel Table** | A range that Excel manages as a single object, adding filter buttons, banded rows, automatic expansion, named columns, and an optional Total Row. Created with Home > Format as Table (Ctrl + T). |
| **Filtering** | A feature that allows you to show only the data that meets certain criteria, hiding rows that do not match. |
| **Function** | A preset formula in Excel that helps users analyze, manage, and compute data (e.g., SUM, AVERAGE). |
| **Gantt Chart** | A type of bar chart used in project management that illustrates a project schedule, showing the start and finish dates of tasks. |
| **Goal Seek** | A tool in Excel that automates a trial-and-error process to find a specific input value that results in a desired output from a formula. |
| **HLOOKUP** | A function used for horizontal lookups, searching for a value in the top row of a table and returning a value from a specified row below it. |
| **IF Function** | A logical function that returns one value if a specified condition is true and another value if it is false. |
| **IFS Function** | A logical function that checks whether one or more conditions are met and returns a value corresponding to the first true condition. |
| **LEFT Function** | A text function that returns a specified number of characters from the beginning of a text string. |
| **MATCH Function** | A function that returns the relative position (index number) of an item in a range of cells. |
| **Milestone** | A zero-duration event in a schedule that marks an important deadline or decision. |
| **Mixed Reference** | A reference that locks either the column or the row but not both (e.g., `H$5` or `$D7`). Essential to conditional-formatting rules that must evaluate every task against every date. |
| **MODE Function** | A function that returns the most frequently occurring number in a range. |
| **Named Cell** | A cell given a meaningful name in the Name Box (e.g., `project_start`). The name can be used in formulas and acts as a fixed reference by default. |
| **Phase** | A group of related tasks in a project schedule, summarized from the task rows beneath it. |
| **Pivot Table** | A tool used to summarize, analyze, and explore large data sets by rearranging rows and columns. Written as PivotTable in the current course readings. |
| **Solver** | An Excel add-in that finds an optimal (maximum, minimum, or specific) value for an objective formula by adjusting one or more variable cells subject to constraints. Requires desktop Excel. |
| **SOLVER Solving Methods** | Simplex LP for linear models, GRG Nonlinear for smooth nonlinear models, and Evolutionary for non-smooth or discontinuous models. |
| **STDEV Function** | Returns the sample standard deviation of its arguments. This unit uses `STDEV`; `STDEV.P` applies when the data represent an entire population. |
| **Structured Reference** | A formula reference to a named Table column, such as `EquipmentCheckout[Days Checked Out]`, used in place of a cell range. |
| **SUMPRODUCT Function** | Multiplies corresponding values in two or more ranges and adds the products. Common in Solver models for resource totals. |
| **TEXT Function** | A function that converts a numeric value into text using a specified format code. |
| **Total Row** | An optional row at the bottom of an Excel Table that calculates Sum, Average, Count, Min, or Max, reflecting only the rows currently visible. |
| **VLOOKUP** | A function used for vertical lookups, searching for a value in the first column of a table and returning a value from a specified column in the same row. |
| **WEEKDAY Function** | A function that returns a number from 1 to 7 representing the day of the week for a given date. |
| **WORKDAY Function** | Returns a date a given number of workdays from a start date, excluding Saturdays and Sundays. Used to calculate task end dates. |
| **XY Scatter Chart** | A chart whose horizontal axis is a numerical value axis, placing each point at its actual x-coordinate. The usual default for measured engineering data. |
