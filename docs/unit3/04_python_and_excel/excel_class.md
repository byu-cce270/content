# In Class Excersise: Working with Excel Files in Python

In this class exercise, we will learn how to work with Excel files in Python. We will read Excel files into pandas dataframes, write dataframes to Excel files, and perform some basic data manipulation tasks. To begin, download the starter notebook here.

<a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit3/04_python_and_excel/(Starter_Notebook)_Class_Python_and_Excel.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Rename it '**(Your_Name)_Class_Python_and_Excel.ipynb'**. Then follow the instructions below. Create and organize your code in cells in the notebook as you go.

## Part 1: Provo River Streamflow Data

In Unit 1, we worked with a set of streamflow data from gauges on the Provo River. In this exercise, we will import a copy of that data in Excel format, perform some data analysis, and write the results back to a new Excel file.

1. Download the Excel file from [streamflow_data.xlsx](streamflow_data.xlsx).
2. Follow the instructions for Part 1 in the notebook.

When finished, Your Excel file should look similar to the one below:

![Streamflow Excel File](images/streamflow_screenshot.png)

**EXTRA**

If you get it done early, here are some things you can play with:

1) When you export the dataframe, it applies a default datetime style. If you try to format the column later with a proper "yyyy-mm-dd" format, it does not override the default date format. There are number of ways to fix that. See if you can figure that out with the help of AI.
2) Change the zoom level on the sheet
3) Experiment with cell formatting (widths, fonts, background colors, etc.)

## Part 2: Accident Database Analysis

In this part of the exercise, we will work with a dataset of workplace accidents that we used in Unit 1. We will read the data from an Excel file, perform some data analysis, and write the results back to a new Excel file along with some column charts.

1. Download the Excel file from [accident_database.xlsx](accident_database.xlsx)
2. Follow the instructions for Part 2 in the notebook.

When finished, Your Excel file should look similar to the one below:

![acc_type_sheet.png](images/acc_type_sheet.png)
![acc_day_sheet.png](images/acc_day_sheet.png)

If you get it done early, here are some things you can play with:

1) Turn off the display of the grid lines in the background. 
2) Change the zoom level on each sheet
3) See if you can figure out how to have bold lines on cells containing data, but none of the other cells. This is a little tricky, but there is a way to do it. 

---
			
## Turning in/Rubric

**_REMINDER_** - For this class, **you will only turn in the links to your Colab notebooks**. You will get a 0 for this assignment if you turn in a python file or a link that is not correct, wrong assignment, or does not give editor permission.

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