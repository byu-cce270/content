# HW: Matplotlib

**Purpose:** Learn how to read in data from Google Sheets and make graphs from it

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit3/01_matplotlib/(Starter_Notebook)_HW_Matplotlib.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "[Your Name] HW 3.1 - Matplotlib"

3. Open the Google Sheet used for this homework here:

[HW Matplotlib Data Sheet](https://docs.google.com/spreadsheets/d/1byVuW2RiFN-AOvD6cf4oMuJk2NeHpZ7eQd9x-Xven-s/edit?usp=sharing){:target="_blank"}

In this assignment, you will be creating graphs of historical weather data in Pasadena, CA, Provo River flowrate data, and U.S. Birth Rates.

---

#### Connecting to Google Sheets

1. Connect the Google Sheets workbook to the Colab notebook
2. Create three separate variables **temp_data**, **stream_data**, and **birth_data** that connect to their related worksheets. For example, the **temp_data** variable should connect to the worksheet titled "Pasadena Precipitation Data", the **stream_data** variable should connect to the worksheet titled "Provo River Streamflow Data," etc.
   
#### Part 1 - Pasadena Precipitation Data

In Part 1, you will be graphing the temperature data from Pasadena, CA. The data is from 2013-2014 and includes the high and low temperatures for each day. We added the numpy code to create the data arrays for you to make plotting easier. We created an array for the x-data called ```x```, an array for the high temperature data called ```y_1```, and an array for the low temperature data called ```y_2```. You will need to plot the data as lines, add labels, titles, and other elements to make the graph look nice. You will  need to rotate the x-axis ticks so they are readable. Add a legend to the graph and grid lines and change the font size.

1. In the 'Graphing the Data' code block, three lists are referenced from the 'Numpy Array Creation & Slicing' block above. These are 'x', 'y_1', and 'y_2'
2. Plot y_1, label it "High Temperature", and color it orange or red
3. Plot y_2, label is "Low Temperature", and color it teal or blue
4. Title the graph "Pasadena Temperature Data 2013-2014"
5. Label the x-axis as "Date"
6. Label the y-axis as "Degrees (Fahrenheit)"
7. Using the xticks function, rotate the ticks by 45 degrees
8. Create a legend and put it in the lower left corner. Make the font size 10
9. Give the graph grid lines
10. Show the graph - it should look something like this:

    ![pasadenagraph.png](images/pasadenagraph.png)

#### Part 2 - Provo River Streamflow Data

In Part 2, we have provided numpy code to create the varables for the Provo River Streamflow Data. We created an array for the x-data called ```x```, and arrays for the streamflow data for five different sites called ```y_1```, ```y_2```, ```y_3```, ```y_4```, and ```y_5```. You will need to plot the data as lines, add labels, titles, and other elements to make the graph look nice. You will need to rotate the x-axis ticks so they are readable. Add a legend to the graph and grid lines and change the font size.

1. In the 'Graphing the Data' code block, three lists are referenced from the 'Numpy Array Creation & Slicing' block above. These are 'x', 'y_1', 'y_2', 'y_3', 'y_4', and 'y_5'
2. Plot y_1, label it "10163000" and color it purple
3. Plot y_2, label it "10155200" and color it teal or blue
4. Plot y_3, label it "10155500" and color it green
5. Plot y_4, label it "10154200" and color it orange
6. Plot y_5, label it "10155000" and color it orange-red or red
7. Title the graph "Provo River Streamflow Data (2021)"
8. Label the x-axis as "Date/Time"
9. Label the y-axis as "Flowrate (cfs)"
10. Using the xticks function, rotate the ticks by 45 degrees
11. Create a legend in the top right corner, make the font size 10, and title it "Site Numbers"
12. Give the graph grid lines
13. Show the graph - it should look something like this:

    ![streamflowgraph.png](images/streamflowgraph.png)

#### Part 3 - Average U.S. Daily Birth Data
Part 3 is similar, we give you numpy code to create the plotting variables similar to the last two plots. However, this time we want you to annotate some interesting data in the graph. We give you a list of dates to annotate with their holiday names. We used a number of different arrow styles to show you some options. The pre-class reading has a link to the documentation for the annotate function with some examples of different arrow properties you can use. You don't need to match our arrow styles, but you should use the annotate function to point to the holidays.

After you annotate the graph, we ask you to explain the drop in birth rates on those days? You don't have to know the answer, but you should be able to make a guess based on the data. **These are real data** not made up for the assignment.

1. In the 'Graphing the Data' code block, three lists are referenced from the 'Numpy Array Creation & Slicing' block above. These are 'x' and 'y_1'.
2. Plot y_1 and give it a color of your choice
3. Title the graph "Average U.S. Daily Birth Data"
4. Label the x-axis as "Date"
5. Label the y-axis as "Births"
6. Using the xticks function, rotate the ticks by 45 degrees
7. Give the graph gridlines
8. Annotate the chart with arrows that point to and label the following holidays:

&nbsp;&nbsp;&nbsp;&nbsp;New Year’s Day (2012-01-01)

&nbsp;&nbsp;&nbsp;&nbsp;Independence Day (2012-07-04)

&nbsp;&nbsp;&nbsp;&nbsp;Halloween (2012-10-31)

&nbsp;&nbsp;&nbsp;&nbsp;Thanksgiving (2012-11-27)

&nbsp;&nbsp;&nbsp;&nbsp;Christmas (2012-12-25)

10. Show the graph - it should look something like this:

    ![birthgraph.png](images/birthgraph.png)

11. Write a comment explaining why you think the birth rate drops during those days

---

# Turning In/Rubric

Turn on sharing and editing. Turn in the link to the Learning Suite feedback box

|                **Item**                              | **Amount** |  
|:----------------------------------------------------:|:----------:|
|         Google Sheets is connected correctly         |     3      |
|  The temperature data graph has all listed elements  |     8      |
|   The streamflow data graph has all listed elements  |     8      |
|     The birth data graph has all listed elements     |     8      |
|        The annotations are created correctly         |     3      |
|     <div style="text-align: right">**Total**</div>   |   **30**   |

The following is not a part of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                      **Reasons for Points Lost**                      | **Amount** |  
|:---------------------------------------------------------------------:|:----------:|
| No comments explaining why AI is used and what its provided code does |    2-3     |
|                        Link shared incorrectly                        |     3      |
|       Turned in late. 10% or 3 points for every week it's late.       |    3-15    |
