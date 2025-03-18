# In-Class Exercise: NumPy

The following exercises will have you create and manipulate arrays. For this exercise, open the in-class workbook, make a copy, and follow the instructions.

You can find the In Class Exercise here:
<a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit3/03_numpy
/[your_name]_3_3_numpy_in_class.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.
svg" alt="Open In Colab"/></a>

## Instructions
1. Open the in-class workbook using the link above.
2. Rename the notebook with your name.
3. Follow the instructions in the notebook to complete the exercise.

---

## Vectorized Operations in NumPy

NumPy is a powerful library for numerical computing in Python. One of the key features of NumPy is its ability to perform vectorized operations on arrays. Vectorized operations are operations that are applied to each element of an array. For example, if you have two arrays `a` and `b`, you can add them together element-wise using the `+` operator:

```python   
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = a + b
print(c)  # Output: [5 7 9]
```
---
# Last part in In-Class Exercise Explanation


## Truss Analysis with NumPy
![truss.png](Images%2Ftruss.png){:width="500px"}

We will use a truss as an example of solving simultaneous equations. A truss is a structure made up of members that are connected at their ends. The members are usually made of steel or wood and are used to support loads. The truss in the image above is a simple truss with three members and three joints. The members are labeled AB, BC, and AC. The joints are labeled A, B, and C. The loads are applied at joint B and joint C.

To create mathematical equations to solve a truss, we need to express the forces in terms of the given angles and loads. Here are the equations derived from the matrices:

### Equilibrium Equations

1. Sum of Forces in the x-direction for each joint have to equal 0:

    $F_{A_x}: \cos(\theta_A) \cdot F_{AB} + 1 \cdot F_{AC} + 1 \cdot R_{A_x} = 0$

    $F_{B_x}: -\cos(\theta_A) \cdot F_{AB} + \cos(\theta_C) \cdot F_{BC} = 0$

    $F_{C_x}: -\cos(\theta_C) \cdot F_{BC} - 1 \cdot F_{AC} = 0$


2. Sum of Forces in the y-direction for each joint have to equal 0:

    $F_{A_y}: \sin(\theta_A) \cdot F_{AB} + 1 \cdot R_{A_y} = 0$

    $F_{B_y}: -\sin(\theta_A) \cdot F_{AB} - \sin(\theta_C) \cdot F_{BC} = -P$

    $F_{C_y}: \sin(\theta_C) \cdot F_{BC} + 1 \cdot R_{C_y} = 0$



We can now "line up" the equations in a matrix form to solve for the unknowns. 

To insert the LaTeX code into a Markdown document using the $$ equation markers, you can wrap the entire code block with double dollar signs. Here's how you can do it:


Sure! Here's the LaTeX code with spaces added between the terms to ensure they line up vertically:


Sure! Here's the updated LaTeX code with the \( R_{A_x} \), \( R_{A_y} \), and \( R_{C_y} \) terms lined up vertically:


Got it! Here's the updated LaTeX code with missing terms multiplied by 0 and the equals signs lined up:


Got it! Here's the updated LaTeX code with each equation including all three \( R \) terms, multiplied by 0 if they don't exist, and the equals signs lined up:


$$
\begin{equation}
\begin{pmatrix}
\cos(\theta_A) \cdot F_{AB} &+ 1 \cdot F_{AC} &+ 0 \cdot F_{BC} &+ 1 \cdot R_{A_x} &+ 0 \cdot R_{A_y} &+ 0 \cdot R_{C_y} &= 0 \\
-\cos(\theta_A) \cdot F_{AB} &+ 0 \cdot F_{AC} &+ \cos(\theta_C) \cdot F_{BC} &+ 0 \cdot R_{A_x} &+ 0 \cdot R_{A_y} &+ 0 \cdot R_{C_y} &= 0 \\
0 \cdot F_{AB} &- 1 \cdot F_{AC} &- \cos(\theta_C) \cdot F_{BC} &+ 0 \cdot R_{A_x} &+ 0 \cdot R_{A_y} &+ 0 \cdot R_{C_y} &= 0 \\
\sin(\theta_A) \cdot F_{AB} &+ 0 \cdot F_{AC} &+ 0 \cdot F_{BC} &+ 0 \cdot R_{A_x} &+ 1 \cdot R_{A_y} &+ 0 \cdot R_{C_y} &= 0 \\
-\sin(\theta_A) \cdot F_{AB} &+ 0 \cdot F_{AC} &- \sin(\theta_C) \cdot F_{BC} &+ 0 \cdot R_{A_x} &+ 0 \cdot R_{A_y} &+ 0 \cdot R_{C_y} &= -P \\
0 \cdot F_{AB} &+ 0 \cdot F_{AC} &+ \sin(\theta_C) \cdot F_{BC} &+ 0 \cdot R_{A_x} &+ 0 \cdot R_{A_y} &+ 1 \cdot R_{C_y} &= 0
\end{pmatrix}
\end{equation}
$$




The matrix form of the equations is:
Sure! Here's the LaTeX code for the matrices that you can insert into a Markdown document:


$$
\begin{pmatrix}
\cos(\theta_A) & 1 & 0 & 1 & 0 & 0 \\
-\cos(\theta_A) & 0 & \cos(\theta_C) & 0 & 0 & 0 \\
0 & -1 & -\cos(\theta_C) & 0 & 0 & 0 \\
\sin(\theta_A) & 0 & 0 & 0 & 1 & 0 \\
-\sin(\theta_A) & 0 & -\sin(\theta_C) & 0 & 0 & 0 \\
0 & 0 & \sin(\theta_C) & 0 & 0 & 1
\end{pmatrix}
\begin{pmatrix}
F_{AB} \\
F_{AC} \\
F_{BC} \\
R_{A_x} \\
R_{A_y} \\
R_{C_y}
\end{pmatrix}
=
\begin{pmatrix}
0 \\
0 \\
0 \\
0 \\
-P \\
0
\end{pmatrix}
$$

The unknowns are the forces in the members and the reactions at the supports. The knowns are the loads and the angles. We can use NumPy to solve for the unknowns, which are:

Certainly! Here's the LaTeX code for the \( F \) matrix that you can insert into a Markdown document:


$$
\begin{pmatrix}
F_{AB} \\
F_{AC} \\
F_{BC} \\
R_{A_x} \\
R_{A_y} \\
R_{C_y}
\end{pmatrix}
$$

Now we can arrange as a table to see the relationships see how we might solve for the unknowns.

In Statics, you now would need to use algebra to solve for the unknowns. This can take a very long time.  But with NumPy, if you can write down the equations,  we can use matrix operations to solve for the unknowns.

|                           |             AB            |             BC            | AC | R<sub>A<sub>x</sub></sub> | R<sub>A<sub>y</sub></sub> | R<sub>C<sub>y</sub></sub> |
|:-------------------------:|:-------------------------:|:-------------------------:|:--:|:-------------------------:|:-------------------------:|:-------------------------:|
| F<sub>A<sub>x</sub></sub> |  cos(&theta;<sub>A</sub>) |             0             |  1 |             1             |             0             |             0             |
| F<sub>A<sub>y</sub></sub> |  sin(&theta;<sub>A</sub>) |             0             |  0 |             0             |             1             |             0             |
| F<sub>B<sub>x</sub></sub> | -cos(&theta;<sub>A</sub>) |  cos(&theta;<sub>C</sub>) |  0 |             0             |             0             |             0             |
| F<sub>B<sub>y</sub></sub> | -sin(&theta;<sub>A</sub>) | -sin(&theta;<sub>C</sub>) |  0 |             0             |             0             |             0             |
| F<sub>C<sub>x</sub></sub> |             0             | -cos(&theta;<sub>C</sub>) | -1 |             0             |             0             |             0             |
| F<sub>C<sub>y</sub></sub> |             0             |  sin(&theta;<sub>C</sub>) |  0 |             0             |             0             |             1             |

|                           | Loads |
|:-------------------------:|:-----:|
| F<sub>A<sub>x</sub></sub> |   0   |
| F<sub>A<sub>y</sub></sub> |   0   |
| F<sub>B<sub>x</sub></sub> |   0   |
| F<sub>B<sub>y</sub></sub> |  -P   |
| F<sub>C<sub>x</sub></sub> |   0   |
| F<sub>C<sub>y</sub></sub> |   0   |

---

For the in-class, and homework exercises, you will be given the equations and the knowns. you will need to use NumPy to solve for the unknowns.

---



## Turning in/Rubric
Turn sharing and editing on, then submit the link to Learning Suite in the feedback box. In-class assignment scores are based on valid effort and completion.
