# Unit 1 Midterm Exam Study Guide

This study guide is designed to help you review and prepare for the Unit 1 Midterm Exam in CCE 270. It includes a summary of core concepts, a practice quiz with answers, and a glossary of key terms.

!!! Note
    This study guide is not exhaustive. Be sure to review the course reading content, in-class exercises, homework assignments, and any additional materials provided by your instructor.

## Core Concepts Summary

This section provides a detailed summary of the key concepts, procedures, and functions covered in the course materials.

### 1.0 - A Tour of Class Resources

This module focuses on the foundational procedures for managing and submitting coursework for the CCE 270 class.

* File Management with OneDrive: Students are required to mount their OneDrive to their local computer to create a centralized, organized folder (e.g., "CCE 270") for all class assignments. This practice is crucial for managing the numerous files that will be downloaded and worked on throughout the course.
* File Naming Convention: When working with starter workbooks, students must rename the file to include their name, such as (Your-Name)-HW-A-Tour-of-Class-Resources. Correctly renaming the workbook is a graded item.
* Assignment Submission Process:
    * Assignments are submitted not as Excel files, but as shareable links to the Excel files stored in OneDrive.
    * Submitting an Excel file directly or a link that is not properly shared will result in a score of 0 for the assignment.
* Generating a Correct Shareable Link:<br>
    1. Ensure the file is saved in the class OneDrive folder.<br>
    2. Click the "Share" button in the top right corner of Excel.<br>
    3. Access the settings next to the "Copy Link" button.<br>
    4. Set permissions so that "Anyone" with the link can access it.<br>
    5. Change the "More settings" permission from "Can view" to "Can edit".<br>
    6. Apply the settings and copy the generated link.<br>
    7. Paste this link into the feedback box for the assignment in Learning Suite.
* Grading and Penalties:
    * Incorrect Link Sharing: A penalty of -10% is applied if the link is not shared correctly (i.e., not set to "anyone" with "can edit" permissions).
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
        2. On the Home tab, go to Sort & Filter and click Filter (Shortcut: Ctrl + Shift + L or Cmd + Shift + L for Mac).<br>
        3. Click the filter arrow in the header of the column to open the filter menu.
    * Filter Types: Users can filter by specific values, numbers (e.g., "Greater Than", "Between"), or cell color.
    * Identifying Filters: A filter icon in the column header indicates an active filter. Row numbers will also appear non-sequential, indicating hidden rows. Filters can be cleared individually or all at once.
* Common Functions for Data Analysis:

| Function | Syntax | Purpose |
| :--- | :--- | :--- |
| Sum | =SUM(arguments) | Adds all arguments together. |
| Average | =AVERAGE(arguments) | Averages all arguments. |
| Max | =MAX(arguments) | Returns the highest number from the arguments. |
| Min | =MIN(arguments) | Returns the lowest number from the arguments. |
| Standard Deviation (Population) | =STDEV.P(arguments) | Calculates standard deviation for an entire population dataset. |
| Standard Deviation (Sample) | =STDEV.S(arguments) | Calculates standard deviation for a sample (subset) of a population. |
| Median | =MEDIAN(arguments) | Returns the median (middle value) of the arguments. |

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

This module covers data visualization through charts and advanced optimization using the Solver add-in.

* Graphing Data: Excel's chart feature helps visualize trends, compare variables, and understand data sets.
    * Creation:<br>
        1. Highlight the data to be graphed.<br>
        2. Go to Insert > Chart. Excel provides "Recommended Charts" or specific types.
    * Common Chart Types:
        * Line Graph: Shows trends over time.
        * Bar/Column Chart: Compares values across different categories. Bar charts are horizontal (categorical data), while column charts are vertical (numerical data).
        * Pie Chart: Shows the proportion of categories in a whole.
        * Scatter Plot: Shows the relationship between two numerical variables.
    * Chart Customization:
        * Chart Design Tab: Add elements (titles, labels, legends), change data sources, switch rows/columns, and apply styles.
        * Chart Icons: Convenient icons next to the chart for Elements, Styles, and Filters.
* Solver: A powerful add-in that finds an optimal (maximum, minimum, or specific) value for a formula by adjusting multiple input cells and adhering to constraints.
    * Enabling Solver: It is not enabled by default. Go to File > Options > Add-ins > Manage: Excel Add-ins > Go, then check the Solver Add-in box. Once enabled, it appears under the Analyze group on the Data tab.
    * Solver vs. Goal Seek: Goal Seek changes one input cell to reach one specific target value. Solver can change multiple input cells, work with multiple constraints, and find a maximum or minimum value, not just a specific target.
    * Solver Parameters:
        * Set Objective: The cell with the formula to optimize.
        * To: The goal (Max, Min, or Value Of).
        * By Changing Variable Cells: The input cells that Solver can adjust.
        * Subject to the Constraints: Rules that the solution must follow (e.g., C5 <= 60).
    * Solving Methods: The GRG Nonlinear method is versatile and used for most problems in the class.

### 1.5 - Gantt Chart - Project Scheduling and Tracking

This module introduces Gantt charts as a project management tool and the Excel functions used to create them.

* Gantt Charts: Bar charts that visualize a project's schedule. They show the start and finish dates of project tasks, helping to manage, schedule, and monitor progress.
    * Purpose: Used by managers and engineers to plan projects, track progress, allocate resources, identify potential problems, and ensure projects are completed on time and within budget.
    * Key Components:
        * Horizontal Bars: Represent individual tasks. The length of the bar indicates the task's duration, and its position on the timeline shows its start and end dates.
        * Timeline: The horizontal axis representing calendar dates.
        * Dependencies: Links between tasks showing sequences (e.g., Task B cannot start until Task A is finished).
* Input Data Needed for a Gantt Chart:<br>
    1. Task List: A complete list of all project activities.<br>
    2. Start Date: The planned start date for each task.<br>
    3. End Date or Duration: Either the finish date or the length of time the task will take.<br>
    4. Dependencies (Optional but powerful): The relationships between tasks.
* Excel Functions for Gantt Chart Creation:

| Function | Syntax | Purpose in Gantt Chart |
| :--- | :--- | :--- |
| WEEKDAY | =WEEKDAY(serial_number, [return_type]) | Returns a number representing the day of the week for a given date. |
| TEXT | =TEXT(value, "format_code") | Converts a number into text using a specified format (e.g., converts the WEEKDAY number to "Mon"). |
| LEFT | =LEFT(text, [num_chars]) | Extracts the first character(s) from a text string (e.g., extracts "M" from "Mon"). |


---


## Midterm Practice Quiz

Sample questions to help you prepare for the midterm exam. Answers are provided at the end of the quiz.

1. According to the class rubric, what is the consequence of submitting an Excel file directly instead of a shareable link?<br>
A. A 10% penalty.<br>
B. A 50% penalty.<br>
C. A score of 0 for the assignment.<br>
D. A warning on the first offense.
2. Which setting is required to ensure a TA can grade an Excel assignment submitted via a link from OneDrive?<br>
A. "Anyone" with the link can "view".<br>
B. "People in your organization" can "edit".<br>
C. "Anyone" with the link can "edit".<br>
D. "Specific people" can "view".
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
5. Which function calculates the standard deviation assuming the data represents the entire population?<br>
A. =STDEV.S()<br>
B. =STDEV()<br>
C. =AVERAGE()<br>
D. =STDEV.P()
6. In the VLOOKUP function, what does the col_index_num argument represent?<br>
A. The number of columns in the lookup table.<br>
B. The column number in the worksheet where the return value is located.<br>
C. The column number within the specified table_array from which to return a value.<br>
D. The number of rows to look down before finding a match.
7. What is the required condition for using VLOOKUP with the range_lookup argument set to TRUE (or omitted)?<br>
A. The entire lookup table must be sorted in ascending order.<br>
B. The first column of the lookup table must be sorted in ascending order.<br>
C. The first column of the lookup table must contain only numbers.<br>
D. The lookup value must be an exact match to a value in the table.
8. What does the MATCH function return?<br>
A. The value from a cell that matches the lookup value.<br>
B. The cell address of the matching value.<br>
C. The relative position (index) of an item in a range.<br>
D. A TRUE or FALSE value indicating if a match was found.
9. Which match_type argument in the MATCH function is used to find an exact match?<br>
A. 1<br>
B. -1<br>
C. TRUE<br>
D. 0
10. What is the primary difference between an IF statement and an IFS statement?<br>
A. IF can handle text, while IFS only handles numbers.<br>
B. IF returns a value, while IFS returns TRUE/FALSE.<br>
C. IF handles one condition, while IFS can handle multiple ordered conditions in a single function.<br>
D. IF is for simple logic, while IFS is used for lookup operations.
11. What feature in Excel is used to control the type of data entered into a cell, for example, by creating a drop-down list?<br>
A. Conditional Formatting<br>
B. Filtering<br>
C. Data Validation<br>
D. Pivot Table
12. In the Pivot Table editor, where would you drag the "Region" field if you want to create a row label for each unique region?<br>
A. The Filters section.<br>
B. The Rows section.<br>
C. The Columns section.<br>
D. The Values section.
13. In the Pivot Table editor, where would you drag the "Total Sales" field to calculate the sum of sales for each category?<br>
A. The Filters section.<br>
B. The Rows section.<br>
C. The Values section.<br>
D. The Columns section.
14. Which tool automates a trial-and-error process by changing a single input cell to make a formula cell reach a specific target value?<br>
A. Solver<br>
B. Data Validation<br>
C. Pivot Table<br>
D. Goal Seek
15. What are the three inputs required for Goal Seek?<br>
A. Set Objective, By Changing Cells, Constraints<br>
B. Set Cell, To Value, By Changing Cell<br>
C. Logical Expression, Value if True, Value if False<br>
D. Lookup Value, Table Array, Column Index
16. Which type of chart is best suited for showing trends over a period of time?<br>
A. Pie Chart<br>
B. Bar Chart<br>
C. Scatter Plot<br>
D. Line Graph
17. Which chart type is most appropriate for showing the proportion of different categories that make up a whole, such as market share?<br>
A. Line Graph<br>
B. Pie Chart<br>
C. Scatter Plot<br>
D. Column Chart
18. What is the key difference between Solver and Goal Seek?<br>
A. Goal Seek is an add-in, while Solver is a built-in function.<br>
B. Goal Seek can only find a minimum value, while Solver can find a maximum or minimum.<br>
C. Solver can change multiple cells and handle constraints, while Goal Seek changes one cell for one target.<br>
D. Solver is used for linear problems, while Goal Seek is for nonlinear problems.
19. How is the Solver Add-in enabled in Excel?<br>
A. It is enabled by default on the Data tab.<br>
B. Through Insert > Add-ins.<br>
C. Through File > Options > Add-ins.<br>
D. By downloading it from the Microsoft Office website.
20. In the Solver parameters, what does the "Set Objective" cell represent?<br>
A. The cell that Solver is allowed to change.<br>
B. The cell containing the formula that you want to optimize (max, min, or set to a value).<br>
C. A cell that contains a constraint for the problem.<br>
D. The cell where the final answer will be displayed.
21. What is a Gantt Chart primarily used for?<br>
A. Analyzing financial data and calculating profit.<br>
B. Visualizing a project schedule, including task durations and timelines.<br>
C. Creating a database of project resources.<br>
D. Performing complex statistical analysis on survey data.
22. In a Gantt chart, what does the length of a horizontal bar typically represent?<br>
A. The budget for the task.<br>
B. The number of people assigned to the task.<br>
C. The duration of the task.<br>
D. The priority level of the task.
23. Which piece of information is essential for creating a basic Gantt chart?<br>
A. A list of tasks, start dates, and durations.<br>
B. The total project budget.<br>
C. The email addresses of all team members.<br>
D. The risk assessment report.
24. Which Excel function is used to return a number representing the day of the week for a specific date?<br>
A. =DAY()<br>
B. =TODAY()<br>
C. =WEEKDAY()<br>
D. =TEXT()
25. What is the purpose of using the TEXT function when creating a Gantt chart in Excel?<br>
A. To extract the first letter of the day of the week.<br>
B. To convert a date into a number.<br>
C. To apply conditional formatting to the chart.<br>
D. To convert the number returned by WEEKDAY() into a text representation like "Mon".
26. To apply a filter to a data table, what is the first step?<br>
A. Create a Pivot Table.<br>
B. Select the columns of data you want to add filters to.<br>
C. Use the VLOOKUP function.<br>
D. Enable the Solver Add-in.
27. In the VLOOKUP formula =VLOOKUP(E13, $B$5:$C$10, 2, FALSE), what does the value 2 signify?<br>
A. Return the value from the second worksheet.<br>
B. The lookup table has two rows.<br>
C. An exact match is required.<br>
D. Return the value from the second column of the range $B$5:$C$10.
28. The keyboard shortcut to add filters to selected columns is:<br>
A. Ctrl + F<br>
B. Ctrl + P<br>
C. Ctrl + Shift + L<br>
D. Ctrl + Alt + Delete
29. A user wants to create a drop-down list in cell A1 containing the options "Yes", "No", and "Maybe". Which feature should be used?<br>
A. Conditional Formatting with a custom rule.<br>
B. Data Validation set to allow a "List".<br>
C. A Pivot Table with a slicer.<br>
D. An IFS function in cell A1.
30. What is the purpose of using absolute references (e.g., $B$5:$C$10) for the table_array in a VLOOKUP function?<br>
A. To ensure the reference is updated when the formula is copied to other cells.<br>
B. To lock the table reference so it does not change when the formula is copied to other cells.<br>
C. To make the lookup faster.<br>
D. To allow for an approximate match.
31. A scatter plot is the most effective chart type for what purpose?<br>
A. Comparing parts of a whole.<br>
B. Showing the relationship between two numerical variables.<br>
C. Displaying categorical data horizontally.<br>
D. Tracking a single variable over time.
32. If an IFS statement has multiple conditions that are true for a given cell, which value will it return?<br>
A. The value corresponding to the last true condition.<br>
B. An error message.<br>
C. A combination of all true values.<br>
D. The value corresponding to the first true condition in the sequence.
33. Which function would be used to extract the letter "S" from the text "Sun"?<br>
A. =TEXT("Sun", "d")<br>
B. =LEFT("Sun", 1)<br>
C. =WEEKDAY("Sun")<br>
D. =MATCH("S", "Sun", 0)
34. A user sets up a Pivot Table and drags "Product" to Rows and "Units Sold" to Values. By default, what calculation will the Pivot Table show for "Units Sold"?<br>
A. Count of Units Sold<br>
B. Average of Units Sold<br>
C. Sum of Units Sold<br>
D. Max of Units Sold
35. What does the term "dependencies" mean in the context of Gantt charts?<br>
A. The budget allocated to each task.<br>
B. The resources assigned to the project.<br>
C. Links showing that one task must wait for another to start or finish.<br>
D. The key project deadlines or milestones.
36. In Solver, what is the role of a "constraint"?<br>
A. It defines the formula cell to be optimized.<br>
B. It specifies which cells the Solver can change.<br>
C. It sets a rule or limit that the solution must adhere to.<br>
D. It selects the algorithm used for solving.
37. A workbook is named (Starter-Workbook)-HW-A-Tour-of-Class-Resources.xlsx. What is the correct way to rename it for submission?<br>
A. HW-A-Tour-of-Class-Resources.xlsx<br>
B. (My-Name)-HW-A-Tour-of-Class-Resources.xlsx<br>
C. (My-Name)-HW.xlsx<br>
D. CCE 270 Assignment 1.xlsx
38. The MEDIAN function returns what value from a set of numbers?<br>
A. The average value.<br>
B. The most frequently occurring value.<br>
C. The middle value when the numbers are sorted.<br>
D. The sum of all values.
39. The range_lookup parameter in VLOOKUP is optional. If it is omitted, what value does Excel assume?<br>
A. FALSE<br>
B. TRUE<br>
C. 0<br>
D. An error is returned.
40. To find the "top 10" values in a dataset, which Excel feature would be most direct?<br>
A. A VLOOKUP function.<br>
B. The "Top/Bottom Rules" option within Conditional Formatting or Filtering.<br>
C. The Solver add-in.<br>
D. Creating a Pie Chart.


---


**Answer Key**

1. C
2. C
3. B
4. B
5. D
6. C
7. B
8. C
9. D
10. C
11. C
12. B
13. C
14. D
15. B
16. D
17. B
18. C
19. C
20. B
21. B
22. C
23. A
24. C
25. D
26. B
27. D
28. C
29. B
30. B
31. B
32. D
33. B
34. C
35. C
36. C
37. B
38. C
39. B
40. B


---


## Glossary of Key Terms

* Conditional Formatting: A feature in Excel that allows you to format cells based on certain conditions, making data easier to read and highlight.
* Data Validation: A feature that allows you to control the type of data entered into a cell, helping to prevent errors.
* Filtering: A feature that allows you to show only the data that meets certain criteria, hiding rows that do not match.
* Function: A preset formula in Excel that helps users analyze, manage, and compute data (e.g., SUM, AVERAGE).
* Gantt Chart: A type of bar chart used in project management that illustrates a project schedule, showing the start and finish dates of tasks.
* Goal Seek: A tool in Excel that automates a trial-and-error process to find a specific input value that results in a desired output from a formula.
* HLOOKUP: A function used for horizontal lookups, searching for a value in the top row of a table and returning a value from a specified row below it.
* IF Function: A logical function that returns one value if a specified condition is true and another value if it is false.
* IFS Function: A logical function that checks whether one or more conditions are met and returns a value corresponding to the first true condition.
* LEFT Function: A text function that returns a specified number of characters from the beginning of a text string.
* MATCH Function: A function that returns the relative position (index number) of an item in a range of cells.
* Pivot Table: A tool used to summarize, analyze, and explore large sets of data in more meaningful ways by rearranging rows and columns.
* Solver: A powerful Excel add-in that finds an optimal (maximum, minimum, or specific) value for a formula by adjusting multiple input cells and adhering to a set of constraints.
* TEXT Function: A function that converts a numeric value into text using a specified format code.
* VLOOKUP: A function used for vertical lookups, searching for a value in the first column of a table and returning a value from a specified column in the same row.
* WEEKDAY Function: A function that returns a number from 1 to 7 representing the day of the week for a given date.
