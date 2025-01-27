# Gantt Charts

**Gantt Charts** are bar charts showing the start and finish dates of the different tasks that comprise a project. These charts can help in scheduling, managing, and monitoring specific tasks and resources in a project. The horizontal bars of different lengths represent the project timeline, which can include task sequences, duration, and the start and end dates for each task and is widely used in project management.

## Use of Gantt Charts
Construction managers, Facilty managers, and Civil Engineers use Gantt charts to plan and schedule construction projects. They are used to track the progress of the project and to ensure that the project is completed on time. Gantt charts are also used to allocate resources and to identify potential problems that may arise during the project. They are an essential tool for construction managers to ensure that the project is completed on time and within budget.

They are used on nearly all projects. The CFM studenst will later take a semester long class that teaches you the specifics of scheduling and go more in-depth so this will be a helpful headstart on the concepts talked about in scheduling.

This figure is from project management software and shows a Gantt chart for a construction project. The chart shows 
the start and finish dates of the different tasks that comprise the project. The horizontal bars of different lengths represent the project timeline, which can include task sequences, duration, and the start and end dates for each task. In the CFM class, you will learn to associate resources, staff, costs, and other important information with these tasks and perform critical path analysis to identify the most critical tasks in the project.

![gantt_chart.png](images/gantt_chart.png)

## Gantt Chart Creation in Google Sheets
We will learn to create Gantt charts in Google Sheets. This involves several distinct steps
* Identify the start date of each task
* Identify the duration or end of each task. One of these can be calculated from the other.
* Create a "calendar" sheet to draw the task lines
* Use conditional formatting to color the Gantt chart
* Use the SPARKLINE function to draw the "percent complete" on Gantt chart

## Formulas Used in Gantt Chart Creation

The following formulas are commonly used in Gantt Chart creation in Google Sheets and Excel. If you want more information or are confused on any of the formulas, click on the title of the function and it will take you to a webstie with a more in-depth explanation.

### [WEEKDAY()](https://support.google.com/docs/answer/3092985?hl=en){:target="_blank"}
This formula returns a number representing the day of the week of the day provided. 

**Syntax**

WEEKDAY(date, [type])

  * date - the date for which to determine the day of the week
  * type - [OPTIONAL - 1 by default] - a number that indicates which numbering system to use to represent weekdays. If type is 1, days are counted from Sunday; the value of Sunday is 1 and the value of Saturday is 7. If type is 2, days are counted from Monday; the value of Monday is 1 and the value of Sunday is 7.

**Use** 

* We will use this to convert a date into a number representing the day of the week. We will do some math to that 
that the week always starts on a Monday.


### [TEXT()](https://support.google.com/docs/answer/3094139?hl=en&sjid=3583168966296803426-NC){:target="_blank"}
This formula converts a number into text according to a specified format.

**Syntax**

TEXT(number, format)

  * number - the number, date, or time that needs formatted
  * format - the pattern by which to format the number, must be enclosed in quotation marks.

**Use**

* We will use TEXT() to convert the number returned by WEEKDAY() into a text representation of the day of the week. So 
a "3" becomes "Mon" for a week that starts on Saturday which is the default in Google Sheets.

### [LEFT()](https://support.google.com/docs/answer/3094079?hl=en){:target="_blank"}
This formula returns a specified number of characters from the beginning of a specified string.

**Syntax**

LEFT(string, [number_of_characters])

  * string - the string from which the left portion will be returned.
  * number_of_characters - [OPTIONAL - 1 by default] - the number of characters you want to return from the left side of the string

**Use**

* We will use Left() to extract the first letter of the day of the week. This will be used to format the Gantt chart  
using only single letters for the days of the week.

### [IFERROR()](https://support.google.com/docs/answer/3093304?hl=en&sjid=3583168966296803426-NC){:target="blank"}
This formula returns the first argument if there is not an error value. If an error value is present, the formula will return the second argument if present, or a blank if the second argument is absent.

**Syntax**

IFERROR(value, [value_if_error])

  * value - the value to return if value itself is not an error
  * value_if_error - [OPTIONAL - blank by default] - the value the function returns if value is an error

**Use**
* This allows us to return a blank cell if an error is computed in the cell. This is useful for the SPARKLINE() 
function we will use later.

### [SPARKLINE()](https://support.google.com/docs/answer/3093289?hl=en&sjid=3583168966296803426-NC){:target="_blank"}
This formula creates a miniature chart contained within a single cell.

**Syntax**

SPARKLINE(data, [options])

  * data - the range or array containing the data to plot
  * options - [OPTIONAL] - a range or array of optional settings and associated values used to customize the chart. For more information on the options argument, view the sparkline help page linked above.

**Use**
* On a more advanced Gantt chart we can have a column that is a sparkline that shows the progress of a task. This is a simple way to visualize the progress of a task in a Gantt chart.


# Pre-Class Quiz Challenge
Here is a link for the pre-class starter sheet: [Pre-Class Challenge: Gantt Charts and Project Scheduling](https://docs.google.com/spreadsheets/d/1kWWKcEMHJBMgLYg-by6k-AcVT_QcRzi-yzFtLiWq2JI/edit?usp=sharing){:target="_blank"}


## Instructions

1. Use the =TODAY() formula in cell B2 to input today’s date.
2. Use the =WEEKDAY() formula in cell B3 to return the weekday today’s date falls on.
3. Use the =TEXT() formula in cell B4 to return the weekday today’s date falls in the “DDD” format.
4. Use the =LEFT() formula in cell B5 to return the first letter of the weekday today’s date falls on.
5. Use the following SPARKLINE formula in cell B7 to create a progress bar:
=SPARKLINE(B6, {“charttype”, “bar”; “color1”, “pink”; “max”, 1})
6. In cell B9, copy the same formula above but modify it to reference B8 instead of B6.

   - Hint: if you did this step correctly, you will get an error when you enter the formula.

7. Use the =IFERROR() formula to return nothing in the cell if an error is computed in the cell.
8. Explain what each of these functions is doing in the C column under formula explanation.
   
Friendly reminder that if you can’t figure any of these steps that’s okay! This assignment is so you have some exposure to these formulas, and we will clarify confusion in class. You are also more than welcome to come to TA office hours or message a TA for help!




**References Used:**

[Gantt Charts](https://www.investopedia.com/terms/g/gantt-chart.asp){:target="_blank"}

[WEEKDAY()](https://support.google.com/docs/answer/3092985?hl=en){:target="_blank"}

[TEXT()](https://support.google.com/docs/answer/3094139?hl=en&sjid=3583168966296803426-NC){:target="_blank"}

[LEFT()](https://support.google.com/docs/answer/3094079?hl=en){:target="_blank"}

[IFERROR()](https://support.google.com/docs/answer/3093304?hl=en&sjid=3583168966296803426-NC){:target="_blank"}

[SPARKLINE()](https://support.google.com/docs/answer/3093289?hl=en&sjid=3583168966296803426-NC){:target="_blank"}
