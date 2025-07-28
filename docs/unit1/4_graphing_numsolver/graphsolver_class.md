# Exercise - Employee Data

We will practice graphing and using the Solver function in Excel. The data we will use is from a sample employee dataset. You can access the data here:

- employee data  [Pivot Tables/Query Starter Sheet](https://docs.google.com/spreadsheets/d/19msUPf9DYVBAMNnoIhYO6RMpdSlKobbJM3Ul7W-qiCU/edit?usp=sharing){:target="_blank"}.

Make sure to rename the starter sheet something like “[Your Name]-Class-Graphing-and-Solver”.

---
## Exercise #1- Graphing Employee Data 

Take a look at the data, it contains information about employees, including their names, departments, salaries, and years of service.

Navigate to the first sheet in the employee data workbook, which is designed to graph employee data. 

1. Try to make a graph that shows the average salary by department. You can use the **Insert** tab in Excel to create 
a chart. Make sure that each chart is created on its own sheet and is titled appropriately. Make sure that the axis 
   are labeled and the chart has a legend. Play around with the chart styles and colors to make it visually appealing.
2. Make a pie chart that shows the distribution of employees by department. 
3. Show a bar graph that shows the number of employees in each department.
4. Make a line graph that shows the trend of average salary over the years of service.

---
## Exercise #2- Using Solver in Excel (with Goal Seek)
Open the second sheet in the employee data workbook,which is designed to solve a quadratic equation using Excel's Solver function.
The workbook is designed to solve a quadratic equation of the form:

$y = ax2 + bx + c$

The user enters the coefficients a, b, & c in cells C4:C6. For the case shown above, we are solving:

$y = x2 - 3x + 1$

The chart at the bottom is used to graph the parabola corresponding to the equation over a specified range. The 
solution to the equation is the two points where the parabola intercepts the y-axis. These are called the "roots" and represent the solution to:

$ax2 + bx + c = 0$

As can be seen on the chart, the roots are approximately 0.4 and 2.6.

We can find the roots using cells F4 and F5. We enter a value for x in cell F4. The corresponding value of y is computed in cell F5 as:

**=C4*F4^2+C5*F4+C6**

To find a root, we can enter a guess (0.4 for starters) into F4 and iteratively tweak that number until the value 
computed for y in F5 is roughly equal to zero. While this works, it can be time-consuming and tedious.

1. Solve for one of the roots of the parabola 
2. Find the x location corresponding the lowest point on the parabola.

## Turning in/Rubric
Turn sharing and editing on, then submit the link to Learning Suite in the feedback box. In-class assignment scores are based on valid effort and completion.
