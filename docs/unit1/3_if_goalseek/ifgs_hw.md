#  HW: IF Statements and Goal Seek

**Purpose:** Learn how to use external/API tools to solve complex equations

## Instructions
1. First make a copy of the starter sheet here:
   [Starter Sheet- HW IF Statements & Goal Seek](https://docs.google.com/spreadsheets/u/0/d/1rUlyf8lmHztFnhjQZp-jJvgtg7bNhADAEoz0q4NbXms/edit){:target="_blank"}
2. Rename it something like “[Your Name] HW 1.4 - IF Statements and Goal Seek”

---

#### Part 1
1. Navigate to the **Three Reservoir Problem** sheet
2. Name the cells in the spreadsheet according to this table:

**Hint:** You can edit cell names by navigating to the name box in the top left corner of the spreadsheet

   | Variable          | Cell | Name |
   |-------------------|------|------|
   | Pipe 1 Diameter   | C5   | Diam1|
   | Pipe 2 Diameter   | C6   | Diam2|
   | Pipe 3 Diameter   | C7   | Diam3|
   | Pipe 1 Length     | D5   | Length1|
   | Pipe 2 Length     | D6   | Length2|
   | Pipe 3 Length     | D7   | Length3|
   | Pipe 1 Friction     | E5   | Fric1|
   | Pipe 2 Friction     | E6   | Fric2|
   | Pipe 3 Friction     | E7   | Fric3|
   | Pipe 1 Elevation     | F5   | Elev1|
   | Pipe 2 Elevation     | F6   | Elev2|
   | Pipe 3 Elevation     | F7   | Elev3|
   | Junction Hydraulic Grade Line     | B11   | HGLj|

3. Use the following table to write the equations shown below in the cells indicated. As you write the formulas, use the names you have defined for the input cells.

**Hint:** The most common mistake on these equations is the parentheses, so be careful when writing your equations.

   | Cell      | Equation                                                                          |
   |-----------|-----------------------------------------------------------------------------------|
   | D11       | $\sqrt{\dfrac{2 * 9.81 * (HGLj - Elev1)}{(\dfrac{Fric1 * Length1}{Diam1}) -1}}$   |
   | F11       | $\sqrt{\dfrac{2 * 9.81 * (Elev2 - HGLj)}{(\dfrac{Fric2 * Length2}{Diam2}) +1}}$   |
   | H11       | $\sqrt{\dfrac{2 * 9.81 * HGLj}{(\dfrac{Fric3 * Length3}{Diam3}) -1}}$           |

4. Use the following table to write the equations shown below in the cells indicated. 

   | Cell      | Equation                                                                          |
   |-----------|-----------------------------------------------------------------------------------|
   | C11       | D11 * $(\dfrac{\pi}{4}*(Diam1)^2)$   |
   | E11       | F11 * $(\dfrac{\pi}{4}*(Diam2)^2)$   |
   | G11       | H11 * $(\dfrac{\pi}{4}*(Diam3)^2)$   |
   | I11       | E11 - C11 - G11        |

5. Use **Goal seek** to compute the three unknown flowrates through setting Q_j (cell I11) to 0 by changing HGL_j (cell B11).

---

#### Part 2

1. Navigate to the **Simply Supported Beam** sheet
2. Name the cells in the spreadsheet according to this table:

**Hint:** You can edit cell names by navigating to the name box in the top left corner of the spreadsheet

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

4. Next, write an **IF** statement in cell **B16** that will return the value in cell **B14** if ***x≤a*** (B7) or cell **B15** if ***x>a*** (B7).

If written correctly, your sheet should look like this when **x** is set to **278** and **15**:

![Deflection1.png](images/Deflection1.png)![Deflection2.png](images/Deflection2.png)

5. The force of the load on the beam causes the deflection to take the shape of a parabola as shown in the diagram. Use **Goal seek** to compute the two **x** locations that result in a deflection of **-2.0** inches: one closer to the left support, and one closer to the right support. Record your answers in cells **B20** and **B21**.

**Hint:** Goal seek will find the answer closest to the pre-existing x value so to find the first solution, start with an x value near the left side, and to find the second solution, start with an x value near the right side. Your first solution should fall in the range between 30 and 40 inches while the second should fall in the range between 90 and 100 inches.

---

**Turn sharing and editing on. Turn in the link to Learning Suite in the feedback box**

---

**Rubric:**

|                         Item (Three Reservoir Problem)                    | Points Possible |
|:-------------------------------------------------------------------------:|:---------------:|
|                              Cells named correctly                        |        3        |
|                     Velocity equations written correctly                  |        4        |
|                     Flowrate equations written correctly                  |        4        |
|               The correct flowrates are found with goal seek (±2)         |        4        |
|              <div style="text-align: right">**Total**</div>               |       15        |

|               Item (Simply Supported Beam)                | Points Possible |
|:---------------------------------------------------------:|:---------------:|
|                   Cells named correctly                   |        3        |
|    Equations are written correctly and use cell names     |        4        |
|           The IF statement is written correctly           |        4        |
|   The two correct values are found with goal seek (±2)    |        4        |
|      <div style="text-align: right">**Total**</div>       |       15        |
