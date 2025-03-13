# HW: Numpy

**Purpose: ** Create and use numpy arrays to find the forces in a given truss. You will then use matplot to graph it.

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit3/02_numpy%5BYour_Name%5D_HW_3_3_Numpy.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "[name] hw 3.3 numpy"

For this assignment, Dr. Doofenshmirtz is partnering with BYU to create a new roof for his building. Instead of a dome, he wants to be fancy and install a triangle roof. He needs you to find the forces in each part of the roof to make sure it will not collapse. Here is the design of his roof:

<img src="https://github.com/user-attachments/assets/12c8eb8b-0bb5-47b5-9a19-23e8e706872c" width="70%" height="70%" align = "center">

Where:
- Joints A, B, and C are where the segments intersect.
- LAB is an unknown length of segment AB
- θA and θC are unknown angles at points A and C respectively
- P is the load being applied at point B acting downward (hence the downward red arrow)
- Joint A has a pin joint (forces in the x and y direction)
- Joint C has a roller (only forces in the x direction)

---

#### Part 1: Solve for the Forces in each segment
 
1. Import the numpy and matplot library into your notebook in the first code block.
2. In the next code block, create a function that will take in 3 parameters: the angle at joint A (θA), the angle at joint B (θB), and the load at joint B (P) to find the forces of each member.
3. Because Numpy works in radians and not degrees, convert the given theta values for A and C from degrees to radians. Save those values into variables.
4. F is the solutions dictionary. The current value for each key is initialized to 0 to start with. You will then solve for the forces and then update each key with its respective value.
5. Under the Forces sums comment contains the sum of the forces for each joint for both the x and y direction. Create a numpy array for each joint in each direction. For example, for joint A, I would create 2 separate arrays, one for the x and y direction. I would then input the data on the F_Ax row in the table for the F_ax variable. Then I would input the data on the F_Ay ron 

|                           |             AB            |             BC            | AC | R<sub>A<sub>x</sub></sub> | R<sub>A<sub>y</sub></sub> | R<sub>C<sub>y</sub></sub> |
|:-------------------------:|:-------------------------:|:-------------------------:|:--:|:-------------------------:|:-------------------------:|:-------------------------:|
| F<sub>A<sub>x</sub></sub> |  cos(&theta;<sub>A</sub>) |             0             |  1 |             1             |             0             |             0             |
| F<sub>A<sub>y</sub></sub> |  sin(&theta;<sub>A</sub>) |             0             |  0 |             0             |             1             |             0             |
| F<sub>B<sub>x</sub></sub> | -cos(&theta;<sub>A</sub>) |  cos(&theta;<sub>C</sub>) |  0 |             0             |             0             |             0             |
| F<sub>B<sub>y</sub></sub> | -sin(&theta;<sub>A</sub>) | -sin(&theta;<sub>C</sub>) |  0 |             0             |             0             |             0             |
| F<sub>C<sub>x</sub></sub> |             0             | -cos(&theta;<sub>C</sub>) | -1 |             0             |             0             |             0             |
| F<sub>C<sub>y</sub></sub> |             0             |  sin(&theta;<sub>C</sub>) |  0 |             0             |             0             |             1             |


6. Convert the system of linear equations into arrays. The first array will only contain the values in the table above and will be presented almost like a list of lists. The second will contain the values of our resources available.
7. Use the numpy function linalg.solve to solve our system of linear equations. This should output the number of units we can make of each product. If your code was written correctly, you should be able to make 12 units of product 1, 15 units of product 2, and 8 units of product 3.
8. Write print statements to display the information from step 4 stating how much of each product can be made. Also include information about the actual amounts of labor hours, equipment hours, and units of materials used to make that many units of each product.

---

#### Part 2

To understand better what is happening we are going to plot modified equations. They need to be modified because there is not a way to show three dimensional lines; however, the second set of linear equation given should have the same solutions for the remaining variables.

7. Create the x plot points using the numpy function arrange or linspace. Zero to twenty is a good range for this assignment.
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




