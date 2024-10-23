#  HW: Functions (Part 2)

**Purpose:** Learn how to use functions to create more simplified blocks of code

##  Instructions
1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/06b_functions/functions2_hw.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "[Your Name] HW 2.6b - Functions (Part 2)"

In this assignment, you will be creating code that will allow a user to find the maximum deflection and maximum bending stress on a beam given these six scenarios:

Scenario 1: Cantilever beam with a moment load

Scenario 2: Cantilever beam with a point load

Scenario 3: Cantilever beam with a distributed load

Scenario 4: Simply supported beam with a moment load

Scenario 5: Simply supported beam with a point load

Scenario 6: Simply supported beam with a distributed load

---

#### Part 1

1. In the first code block, write six appropriately named functions that calculate and return the deflection and moment for each beam scenario shown in the chart below. Your parameters will be the variables corresponding to each scenario's max deflection and max bending moment.

    ![beamchart.png](images/beamchart.png)

2. Create a seventh function that calculates and returns the moment of inertia using this formula:

    $$\ I=\frac{bh^3}{12} \$$

3. Create an eighth function that calculates and returns maximum bending stress using this formula:

     $$\sigma_{max}=\frac{My}{I}\$$

#### Part 2

1. In the second code block, create the following input statements:

   | Variable Name |                            Prompt                           | Variable Type |
   |:-------------:|:-----------------------------------------------------------:|:-------------:|
   |   beam_type   | Asks what the beam type is (cantilever or simply supported) |    string     |
   |   load_type   | Asks what the load type is (moment, point, or distributed)  |    string     |

2. On a new line, create IF and ELIF statements that check if the load_type entered is a moment, a point, or a distributed load. Depending on which load_type is entered, your IF and ELIF statements will return one of the following input statements:

   | Variable Name |                            Prompt                           | Variable Type |
   |:-------------:|:-----------------------------------------------------------:|:-------------:|
   |  moment_load  |    Asks what the value of the moment load is (in lb-in)     |     float     |
   |   point_load  |      Asks what the value of the point load is (in lb)       |     float     |
   |   dist_load   |  Asks what the value of the distributed load is (in lb/in)  |     float     |

3. On a new line, create the following input statements:

   | Variable Name |                            Prompt                           | Variable Type |
   |:-------------:|:-----------------------------------------------------------:|:-------------:|
   |       L       |        Asks what the length of the beam is (in inches)      |     float     |
   |       E       |        Asks what the modulus of elasticity is (in psi)      |     float     |
   |       b       |         Asks what the base of the beam is (in inches)       |     float     |
   |       h       |        Asks what the height of the beam is (in inches)      |     float     |
   

