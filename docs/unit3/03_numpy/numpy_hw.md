# HW: Numpy

**Purpose:** Create and use numpy arrays to find the forces in a given truss. You will then use matplot to graph it.

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit3/02_numpy%5BYour_Name%5D_HW_3_3_Numpy.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "[name] hw 3.3 numpy"

For this assignment, Dr. Doofenshmirtz is partnering with BYU to create a new roof for his building. Instead of a dome, he wants to be fancy and install a triangle roof. He needs you to find the internal forces in each of the segments of his roof truss to ensure it will not collapse. Here is the design of the trusses for his roof:

<center>
    <img src="https://github.com/user-attachments/assets/d297256a-4b28-4dee-9d92-e634e1cc7d2d" width="60%" height="60%" alt = "Centered Image">
</center>

_(image updated fron [trussanalysis.com](https://trussanalysis.com/?cat=custom&cmems=0~1~5~29000_0~2~5~29000_1~2~5~29000&cnodes=0~0~p~0~0_4~4~f~0~0_8~0~r~0~0))_

Where:
  - LAB is an unknown length of segment AB
  - θ_A and θ_C are unknown angles at points A and C respectively
  - P is a load being applied at point B acting downward (denoted with the red arrow)
  - Joint A has a pin joint (only forces in the x and y direction)
  - Joint C has a roller (only forces in the x direction)


Using the Method of Joints we derive the following equations:


$$\sum F_{A_x} = ABcos(θ_A) + AC+R_{A_x} = 0$$
$$\sum F_{A_y} = ABsin(θ_A) + R_{A_y} = 0$$
$$\sum F_{B_x} = -ABcos(θ_A) + BCcos(θ_C) = 0$$
$$\sum F_{B_y} = -ABsin(θ_A) - BCcos(θ_C) = -P$$
$$\sum F_{C_x} = -BCcos(θ_C) - AC = 0$$
$$\sum F_{C_y} = BCsin(θ_C) + R_{C_y} = 0$$

We can then use these equations to solve for our unknown forces in $$\ AB, AC, BC, R_{A_x}, R_{A_y}$$. Typically this could take a long time when doing it by hand, but can be solved in seconds with some code! The way we go about this is by setting up our forces as a system of equations. These can be written in matrix form as:

$$
\begin{bmatrix} 
\cos(\theta_A) & 0 & 1 & 1 & 0 & 0 \\ 
\sin(\theta_A) & 0 & 0 & 0 & 1 & 0 \\ 
-\cos(\theta_A) & \cos(\theta_C) & 0 & 0 & 0 & 0 \\ 
-\sin(\theta_A) & -\sin(\theta_C) & 0 & 0 & 0 & 0 \\ 
0 & -\cos(\theta_C) & -1 & 0 & 1 & 0 \\ 
0 & \sin(\theta_C) & 0 & 0 & 0 & 1 
\end{bmatrix}
\begin{bmatrix}
AB \\
AC \\
BC \\
R_{C_y} \\
R_{A_x} \\
R_{A_y}
\end{bmatrix} =
\begin{bmatrix}
0 \\
0 \\
0 \\
-P \\
0 \\
0
\end{bmatrix}
$$

This may seem daunting! But it can be rather simple. Let's jump into it!

---

#### Part 1: Solve for the Forces in each segment
 
1. Import the numpy and matplot library into your notebook.
2. In the next code block, create a function that will take in 3 parameters: the angle at joint A (θA), the angle at joint B (θB), and the load at joint B (P) to find the forces of each member.
3. Because Numpy works in radians and not degrees, convert the given theta values for A and C from degrees to radians. Save those values into variables.
4. F is the solutions dictionary. The current value for each key is initialized to 0 to start with. You will then solve for the forces and then update each key with its respective value.
5. Under the Forces sums comment contains the sum of the forces for each joint for both the x and y direction. Create a numpy array for joint A in both the x an y direction using the table below. For example, I would create 2 separate arrays, one for the x and y direction. I would then input the data on the F<sub>Ax</sub> row in the table for the F_ax variable. Then I would input the data on the F<sub>Ay</sub> row from the table for the F_ay variable. Repeat for joints B and C. 

|                           |             AB            |             BC            | AC | R<sub>A<sub>x</sub></sub> | R<sub>A<sub>y</sub></sub> | R<sub>C<sub>y</sub></sub> |
|:-------------------------:|:-------------------------:|:-------------------------:|:--:|:-------------------------:|:-------------------------:|:-------------------------:|
| F<sub>A<sub>x</sub></sub> |  cos(&theta;<sub>A</sub>) |             0             |  1 |             1             |             0             |             0             |
| F<sub>A<sub>y</sub></sub> |  sin(&theta;<sub>A</sub>) |             0             |  0 |             0             |             1             |             0             |
| F<sub>B<sub>x</sub></sub> | -cos(&theta;<sub>A</sub>) |  cos(&theta;<sub>C</sub>) |  0 |             0             |             0             |             0             |
| F<sub>B<sub>y</sub></sub> | -sin(&theta;<sub>A</sub>) | -sin(&theta;<sub>C</sub>) |  0 |             0             |             0             |             0             |
| F<sub>C<sub>x</sub></sub> |             0             | -cos(&theta;<sub>C</sub>) | -1 |             0             |             0             |             0             |
| F<sub>C<sub>y</sub></sub> |             0             |  sin(&theta;<sub>C</sub>) |  0 |             0             |             0             |             1             |


6. Put all of the force sums array into a new array. This represents the total force matrix of the truss.
7. Now, create a new array for the external forces acting on the truss using the table below:

|                           | Loads |
|:-------------------------:|:-----:|
| F<sub>A<sub>x</sub></sub> |   0   |
| F<sub>A<sub>y</sub></sub> |   0   |
| F<sub>B<sub>x</sub></sub> |   0   |
| F<sub>B<sub>y</sub></sub> |  -P   |
| F<sub>C<sub>x</sub></sub> |   0   |
| F<sub>C<sub>y</sub></sub> |   0   |

8. Solve the system of equations with the combined forces array and the loads array as the inputs
9. Write a loop that with update the values of the solutions dictionary with the solutions you got from your system of equations, and print out their associated values. For example, my print statement would say somthing like "AB = 3000 lbs", "R_AY = -200 lbs" when displayed.
10. Return your solutions dictionary. This will be used later :)

---

#### Part 2: Find Coordinates of each point

Now that you have all of the forces, Dr. Doofenshirtz need to know how tall his roof is going to be. This will involve solving for the x and y coordinates of joints A, B, and C.
1. Create a new function that will take in 3 parameters: angle A, Angle C, and the length of AC. This function will solve for the y and x values of each joint. (We will say that A is the origin)
2. Since we are only given theta A and theta B, solve for theta B
3. Convert theta A, B, and C from degrees to radians (since this is that Numpy does its calculations in)
4. Time to bring back your geometry skills, now that you know all of your angles and one side length you can use the law of sines to solve for the other lengths. Save each length of the truss in their own vairables.

Here is the law of sines for reference:

<img src="https://github.com/user-attachments/assets/99d5bbfa-fc1a-4873-b687-679e7e139e52" width="70%" height="70%" align = "center">

_(image from [CalcWorkshop](https://calcworkshop.com/law-sines-cosines/law-of-sines/))_


8. Solve each of our linear equation for y and input those formulas as variable y_1, y_2, and y_3 respectively.
9. Plot the three linear equations with the values for x and y. This will need to be done on three lines of code for y_1, y_2, and y_3. Notice that the intersection of these lines is at x = 12 and y = 15.
10. Write comments explaining your code because even the best coders forget what their code does.

---

# Turning In/Rubric

Turn on sharing and editing. Turn in the link to the Learning Suite feedback box

|                **Items**                       | **Amount** |  
|:----------------------------------------------:|:----------:|
|        First array is created correctly        |     9      |
|       Second array is created correctly        |     3      |
|  Amount of units of product made are correct   |     6      |
| Units produced are displayed in a clear manner |     3      |
| Actual amounts of resources used are displayed |     3      |
| Second linear equations are graphed correctly  |     3      |
|       Comments are added to explain code       |     3      |
| <div style="text-align: right">**Total**</div> |   **30**   |


The following is not apart of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.


|                      **Reasons for Points Lost**                      | **Amount** |  
|:---------------------------------------------------------------------:|:----------:|
| No comments explaining why AI is used and what its provided code does |    2-3     |
|                        Link shared incorrectly                        |     3      |
|       Turned in late. 10% or 3 points for every week it's late.       |    3-15    |




