# HW: Numpy

**Purpose:** Learn how to use arrays and create and solve a system of linear equations.

## Instructions

1. First, make a copy of the starter sheet here: <a href="Add link here" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "[Your Name] HW 3.3 - Numpy"

For this assignment, imagine that there is a hypothetical company called Computer Methods Incorporated, CMI for short. CMI makes a total of 3 different products at their factories. Each product requires a certain amount of labor hours, equipment hours, and units of material per unit to make as shown below.

|                   | Product 1 | Product 2 | Product 3 |
|-------------------|:---------:|:---------:|:---------:|
| Labor Hours       |     4     |     7     |     1     |
| Equipment Hours   |     5     |     2     |     4     |
| Units of Material |     3     |     8     |     6     |

CMI has limited resources that they can use per day across all of their products. CMI currently has 161 labor hours, 122 equipment hours, and 204 units of material available to them per day. They have hired you to find quantities of each product they can make per day while maximizing the use of their resources. Luckily, you took a coding class in college and know exactly how to solve this problem. The steps are as follows:

1. Import the numpy library into your notebook in the first code block
2. Create your system of linear equations. (This is already done for you in the starter sheet.) In this system are variables represent the number of units made for each product. Product 1, Product 2, and Product 3 being represented by variables x, y, and z respectively.
3. Convert the system of linear equations into arrays. The first array will only contain the values in the table above and will be presented almost like a list of lists. The second will contain the values of our resources available.
4. Use the numpy function linalg.solve to solve our system of linear equations. This should output the number of units we can make of each product. If your code was written correctly, you should be able to make 12 units of product 1, 15 units of product 2, and 8 units of product 3.
5. Write print statements to display the information from step 4 in a way that is clear. Also include information about the actual amounts of resources used to make that many units of each product.
6. Write comments explaining your code.

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
