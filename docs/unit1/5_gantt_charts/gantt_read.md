# Gantt Charts

**Gantt Charts** are bar charts showing the start and finish dates of the different tasks that comprise a project. These charts can help in scheduling, managing, and monitoring specific tasks and resources in a project. The horizontal bars of different lengths represent the project timeline, which can include task sequences, duration, and the start and end dates for each task and is widely used in project management.

## Formulas Used in Gantt Chart Creation

The following formulas are commonly used in Gantt Chart creation in Google Sheets and Excel. 

### [WEEKDAY()](https://support.google.com/docs/answer/3092985?hl=en)
This formula returns a number representing the day of the week of the day provided. 

**Syntax**

WEEKDAY(date, [type])
  * date - the date for which to determine the day of the week
  * type - [OPTIONAL - 1 by default] - a number that indicates which numbering system to use to represent weekdays. If type is 1, days are counted from Sunday; the value of Sunday is 1 and the value of Saturday is 7. If type is 2, days are counted from Monday; the valye of Monday is 1 and the value of Sunday is 7.


### [TEXT()](https://support.google.com/docs/answer/3094139?hl=en&sjid=3583168966296803426-NC)
This formula converts a number into text according to a specified format.

**Syntax**

TEXT(number, format)
  * number - the number, date, or time that needs formatted
  * format - the pattern by which to format the number, must be enclosed in quotation marks.

### [LEFT()](https://support.google.com/docs/answer/3094079?hl=en)
This formula returns a specified number of characters from the beginning of a specified string.

**Syntax**

LEFT(string, [number_of_characters])
  * string - the string from which the left portion will be returned.
  * number_of_characters - [OPTIONAL - 1 by default] - the number of characters you want to return from the left side of the string

### [IFERROR()](https://support.google.com/docs/answer/3093304?hl=en&sjid=3583168966296803426-NC)
This formula returns the first argument if there is not an error value. If an error value is present, the formula will return the second argument if present, or a blank if the second argument is absent.

**Syntax**

IFERROR(value, [value_if_error])
  * value - the value to return if value itself is not an error
  * value_if_error - [OPTIONAL - blank by default] - the value the function returns if value is an error

### [SPARKLINE()](https://support.google.com/docs/answer/3093289?hl=en&sjid=3583168966296803426-NC)
This formula creates a miniature chart contained within a single cell.

**Syntax**

SPARKLINE(data, [options])
  * data - the range or array containing the data to plot
  * options - [OPTIONAL] - a range or array of optional settings and associated values used to customize the chart. For more information on the options argument, view the sparkline help page linked above.

**References Used:**

[Gantt Charts](https://www.investopedia.com/terms/g/gantt-chart.asp)

[WEEKDAY()](https://support.google.com/docs/answer/3092985?hl=en)

[TEXT()](https://support.google.com/docs/answer/3094139?hl=en&sjid=3583168966296803426-NC)

[LEFT()](https://support.google.com/docs/answer/3094079?hl=en)

[IFERROR()](https://support.google.com/docs/answer/3093304?hl=en&sjid=3583168966296803426-NC)

[SPARKLINE()](https://support.google.com/docs/answer/3093289?hl=en&sjid=3583168966296803426-NC)
