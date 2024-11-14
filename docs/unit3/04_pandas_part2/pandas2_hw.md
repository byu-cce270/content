#  HW: Manipulating and Grouping Pandas DataFrames

**Purpose:** In this assignment you are given an Excel file for different excavation and grading equipment. You will upload the provided file to your Colab notebook and practice merging, grouping, and manipulating the data in Python. 

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit3/03_pandas_part1/hw_startersheet_pandas_part1.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
2. Rename it something like "[Your Name] 3_5_Pandas-Part2_HW"

You will be using the following data set:
[Productivity Data - Pandas Part 2](https://github.com/user-attachments/files/17743998/productivity-part2pandas.1.xlsx)

3. In the first code block, import the necessary modules.
4. Load the excel file into the notebook. Hint: this is just like we did in class.
5. Load the data from the equipment and productivity sheets in the excel file into seperate dataframes.
6. Standardize the column names by making them lowercase and removing any extra spaces.
7. Remove any duplicate rows using .drop_duplicates().
8. Display the data to make sure everything is correct.
9. To calculate the equipment age, convert the 'year purchased' column to a datetime format using the .to_datetime() command.
10. Calculate the current age of the equipment by subtracting the year purchased from the year 2024.
11. Merge the equipment and productivity dataframes on the common column 'equipment id'.
12. Filter out rows where no hours were used.
13. You will now add the following columns to your merged dataframe using the following formulas:

|    **New Column Name**                | **Formula** |
|:---------------------------------------------------:|:----------:|
|       efficiency (cubic yards/hour)         |     soil moved (cu yds) / hours used      |
|   fuel efficiency (cubic yards/gallon)    |     soil moved (cu yds) / fuel consumed (gallons)|
|          total cost ($)         |     hourly rate * hours used      |
|          cost per cubic yard ($)        |     total cost ($) / soil moved (cu yds)      |
    
14. Verify the columns were added correctly by printing a .head() of only the newly added columns.
15. Using the .groupby() method, compute the following:

|    **New Column Name**                | **Formula** |
|:---------------------------------------------------:|:----------:|
|       efficiency (cubic yards/hour)         |     soil moved (cu yds) / hours used      |
|   fuel efficiency (cubic yards/gallon)    |     soil moved (cu yds) / fuel consumed (gallons)|
|          total cost ($)         |     hourly rate * hours used      |
|          cost per cubic yard ($)        |     total cost ($) / soil moved (cu yds)      |

---

    
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
