# HW: For Loops

---

**Purpose:** Learn how to use for loops to analyze lists. You will work with a list of beams and use for loops to 
calculate and print the deflection of the beams. Assume that the beams are cantilevered with a point load at some 
distance **a** from the fixed side on the left as shown in the following diagram. 

![image](https://www.vcalc.com/attachments/f79744e5-e005-11e3-b7aa-bc764e2038f2/CantileverBeamConcentratedloadPatanypoint-illustration.png)

The deflection at the end of the beam is given by the following equation:

>>$\delta_{max}=\dfrac{Pa^2}{6EI}\left(3l-a\right)$

where:

>>$\delta_{max}$ = the maximum deflection at the end of the beam<br>
$P$ = the point load<br>
$a$ = the distance from the fixed side to the point load<br>
$l$ = the length of the beam<br>
$E$ = the modulus of elasticity<br>
$I$ = the moment of inertia

For multiple loads, the total deflection is the sum of the deflections due to each individual load. For this assignment, you will analyze a list of beams and calculate the deflection of each beam. For each beam, you will calculate the total deflection due to multiple loads using the equation above.

---

**Instructions**

1.  Create a copy of the starter sheet and rename it something like "[Your Name] HW 2.3 - For Loops"
<a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/02_for_loops_into_functions/for_loops_hw.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
2. Follow the instructions on the notebook.
3. When you are finished, turn sharing and editing on, and then turn in the link to your notebook to Learning Suite in 
   the feedback box.

---

**Turn sharing and editing on. Turn in the link to Learning Suite in the feedback box**

---

**Rubric:**

|                                            Lists                                                     | Points Possible |
|:----------------------------------------------------------------------------------------------------:|:---------------:|
|              In the 1st code block, a value of 5.7 is appended to the beam_lengths list              |        2        |
|                  Variable created to store the value of total length of the beam                     |        2        |
|                     For loop created to calculate the total length of the beam                       |        5        |
|                            Average length of the beams is calculated                                 |        2        |
|                For loop created to count the number of beams longer than 5 meters                    |        5        |
|                         Print statements created to output the results                               |        2        |
|                   In the 2nd code block, the last length in the list is deleted                      |        2        |
|                     A variable is created to store the deflection of the beam                        |        2        |
|                   For loop is created to calculate the deflection of each beam                       |        5        |
|        Print statements created that specify the length of the beam and the total deflection         |        3        |
|                          <div style="text-align: right">**Total**</div>                              |       30        |

The following is not apart of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                      **Reasons for Points Lost**                      | **Amount** |  
|:---------------------------------------------------------------------:|:----------:|
| No comments explaining why AI is used and what its provided code does |    2-3     |
|                        Link shared incorrectly                        |     3      |
|       Turned in late. 10% or 3 points for every week it's late.       |    3-15    |
