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
    
      
  7. Adjust the size of the columns F:T to be small boxes.
  8. Using the LEFT() and TEXT() formulas in cell E6, give the day of the week the date falls on in the schedule.

       * Hint: For the date in E5, the corresponding day of the week in cell E6 should be 'M'.

  9. Drag the formula over to fill row 6 all way to cell T6.
  10. Under column A, starting in row 7, list a minimum of 5 tasks to be completed.
  11. Set the start of your first task to be the project start date.
  12. Give all tasks a duration based on how long you think they will take to complete.
  13. Set the end date for all tasks to be the start date + the duration of the task.
  14. You have two options here, you can either set the start date of the next four(+) tasks to be the end date of the previous task, or you can give them their own start date. In scheduling, we talk about task relationships and delays between tasks, but for this class just realize that you don't always have to finish a task to start a new one.

      * For example you can start putting concrete forms up after a couple days of excavating v. waiting for the excavation to be completed before starting formwork. Or you can have cabinets installed while lighting is also being installed. Having tasks going on at the same time makes your project faster and saves you money as a contractor.

  16. Set a conditional formatting rule using the AND() function on the range E7:T11 to fill the cell in a solid color if the calendar date is within the range of the start and end date for the task.

        * Hint: The AND() function will take multiple conditions. You will want to select a custom formula for your conditional formatting rule. The first condition will be if the calendar date is greater than or equal to the start date. The second condition will be if the calendar date is less than or equal to the end date.
        * Another Hint: Make sure to watch your absolute and relative references. For this formula, you'll have rows that are absolute while the column is not, and columns that are absolute while rows are not.
          
  17. Format the chart with headers and colors.
      
      * Optional Formatting Tip: You can make the gridlines on your google sheet disappear by going to the "View" Tab at the top of your sheet, selecting "Show" and then unselecting "Gridlines". Not required, but it makes the formatting look nicer.

When you are done, your chart should look something like this:

![inclassgantt](https://github.com/user-attachments/assets/36fede87-3cd4-48ca-a23b-3d871b297848)


---

## Turning in/Rubric
Turn sharing and editing on, then submit the link to Learning Suite in the feedback box. In-class assignment scores are based on valid effort and completion.
