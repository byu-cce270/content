# In Class Exercise: Pandas Grouping and Combining DataFrames

The following exercises will have you manipulate and combine different DataFrames from lists and external files. For this exercise, open the in-class workbook, make a copy, and follow the instructions. You can find the Colab notebook for the In Class Exercise here:

<a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit3/03_continuing_pandas/(Starter_Notebook)_Class_Continuing_with_Pandas.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

As part of this exercise, you will be asked to read the following Excel file into the in-class workbook and create Panda's dataframes. Download the file from this link.

[accidents.xlsx](data/accidents.xlsx)

After opening the notebook, drag and drop the files into the Colab file explorer on the left side of the notebook. It may be closed, but you can open it by clicking on the folder icon on the left side of the screen, to open the file explorer in Colab. 

This spreadsheet contains data on accidents from 2020 to 2022. You will be using these data to complete the exercises in the notebook. The spreadsheet contains columns for the date, Injury Location, Gender, Age Group, Incident Type, Days Lost, Plant, Report Type, Shift, Department, and Incident cost. We will be using the panda's `.groupby()` method to summarize and analyze these data. 

In addition to the accident data, we will be working with datetime data. We will  create datetime data using a datetime function and to create additional columns, such as month, day, etc. to  summarize the data.

## Instructions
1. Download the Excel data file from the link above
2. Open in-class notebook using the link above.
3. Rename the notebook to something like "(Your_Name)_Class_Continuing_with_Pandas.ipynb"
4. Drag and drop the downloaded file into the file explorer on the left side of the notebook.
5. Follow the instructions in the notebook to complete the exercise.
   
---
			
## Turning in/Rubric

**_REMINDER_** - For this class, **you will only turn in the links to your colab notebooks**. You will get a 0 for this assignment if you turn in a python file or a link that is not correct, wrong assignment, or does not give editor permission.

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