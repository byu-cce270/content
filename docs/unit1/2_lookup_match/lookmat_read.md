
#  Reading: Lookups, Match, Data Validation

---
# Pre Class Reading Assignment

### Indexing a List with VLOOKUP
When writing formulas, we often encounter cases where one or more of the inputs to the function will depend on the value of another input. More specifically, we need to use one of the inputs to lookup the other input from a table. This can be easily accomplished using the VLOOKUP function.

For example, the following workbook computes the volume and weight of a set of cylinders. The weight is computing from the volume and the unit weight. However, the unit weight depends on the material being used. Unit weights for a set of common materials are shown in a table at the top:

Vlookup_Image_1

The objective of this exercise is to determine the appropriate unit weight for each cylinder and calculate the correct weight by multiplying the selected unit weight by the computed volume. We will do this by automatically selecting the correct unit weight from the list using the VLOOKUP function.

### VLOOKUP Function
Once the material values are entered in column E, we are ready to use the VLOOKUP function. The syntax for the VLOOKUP function is as follows:

VLOOKUP(search_key,range,index,[is_sorted])

where:
|  Parameter  |                                          Explanantion                                           |
|-------------|-------------------------------------------------------------------------------------------------|
|  Search_key |                     The value to be found in the first column of the array                      |
|    Range    | The table of information in which data is looked up. Use a reference to a range or a range name |
|    Index    |         The column number in table_array from which the matching value must be returned         |
| [is_sorted] | A logical value (TRUE or FALSE) that specifies whether you want VLOOKUP to find an exact match or an approximate match. Explained in more detail below. |

So for our case, we will use VLOOKUP to select a unit weight value from the table using the user-specified material. The unit weight returned by the function is then multiplied by the volume to compute the cylinder weight as follows:

Vlookup_Image_2

The first argument (E13) to the VLOOKUP function refers to the Material value on the same row and is a relative reference. The second argument ($B$5:$C$10) is an absolute reference to the table use for the lookup. The lookup value ("Concrete" in this case) is used to search through the first column in the table to find the row matching the lookup value. In this case, the match is found on the third row of the table (cell B7). The third argument ("2") tells the VLOOKUP function from which column of the table the return value should be selected. Since the value is 2, we go to the second column of the lookup table on the selected row and find our value ("150"). This is the value that is returned by the function and multiplied by the volume ("1.6") to compute the weight. After copying this formula to the rest of the column, the weight values are all correctly computed as follows:

Vlookup_Image_3

If the the values in the lookup table are edited, all of the weights would be automatically updated.

Range Lookups
In the example shown in the previous section, we are doing an exact match on the lookup value in the first column. In some cases we are not looking for an exact match, but we need to find a match from a set of numerical ranges. For example, suppose that we wanted to categorize the cylinder weights using the following guidelines:

|          Range          |   Category  |
|-------------------------|-------------|
|        wt <= 1000       | Ultra Light |
|   1000 <= wt <= 2000    |    Light    |
|   2000 <= wt <= 10,000  |    Medium   |
| 10,000 <= wt <= 100,000 |    Heavy    |
|      100,000 <= wt      | Extra Heavy |






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

