#  HW: While Loops

**Purpose:** Learn how to create a while loop.

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/05_while_loops/[Your_Name]_2_6_While_Loops_HW.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "[Your Name] HW 2.6 - While Loops"

In this assignment, you will be creating a while loop and using it to calculate the current capacity of a watershed based on a fixed avaporation rate and the amount of precipitation. You will also be counting the days it took for the watershed to either fill or dry up

---

   1. In the first code block, this is where the variables are going to be defined. In some cases, input statements will be used to test out different values. The variables should be defined as follows:

   | Variable                                     | Value                                           | Units      |
   |----------------------------------------------|-------------------------------------------------|------------|
   | Surface Area of Watershed (A)                | input statement                                 | acres      |
   | Max Height of Watershed (h)                  | input statement                                 | feet       |
   | Max Volume of Watershed (max)                | Surface Area * Max Height                       | acre-feet  |
   | Current Depth of the Water (d)               | input statement                                 | feet       |
   | Rate of Evaporation (evap)                   | 5                                               | inches/day |
   | Number of Days Elapsed (days)                | 0                                               | days       |
   | Current Capacity of the Watershed (capacity) | Current Depth * Surface Area / Max Volume * 100 | %          |

   2. In the second code block, this is where the while loop is going to be created, but first state the current capacity of the watershed. Write a print statement telling the current capacity of the watershed.

   3. Next, create a while loop that continues to loop under the condition that the current capacity is greater than or equal to 10%. This is the arbitrary threshold given. If the watershed reaches 10% or below, it is considered "dried up."

   4. After starting the while loop, create a new variable called precip and assign it an input statement asking about how much it rained today in inches.

   5. Now update the value for depth (d) with the previous depth plus this new value. Take the value for precipitation just defined by the input statement and subtract the rate of evaporation defined in the earlier code block. This gives the total additional rainfall for the day in inches. This new value will be added the previous depth (d) to give the new depth (d). Double check that the units are consistant.

   6. With this new depth calculate the new capacity using the same formula for capacity in the table. Then add 1 to the variable days, as one day has passed. Finally, print the new capacity of the watershed.

   7. The while loop should stop under two conditions. The first is if the watershed sinks below 10% capacity. This is covered in the initial conditions of our while loop. However, it is important for this assignment to know how long it took for the watershed to dry up. Create an if statement that prints the amount of days it took the watershed to dry up.

   8. The second stop condition is if the watershed fills completely (i.e reaches a capacity of 100% or greater). Create an if statement that prints the amount of days it took to fill the watershed and break the loop.

---

# Turning In/Rubric

Turn on sharing and editing. Turn in the link to the Learning Suite feedback box

|                            **Item**                               | **Amount** |  
|:-----------------------------------------------------------------:|:----------:|
| The variables are defined properly                                |           |
| The while loop is created under the correct first break condition |           |
| The input statements have a clear prompt string                   |           |
| The new total depth is calculated based on the old depth          |           |
| The function prints the correct statement for each outcome        |           |
| The function prints the days elapsed after each outcome           |           |
| the loop breaks under the second condition                        |           |
|         <div style="text-align: right">**Total**</div>            |   **30**   |
   
