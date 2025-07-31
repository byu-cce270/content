# In-Class Exercise: Graphing and Solver

We will practice graphing and using the Solver function in Excel. The data we will use is an expanded edition of the 
preclass construction surplus store. You can 
access the data here: [(Your Name)-Class-Graphing-and-Solver.xlsx](%28Your%20Name%29-Class-Graphing-and-Solver.xlsx)
{:target="_blank"}

Make sure to rename the starter sheet something like “[Your Name]-Class-Graphing-and-Solver.”

---
## Exercise #1- Graphing Sales Data 

This data contains information about specific sales, including the date, region, product, sales 
associate and more. You are tasked with creating various graphs to visualize the data. Make sure that each chart is created on **its own 
sheet** and is titled appropriately. Each chart should have the x and y-axis labeled and have a legend. 

1. Navigate to the first sheet in the data workbook,"Construction_Sales" which is the data that we will be graphing.
2. Try to make a pie chart that shows the total sales by product. You can use the **Insert** tab in Excel to create 
a chart. 
3. Your boss wants to know the relationship between quality sold and revenue. Make a scatter plot that shows the units 
   sold vs total 
   sales. Does higher quantity sales lead to higher revenue?
4. Create a bar graph that shows the average total sales by region. With this graph, we are looking to see which 
   regions are performing the best in terms of sales.
5. Make a line graph that shows the total monthly sales trend over time. (Include a trendline to show the overall trend.) 
   This will help us understand how sales are changing over time.

The goal of this exercise is to practice creating different types of graphs in Excel and to understand how to visualize data effectively, so feel free to experiment with different colors and styles! 

---
## Exercise #2- Using Solver in Excel (with Goal Seek)

Navigate to the second sheet in the Graphing-and-Solver workbook, "Parabola-Solver", which is designed to solve a 
quadratic 
equation 
using Excel's Solver function.

This sheet is designed to solve a quadratic equation of the form:

$y = ax^2 + bx + c$

The user enters the coefficients a, b, & c in cells C4:C6. For the case shown above, we are solving:

$y = x^2 - 3x + 1$

The chart at the bottom is used to graph the parabola corresponding to the equation over a specified range. The 
solution to the equation is the two points where the parabola intercepts the y-axis. These are called the "roots" and represent the solution to:

$ax^2 + bx + c = 0$

As can be seen on the chart, the roots are approximately 0.4 and 2.6. We can find the roots using cells F4 and F5. We enter a value for x in cell F4. The corresponding value of y is computed in cell F5 as:

**=C4*F4$^2$+C5*F4+C6**

To find a root, we can enter a guess (0.4 for starters) into F4 and iteratively tweak that number until the value 
computed for y in F5 is roughly equal to zero. While this works, it can be time-consuming and tedious.

1. Solve for one of the roots of the parabola using **Solver.**
2. Find the x location corresponding the lowest point on the parabola.

---

## Turning in/Rubric

**_REMINDER_** - For this class, **you will only turn in the links to your Excel files**. You will get a 0 for this assignment if you turn in an Excel file or a link that is not shareable. 

1. On the top right, click the share button --> share --> settings
2. Click "anyone" at the top, then underneath "More settings", change "can view" to "can edit". Then click apply. 
3. Copy the link, then turn it into Learning Suite in the feedback box for that assignment.

---

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

