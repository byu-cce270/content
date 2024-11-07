#  HW: Manipulating and Grouping Pandas DataFrames

**Purpose:** In this assignment you are given an excel file for some EPA Highway Data. 
You will download the file and create a DataFrame out of the data provided, then manipulate, combine, and perform calculations on the DataFrames as instructed. 

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit3/03_pandas_part1/hw_startersheet_pandas_part1.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
2. Rename it something like "[Your Name] 3_5_Pandas-Part2_HW"

You will be using the following data set:

[Drive Cycles Data](https://github.com/user-attachments/files/17670334/HW.3.3.Drive.cycles.KEY.xlsx)

---

### Creating and Formatting the DataFrame

1. Upload the Drive Cycles Data excel file to your Python notebook.
2. Write appropriate import statements to read each separate tab in the spreadsheet into its own pandas dataframe.
3. Rename the pandas dataframes for EPA_HWY, EPA_CTY, and US_06 so they are useable as their own dataframe.
4. Add a column called 'cycle' to the three dataframes just renamed and store the different cycle names in the column.
   * Hint: make sure they are spelled exactly the same as they are in the grade tab on the excel file (they will be merged later).
5. Stack the different cycles into one DataFrame called cycles.
6. Add a new column to the new cycles dataframe by calculating speed in units of meters/sec.
7. Calculate acceleration in meters/s^2 in a new column in the cycles dataframe.
     * Hint: Calculate acceleration as the change of speed over each second.
     * accel = (change in speed)/(change in time) = (speed(t)=speed(t-1)/(1-sec)
     * use the pandas .diff function, you can read more [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.diff.html)
8. Read the grade tab from the spreadsheet into a dataframe.
9. Create a new dataframe called cycle_power by merging the grade to the cycles dataframe by the cycle name.
    * 



    
11. Turn sharing, and editing on. Then turn in your link to Learning Suite.

---

# Turning In/Rubric

Turn on sharing and editing. Turn in the link to the Learning Suite feedback box. ONLY turn in the workbook. **You don't need to turn in the file you created. 
**

|                      **Item**                       | **Amount** |
|:---------------------------------------------------:|:----------:|
|        First code block has import statements and uploads file correctly        |     5      |
|        Second code block displays the table that pandas made        |     3     |
|            Third code block displays flow rate data summary            |     2      |
|  Fourth code block finds the shape of the table  |     2      |
|  Fifth code block displays a summary of the Date/Time column  |     2     |
|  Sixth code block displays the last 8 rows of the table  |     2     |
|  Seventh code block creates a table that only shows flowrates over 100  |     3      |
|  Eighth code block only displays data from Approved Status 'P'  |     6      |
|  Ninth code block displays bar graph correctly  |     5      |
|   <div style="text-align: right">**Total**</div>    |   **30**   |

The following is not apart of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                      **Reasons for Points Lost**                      | **Amount** |  
|:---------------------------------------------------------------------:|:----------:|
| No comments explaining why AI is used and what its provided code does |    2-3     |
|                        Link shared incorrectly                        |     3      |
|       Turned in late. 10% or 3 points for every week it's late.       |    3-15    |
