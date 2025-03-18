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

## Vectorized Operations in NumPy

NumPy is a powerful library for numerical computing in Python. One of the key features of NumPy is its ability to perform vectorized operations on arrays. Vectorized operations are operations that are applied to each element of an array. For example, if you have two arrays `a` and `b`, you can add them together element-wise using the `+` operator:

```python   
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = a + b
print(c)  # Output: [5 7 9]
```


## Turning in/Rubric
Turn sharing and editing on, then submit the link to Learning Suite in the feedback box. In-class assignment scores are based on valid effort and completion.
