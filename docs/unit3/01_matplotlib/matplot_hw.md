# HW: Matplotlib

**Purpose:** Learn how to read in data from Google Sheets and make graphs from it

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit3/01_matplotlib/(Starter_Notebook)_HW_Matplotlib.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "(Your_Name)_HW_Matplotlib.ipynb"

3. Download each CSV. You will use one for each problem:

    * [2013-2014 Pasadena Temperatures.csv](2013-2014%20Pasadena%20Temperatures.csv)
    * [June 2021 Provo River Streamflow Rates.csv](June%202021%20Provo%20River%20Streamflow%20Rates.csv)
    * [2012 U.S. Birth Rates.csv](2012%20U.S.%20Birth%20Rates.csv)

In this assignment, you will be creating graphs of historical weather data in Pasadena, CA, Provo River flowrate data, and U.S. Birth Rates.

---

#### Part 1 - Shear and Moment Diagrams

For this exercise, we will be creating shear and moment diagrams for a simply supported beam. Such diagrams are used to better visualize the internal forces acting within the beam. The shear along the beam is represented by the variable $V$, while the moment along the beam is represented by the variable $M$. The shear diagram for the beam below is represented by the green graph while the moment diagram is represented by the red graph. 

![shear_moment_example.png](images/shear_moment_example.png)

(image from https://mechanicalc.com/reference/beam-analysis)

We will be graphing the diagrams for the cantilevered simply supported beam shown below:

![beam.png](images/beam.png)

Where:
  - $L$ is the full length of the beam
  - $x$ is any point taken along the beam measured from its left end
  - $A$ is the pin support of the beam located at $x=0 ft$  
  - $B$ is the roller support of the beam located at $x=4 ft$ 
  - $R_{A}$ is the reaction force of 170 $lb$ associated with the pin support located at $x=0 ft$
  - $R_{B}$ is the reaction force of 410 $lb$ associated with the roller support located at $x=4 ft$
  - $P_{1}$ is a point load of 100 $lbf$ acting at $x=2 ft$
  - $q_{1}$ is a distributed load of 120 $lb/ft$ per foot acting from $x=0 ft$ to $x=2 ft$
  - $q_{2}$ is a distributed load of 120 $lb/ft$ per foot acting from $x=4 ft$ to $x=6 ft$

1. In the 'Part 1a - Shear Diagram' code block, define the following variables:

| Variable |    Value    |
|:--------:|:-----------:|
|   $L$    |   6 $ft$    |
|  $R_A$   |  170 $lb$   |
|  $R_B$   |  410 $lb$   |
|  $P_1$   |  100 $lb$   |
|  $q_1$   | 120 $lb/ft$ |
|  $q_2$   | 120 $lb/ft$ |

2. Define a variable ```x``` using ```np.linspace()``` with the following arguments:
  - start: 0
  - stop: L
  - num: 500

3. Define a variable ```V``` using ```np.zeros_like()``` with ```x``` as the argument. This will create a list of zeros with the same length as ```x```. 
4. Create a for loop that loops over the length of ```x``` and defines ```V``` to be the following piecewise function under the respective boundary conditions:

$$
V(x) =
\begin{cases}
x^2, & \text{if } x > 1 \\
2x + 3, & \text{if } 0 \le x \le 1 \\
-4, & \text{if } x < 0
\end{cases}
$$

#### Part 2 - Pasadena Precipitation Data

You will now graph the temperature data from Pasadena, CA from 2013-2014. The data is from 2013-2014 and includes the high and low temperatures for each day. We added the numpy code to create the data arrays for you to make plotting easier. We created an array for the x-data called ```x```, an array for the high temperature data called ```y_1```, and an array for the low temperature data called ```y_2```. You will need to plot the data as lines, add labels, titles, and other elements to make the graph look nice. You will  need to rotate the x-axis ticks so they are readable. Add a legend to the graph and grid lines and change the font size.

1. In the 'Graphing the Data' code block, three lists are referenced from the 'Numpy Array Creation & Slicing' block above. These are 'x', 'y_1', and 'y_2'
2. Plot a replica of the graph below - it should look something like this:

    ![pasadenagraph.png](images/pasadenagraph.png)

#### Part 2 - Provo River Streamflow Data

In Part 2, we have provided numpy code to create the variables for the Provo River Streamflow Data. We created an array for the x-data called ```x```, and arrays for the streamflow data for five different sites called ```y_1```, ```y_2```, ```y_3```, ```y_4```, and ```y_5```. You will need to plot the data as lines, add labels, titles, and other elements to make the graph look nice. You will need to rotate the x-axis ticks so they are readable. Add a legend to the graph and grid lines and change the font size.

1. In the 'Graphing the Data' code block, three lists are referenced from the 'Numpy Array Creation & Slicing' block above. These are 'x', 'y_1', 'y_2', 'y_3', 'y_4', and 'y_5'
2. Plot a replica of the graph below - it should look something like this:

    ![streamflowgraph.png](images/streamflowgraph.png)

#### Part 3 - Average U.S. Daily Birth Data
Part 3 is similar, we give you numpy code to create the plotting variables similar to the last two plots. However, this time we want you to annotate some interesting data in the graph. We give you a list of dates to annotate with their holiday names. We used a number of different arrow styles to show you some options. The pre-class reading has a link to the documentation for the annotate function with some examples of different arrow properties you can use. You don't need to match our arrow styles, but you should use the annotate function to point to the holidays.

After you annotate the graph, we ask you to explain the drop in birth rates on those days? You don't have to know the answer, but you should be able to make a guess based on the data. **These are real data** not made up for the assignment.

1. In the 'Graphing the Data' code block, three lists are referenced from the 'Numpy Array Creation & Slicing' block above. These are 'x' and 'y_1'.
2. Plot a replica of the graph below - it should look something like this:

!!! Hint
   In your first line, enter `plt.figure(figsize=(12, 4))` to create the correct size for your plot.

![birthgraph.png](images/birthgraph.png)

3. Write a comment explaining why you think the birth rate drops during those days



---

## Turning in/Rubric

**_REMINDER_** - For this class, **you will only turn in the links to your colab notebooks**. You will get a 0 for this assignment if you turn in a python file or a link that is not correct, wrong assignment, or does not give editor permission.

**Rubric:**

|                     **Item**                      | **Amount** |  
|:-------------------------------------------------:|:----------:|
|           CSV files are correctly read            |     3      |
| The temperature data graph has all elements shown |     8      |
| The streamflow data graph has all elements shown  |     8      |
|    The birth data graph has all elements shown    |     8      |
|       The annotations are created correctly       |     3      |
|  <div style="text-align: right">**Total**</div>   |   **30**   |

---

The following is not a part of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                       **Reasons for Points Lost**                       |    **Amount**     |  
|:-----------------------------------------------------------------------:|:-----------------:|
|                         Link shared incorrectly                         |       -10%        |
|                        Turned in late (per week)                        | -10% (up to -50%) |
| No comments explaining where AI is used and what its provided code does |       -10%        |