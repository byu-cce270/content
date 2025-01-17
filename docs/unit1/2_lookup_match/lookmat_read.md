
#  Reading: Lookups, Match, Data Validation

---

### Indexing a List with VLOOKUP
When writing formulas, we often encounter cases where one or more of the inputs to the function will depend on the value of another input. More specifically, we need to use one of the inputs to lookup the other input from a table. This can be easily accomplished using the VLOOKUP function. 

For example, the following workbook computes the volume and weight of a set of cylinders. The weight is computed from the volume and the unit weight. However, the unit weight depends on the material being used. Unit weights for a set of common materials are shown in a table at the top:

![Vlookup_Image_1.png](images/Vlookup_Image_1.png)

The objective of this example is to determine the appropriate unit weight for each cylinder and calculate the correct weight by multiplying the selected unit weight by the computed volume. We will do this by automatically selecting the correct unit weight from the list using the VLOOKUP function.

### VLOOKUP Function
Once the material values are entered in column E, we are ready to use the VLOOKUP function. The syntax for the VLOOKUP function is as follows:

    VLOOKUP(search_key, range, index, [is_sorted])

where:

| Parameter   | Explanation                                                                                                                 |
|-------------|-----------------------------------------------------------------------------------------------------------------------------|
| search_key  | The value to be found in the first column of the array.                                                                     |
| range       | The table of information in which data is looked up. Use a reference to a range or a range name.                            |
| index       | The column number in the table defined by `range` from which the matching value must be returned.                             |
| [Is_sorted] | A logical value (`TRUE` or `FALSE`) that specifies whether you want VLOOKUP to find an exact match or an approximate match. |

For our case, we will use VLOOKUP to select a unit weight value from the table using the user-specified material. The unit weight returned by the function is then multiplied by the volume to compute the cylinder weight as follows:

![Vlookup_Image_2.png](images/Vlookup_Image_2.png)

The first argument (E13) to the VLOOKUP function refers to the Material value on the same row and is a relative 
reference. The second argument (\$B\$5:\$C\$10) is an absolute reference to the table use for the lookup. The 
search_key ("Concrete" in this case) is used to search through the first column in the table to find the row 
matching the search_key. In this case, the match is found on the third row of the table (cell B7). The third 
argument (2) tells the VLOOKUP function from which column of the table the return value should be selected. Since the value is 2, we go to the second column of the lookup table on the selected row and find our value (150). This is the value that is returned by the function and multiplied by the volume (1.6) to compute the weight. After copying this formula to the rest of the column, the weight values are all correctly computed as follows:

![Vlookup_Image_3.png](images/Vlookup_Image_3.png)

If the  values in the lookup table are edited, all of the weights would be automatically updated.

### Is_Sorted Parameter
In the example shown in the previous section, we are doing an exact match on the lookup value in the first column. In some cases we are not looking for an exact match, but we need to find a match from a set of numerical ranges. For example, suppose that we wanted to categorize the cylinder weights using the following guidelines:

|         Range         |   Category  |
|:---------------------:|:-----------:|
|       wt ≤ 1000       | Ultra Light |
|   1000 ≤ wt ≤ 2000    |    Light    |
|  2000 ≤ wt ≤ 10,000   |    Medium   |
| 10,000 ≤ wt ≤ 100,000 |    Heavy    |
|     100,000 ≤ wt      | Extra Heavy |

We will then add a new table and an extra column as follows:

![Vlookup_Image_4.png](images/Vlookup_Image_4.png)

Note that the weight values in the first column of the weight-category table at the top right has been sorted in ascending order. This is critical in order for the lookup to work. Next, we enter a formula using the VLOOKUP function as follows:

![Vlookup_Image_5.png](images/Vlookup_Image_5.png)

Notice that the last argument (is_sorted) has a value of TRUE. This means that we take the search_key (235.6 in this case) and we look through the first column of the table until we find a row where the value on the row is less than or equal to the search_key and the value on the next row is greater than the search_key. In this case, the match occurs on the first row and so the resulting value from column 2 is "Ultra Light". After copying the formula to the rest of the Category column, the resulting values are as follows:

![Vlookup_Image_6.png](images/Vlookup_Image_6.png)

It is important to note that the is_sorted argument to the VLOOKUP function is optional. If it is omitted, it is assumed to be TRUE by default. A common error with the VLOOKUP function is to omit this argument when the VLOOKUP function is intended to be used as an exact match. This can lead to unintended errors, depending on how the values in the first column are ordered. Therefore, it is strongly recommended to always enter a TRUE or FALSE value for the is_sorted argument every time the VLOOKUP function is used.

Here is an extra resource for further information on Vlookup: [VLOOKUP](https://www.benlcollins.com/spreadsheets/vlookup-function/){:target="_blank"}

### MATCH Function

The MATCH function returns the position of an item in a range of cells. Let's first look at the syntax of the function.

    MATCH(search_key, range, [search_type])

where:

| Parameter   | Explanation                                                                                     |
|-------------|-------------------------------------------------------------------------------------------------|
| search_key  | The value to be found in the range of cells.                                                    |
| range       | The table of information in which data is looked up. Use a reference to a range or a range name.|
| search_type | An optional parameter that directs the function on how to find the `search_key` in the `range`.   |

The search_type has three different options for an input as shown in the table below. If nothing is input for this parameter, the default value will be **1** which indicates that the values are sorted in ascending order. It will perform a range lookup and return the largest value less than or equal to the search_key. The second value is **-1** and works opposite to 1. It indicates that the values are sorted in descending order and perform a range lookup and return the smallest value greater than or equal to the search_key. The last acceptable input is **0**. This option directs the function to search for an exact match to the search_key.  

| Search Type |        Explanation        |
|:-----------:|:-------------------------:|
|      1      | Ascending Order (default) |
|      0      |        Exact Match        |
|     -1      |     Descending Order      |

MATCH is a great function to pair with the VLOOKUP function. Occasionally it is useful to do a two-dimensional lookup where a value is found from a table containing both rows and columns. For example, consider the following sheet containing a table of temperatures in degree F illustrating a relationship between average monthly temp and elevation in ft for a particular location.

![match_fig1.png](images/match_fig1.png)

Starting at row 24, another table is listed and the objective is to fill in the **Temp** column with a formula that looks up the temperature corresponding to the elevation from column **C** and the month associated with the date provided in column **B**. This requires a double lookup. We use VLOOKUP to find the row we need based on a range lookup of elevation using the VLOOKUP function. Then, for the third argument to VLOOKUP, we need to determine which column to use based on the month desired. To find the right column based on the month, we first need to find the month label ("Jan", "Feb", etc.) from a date value. This can be accomplished using the **TEXT** function which takes a date as an argument and returns the month or day value depending on the format specified by the second argument as follows:

    TEXT(B28,"MMM")

For the values shown, the function would return "**Mar**". Then we need to use this text string to automatically find the index of the column corresponding to this month. This can be done with the MATCH function as follows:

    MATCH(TEXT(B28,"MMM"),$B$7:$N$7,0)

The first argument to the MATCH function is the lookup value, the second argument is an array (row or column of values) and the third argument indicates the type of match to perform (a value of **0** tells it to find an exact match). The function looks through the array to find the lookup value and returns the index of the item if found. For the arguments shown, the function would return a value of **3**. At this point, we are ready to use the VLOOKUP function. We would formulate the function call as follows:

![match_fig2.png](images/match_fig2.png)

Note that we are using a range lookup on elevation so the last argument to VLOOKUP is **TRUE**.

Here is an extra resource for further information on Match: [MATCH](https://blog.sheetgo.com/google-sheets-formulas/match-formula-google-sheets/){:target="_blank"}

### Data Validation

Data validation is a feature in Google Sheets that allows you to control the type of data entered into a cell. This 
can be useful to ensure that the data entered into a cell is appropriate for the context of how it will be used. For 
example, you may have a formula that only works with positive values. You can can use data validation to ensure that 
the cell(s) used as input to the formula only accepts positive values. 
This is different from 
filtering 
data as data 
validation controls the data that can be entered into a cell while filtering data changes the range of data you see.
Data validation can help prevent errors in your data and make it easier to work with.  

Let's go over how to add data validation to your data in Google Sheets:

1. Select the range of cells you want to add data validation to.<br>
2. Click on **Data | Data validation**.<br>
3. In the data validation criteria box, you can set up the criteria for the data that can be entered into the cells. For example, you can choose to allow only numbers, text, dates, or a list of items.<br>
4. You can also choose the output of the data validation you want to apply to the cells. For example, you can choose to show a warning message if the data entered does not meet the criteria or to reject the data altogether.<br>
5. Once you have set up the criteria and output options, click on Save to apply the data validation to the selected range of cells.

#### Specific Examples

**Dropdown**  

This is useful when you want to limit the data that can be entered into a cell to a specific list of items. For example, you can create a drop-down list of options for a cell that allows the user to select from a list of items. To do this, follow the same steps as above and select **Dropdown**. You can then enter the items you want to include in the drop-down list, and choose what color you want the cell to be if the data is selected.
In the example below, the data validation is set up to allow only the values in the drop-down list to be entered into the cells, each having a color.

![Screenshot 2025-01-08 175658](https://github.com/user-attachments/assets/d1015fee-aae6-4d32-8cf0-7b30e53eca1d)

![Screenshot 2025-01-08 175727](https://github.com/user-attachments/assets/6800e356-c21d-4763-b656-02244eb5bebf)

If you select the **Dropdown (from a range)** option, you can select a range of cells that contain the items you want to include in the drop-down list. This is useful when you have a long list of items that you want to include in the drop-down list.

**Dates**  

This is useful when you want to limit the data that can be entered into a cell to a specific date range. For example, you can create a data validation that only allows dates between 6/1/2021 and 6/30/2021 to be entered into the cells. To do this, follow the same steps as above and select the criteria that best fit the date range you want your data to have. In the example below, the data validation is set up to allow only dates between 6/1/2021 and 6/30/2021 to be entered into the cells.

![Screenshot 2025-01-08 182405](https://github.com/user-attachments/assets/73cda15f-3f37-4f4f-a6ca-bbe29bc104b4)


There are many other options for data validation. Here is an extra resource for further examples of Data Validation: [Data Validation](https://unito.io/blog/data-validation-google-sheets/){:target="_blank"}

## Things to look out for and think about
- Look for the differences in the function syntax between the VLOOKUP and MATCH.
- Think about how using Data Validations can help minimize errors in your formulas
- Watch for white space (e.g., spaces) either before or after your match text, it can cause problems


---

# Pre-Class Quiz Challenge

## Instructions
1. First make a copy of the starter sheet here: [Starter Sheet Pre - Lookups, Match, Data Validation](https://docs.google.com/spreadsheets/d/1uMdVl5TzfQAnsSvh1fv3kuw2ci_jPpJNpaVRDbW3EH8/edit?usp=sharing){:target="_blank"}
2. Using Data Validations, add dropdowns in cells B2 to B25 for all the different types of services. (Tree Removal, 
   Sidewalk Replacement, Siding Replacement, Gutter Cleaning, Gutter Replacement, Grass Removal, and Grass 
   Replacement). Use the **Dropdown (from a range)** option to reference the first column in the table on the right.
3. Now add dropdowns in cells D2 to D25 for the level of each service can receive (Full, Partial, and Finishing)
4. In cells E2 to E25 use the Vlookup and Match functions to correctly give a quote for the service and type that 
   the customer would like multiplied by the quantity. You will use the VLOOKUP function to find a price from the 
   service table based on the service selected in column B, and you will use the MATCH function to find the correct 
   column in the service table from which to find a price, based on the type selected in column D.

Look below for a solution to see if you did it correctly and for some hints. (Click on the **bold** words to see the hints)

<details>
<summary><b>Solution</b></summary>

For any customer with the Service: "Sidewalk Replacement", Quantity: "10", and Type: "Full", the cost should be $1,890.

</details>


<details>
<summary><b>Hint 1: Function Syntax</b></summary>

Column B - Search Key
Column C - Multiply the total of your VLOOKUP and Match Function at the end
Column D - Search Key for the Index or MATCH Function

</details>


<details>
<summary><b>Hint 2: N/A Errors</b></summary>

If you are getting a lot of N/As maybe your is_sorted on your Vlookup is not correct or your search type for match is incorrect. Look over the pre-class readings for help

</details>


<details>
<summary><b>Hint 3: N/A Errors Part 2</b></summary>
  
Make the is_sorted false and the search type 0

</details>

<br>
