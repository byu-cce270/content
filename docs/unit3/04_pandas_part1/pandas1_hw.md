#  HW: Pandas DataFrame

**Purpose:** In this assignment you are given a Google Sheet with different data. You will import the google sheet into your python code and use it to create pandas dataframes. You will then graph information from the different dataframes.

You will be using the following Google Sheet:  

<a href="https://docs.google.com/spreadsheets/d/1W645cg4v6esPkslndyoU2jV31Y4Yg3Z5VT_JB3--t40/edit?gid=210801436#gid=210801436" target="_blank">
    <img src="https://miro.medium.com/v2/resize:fit:800/1*K_GFTHJpnGQ4YRhexggvHw.png" alt="Google Sheets" width="100"/>
</a>

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit3/04_pandas_part1/starter_sheet_pandas_part_1.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
2. Rename it something like "[Your Name] 3_4_Pandas-Part1_HW"
3. In the code block titled "Imports and Authentication" input the correct import statements to connect gspread. Also import:
    - matplotlib.pylot as plt
    - numpy as np
    - pandas as pd
    - seaborn as sns
4. After inputting the correct input statements, open your google sheet under the comment titled "Read in your Google Sheet here"

---

### Creating and Formatting the DataFrames

1. Under the code block titled "Create DataFrames", write the appropriate code to turn the three sheets of the Google Sheet into dataframes. When you are done you should have a bridge dataframe, traffic dataframe, and concrete dataframe.
2. Under the text block titled "BRIDGE DATAFRAME" filter the bridge dataframe into a new dataframe that only includes bridges in critical condition.
3. Display the dataframe you just created.
4. The next code block includes code that is given to you. It takes the bridge age data from the dataframe and converts the numbers into actual dates so we can perform analysis on the numbers.
5. Under the line given, use the .groupby() method to display an average bridge age based on the condition the bridges are in. If you've done everything correctly the following should display:
   
![bridge df](https://github.com/user-attachments/assets/242fefdb-276f-496d-957c-11597bd3d5ca)

6. In a new code block, write code to display a bar graph of the number of bridges there are based on their condition rating. Include:
    - x and y labels
    - a title
    - change the default color scheme

    When you are finished your bar graph should look something like this:
   
![bridge bar graph](https://github.com/user-attachments/assets/fb37f510-746b-4aaa-84c8-70a683ea64c7)

7. Under the text block titled "TRAFFIC DATAFRAME", write code to display a bar graph of the count of congestion levels throughout the day. Include:
    - a title
    - x and y labels
    - change the default color scheme

    When you are finished your bar graph should look something like this:
   
![count of congestion](https://github.com/user-attachments/assets/043a47ea-d73b-41c3-b4a4-fb13d42c769a)

8. Under the text block titled "CONCRETE DATAFRAME", write code to sort the dataframe by the 'Age (day)' column.
9. Display the sorted dataframe.
10. In a new code block, write a function with one parameter that returns "Early Strength" if it has been less than 7 days, "Medium Strength" if it has been less than 28 days, and "Long-Term Strength" if it has been longer than 28 days.
11. Using the .apply method with the function you just created on the 'Age (day)' column in your dataframe, add a new column to your dataframe called "Age Category" that includes whether the concrete measurement is early, medium, or long-term strength.
12. In a new codeblock, use .describe() to find the statistics of your dataframe.
13. In a new codeblock, create a new dataframe by grouping the compressive strength of the concrete by the age catgeory column you created in step 11. When you display the new dataframe, it should look something like this:
    
    ![concrete strength](https://github.com/user-attachments/assets/7edd177a-c47d-48a4-baef-fce9c2602729)

14. In a new codeblock, write code to display a scatter plot that compares the compressive strength of the concrete with its cement content. Include:
     - a title
     - x and y labels
     - change the default color
     - change the marker from the default circle marker
   
    When you are finished your scatter plot should look something like this:

    ![scatter plot](https://github.com/user-attachments/assets/afa9b630-6990-48ae-be4c-c58cb69ad2e2)

15. In a new codeblock, write code to display a boxplot that compares the compressive strength for each age category. Include:
     - a title
     - x and y labels
     - change the default color

    When you are finished your boxplot should look something like this:
    
    ![boxplot](https://github.com/user-attachments/assets/1abbd39f-c61e-4d36-bd23-37f75c62b0d7)

16. For extra credit, create a heatmap that looks like the following:

    ![heatmap](https://github.com/user-attachments/assets/b937857d-eca3-4be5-9298-9f80d3200d65)

17. Turn sharing, and editing on. Then turn in your link to Learning Suite.

---

# Turning In/Rubric

Turn on sharing and editing. Turn in the link to the Learning Suite feedback box. 
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

