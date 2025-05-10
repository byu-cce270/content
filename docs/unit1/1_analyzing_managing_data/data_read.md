#  Reading: Analyzing & Managing Data

---

In Excel, there are many ways to analyze and display data. For this topic, we will focus on Conditional Formatting, Filtering Data, and working with Functions. These are all important tools to know when working with data in Excel. They will help you to better understand your data and make it easier to read and analyze. In this reading, we will go over what each of these tools are and how to use them.

---

## Conditional Formatting
Conditional formatting is a feature in Excel that allows you to format cells based on certain conditions. This can be useful when you want to highlight certain data points or make your data easier to read.

There are many different ways to use conditional formatting in Excel. Some common uses include:
- Highlighting cells that contain certain values, text, dates, or numbers
- Highlighting cells that are above or below a certain value
- Highlighting cells that contain duplicate values
- Highlighting cells that are blank or contain errors
- Putting icons next to cells that meet certain criteria
- Data bars to show the relative size of values in a range
- Color scales to show the relative size of values in a range

To set up conditional formatting to your data in Excel, follow these steps:

1. Select the range of cells you want to format. This can be a single cell, a row, a column, or a range of cells. 

![CondFormat1.png](../2_lookup_match_if/images/CondFormat1.png)

2. Make sure you are on the Home tab, then select Conditional Formatting from the ribbon. This will open a drop-down menu with several options for conditional formatting.

![CondFormat2.png](../2_lookup_match_if/images/CondFormat2.png) 

3. Select the type of conditional formatting you want to apply. There are several options to choose from, including Highlight Cells Rules, Top/Bottom Rules, Data Bars, Color Scales, and Icon Sets. You can also create a new rule by selecting "New Rule" from the drop-down menu. 

![CondFormat3.png](../2_lookup_match_if/images/CondFormat3.png)

4. Once you have selected the type of conditional formatting you want to apply, a dialog box will appear. This dialog box will allow you to set the conditions for the formatting and choose the formatting options. Say for example, we want to highlight any cells that contains a "5" in the data set. We would select "Text that contains" from the drop-down menu.

![CondFormat4.png](../2_lookup_match_if/images/CondFormat4.png)

5. This will open a dialog box where you can enter the value you want to format. In this case, we would enter "5" in the box. You can also choose the condition to be based on a formula. For example, if you want to highlight cells that are greater than 5, you would enter the formula ">=5" in the box. The condition could also be based off another cell. For example, if you want to highlight cells that are greater than the value in cell A1, you would enter the formula ">=A1" in the box.

![CondFormat5.png](../2_lookup_match_if/images/CondFormat5.png)

6. After you have entered the value or formula, you can choose the formatting options. This includes the font color, fill color, and border style. You can also choose to apply the formatting to the entire row or column. There are some preset options to choose from, or you can create your own custom formatting by selecting "Custom Format" from the drop-down menu.

![CondFormat6.png](../2_lookup_match_if/images/CondFormat6.png)

7. Inside the custom format dialog box, you can choose the font, border, and fill options. You can also choose to apply the formatting to the entire row or column. Once you have selected the formatting options, click "OK" to apply the formatting.

![CondFormat7.png](../2_lookup_match_if/images/CondFormat7.png)

8. Once we have selected what the condition is and how we want it to look, we can click OK. This will apply the conditional formatting to the selected cells. 

![CondFormat8.png](../2_lookup_match_if/images/CondFormat8.png)

You can also add multiple conditional formatting rules to the same range of cells. To do this, simply repeat the steps above for each rule you want to add. The rules will be applied in the order they are listed in the Conditional Formatting Rules Manager. Conditional formatting rules can be edited or deleted at any time by selecting the rule in the Conditional Formatting Rules Manager and clicking "Edit Rule" or "Delete Rule". It is important to note that the order of the rules can affect how they are applied. For example, if you have two rules that apply to the same cells, the first rule will take precedence over the second rule. This means that if the first rule is true, the second rule will not be applied. Conditional formatting rules can also be copied and pasted to other cells. To do this, simply select the cells with the conditional formatting you want to copy, right-click, and select "Copy". Then, right-click on the cells where you want to paste the formatting and select "Paste Special". In the Paste Special dialog box, select "Formats" and click "OK". This will apply the conditional formatting to the selected cells.

To see more examples of conditional formating and the different options available, check out this link from W3Schools: [Conditional Formatting](https://www.w3schools.com/excel/excel_conditional_formatting.asp){:target="_blank"}

---

## Filtering Data
Filtering data is a feature in Google Sheets that allows you to show only the data that meets certain criteria. This can be useful when you have a large data set and only want to focus on a specific section of it. This differs from conditional formatting as filtering allows you to change the range of data you see, while conditional formatting changes the visual aspect of the data but does not alter the view range.

### Set up
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

### Specific Examples
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

## Working with Functions  
In Google Sheets, functions help users to analyze, manage, and compute data. A function is set up in three parts:

![Screenshot 2025-01-08 221445](https://github.com/user-attachments/assets/76daef2b-be63-4f76-8bcc-cb70ebb098dc)

Throughout this unit, you will learn new and useful functions. For this topic, we will focus on the most common functions for analyzing data:

   | Function           | Syntax              | Purpose                                         |
   |--------------------|---------------------|-------------------------------------------------|
   | Sum                | =SUM(arguments)     | Adds all of the arguments together              |
   | Average            | =AVERAGE(arguments) | Averages arguments together                     |
   | Max                | =MAX(arguments)     | Returns the highest number out of the arguments |
   | Min                | =MIN(arguments)     | Returns the lowest number out if the arguments  |
   | Standard Deviation | =STDEV(arguments)   | Returns the stardard deviation of the arguments |
   | Median             | =Median(arguments)  | Returns the median of the arguments             |


## Pre-Class Quiz Challenge

1. First, make a copy of the starter sheet here: [(Starter-Workbook)-Pre-Analyzing-&-Managing-Data.xlsx](%28Starter-Workbook%29-Pre-Analyzing-%26-Managing-Data.xlsx)
   </br> The challenge is a modified version of one from this website [Filtering and Sorting Data](https://edu.gcfglobal.org/en/googlespreadsheets/sorting-and-filtering-data/1/){:target="_blank"}. 
2. **Highlight** those in the **Type** column that checked out Cameras.
   <br> Hint: Use conditional formatting
3. **Highlight** those in **column A** that have an ID number between 1000 and 2500.
4. **Add filters** to the table (Columns A:F)
5. **Sort** the spreadsheet by the **Checked Out** date from most recent to the oldest.
6. **Sort** the spreadsheet by **Days Checked Out** to only show those who have a value of 5 and higher.
7. Fill in the **Days Checked out Statistics** chart using the **Days checked out** info in the main table.
8. When you're finished, your spreadsheet should look something like this:

![Pre-Analyzing-&-Managing-Data-Challenge-Solution.png](images/Pre-Analyzing-%26-Managing-Data-Challenge-Solution.png)

---

## Turning in/Rubric

**_REMINDER_** - For this class, **you will only turn in the links to your Excel files**. You will get a 0 for this assignment if you turn in an Excel file or a link that is not shareable. 

1. On the top right, click the share button --> share --> settings
2. Click "anyone" at the top, then underneath "More settings", change "can view" to "can edit". Then click apply. 
3. Copy the link, then turn it into Learning Suite in the feedback box for that assignment.

**Rubric:**

|                      Item                      | Points Possible |
|:----------------------------------------------:|:---------------:|
|                                                |                 |
| <div style="text-align: right">**Total**</div> |        5        |

The following is not apart of the rubric, but specifies how you can lose points. For example: if you fail to share your link correctly.

|               **Reasons for Points Lost**                | **Amount** |  
|:--------------------------------------------------------:|:----------:|
|                 Link shared incorrectly                  |     3      |
|      Turned in late. 10% for every week it's late.       |            |
