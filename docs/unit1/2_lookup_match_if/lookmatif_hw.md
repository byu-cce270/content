# HW: Lookups, Match, and IF Functions

**Purpose:** This assignment gives you practice using VLOOKUP, MATCH, IF, and IFS in several engineering examples.

---

## Getting Started
1. First make a copy of the starter workbook: [(Starter-Workbook)-HW-Lookups-Match-IF.xlsx](%28Starter-Workbook%29-HW-Lookups-Match-IF.xlsx)

2. Remember to save it in the CCE 270 folder that you created in the first assignment.

!!! note "Skills used in this assignment"
    - **Named cells:** Select a cell, enter a name in the Name Box, and press Enter. A name can then be used in a formula instead of the cell reference.
    - **Absolute references:** Use `$` to keep a lookup range fixed when filling a formula. While editing a reference, press `F4` on Windows or `Command+T` on Mac to cycle through reference types.
    - **Unit conversions:** Write the conversion as a formula so the result updates when the input changes.
    - **Fill formulas:** After filling a formula, check that relative references moved and absolute references stayed fixed.
    - **Summary functions:** `AVERAGE(range)` returns the arithmetic mean and `MEDIAN(range)` returns the middle value.

---

## Part 1 - Hydrometer Analysis Worksheet

1. Navigate to the **Hydrometer Analysis** worksheet.

2. Name the cells in the workbook according to this table:
    
      | Variable                           | Cell | Name |
      |------------------------------------|------|------|
      | Dry weight of soil sample          | E3   | Ws   |
      | Specific gravity                   | E4   | Gs   |
      | Temperature (°F)                   | E5   | Tf   |
      | Temperature (°C)                   | E6   | Tc   |
      | Meniscus correction factor         | E7   | Fm   |
      | Zero correction Factor	            | E8   | Fz   |
      | Temperature correction factor      | E9   | Ft   |
      | Stokes' law coefficient            | E10  | K    |
      | Specific gravity correction factor | E11  | Gc   |

**Hint**: To name a cell, click on the cell, then click on the name box in the top left corner of the screen, it should have the cell reference list. Type the name you want to give the cell. Press Enter to save the name. You can then reference the cell by its name in formulas. You can also go the Formulas tab, under the "Defined Names" group, you can manage names, create new names, or edit existing ones.

3. Use the equations below to calculate the following cell values:
    
   | Cell | Equation                                       |
   |------|------------------------------------------------|
   | E6   | $\,^oC = \left(\,^oF - 32\right) \dfrac{5}{9}$ |
   | E9   | $F_t = -4.85 + \dfrac{\,^oC}{4}$               |

4. In cell `E10`, use VLOOKUP and MATCH to find the Stokes' law coefficient from `Tables!$A$4:$H$17`. Use the temperature in `E6` as the VLOOKUP `lookup_value`. Use MATCH on the specific-gravity headings in `Tables!$B$3:$H$3` to help determine `col_index_num`. Add 1 to the MATCH result because the VLOOKUP range also includes the temperature column.

!!! note
    The temperature will not usually appear exactly in the coefficient range. Use an approximate VLOOKUP (`range_lookup = TRUE`) so Excel selects the largest listed temperature less than or equal to the calculated temperature. The temperature values must remain sorted in ascending order. Use an exact MATCH (`match_type = 0`) for the specific-gravity heading. Do not round the temperature: rounding selects the nearest whole number, which is a different rule from selecting the lower breakpoint.

5. Use the equations below to calculate the following cell values, then fill down the remaining rows in the calculation range:
 
   | Cell | Equation                          |
   |------|-----------------------------------|
   | C15  | $R_{cp} = R + F_T - F_Z$          |
   | D15  | $P_f = \dfrac{G_cR_{cp}}{W_S}$       |
   | E15  | $R_{cl} = R + F_m$                |
   | G15  | $D = K\sqrt{\dfrac{L}{t}}$        |

   Column **D** is already formatted as a percentage. Enter `=Gc*Rcp/Ws`; do not multiply by 100 in the Excel formula.

6. If you did everything right, the first row should look like this:

 ![Completed first row of the hydrometer calculations](images/checkwork.png){width=750px}

---

## Part 2 - Soil Services Worksheet

1. Navigate to the **Soil Services** worksheet.

2. In column **D**, use VLOOKUP and MATCH to find the correct price per test from `Tables!$J$3:$T$9`. Use an exact VLOOKUP (`range_lookup = FALSE`) for the service name. Use an approximate MATCH (`match_type = 1`) on the quantity headings in `Tables!$K$2:$T$2`, which are sorted in ascending order. Add 1 to the MATCH result because the VLOOKUP range begins with the service-name column. Quantities of 10 or more use the ten-test price.

3. In column E, multiply the test quantities and prices per test to get the total price for each row

4. In cell E35, sum the total prices in column E - if you did it correctly, your total should be $16,774.00

5. Use the Median and Average functions to find the median and average of the total prices in column E. Place the median in cell E34 and the average in cell E33

6. In column F, use the IF function to determine if the total price in column E is above or below the average price in cell E33. If it is above or equal to, return "Above Average", if it is below, return "Below Average"

7. In column G, use the IF function to determine if the total price in column E is above or below the median price 
   in cell E34. If it is above, return "Above Median", if it is equal to or below, return "Below Median"

---

## Part 3 - Material Estimator Worksheet

1. Navigate to the **Material Estimator** worksheet.

2. When you select cell `B2`, an arrow appears on the right side of the cell. Use the preconfigured Data Validation dropdown to choose a gravel type from the lookup range in the **Tables** worksheet. You will learn how to create dropdown lists in a later lesson.

![data_validation_example.png](images/data_validation_example.png)

3. In cell B5, convert the area of the gravel into volume. You will also need to go from square feet to cubic yards

4. In cell B6, convert the volume to tons by multiplying B5 by 1.4

5. In cell `B7`, use VLOOKUP with an exact match (`range_lookup = FALSE`) to find the price for the gravel type selected from the dropdown menu.

6. In cell B8, multiply cells B6 and B7 to get your total

7. You can make sure everything is right by checking your answer below:
   
![mat_est_table.png](images/mat_est_table.png)

---

## Part 4 - Simply Supported Beam Worksheet

1. Navigate to the **Simply Supported Beam** worksheet.

2. Name the cells in the workbook according to this table:

   | Variable          | Cell | Name |
   |-------------------|------|------|
   | Load              | B4   | P    |
   | Modulus           | B5   | E    |
   | Length            | B6   | L    |
   | Load offset       | B7   | a    |
   | Load offset       | B8   | b    |
   | Base              | B9   | base |
   | Height            | B10  | ht   |
   | Distance          | B11  | x    |
   | Moment of Inertia | B13  | Iu   |
   | Deflection        | B16  | v    |

3. Use the following table to write the equations shown below in the cells indicated. As you write the formulas, use the names you have defined for the input cells.

**Hint:** The most common mistake on these equations is the parentheses, so be careful when writing your equations.

   | Cell      | Equation                                                                          |
   |-----------|-----------------------------------------------------------------------------------|
   | B8        | $b=L-a$                                                                           |
   | B13       | $I_u=\dfrac{1}{12}base*ht^3$                                                      |
   | B14 (x≤a) | $v=\dfrac{Pbx}{6EI_uL}\left(b^2+x^2-L^2\right)$                                   |
   | B15 (x>a) | $v=\dfrac{-Pb}{6EI_uL}\left[\dfrac{L}{b}(x-a)^3+\left(L^2-b^2\right)x-x^3\right]$ |

4. Write an **IF** formula in cell **B16** that returns the value in cell **B14** if ***x≤a*** (`B7`) or the value in cell **B15** if ***x>a***. Use only distance values in the physical beam domain, `0 ≤ x ≤ L`.

If written correctly, the two branches of your formula should look like the examples below.

**For `x = 38.18 in` (`x ≤ a`):**

![Beam calculation with x equal to 38.18 inches](images/Deflection1.png)

**For `x = 96.53 in` (`x > a`):**

![Beam calculation with x equal to 96.53 inches](images/Deflection2.png)

5. These equations describe a simplified, piecewise cubic deflection curve. Change **x** in cell **B11** to evaluate the beam at different positions. When **x** is **38.18 in**, the deflection should be approximately **-2.00 in**. When **x** is **96.53 in**, the deflection should also be approximately **-2.00 in**. This engineering example is used to practice named cells, formulas, and conditional logic.

---

## Turning in/Rubric


!!! note "Do not put your name or NetID in the file"
    Learning Suite records who submitted each file, so your name is not needed
    inside the file itself. Leaving it out means your work can be graded
    anonymously, which keeps grading fair. This applies to scans and photos
    too — please don't write your name on the page.

**_REMINDER_** - For this class, **you will upload your Excel file directly to Learning Suite**. Make sure the file you upload is for the correct assignment and contains your finished work.

1. Make sure your work is saved, then close the workbook so that all of your changes are written to the file.
2. Go to the assignment in Learning Suite and upload your `.xlsx` file as an attachment.
3. Double-check that the file you uploaded is the one that contains your completed work.

**Rubric:**

|                         Item                         | Points Possible |
|:----------------------------------------------------:|:---------------:|
|  Part 1 - All cells named like the table instructs   |        1        |
| Part 1 - Temperature equations are written correctly |        2        |
|    Part 1 - VLOOKUP and MATCH equation is correct    |        5        |
|    Part 1 - Table equations are written correctly    |        2        |
|   Part 2 - VLOOKUP and MATCH equations are correct   |        5        |
|        Part 2 - Total price column is correct        |        2        |
|     Part 2 - IF statements are written correctly     |        2        |
|       Part 3 - Equations are written correctly       |        2        |
|         Part 3 - VLOOKUP equation is correct         |        4        |
|  Part 4 - All cells named like the table instructs   |        1        |
|       Part 4 - Equations are written correctly       |        2        |
|     Part 4 - IF statements are written correctly     |        2        |
|    <div style="text-align: right">**Total**</div>    |       30        |

---

The following is not a part of the rubric, but specifies how you can lose points. For example: if you fail to upload your file correctly.

| **Reasons for Points Lost** |    **Amount**     |  
|:---------------------------:|:-----------------:|
|  File uploaded incorrectly  |       -10%        |
|  Turned in late (per week)  | -10% (up to -50%) |
