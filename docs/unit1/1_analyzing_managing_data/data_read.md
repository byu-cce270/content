#  Reading: Analyzing & Managing Data

---
## Intro:
In Google Sheets, there are many ways to analyze and display data. For this class, we will focus on Conditional Formatting, Filtering Data, Graphing Data, and Working with Functions. These are all important tools to know when working with data in Google Sheets. They will help you to better understand your data and make it easier to read and analyze. In this reading, we will go over what each of these tools are and how to use them.

## Reading:
### Conditional Formatting
Conditional formatting is a feature in Google Sheets that allows you to format cells based on certain conditions. This can be useful when you want to highlight certain data points or make your data easier to read. For example, you can use conditional formatting to highlight cells that contain a certain value or to format cells based on their value. 

#### Set Up
Now let's go over how to add conditional formatting to your data in Google Sheets:

1. Select the range of cells you want to format

![CondFormat1](https://github.com/user-attachments/assets/c08529d5-6684-48df-9c42-48a55af6a174)

2. Click on Format --> Conditional formatting

![CondFormat2](https://github.com/user-attachments/assets/1281a3ef-6354-4caf-aa39-f073413642c3)

3. Select the condition you want to format your cells on. In the conditional format rules drop box, you can set up the conditions or rules you want to format the cells based on. For example, you can format the cells if the value of the cell is greater than a given value. Another is to format if the date is between a given date range. 

![CondFormat3](https://github.com/user-attachments/assets/b997402f-1f0e-4d60-bb84-d2677aed8b88)

4. You can also choose the formatting options you want to apply to the cells that meet the condition. For example, you can choose to change the text color, background color, font style, or border style of the cells.

![CondFormat4](https://github.com/user-attachments/assets/f72dcb82-2388-49c4-92c9-c9fef5c1e152)

5. Once you have set up the conditions and formatting options, click on Done to apply the conditional formatting to the selected range of cells.

![CondFormat5](https://github.com/user-attachments/assets/6db829af-8c1a-40d0-8c4b-bb9ddc997db9)

6. Your cells will now be formatted based on the conditions you set up. For example, in the screenshot below, the cells are highlighted red if they contain the number 5.

![Screenshot 2025-01-07 142718](https://github.com/user-attachments/assets/369d360f-07e5-4b70-8828-b270ffb8538f)

#### Specific Examples
**Color Scale**  
This is useful for sheets with large amounts of data as you can visually distinguish the higher and lower values of the data. To add this to your data, follow the same steps as above but instead, select color scale instead of single color. 

![CondFormat7](https://github.com/user-attachments/assets/ad3d73a8-5c7d-4452-aabc-562fef9e5c99)

From here you can change the type of color scale you want to use. You can even create your own! The kind of scale you use will depend on the type of data you have. For data that slowly increases/decreases (such as river flow speed at different river spots), doing a scale of the same color may be nice so you can see the gradual change in the water flow.  

![Screenshot 2025-01-07 ](https://github.com/user-attachments/assets/62b50818-e8f3-4af2-9930-650a19f8e542)

**Note** Make sure that you select the correct range of data! In the example below, you must select the data below the third row, or the site number on row 1 will skew our color gradient.

![Screenshot 2025-01-07 161140](https://github.com/user-attachments/assets/7418b1a3-65c5-4247-8730-38abffa6e5cb)

**Multiple Conditional Formats**  
There may be instances when you want to apply multiple conditional formats to the same data set. This may happen when you want a more precise number range, such as highlighting the cells that contain the values 3-5 and 1-10. Conditional formatting only applies to the first rule (from top to bottom) that is true. Any other, even if it is also true, will not show. You can make sure yours will display by changing the order they appear. This is done by dragging the dots to the left of the rule to the correct position. In the example below, there are 2 conditions. If they are kept as are, ALL of the cells will appear green as each cell fulfills the first condition BEFORE the second. 

![Screenshot 2025-01-07 163902](https://github.com/user-attachments/assets/582cff30-ddd0-49d4-86e4-604f9c7a799b)


But if we change the order, we can see that both conditions now show. It's as simple as that!

![Screenshot 2025-01-07 163918](https://github.com/user-attachments/assets/8f43cb38-5d27-44ec-80a6-8fec9b6e0b38)

Here is an extra resource for further examples of conditional formatting: [Conditional Formatting](https://blog.coupler.io/conditional-formatting-google-sheets/){:target="_blank"}

---

### Filtering Data
Filtering data is a feature in Google Sheets that allows you to show only the data that meets certain criteria. This can be useful when you have a large data set and only want to focus on a specific section of it. This differs from conditional formatting as filtering allows you to change the range of data you see, while conditional formatting changes the visual aspect of the data but does not alter the view range.

#### Set up
1. Select the columns of data you want to add filters to.

![Screenshot 2025-01-08 170010](https://github.com/user-attachments/assets/346aa4e2-8bc3-4232-96b9-9892b607a05d)

2. Select Data, and then create a filter.

![Filter1](https://github.com/user-attachments/assets/e2ced105-71a1-4bef-931f-8ae1b57b4475)

3. Click on the upside-down triangle with 3 lines to edit the filter.

![Screenshot 2025-01-07 170409](https://github.com/user-attachments/assets/9cfd95dc-2932-4ab6-85d9-89e34b61d3c7)

4. There are many ways to filter data, for this class, we will focus on the filter by condition. Select filter by condition, and then the drop box. Select the condition that fits your data, then select ok at the bottom.

![Screenshot 2025-01-07 171430](https://github.com/user-attachments/assets/51b62ef6-aafa-4e96-ad20-e772ff37a830)

5. In the example below, the Width of Bridge Segment column is filtered to only show the cells with values greater than 50.

![Screenshot 2025-01-07 171729](https://github.com/user-attachments/assets/03dbeebd-c718-4732-a8d4-5438de15e5e5)


6. To reset a filter, select "None" and then Ok.

![Screenshot 2025-01-07 172034](https://github.com/user-attachments/assets/f42fb230-1121-43a6-a003-76c94bee78e2)

#### Specific Examples
**Filtering By Date**  
There are many cases when you may want to filter your data to show only dates past a certain day or even a range of dates. To enter an exact date, you will need to use the DD/MM/YYYY format. In the example below, the data is filtered to only show those dates before 6/24/2021, NOT including 6/24/2021.

![Screenshot 2025-01-07 172944](https://github.com/user-attachments/assets/98d7eea0-e65f-4ca5-95d6-3886db868f88)

**Filtering Numerical Data**  
Many data sets will have large amounts of numerical data. To make it easier to read, you can filter out the unwanted data by choosing the condition. This can be very useful for data sets with thousands of inputs! In the example below, the data is filtered to show all data between 35-40 (not including 35 & 40).

![Screenshot 2025-01-07 180024](https://github.com/user-attachments/assets/dcffcfc8-6b19-448d-98f7-1c884dc51b46)


**Multiple Filters**  
Like conditional formatting, you can have multiple filters! This may be useful when you want to filter by multiple conditions. Unlike conditional formatting, the order does not matter. This means I can apply the filters in any order I'd like and the same data will show. In the example below, there 2 different filters to show the data that is before 6/21/2021 and has an approved status A. 

![Screenshot 2025-01-07 175522](https://github.com/user-attachments/assets/5e2aaf4c-a296-4784-8324-2db9597885d8)

**DISCLAIMER**  
The value you input to filter by is NOT included unless you choose a filter that has equal to. For example, if I have a filter to only show data greater than 45 then any value that is equal to 45 IS NOT included. This is critical when filtering by date/day! Make sure that the value you filter by includes ALL of the data you want.

Here is an extra resource for further examples of Filters: [Filtering and Sorting Data](https://edu.gcfglobal.org/en/googlespreadsheets/sorting-and-filtering-data/1/){:target="_blank"}

---

### Graphing Data
Another valuable tool for analyzing data is graphing. This allows us to see trends in data, compare variables, and visualize the values in our data set. This can be hard to do by hand, and Google Sheets makes it much easier! Let's walk through how to graph a given data set. 

1. Highlight the data that you want to graph. Sometimes you don't need all of the data, so only highlight what you need. In the example below, there is too much information for one graph so only the needed columns were highlighted.

![Screenshot 2025-01-08 204941](https://github.com/user-attachments/assets/8e069659-e380-4fc6-968b-34074d903476)

2. Select insert --> chart

![Screenshot 2025-01-08 205053](https://github.com/user-attachments/assets/c7f2955a-daa4-4209-acfc-64474ea5ec20)

3. From here, Google Sheets will give you an auto-generated graph. If that works for your data set then great! For much of the data you are given, you will need to choose the graph that best fits the data. This is done by selecting the drop box underneath the chart type. For this class, we will primarily use line, bar, column, and pie graphs.

![Screenshot 2025-01-08 205510](https://github.com/user-attachments/assets/77e78c7d-a544-4c63-9ad4-a9a268c561a0)

4. After selecting the graph, check and make sure the data are on the proper x and y axes. You can change this by clicking on the grey labels underneath the X-axis label and Series label. 
5. The checkboxes at the bottom are also very useful to make sure that Google Sheets knows how to read your data properly
- switch rows/columns - useful when you want to change rows and columns in your data set (like turning a landscape table into a portrait one)
- Use row 1 as headers - this uses the top highlighted row as a label for the x and y axes. Most of the time this is useful when you have data sets with labeled columns
- Use columns as labels - this will allow you to use that column as the values for the x-axis.
- Treat labels as text - this will treat the above column only as text and not numbers. This means that your graph will label every data point. This is useful when wanting to know exact data points. In other cases, only an approximation is needed. In the example below, you can see the difference:

![Screenshot 2025-01-08 211726](https://github.com/user-attachments/assets/a92f7b97-28b8-476d-9f87-7768b530aba1)

![Screenshot 2025-01-08 211817](https://github.com/user-attachments/assets/1e109c7d-462f-414e-99be-db32fd7dcb42)

6. Many times, you may want to add more in-depth features to the graph such as a title, labels for the x and y axes, a legend, or even change the spacing for the data points. This can all be done in the Customize tab.

![Screenshot 2025-01-08 212310](https://github.com/user-attachments/assets/c3874f97-5a13-479a-97dc-e8e848e645dd)

From here, there are many options. Most of these are for visual changes, but help to distinguish our data:

![Screenshot 2025-01-08 212641](https://github.com/user-attachments/assets/c72e210a-c06f-415a-ba9f-ff96580dd5bb)

- Chart style - Edit the background color, border color, font, and other neat features
- Chart & axis titles - Allows to add titles for the graph and labels for x and y axes
- Series - Allows edits to the y-axis such as changing the color of the line (for line graphs), and the type of line
- Legend - Allows edits to the legend of the graph such as its size, color, and placement.
- Horizontal axis - allows edits to x-axis such as choosing the label font, adding slant labels, etc.
- Vertical axis - Allows edits to the y-axis such as what value to start and stop at, the scale of the data, and other visual features.
- Gridline and ticks - Allows to add grid lines to the x and y axes to more accurately see data points.

Other types of graphs have more unique features to them, but these are the general few! 

#### Specific Examples
**Line Graph**
Use to track changes over time intervals, such as the speed of a car during a drive. In the example below, the temperature of a place is graphed over a few days.

![Screenshot 2025-01-08 215839](https://github.com/user-attachments/assets/79582e17-4650-4476-a6b4-64a77d314ad1)


**Bar/Column chart**
Use to track differences between groups, such as grades in a class. In the example below, customers with the same ID are compared to see the amount of each order.

![Screenshot 2025-01-08 215721](https://github.com/user-attachments/assets/540118f2-144e-4ec8-abb1-38a69751dd96)


**Pie Chart**
Used to compare amounts/ratios of a whole such as wins vs losses during a BYU basketball season. In the example below, the percentage of each material purchased is graphed from a customer's order.

![Screenshot 2025-01-08 220114](https://github.com/user-attachments/assets/3faa6ffe-0f61-4508-86af-ace6b95fa971)

Here is an extra resource for further examples of graphing: [Graphing](https://support.google.com/docs/answer/190718?hl=en#zippy=){:target="_blank"}

---

### Working with Functions
In Google Sheets, functions help users to analyze, manage, and compute data. A function is set up in three parts:

![Screenshot 2025-01-08 221445](https://github.com/user-attachments/assets/76daef2b-be63-4f76-8bcc-cb70ebb098dc)

Throughout this unit, you will learn new and useful functions. For this topic, we will focus on the most common functions for analyzing data:

   | Function           | Syntax              | Purpose                                          |
   |--------------------|---------------------|--------------------------------------------------|
   | Sum                | =SUM(arguments)     | Adds all of the arguments together               |
   | Average            | =AVERAGE(arguments) | Averages arguments together                      |
   | Max                | =MAX(arguments)     | Returns the highest number out of the arguments  |
   | Min                | =MIN(arguments)     | Returns the lowest number out if the arguments   |
   | Standard Deviation | =STDEV(arguments)   | Returns the stardard deviation of the arguments |
   | Median               | =Median(arguments)    | Returns the median of the arguments                |


# Pre-Class Quiz Challenge

## Instructions
1. First make a copy of the starter sheet here: [Starter Sheet Pre - Analyzing & Managing Data](https://docs.google.com/spreadsheets/d/1nHMTqHvprWHruS2jWq81fNMTIU7UjirWh8wV3Ddkvtg/edit?usp=sharing){:target="_blank"}
   </br> The challenge is a modified version of one from this website [Filtering and Sorting Data](https://edu.gcfglobal.org/en/googlespreadsheets/sorting-and-filtering-data/1/){:target="_blank"}. 
2. **Highlight** those in the **Type** column that checked out Cameras.
   <\br > Hint: Use conditional formatting
3. **Highlight** those in **column A** that have an ID number between 1000 and 2500.
4. **Add filters** to the table (Columns A:F)
5. **Sort** the spreadsheet by the **Checked Out** date from most recent to the oldest.
6. **Sort** the spreadsheet by **Days Checked Out** to only show those who have a value of 5 and higher.
7. Fill in the **Days Checked out Statistics** chart using the **Days checked out** info in the main table.
8. Create a **pie chart** of who checked out which equipment type (column B) to see what was checked out most. Give the chart a title and label each slice.
9. When you're finished, your spreadsheet should look something like this:

![Screenshot 2025-01-08 234149](https://github.com/user-attachments/assets/7bfa3bdb-6e5b-4df7-a099-bfe8b76f5e00)

10. **Change the access so anyone with the link can edit**. Copy the Link and paste it into the pre-class quiz.
   
