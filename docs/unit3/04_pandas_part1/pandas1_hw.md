#  HW: Pandas DataFrame

**Purpose:** In this assignment you are given a Google Sheet with different data. You will import the google sheet into your python code and use it to create pandas dataframes. You will then graph information from the different dataframes.

You will be using the following Google Sheet:

<a href="https://docs.google.com/spreadsheets/d/1W645cg4v6esPkslndyoU2jV31Y4Yg3Z5VT_JB3--t40/edit?gid=210801436#gid=210801436" target="_blank">
    <img src="https://miro.medium.com/v2/resize:fit:800/1*K_GFTHJpnGQ4YRhexggvHw.png" alt="Google Sheets" width="150"/>
</a>

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit3/04_pandas_part1/starter_sheet_pandas_part_1.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
2. Rename it something like "[Your Name] 3_4_Pandas-Part1_HW"

You will be using the following data set:
[ProvoRiverData](https://github.com/user-attachments/files/17669682/ProvoRiverData.csv)

---

### Creating and Formatting the DataFrame

1. Upload the Provo River Data csv file to your Python notebook.
2. Write appropriate import statements and read the file into a pandas dataframe.
   (remove any columns that have no data)
3. In the second code block display the table that pandas made.
4. In the third code block write code that will display a table like this:
   
![df_python](https://github.com/user-attachments/assets/f6726e28-0559-4b73-8d13-6883bf984877)

5. In the fourth code block find the shape of the initial data frame (how many columns and rows there are).
6. Display a summary of the Date/Time column. It should look something like this:
 
![python_df](https://github.com/user-attachments/assets/b494e31f-8f49-4a10-8fbf-c6ea8bafe1cc)


**extra credit (items 7-9 are extra credit)
7. In the fifth code block convert the Date/Time column to a date/time data type
8. Set the index to the date/time column
9. Show the dataframe header with the new index

**extra credit


10. In the sixth code block display the last 8 rows of the table.
11. In the seventh code block create a table that only shows flowrate over 100.
12. In the eighth code block create a table that only shows Approved Status 'P'.
13. Create a bar graph using matplotlib to compare how many approved statuses are 'P' v. 'A'. When you are done it should look like this:

![pandas_graph](https://github.com/user-attachments/assets/3e9ed32e-626f-4156-acc7-026143845f95)

    
4. Turn sharing, and editing on. Then turn in your link to Learning Suite.

---

# Turning In/Rubric

Turn on sharing and editing. Turn in the link to the Learning Suite feedback box. ONLY turn in the workbook. **You don't need to turn in the file you created. 
**

|                                **Item**                                | **Amount** |
|:----------------------------------------------------------------------:|:----------:|
|   First code block has import statements and uploads file correctly    |     5      |
|         Second code block displays the table that pandas made          |     2      |
|            Third code block displays flow rate data summary            |     2      |
| Fourth code block finds the shape of the table and summary of DateTime |     2      |
|                                  Fifth code block - display new index|  2 extra   |                                 
|      Fifth code block displays a summary of the Date/Time column       |     2      |
|         Sixth code block displays the last 8 rows of the table         |     2      |
| Seventh code block creates a table that only shows flowrates over 100  |     5      |
|     Eighth code block only displays data from Approved Status 'P'      |     5      |
|             Ninth code block displays bar graph correctly              |     5      |
|             <div style="text-align: right">**Total**</div>             |   **30**   |

The following is not apart of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                      **Reasons for Points Lost**                      | **Amount** |  
|:---------------------------------------------------------------------:|:----------:|
| No comments explaining why AI is used and what its provided code does |    2-3     |
|                        Link shared incorrectly                        |     3      |
|       Turned in late. 10% or 3 points for every week it's late.       |    3-15    |

