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
# Speed of vectorized operations
Numpy vectorization is much faster than using a for loop to iterate over the elements of an array. This is because NumPy uses optimized C code to perform the operations, whereas a for loop in Python is interpreted and slower. Here is an example of how much faster NumPy vectorization is compared to a for loop. We create two numpy arrays with 1 million members each and add them together using both a for loop and NumPy vectorization. We then use the `%timeit` command to measure the time it takes to run each operation. :

```python
import numpy as np

# function to add two arrays using loops
def plusarray(x1, x2):
  x3 = np.zeros(len(x1))
  for i in range(len(x1)):
    x3[i] = x1[i] + x2[i]
  return x3


# two arrays with 1 million members
x4 = np.random.rand(1000000)
x5 = np.random.rand(1000000)

print('Numpy vectorization')
%timeit x4 + x5

print('Function using loops')
%timeit plusarray(x4, x5)
```
Which results in the following output:
```txt
Numpy vectorization
1.5 ms ± 169 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

Function using loops
590 ms ± 151 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

the `%timeit` command is a magic command in  notebooks that measures the time it takes to run a piece of code. The output shows that the NumPy vectorization is about 400 times faster than the function using loops. This is because NumPy uses optimized C code to perform the operations, whereas a for loop in Python is interpreted and slower.'

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

**Note**: Even though P is shown in the diagram as acting in the negative y-direction, we treat it as a positive value in the derivation. It has a minus sign after moving it from the left-hand side to the right-hand side. With this solution, for a force P acting downward, we would enter a negative value for P. If P were acting upward, we would enter a positive value for P.

We can now "line up" the equations in a matrix form to solve for the unknowns. 

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

You may recognize this as a system of linear equations, which are typically referenced as $Ax = b$, where $A$ is the matrix of coefficients, $x$ is the vector of unknowns, and $b$ is the vector of knowns. The big matrix on the left is a set of coefficients we have derived based on statics and geometry. The vector on the right (mostly zeros) represents the known loads on the truss, and the vector in the middle corresponds to the unknown x vector and it represents the forces in the members and the reactions at the supports. 

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

For reference, here are our coefficients and loads in table format. **Note**: If you compare this table to the the equations above, you will notice that we have changed the order of the equations so that the two A equations are first, followed by the two B equations, and finally the two C equations. Also, we switched the order of 2nd and 3rd columns.

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

As you may recall, it is possible to solve a system of linear equations. This can be rather cumbersome, but fortunately, there is a simple way to do it in NumPy using the `np.linalg.solve()` function. Once you have formulated the A matrix and the b vector, you can solve for the unknowns using the following code:

```python

import numpy as np

x = np.linalg.solve(A, b)

```

For the in-class, and homework exercises, you will be given the equations and the knowns. you will need to use NumPy to solve for the unknowns.

---



## Turning in/Rubric
Turn sharing and editing on, then submit the link to Learning Suite in the feedback box. In-class assignment scores are based on valid effort and completion.
