#  HW: While Loops

**Purpose:** Learn how to create a While loop.

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/05_while_loops/[Your_Name]_2_6_While_Loops_HW.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "[Your Name]_While_Loops_Homework"

In this assignment, you will be creating a while loop and using it to calculate the current capacity of a watershed based on a fixed evaporation rate and the amount of precipitation. You will also be counting the days it took for the watershed to either fill or dry up

---

   1. In the first code block, this is where the variables are going to be defined. You will need to replace the default assignment statements in the code block with default values, formulas, or input statements as outlined in the following table: 

|  Variable   | Description                       |       Units       |      Source/Value      |
|:-----------:|-----------------------------------|:-----------------:|:----------------------:|
|      A      | Surface area of watershed         |       acres       |    input statement     |
|      h      | Max height of watershed           |       feet        |    input statement     |
|     max     | Max capacity (volume) of watershed |     acre-feet     |         A * h          |
|      d      | Current depth of the water        |       feet        |    input statement     |
|    evap     | Rate of evaporation               |    inches/day     |           5            |
|    days     | Number of days elapsed            |       days        |           0            |
|  capacity   | Current capacity (volume) of the watershed |         %         |   100 * d * A / max  |


   2. In the second code block, this is where the while loop is going to be created, but first state the current capacity of the watershed. Write a print statement telling the current capacity of the watershed.

   3. Next, create a while loop that continues to loop under the condition that the current capacity is greater than or equal to 10%. This is the arbitrary threshold given. If the watershed reaches 10% or below, it is considered "dried up."

   4. After starting the while loop, create a new variable called precip and assign it an input statement asking about how much it rained today in inches.

   5. Now update the value for depth (d) with the previous depth plus this new value. Take the value for precipitation just defined by the input statement and subtract the rate of evaporation defined in the earlier code block. This gives the total additional rainfall for the day in inches. This new value will be added to the previous depth (d) to give the new depth (d). Double-check that the units are consistent.

   6. With this new depth calculate the new capacity using the same formula for capacity in the table. Then add 1 to the variable days, as one day has passed. Finally, print the new capacity of the watershed.

   7. The while loop should stop under two conditions. The first is if the watershed sinks below 10% capacity. This is covered in the initial conditions of our while loop. However, it is important to know how long it took for the watershed to dry up. Create an if statement that prints the amount of days it took the watershed to dry up.

   8. The second stop condition is if the watershed fills completely (i.e reaches a capacity of 100% or greater). Create an if statement that prints the amount of days it took to fill the watershed and break the loop.

---

#### Test Code

If you'd like to check your code so that it is working properly, run the first code block and enter these values:

* Watershed Area = 10 acres 
* Watershed Height = 10 feet 
* Water Depth = 5 feet

Next, run the second code block and enter these values for precipitation:

* 23, 14, 2, 17, 8, 26

You should get an output that looks something like this:

![HW_2_6_Example_1_1.png](images/HW_2_6_Example_1_1.png)
![HW_2_6_Example_1_2.png](images/HW_2_6_Example_1_2.png)

# Turning In/Rubric

Turn on sharing and editing. Turn in the link to the Learning Suite feedback box

|                             **Item**                              | **Amount** |  
|:-----------------------------------------------------------------:|:----------:|
|                The variables are defined properly                 |     6      |
| The input statements have a clear prompt string                   |     6      |
| The function prints the correct statement for each outcome        |     6      |
| The while loop is created under the correct first break condition |     3      |
| The new total depth is calculated based on the old depth          |     3      |
| The function prints the days elapsed after each outcome           |     3      |
| The loop breaks under the second condition                        |     3      |
|         <div style="text-align: right">**Total**</div>            |   **30**   |

The following is not apart of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                      **Reasons for Points Lost**                      | **Amount** |  
|:---------------------------------------------------------------------:|:----------:|
| No comments explaining why AI is used and what its provided code does |    2-3     |
|                        Link shared incorrectly                        |     3      |
|       Turned in late. 10% or 3 points for every week it's late.       |    3-15    |
   
