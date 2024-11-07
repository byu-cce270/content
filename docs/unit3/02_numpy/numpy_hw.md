# HW: Numpy

**Purpose:** Learn how to use arrays and create and solve a system of linear equations.

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit3/02_numpy%5BYour_Name%5D_HW_3_3_Numpy.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "[Your Name] HW 3.3 - Numpy"

For this assignment, imagine that there is a hypothetical company called Computer Methods Incorporated, CMI for short. CMI makes a total of 3 different products at their factories. Each product requires a certain amount of labor hours, equipment hours, and units of material per unit to make as shown below.

|                   | Product 1 | Product 2 | Product 3 |
|-------------------|:---------:|:---------:|:---------:|
| Labor Hours       |     4     |     7     |     1     |
| Equipment Hours   |     5     |     2     |     4     |
| Units of Material |     3     |     8     |     6     |

CMI has limited resources that they can use per day across all of their products. CMI currently has 161 labor hours, 122 equipment hours, and 204 units of material available to them per day. They have hired you to find quantities of each product they can make per day while maximizing the use of their resources. Luckily, you took a coding class in college and know exactly how to solve this problem. The steps are as follows:

---

#### Part 1
 
1. Import the numpy library into your notebook in the first code block
2. Create your system of linear equations. (This is already done for you in the starter sheet.) In this system are variables represent the number of units made for each product. Product 1, Product 2, and Product 3 being represented by variables x, y, and z respectively.
3. Convert the system of linear equations into arrays. The first array will only contain the values in the table above and will be presented almost like a list of lists. The second will contain the values of our resources available.
4. Use the numpy function linalg.solve to solve our system of linear equations. This should output the number of units we can make of each product. If your code was written correctly, you should be able to make 12 units of product 1, 15 units of product 2, and 8 units of product 3.
5. Write print statements to display the information from step 4 in a way that is clear. Also include information about the actual amounts of resources used to make that many units of each product.

---

#### Part 2

To understand better what is happening we are going to plot modified equations. They need to be modified because there is not a way to show three dimensional lines; however, the second set of linear equation given should have the same solutions for the remaining variables.

7. Create the x plot points using the numpy function linspace. Zero to twenty is a good range for this assignment.
8. Solve each of our linear equation for y and input those formulas as variable y_1, y_2, and y_3 respectively.
9. Plot the three linear equations with the values for x and y. This will need to be done on three lines of code for y_1, y_2, and y_3. Notice that the intersection of these lines is at x = 12 and y = 15.
10. Write comments explaining your code because even the best coders forget what their code does.

---

# Turning In/Rubric

Turn on sharing and editing. Turn in the link to the Learning Suite feedback box

|                **Part 1 Items**                | **Amount** |  
|:----------------------------------------------:|:----------:|
|        First array is created correctly        |     9      |
|       Second array is created correctly        |     6      |
|  Amount of units of product made are correct   |     6      |
| Units produced are displayed in a clear manner |     3      |
| Actual amounts of resources used are displayed |     3      |
|       Comments are added to explain code       |     3      |
| <div style="text-align: right">**Total**</div> |   **30**   |


The following is not apart of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.


|                      **Reasons for Points Lost**                      | **Amount** |  
|:---------------------------------------------------------------------:|:----------:|
| No comments explaining why AI is used and what its provided code does |    2-3     |
|                        Link shared incorrectly                        |     3      |
|       Turned in late. 10% or 3 points for every week it's late.       |    3-15    |




