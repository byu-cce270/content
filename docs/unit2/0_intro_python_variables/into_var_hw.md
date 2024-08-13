#  HW: Introduction to Python and Variables

**Problem/Program:** Building an Open Channel Flow Calculator

**Purpose:** To use your knowledge of different variables to calculate the flow in an open channel. You will create different types of variables and then use them in equations.

**Challenge:** While working on this assignment, look through the code that was already written and try to see if you understand it. We will be teaching you about this later on. 

There are two common types of channel geometries: Rectangular and Trapezoidal as shown here:

![channel_flow_example.png](images/channel_flow_example.png)

## Instructions
1. First make a copy of the starter sheet here:
  <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/0_intro_python_variables/Starter_Sheet_HW_Introduction_to_Python_and_Variables.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
   </br> The original file should be called: **Starter Sheet HW - Introduction to Python and Variables**

2. Rename it something like “[your name] HW - Introduction to Python and Variables”

Don’t be too overwhelmed by the code. It will clearly indicate where to put different steps.

---
Step 3. Find the part of the code that looks like this:
> ################################ Step 3 here ##################################

Create the following variables with comments explaining the options:

| Variable name |                     Things the comments                     | Variable Type |
|:-------------:|:-----------------------------------------------------------:|:-------------:|
|     units     |                      english or metric                      |    string     |
|   material    | asphalt, concrete, clean earth, weedy earth, natural stream |    string     |
|       b       |                        bottom width                         |     float     |
|       T       |                          top width                          |     float     |
|      So       |                            slope                            |     float     |
|       y       |                         water depth                         |     float     |

Steps 4-10. Use the  following table to write equations in the indicated  places. They should be written under the ########### Step # ############# line:

|    Location     | Output Variable | Indentation |            Equation            |
|:---------------:|:---------------:|:-----------:|:------------------------------:|
| ### Step 4 ###  |        A        |     yes     |             A = by             |
| ### Step 5 ###  |        A        |     yes     |         A = (b+T)/2*y          |
| ### Step 6 ###  |        P        |     yes     |            P = b+2y            |
| ### Step 7 ###  |        P        |     yes     |  P = b+2*(((T-b)/2)^2+y^2)^.5  |
| ### Step 8 ###  |       Rh        |     no      |            Rh = A/P            |
| ### Step 9 ###  |        Q        |     no      | Q = (u/n)A(Rh^(2/3))*(So**.5)  |
| ### Step 10 ### |        V        |     no      |            V = Q/A             |

## Test Your Code
Try out your code! Use the following inputs:

| Variable name |   Input   |
|:-------------:|:---------:|
|     units     |  english  |
|   materials   | concrete  |
|       b       |    20     |
|       T       |    20     |
|      So       |   0.002   |
|       y       |     6     |

It should output something like this:
> Flow rate =  1608.38  cubic feet per second </br>
> Average velocity =  13.403  feet per second </br>
> u=  1.49  n=  0.012  A=  120.0  P=  32.0  Rh=  3.75  Q=  1608.380422171807  V=  13.403170184765058

## Turning in/Rubric
Turn sharing, editing on. Then turn in the link to learning suite in the feedback box

**Rubric:**

|                                                      Item                                                       | Points Possible |
|:---------------------------------------------------------------------------------------------------------------:|:---------------:|
| Input statements are made correctly, stored in the correct variable and are stored as the correct variable type |       15        |
|                     Equations are typed in correctly and are stored in the correct variable                     |       15        |