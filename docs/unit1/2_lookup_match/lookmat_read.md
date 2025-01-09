
#  Reading: Lookups, Match, Data Validation

---
# Pre Class Reading Assignment

### Indexing a List with VLOOKUP
When writing formulas, we often encounter cases where one or more of the inputs to the function will depend on the value of another input. More specifically, we need to use one of the inputs to lookup the other input from a table. This can be easily accomplished using the VLOOKUP function.

For example, the following workbook computes the volume and weight of a set of cylinders. The weight is computing from the volume and the unit weight. However, the unit weight depends on the material being used. Unit weights for a set of common materials are shown in a table at the top:

![Vlookup_Image_1.png](images/Vlookup_Image_1.png)

The objective of this exercise is to determine the appropriate unit weight for each cylinder and calculate the correct weight by multiplying the selected unit weight by the computed volume. We will do this by automatically selecting the correct unit weight from the list using the VLOOKUP function.

### VLOOKUP Function
Once the material values are entered in column E, we are ready to use the VLOOKUP function. The syntax for the VLOOKUP function is as follows:

VLOOKUP(search_key,range,index,[is_sorted])

where:
|  Parameter  |                                                                      Explanantion                                                                       |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
|  Search_key |                                                 The value to be found in the first column of the array                                                  |
|    Range    |                             The table of information in which data is looked up. Use a reference to a range or a range name                             |
|    Index    |                                     The column number in table_array from which the matching value must be returned                                     |
| [is_sorted] | A logical value (TRUE or FALSE) that specifies whether you want VLOOKUP to find an exact match or an approximate match. Explained in more detail below. |

So for our case, we will use VLOOKUP to select a unit weight value from the table using the user-specified material. The unit weight returned by the function is then multiplied by the volume to compute the cylinder weight as follows:

![Vlookup_Image_2.png](images/Vlookup_Image_2.png)

The first argument (E13) to the VLOOKUP function refers to the Material value on the same row and is a relative reference. The second argument ($B$5:$C$10) is an absolute reference to the table use for the lookup. The lookup value ("Concrete" in this case) is used to search through the first column in the table to find the row matching the lookup value. In this case, the match is found on the third row of the table (cell B7). The third argument ("2") tells the VLOOKUP function from which column of the table the return value should be selected. Since the value is 2, we go to the second column of the lookup table on the selected row and find our value ("150"). This is the value that is returned by the function and multiplied by the volume ("1.6") to compute the weight. After copying this formula to the rest of the column, the weight values are all correctly computed as follows:

![Vlookup_Image_3.png](images/Vlookup_Image_3.png)

If the the values in the lookup table are edited, all of the weights would be automatically updated.

### Range Lookups
In the example shown in the previous section, we are doing an exact match on the lookup value in the first column. In some cases we are not looking for an exact match, but we need to find a match from a set of numerical ranges. For example, suppose that we wanted to categorize the cylinder weights using the following guidelines:

|          Range        |   Category  |
|-----------------------|-------------|
|        wt ≤ 1000      | Ultra Light |
|   1000 ≤ wt ≤ 2000    |    Light    |
|   2000 ≤ wt ≤ 10,000  |    Medium   |
| 10,000 ≤ wt ≤ 100,000 |    Heavy    |
|      100,000 ≤ wt     | Extra Heavy |

We will then add a new table and an extra column as follows:

![Vlookup_Image_4.png](images/Vlookup_Image_4.png)

Note that the weight values in the first column of the weight-category table at the top right has been sorted in ascending order. This is critical in order for the lookup to work. Next, we enter a formula using the VLOOKUP function as follows:

![Vlookup_Image_5.png](images/Vlookup_Image_5.png)

Notice that the last argument (range_lookup) has a value of TRUE. This means that we take the lookup_value ("235.6" in this case) and we look through the first column of the table until we find a row where the value on the row is less than or equal to the lookup_value and the value on the next row is greater than the lookup_value. In this case, the match occurs on the first row and so the resulting value from column 2 is "Ultra Light". After copying the formula to the rest of the Category column, the resulting values are as follows:

![Vlookup_Image_6.png](images/Vlookup_Image_6.png)

It is important to note that the range_lookup argument to the VLOOKUP function is optional. If it is omitted, it is assumed to be TRUE by default. A common error with the VLOOKUP function is to omit this argument when the VLOOKUP function is intended to be used as an exact match. This can lead to unintended errors, depending on how the values in the first column are ordered. Therefore, it is strongly recommended to always enter a TRUE or FALSE value for the range_lookup argument every time the VLOOKUP function is used.

### MATCH Function

The MATCH function given a range of cells will return a position. Let's first look at the syntax of the function.

MATCH(search_key,range,[search_type])

where:
|  Parameter  |                                           Explanation                                           |
|-------------|-------------------------------------------------------------------------------------------------|
| Search_key  |                         The value to to be found in the range of cells                          |
|    Range    | The table of information in which data is looked up. Use a reference to a range or a range name |
| Search_type |      Optional parameter that directs the function how to find the search_key in the range       |

The search_type has 3 different options for an input. If nothing is input for this parameter, the default value will be 1 which indicates that the values are sorted in ascending order. It will return the largest value less than or equal to the search_key. The second value is -1 and works opposite to 1. It indicates that the values are sorted in descending order and will return the smallest value greater than or equal to the search_key. The last acceptable input is 0. This option directs the function to search for an exact match to the search_key. If the range is not sorted, this is the best option. 

MATCH is a great function to pair with the MATCH function. Let's incorporate it in the VLOOKUP example:

![Match_Image_1.png](Match_Image_1.png)

For this instance, MATCH will always output position 2, but this will be very useful for larger tables or when the search_key may be different for each instances. It should also be noted that MATCH does output the column position, but rather the position in the range. MATCH also works vertically, but must remain 1 dimensional. 

### Data Validation
Data validation is a feature in Google Sheets that allows you to control the type of data entered into a cell. This can be useful to ensure that the data entered into a cell is accurate and consistent. This is different from filtering data as data validation controls the data that can be entered into a cell while filtering data changes the range of data you see.
Data validation can help prevent errors in your data and make it easier to work with.  

Let's go over how to add data validation to your data in Google Sheets:
1. Select the range of cells you want to add data validation to.
2. Click on Data --> Data validation.
3. In the data validation criteria box, you can set up the criteria for the data that can be entered into the cells. For example, you can choose to allow only numbers, text, dates, or a list of items.
4. You can also choose the output of the data validation you want to apply to the cells. For example, you can choose to show a warning message if the data entered does not meet the criteria or to reject the data altogether.
5. Once you have set up the criteria and output options, click on Save to apply the data validation to the selected range of cells.

#### Specific Examples
**Dropdown**  
This is useful when you want to limit the data that can be entered into a cell to a specific list of items. For example, you can create a drop-down list of options for a cell that allows the user to select from a list of items. To do this, follow the same steps as above and select Dropdown. You can then enter the items you want to include in the drop-down list, and choose what color you want the cell to be if the data is selected.
In the example below, the data validation is set up to allow only the values in the drop-down list to be entered into the cells, each having a color.

![Screenshot 2025-01-08 175658](https://github.com/user-attachments/assets/d1015fee-aae6-4d32-8cf0-7b30e53eca1d)

![Screenshot 2025-01-08 175727](https://github.com/user-attachments/assets/6800e356-c21d-4763-b656-02244eb5bebf)


**Dates**   
This is useful when you want to limit the data that can be entered into a cell to a specific date range. For example, you can create a data validation that only allows dates between 6/1/2021 and 6/30/2021 to be entered into the cells. To do this, follow the same steps as above and select the criteria that best fit the date range you want your data to have. In the example below, the data validation is set up to allow only dates between 6/1/2021 and 6/30/2021 to be entered into the cells.

![Screenshot 2025-01-08 182405](https://github.com/user-attachments/assets/73cda15f-3f37-4f4f-a6ca-bbe29bc104b4)


Here is an extra resource for further examples of Data Validation: [Data Validation](https://unito.io/blog/data-validation-google-sheets/){:target="_blank"}




There will be 3 short reading assignment before the next class. It will be on Lookups (specifically vlookup), Match, and Data Validation.

 [VLOOKUP](https://www.benlcollins.com/spreadsheets/vlookup-function/){:target="_blank"} - **Read Until** you get the the heading "VLOOKUP function template"
 
 [MATCH](https://blog.sheetgo.com/google-sheets-formulas/match-formula-google-sheets/){:target="_blank"} - **Read Until** you get the heading "How to use the INDEX MATCH function combination"

 [Data Validations](https://unito.io/blog/data-validation-google-sheets/){:target="_blank"}
 

## Things to look out for and think about
- Look for the differences in the function syntax between the VLOOKUP and MATCH.
- Think about how using Data Validations can help minimize errors in your formulas


---

# Pre-Class Quiz Challenge

## Instructions
1. First make a copy of the starter sheet here: [Starter Sheet Pre - Lookups, Match, Data Validation](https://docs.google.com/spreadsheets/d/1uMdVl5TzfQAnsSvh1fv3kuw2ci_jPpJNpaVRDbW3EH8/edit?usp=sharing){:target="_blank"}
2. Using Data Validations, add dropdowns in cells B2 to B25 for all the different types of services. (Tree Removal, Sidewalk Replacement, Siding Replacement, Gutter Cleaning, Gutter Replacement, Grass Removal, and Grass Replacement)
3. Now add dropdowns in cells D2 to D25 for the level of each service can receive (Full, Partial, and Finishing)
4. In cells E2 to E25 use the Vlookup and Match functions to correctly give a quote for the service and type that the customer would like multiplied by the quantity.

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

