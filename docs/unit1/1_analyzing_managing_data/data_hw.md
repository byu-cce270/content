#  HW: Analyzing & Managing Data

**Purpose:** This assignment tests your ability to manage and format data. You will filter data on different worksheets and use the data-management methods covered in class: conditional formatting, filters, and functions. The data are measurements taken from the Provo River. If you are interested in exploring more Provo River data, you can access them at this link:
[Provo River Data](https://waterdata.usgs.gov/monitoring-location/10163000/#parameterCode=00065&period=P7D){:target="_blank"}

---

## Getting Started

1. First, make a copy of the starter workbook here:
   [(Starter-Workbook)-HW-Analyzing-&-Managing-Data.xlsx](%28Starter-Workbook%29-HW-Analyzing-%26-Managing-Data.xlsx)
2. Remember to save it in the CCE 270 folder that you created in the first assignment.

Need a reminder about references such as `A1:F2883`? See [Cells and Formulas](../../resources/excel_review/basic_excel_review.md).

---

## Part 1 - Filtering Data

1. Navigate to the worksheet named “Streamflow Data Part 1.”
2. Select cells **A1:F2881** and add filters. A filter button should appear in each header cell from A1 through F1. Reformat the headers if needed so that they remain readable.
3. Filter the Approval Status column to show only rows with provisional status, `P`.
4. Duplicate that worksheet and rename it “Part 1 Approved Status.”
5. Return to the worksheet named “Streamflow Data Part 1.”
6. Reset the filter.
7. Filter the data by date. Show only rows with dates earlier than June 21, 2021; do not include June 21.
8. Duplicate that worksheet and rename it “Part 1 Date.”
9. Return to the worksheet named “Streamflow Data Part 1.”
10. Reset the filter.
11. Filter the data by Flowrate (CFS). Show rows with flow rates from 45 through 50, including both 45 and 50.
12. Duplicate that worksheet and rename it “Part 1 Flow Rate.”

At this point, you should have six worksheets in your workbook.

---

## Part 2 - Formatting Data

1. Navigate to the worksheet named “Streamflow Data Part 2.”
2. Format **A1:F2883** using colors, bold headers, and a clear, professional layout.
3. Apply a green-yellow-red color scale to **B4:B2883**: low values are green, middle values are yellow, and high values are red.
4. Apply conditional formatting to **C4:C2883** for values greater than 180.
5. Apply conditional formatting to **D4:D2883** for values equal to 230.
6. Apply a color scale to **E4:E2883**, with darker shading for lower values and lighter shading for higher values.
7. Apply conditional formatting to **F4:F2883** for entries that do not contain the digit 5.

---

## Part 3 - Summary Statistics

1. Navigate to the Summary Statistics worksheet.
2. Complete the CFS results in **C4:G9** using the measurements in cells **B4:F2883** on the **Streamflow Data Part 2** worksheet. In an Excel formula, that source range is written as `'Streamflow Data Part 2'!B4:F2883`; the exclamation point separates the worksheet name from the range. Match each data column to the station number shown in row 3. Use the appropriate functions, including `MODE` and `STDEV`. For this assignment, use `STDEV`, not `STDEV.S` or `STDEV.P`.
3. Engineers commonly express flow rates in cubic meters per second (CMS). Determine or confirm the factor for converting cubic feet (ft³) to cubic meters (m³); you may use AI. Select **C20** and name it `con_fac`. The name acts as a fixed reference, like `$C$20`, but makes a formula's purpose easier to read and debug.
4. Use `con_fac` to convert the CFS results in **C4:G9** to the corresponding CMS results in **C12:G17**.

---

## Turning in/Rubric


!!! note "Do not put your name or NetID in the file"
    Learning Suite records who submitted each file, so your name is not needed
    inside the file itself. Leaving it out means your work can be graded
    anonymously, which keeps grading fair. This applies to scans and photos
    too — please don't write your name on the page.

**_REMINDER_** - For this class, **you will upload your Excel file directly to Learning Suite**. Make sure the file you upload is for the correct assignment and contains your finished work.

1. Make sure your work is saved, then close the workbook so that all of your changes are written to the file.
2. Go to the assignment in Learning Suite and upload your `.xlsx` file as an attachment.
3. Double-check that the file you uploaded is the one that contains your completed work.

**Rubric:**

|                                                 Item                                                  | Points Possible |
|:-----------------------------------------------------------------------------------------------------:|:---------------:|
|                              HW file uploaded correctly the first time                               |        3        |
|           Part 1 - All sheets in the workbook are named as the instructions say to be named           |        3        |
|                            Part 1 - Approved Status is filtered correctly                             |        2        |
|                                 Part 1 - Date  is filtered correctly                                  |        2        |
|                               Part 1 - Flow Rate is filtered correctly                                |        2        |
|                         Part 2 -  Streamflow Data Part 2 is nicely formatted                          |        3        |
|                     Part 2 - Streamflow Data Part 2 columns are colored correctly                     |        3        |
|               Part 3 - Correct equations and data are used in the CFS half of the table               |        5        |
|                                  Part 3 - Cell name for C20 is made                                   |        2        |
| Part 3 - Correct equations, data, and use of the conversion factor reference are used in the CMS half |        5        |
|                            <div style="text-align: right">**Total**</div>                             |       30        |

---

The following is not a part of the rubric, but specifies how you can lose points. For example: if you fail to upload your file correctly.

| **Reasons for Points Lost** |    **Amount**     |  
|:---------------------------:|:-----------------:|
|  File uploaded incorrectly  |       -10%        |
|  Turned in late (per week)  | -10% (up to -50%) |
