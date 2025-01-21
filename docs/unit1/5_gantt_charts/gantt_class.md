# Gantt Chart In-Class Practice

The following exercise will have you create a simple Gantt chart in a Google sheets. For this exercise, open the in-class workbook, make a copy, and follow the instructions.

You can find the Gantt Chart In-Class Exercise here: [Gantt Chart In-Class Starter Sheet](https://docs.google.com/spreadsheets/d/1k8ACDgTKBveKUnfcdLnX6djCPG3-Sa6K8LO9h9yh3A0/edit?usp=sharing){:target="_blank"}

## Instructions

  1. In the cells indicated, insert your company name and write your name as the PM.
  2. Set the project start date for today's current date using the TODAY() function.
  3. We are going to set up the Gantt Chart so the weekday will always start on a Monday so the formatting will always be consistent. To do this, set cell E5 to be equal to the project start date minus the weekday the project start date falls on.

       * Hint: When using the WEEKDAY() function, set the [type] to '3' to set the start of the week to Monday.
    
      
  4. Set cell F5 to be E5+1.
  5. Drag over the dates to fill row 5 all the way to cell T5.
  6. Select E5:T5 and change the format of the dates to just show the day of the month.
     
       * Hint: To do this, you'll navigate to the format tab at the top, then number, and change the format to just show the numeric day of the month.
    
  8. Adjust the size of columns F:T to be small boxes.
  9. Use the formula =LEFT(TEXT(E5,"ddd"),1) in cell E6 to give the day of the week the date falls on in the schedule.
  10. List a minimum of 5 tasks to be completed.
  11. Set the start of your first task to the project start date.
  12. Give the tasks duration for how many days you think they will take to complete.
  13. Set the tasks end date to be the start date + the duration of the task.
  14. Set a conditional formatting rule using the AND() function on the range E7:T11 to fill the cell if the calendar date is within the range of the start and end date for the task.
  15. Format the chart with headers and colors.

When you are done, your chart should look something like this:

![inclassgantt](https://github.com/user-attachments/assets/36fede87-3cd4-48ca-a23b-3d871b297848)


---

## Turning in/Rubric
Turn sharing and editing on, then submit the link to Learning Suite in the feedback box. In-class assignment scores are based on valid effort and completion.
