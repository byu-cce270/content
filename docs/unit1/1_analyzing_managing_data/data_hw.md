#  HW: Analyzing & Managing Data

**Purpose:** This assignment aims to test your ability to manage and format data. In this assignment, you will filter out certain types of data in different sheets. You will use the different ways of managing data that we went over in class: Conditional formatting, filters, and functions. The data we will be using is measurements taken from the Provo River. If you are interested in looking at more data from the Provo River you can access it at this link:
[Provo River Data](https://waterdata.usgs.gov/monitoring-location/10163000/#parameterCode=00065&period=P7D){:target="_blank"}

---

## Getting Started

1. First, make a copy of the starter sheet here: 
   [(Starter-Workbook)-HW-Analyzing-&-Managing-Data.xlsx](%28Starter-Workbook%29-HW-Analyzing-%26-Managing-Data.xlsx)
2. Rename it something like “(Your-Name)-HW-Analyzing-&-Managing Data”
3. Remember to save it in your OneDrive folder that you created in the first assignment.

---

## Part 1 - Filtering Data

1. Navigate to the sheet that says “Streamflow data Part 1”
2. Select the entire table and create a filter, the filter icon should be in each of the headers. Be sure to reformat the headers so that they can still be read.
3. Filter by Approved status so it only shows rows with the approved status as pending, "P"
4. Duplicate that sheet and rename it: “Part 1 Approved Status”
5. Go back to the sheet called "Streamflow data Part 1"
6. Reset the filter
7. Next, filter the data by date. Only show rows of data that were taken before 6/21/21
8. Duplicate that sheet and rename it “Part 1 Date”
9. Go back to the sheet called "Streamflow data Part 1"
10. Reset the filter
11. Next, filter the data by Flowrate (CFS). Only show the rows whose flow is between 45 - 50
12. Duplicate that sheet and rename it “Part 1 Flow Rate”

At this point, you should have 6 sheets in your workbook.

---

## Part 2 - Formatting Data

1. Navigate to the sheet that says “Streamflow Data Part 2”
2. Format the table using colors, bold the headers, and make it look nice.
3. Give the data in column B a scaled color scheme that will have the low numbers be green the high numbers be red and the middle numbers be yellow
4. Give the data in column C a color if it is greater than 180
5. Give the data in column D a color if it is equal to 230
6. Give the data in column E a scaled color where the lower numbers are the darker version of the color and the higher numbers are the lighter version of that color
7. Give the data in column F a color if the text does not contain a 5

---

## Part 3 - Summary Statistics

1. Navigate to the Summary Statistics sheet.
2. On this page, you will see spots to use formulas to summarize the data taken at different places on the river (or stations). Use the appropriate formula and data from your “Streamflow data Part 2” sheet to make those calculations in the top half of the table.
3. Most engineers when making calculations use cubic meters per second (CMS). Under the main table, name the cell C20 to "con_fac" to create an absolute cell reference for the conversion factor.
4. Use the conversion factor reference we just made to convert all the values in the top half of the table from cfs to cms.

---

## Turning in/Rubric

**_REMINDER_** - For this class, **you will only turn in the links to your Excel files**. You will get a 0 for this assignment if you turn in an Excel file or a link that is not shareable. 

1. On the top right, click the share button --> share --> settings
2. Click "anyone" at the top, then underneath "More settings", change "can view" to "can edit". Then click apply. 
3. Copy the link, then turn it into Learning Suite in the feedback box for that assignment.

**Rubric:**

|                                                 Item                                                  | Points Possible |
|:-----------------------------------------------------------------------------------------------------:|:---------------:|
|                              HW link turned in correctly the first time                               |        3        |
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

The following is not apart of the rubric, but specifies how you can lose points. For example: if you fail to share your link correctly.

|                **Reasons for Points Lost**                | **Amount** |  
|:---------------------------------------------------------:|:----------:|
|                  Link shared incorrectly                  |     3      |
| Turned in late. 10% or 3 points for every week it's late. |    3-15    |

