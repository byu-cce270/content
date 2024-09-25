#  HW: Gantt Chart/Project Scheduling and Tracking

**Purpose:** Learn how to format and display a project schedule using a Gantt chart in Google Sheets.

## Instructions
1. Create a new Google Sheet and rename is something like "[Your Name] HW 1.6 - Gantt Charts"
2. Following the same format as the in class activity, give your project a project title, insert your company name, project manager name, and the start date as today's current date. 
3. Create a header starting in cell A5 with the following titles:
      
      * A5: TASK
      * B5: ASSIGNED TO
      * C5-D5: PROGRESS (merge these two columns)
      * E5: START
      * F5: DURATION
      * G5: END

4. Create a project begin date box with the following:

      * F2: Project Begins:
      * F3: Display Week:
      * G2: Outline the box and enter a random date you would like to start on
      * G3: Outline the box and enter 1

    When you're finished your sheet should look something like this:

    ![header_format.png](images/header_format.png)

5. In cell I4, write this formula: =G2-weekday(G2,3)+(G3-1)*7.
6. In cell J4, write =I4+1 and hit enter. Drag this formula/cell out to AJ4.

   - Hint: The formula will look like = [cell where your project start date is] - WEEKDAY([cell where your project start date is], 3).
    
7. In cell I5, we will reference the day of the week the date above it will fall on.
   
   - Hint: Use the LEFT() and TEXT() functions to do this.
    
8. Merge cells I3:O3. Set the value of the new merged cell to the date in cell I4, or the start of the week.
9. Use the format painter to apply these same changes to the rest of the weeks. When you're done, the formatting of your weeks should look something like this:

      ![week_view.png](images/week_view.png)

10. In the TASK column (column A), write PHASE 1 in cell A6. Below this cell, create four tasks that will take place during phase 1.
11. Below the first phase and its 4 tasks, write PHASE 2, and create four tasks below it that will take place during phase 2.
12. For your first task, reference its start date as the start of the project. 
13. Create a duration for each of the tasks and set the end date for the tasks as their start date + the duration.
14. Once all task start and end dates are in, input the start and end dates of PHASE 1 and PHASE 2 by referencing the day the first task in the phase started as the start date, and the last day the last task in the phase ended as the end date.
15. Create a conditional formatting rule that will take the duration of the task and input a bar in the schedule for the correct amount of days.
    
    - Hint: This rule is very similar to what we did for the in class activity.
    
16. Now that most of your data is inserted into the Gantt Chart, format the headers and add borders to certain cells to display the data in the way that makes the most sense to you.
17. Create a conditional formatting rule that applies to cells I4:AJ5 that will highlight the cells if the date in those cells is today's date.
    
    - Hint: Use the TODAY() function.
    
18. In column C in your table, insert percentages for how complete at least 4 of your tasks are. 
19. In colum.n D in your table, use the IFERROR and SPARKLINE function to create a bar chart to display the completion progress of each your tasks.
    
    - Hint: If you did your formula correctly, nothing will display in the column D if there is no percentage complete given for a task.

---


**Turn sharing and editing on. Turn in the link to Learning Suite in the feedback box**

---

**Rubric:**

|                     Gantt Chart                  | Points Possible |
|:-------------------------------------------------------------------------:|:---------------:|
|   Sheet notes project title, company name, and student name as the project manager       |        2        |
|  Headers are all included correctly as noted in step 3      |        6        |
|   Tasks and phases are included with each phase including 4 tasks      |        4        |
|     Start and end dates for each task are computed correctly  | 4  |
| Phase start and end dates are computed correctly    |        2        |
|  Conditional formatting rule for task durations is input correctly and displays task durations correctly    |        5        |
|      Table is formatted with colors and headers         |        2        |
|       Conditional formatting rule to highlight today's date works correctly       |        2        |
|     SPARKLINE and IFERROR formulas are used correctly together    |        3        |
|  <div style="text-align: right">**Total**</div>                           |       30        |
