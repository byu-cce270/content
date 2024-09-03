#  HW: Lookups, Match, Data Validation

**Purpose:** Learn how to use lookups, match functions, and data validation when working with tables of data.

## Instructions
1. First make a copy of the starter sheet here:
   [Starter Sheet- HW Lookups, Match, Data Validation](https://docs.google.com/spreadsheets/d/1AVq6HfUD7hCXnJXD6L9dSqogVHGz_7yDUDuqRiZO5n0/edit?usp=sharing)
2. Rename it something like “[Your Name] HW 1.2 - Lookups, Match, Data Validation”

---

### Hydrometer Analysis Sheet

#### Part 1
1. Navigate to the Hydrometer Analysis sheet
2. Name the cells in the spreadsheet according to this table:
    
      Variable                          |  Cell  | Name
      --------------------------------- | ------ | -----
      Dry weight of soil sample         |   E3   |  Ws
      Specific gravity                  |   E4   |  Gs
      Temperature (°F)                  |   E5   |  Tf
      Temperature (°C)                  |   E6   |  Tc
      Meniscus correction factor        |   E7   |  Fm
      Zero correction Factor		        |   E8   |  Fz
      Temperature correction factor     |   E9   |  Ft
      Stoke's law coefficient           |   E10  |  A
      Specific gravity correction factor|   E11  |  Gc

3. Use the equations below to calculate the following cell values:

      Cell | Equation
     ----- | ---------------
       E6  | ![equationc.png](images/equationc.png)
       E9  | ![equationft.png](images/equationft.png)
   
4. In cell E10, use the VLOOKUP and MATCH functions to find the correct Stokes’ law coefficient (Use the purple Table of Stokes Law Coefficients in the Tables sheet)
5. Use the equations below to calculate the following cell values, then fill down the remaining rows in the relevant table:
   <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Hint:** You will need to use both absolute and relative cell references to fill down the table correctly </br>
   
      Cell | Equation
     ----- | ---------------
       C15  | ![equationrcp.png](images/equationrcp.png)
       D15  | ![equationpf.png](images/equationpf.png)
       E15  | ![equationcl.png](images/equationcl.png)
       G15  | ![equationd.png](images/equationd.png)
   
6. If you did everything right, the first row should look like this:

   ![checkwork.png](images/checkwork.png)
---

### Soil Services Sheet

#### Part 2
1. Navigate to the Soil Services sheet
2. In column D, use the VLOOKUP and MATCH functions to find the correct price per test for each row (Use the blue table in the Tables sheet)
   <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Hint:** Be careful with the search_type parameter in your MATCH function - in this case, your </br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;search_key must be approximated rather than exact</br>
4. In column E, multiply the test quantities and prices per test to get the total price for each row
5. In cell E33, sum the total prices in column E - if you did it correctly, your total should be $15,202

---

### Material Estimator Sheet

#### Part 3
1. Navigate to the Material Estimator sheet
2. In the merged cell B2:C2, create a dropdown menu using data validation that includes the four gravel types in the red table in the Tables sheet
3. In cell B7, use the VLOOKUP function to find the correct price based on the gravel type that is chosen using the dropdown menu

**Turn sharing and editing on. Turn in the link to Learning Suite in the feedback box**
