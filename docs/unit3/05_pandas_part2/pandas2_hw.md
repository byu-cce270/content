#  HW: Manipulating and Grouping Pandas DataFrames

**Purpose:** In this assignment you are given an Excel file for different excavation and grading equipment. You will upload the provided file to your Colab notebook and practice merging, grouping, and manipulating the data in Python. 

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit3/05_pandas_part2/starter_sheet_HW_2_Pandas.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
2. Rename it something like "[Your Name] 3_5_Pandas-Part2_HW"
3. In the code block titled "Imports and Authentication" input the correct import statements to connect to gspread. Also import:
    - matplotlib.pyplot as plt
    - pandas as pd
    - seaborn as sns
4. After authenticating yourself, open your google sheet in python using gspread.
5. In a new code block, write code to open the two different sheets into two seperate pandas dataframes.
    * Note: You can name the dataframes whatever you would like. For the purposes of these instructions the first sheet will be referred to as the resurface_df and the second sheet will be referred to as the pavement_df.
6. In a new code block, converte the "Date" column in the resurface_df to a date/time format.
7. Use the .dt.day_name() method in pandas to add a new column to the resurface_df that specifies what day of the week the resurfacing took place on.
8. Display the dataframe with the new column added.
9. In a new code block, use the .groupby() method to count the number of jobs under each borough for both milling and paving.

   When you are done, the dataframe that displays should look like this:

    ![groupby](https://github.com/user-attachments/assets/e52726c4-e0ef-4a37-b9f0-11a3d7028897)


10. In a new code block, create a new dataframe that finds that most common street names for paving jobs.
11. Rename the columns in your new dataframe to be 'Street Name' and 'Job Count'.

    When you are done, the dataframe that displays should look like this:

    ![streets](https://github.com/user-attachments/assets/9a9dcfd3-356e-44cb-9ce6-eb56b1beb9e4)

    
12. Starting in a new codeblock, assume that each shift for resurfacing last 8 hours. Add a work duration column to the resurface_df that has the value of 8 for each row.
13. Use the .groupby() method to determine the number of work hours completed by each community board.

    When you are done, the dataframe that displays should look like this:

    ![community hours](https://github.com/user-attachments/assets/d1e44013-40e5-4516-a9b9-0ce9622af326)

14. In a new code block, create a bar graph that displays the number of work jobs by borough. Include:
     - a title
     - x and y labels
     - horizontal gridlines
     - change the default colors

    When you are done, the graph should look something like this:

    ![pandas2](https://github.com/user-attachments/assets/3ae94a3c-c42f-4a7a-9116-689f3df53353)

15. In a new codeblock under the 'PAVEMENT RATING' text block create a dictionary to map the pavement_df boroughs.
     - X : Bronx
     - B : Brooklyn
     - M : Manhattan
     - Q : Queens
     - S : Staten Island
   
16. Map the BoroughCod column of the pavement_df to insert a new column titled "Borough" that includes the full name of the boroughs.
17. In a new code block, use the .groupby() method to sort the different ratings the boroughs have given out.

    When you are done, the data frame that displays should look like this:

    ![ratings](https://github.com/user-attachments/assets/9f6f0a59-18f6-4c4c-9a82-7555da13849d)

18. In a new code block, use the .groupby() method to display the average of the manual rating and count of the borough measurements by their inspection time, rating, and borough code.

    When you are done, the data frame that displays should look like this:

    ![df ratings](https://github.com/user-attachments/assets/d0a41271-d9bb-4f0d-8c85-47ac06657784)

19. In a new code block, use the query function to display a dataframe that includes only the strrts in poor condition evaluated by borough B.
20. In w new code block, create a pie chart that displays the pavement conditions by ratings. Include:
     - a title
     - change the default colors
   
    When you are done, the chart should look like this:

    ![pavement_rating](https://github.com/user-attachments/assets/b627382e-dc69-44ef-9401-2d9d70505ee6)

    
---

# Turning In/Rubric

Turn on sharing and editing. Turn in the link to the Learning Suite feedback box. ONLY turn in the workbook. **You don't need to turn in the file you created. 
**

|                      **Item**                       | **Amount** |
|:---------------------------------------------------:|:----------:|
|        Correct import statements used and file uploaded correctly        |     5      |
|        Tabs in the Excel file are loaded in separate data frames        |     3     |
|            Correct column names created with duplicates removed            |     3      |
|                Equipment age calculated correctly  |     3     |
|    Equipment and Productivity dataframes are merged into a new dataframe correctly  |     2     |
|  Correct columns with correct calculations are added to the merged dataframe  |     8      |
|              .groupby() is used to filter correctly  |     3      |
|   Bar graph displays correctly with titles, labels, and colors |     3      |
|   <div style="text-align: right">**Total**</div>    |   **30**   |

The following is not apart of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                      **Reasons for Points Lost**                      | **Amount** |  
|:---------------------------------------------------------------------:|:----------:|
| No comments explaining why AI is used and what its provided code does |    2-3     |
|                        Link shared incorrectly                        |     3      |
|       Turned in late. 10% or 3 points for every week it's late.       |    3-15    |
