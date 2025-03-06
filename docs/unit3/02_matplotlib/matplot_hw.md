# HW: Matplotlib

**Purpose:** Learn how to read in file data (.csv) and make graphs from it

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit3/01_matplotlib/matplotlib_hw.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "[Your Name] HW 3.1 - Matplotlib"

3. Open the Google Sheet used for this homework here:

[HW Matplotlib Data Sheet](https://docs.google.com/spreadsheets/d/1byVuW2RiFN-AOvD6cf4oMuJk2NeHpZ7eQd9x-Xven-s/edit?usp=sharing){:target="_blank"}

In this assignment, you will be creating graphs of historical weather data in Pasadena, CA, Provo River flowrate data, and U.S. Birth Rates.

---

#### Part 1

1. In the first code block, create a variable 'x' with an empty list. Do this two more times on separate lines with a list 'y_1' and 'y_2'
2. Read in the Pasadena CSV file in reading mode. Create an appropriately named variable and pass the file through the 'csv.reader', then skip the header row using the 'next()' function with the variable as its parameter
3. Write a for loop referencing your csv file variable. Within the for loop, append each of your lists with the information from each column
<br>&nbsp;&nbsp;&nbsp;&nbsp;**Hint**: Use float inside your append function for y_1 and y_2, as most of this data does not include whole numbers
4. Plot y_1, label it "High Temperature", and color it orange or red
5. Plot y_2, label is "Low Temperature", and color it teal or blue
6. Title the graph "Pasadena Temperature Data 2013-2014"
7. Label the x-axis as "Date"
8. Label the y-axis as "Degrees (Fahrenheit)"
9. Using the xticks function, input the list below into the first parameter and in the second parameter, rotate the ticks by 45 degrees

    ```[0,50,100,150,200,250,300,350]```

10. Create a legend and put it in the lower left corner. Make the font size 10
11. Give the chart grid lines
12. Show the chart

#### Part 2

1. In the second code block, create a variable 'x' with an empty list. Do this five more times on separate lines with lists 'y_1', 'y_2', 'y_3', 'y_4', and 'y_5'
2. Read in the Provo River Streamflow CSV file and create a for loop just like you did in Part 1
3. Plot y_1, label it "10163000" and color it purple
4. Plot y_2, label it "10155200" and color it teal or blue
5. Plot y_3, label it "10155500" and color it green
6. Plot y_4, label it "10154200" and color it orange
7. Plot y_5, label it "10155000" and color it orange-red or red
8. Title the graph "Provo River Streamflow Data (2021)"
9. Label the x-axis as "Date/Time"
10. Label the y-axis as "Flowrate (cfs)"
11. Using the xticks function, input the list below into the first parameter and rotate the ticks by 45 degrees in the second parameter

     ```[0,500,1000,1500,2000,2500]```

12. Create a legend in the top right corner, make the font size 10, and title it "Site Numbers"
13. Give the chart grid lines
14. Show the chart

---

# Turning In/Rubric

Turn on sharing and editing. Turn in the link to the Learning Suite feedback box

|                        **Part 1 Items**                         | **Amount** |  
|:---------------------------------------------------------------:|:----------:|
|                     Empty lists are created                     |     1      |
|                     Read in file correctly                      |     3      |
|              For loop and list appends are correct              |     3      |
|                  Graph is formatted correctly                   |     8      |
|         <div style="text-align: right">**Total**</div>          |   **15**   |


|                **Part 2 Items**                | **Amount** |  
|:----------------------------------------------:|:----------:|
|            Empty lists are created             |     1      |
|             Read in file correctly             |     3      |
|     For loop and list appends are correct      |     3      |
|          Graph is formatted correctly          |     8      |
| <div style="text-align: right">**Total**</div> |   **15**   |

The following is not apart of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                      **Reasons for Points Lost**                      | **Amount** |  
|:---------------------------------------------------------------------:|:----------:|
| No comments explaining why AI is used and what its provided code does |    2-3     |
|                        Link shared incorrectly                        |     3      |
|       Turned in late. 10% or 3 points for every week it's late.       |    3-15    |
