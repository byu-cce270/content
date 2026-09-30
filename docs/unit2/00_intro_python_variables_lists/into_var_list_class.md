# In Class Exercise: Introduction to Python, Variables, and Lists

The following exercises will have you create a set of variables, formulas, and list in Python. For this exercise, open the in-class workbook, make a copy, and follow the instructions.

You can find the In Class Exercise here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/00_intro_python_variables_lists/Class_Introduction_to_Python_Variables_Lists.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

---

## Instructions

After opening the workbook, follow the instructions in the workbook to complete the exercises. There are two parts to this exercise. Part 1 will go over the basics of Python and variables. Part 2 will give you practice with the basics of Lists in Python.

For Part 2, here is a list of common list methods you will be using:

|         Method         | Description                                                                                           |
|:----------------------:|-------------------------------------------------------------------------------------------------------|
|    append(element)     | Adds a single element to the end of the list.                                                         |
|      extend(list)      | Adds all elements of another list to the end of the list.                                             |
| insert(index, element) | Inserts an element at the specified position.                                                         |
|     remove(value)      | Removes the first item with the specified value. Raises a ValueError if the value is not in the list.  |
|      pop([index])      | Removes and returns the element at index. If no index is given, removes and returns the last element. |
|        clear()         | Removes all items from the list.                                                                      |
|      index(value)      | Returns the index of the first element with the specified value. Raises a ValueError if the value is not in the list. |
|      count(value)      | Returns the number of elements with the specified value.                                              |
|         sort()         | Sorts the list in place and returns None.                                                             |
|       reverse()        | Reverses the order of the list in place and returns None.                                             |

Square brackets mark an optional argument, so both `pop()` and `pop(1)` are valid.

`len()` is a built-in function rather than a list method, so it is called as `len(items)`, not `items.len()`. It returns the number of items in a sequence or collection.

Here is how several of these work together:

```python
items = ["a", "b", "c"]

x = items.pop(1)          # removes and returns "b"; items is now ["a", "c"]
y = items.pop()           # removes and returns "c"; items is now ["a"]

items = ["a", "b", "c"]   # start over with the full list

items.append("d")         # items is now ["a", "b", "c", "d"]
items.extend(["e", "f"])  # items is now ["a", "b", "c", "d", "e", "f"]
items.insert(1, "z")      # items is now ["a", "z", "b", "c", "d", "e", "f"]
items.remove("z")         # items is now ["a", "b", "c", "d", "e", "f"]

position = items.index("d")     # 3
appearances = items.count("a")  # 1
size = len(items)               # 6

letters = ["c", "a", "b"]

letters.sort()            # letters is now ["a", "b", "c"]; sort() itself returns None
letters.reverse()         # letters is now ["c", "b", "a"]
letters.clear()           # letters is now []
```

!!! Note 
    The len() function and the count() method are similar, but they are not the same. len() returns the number of items in a list, while count() returns the number of times a specific item appears in a list.

---
			
## Turning in/Rubric

**_REMINDER_** - For this class, **you will download your completed Colab notebook and upload the `.ipynb` file to Learning Suite**. Make sure the notebook you upload is for the correct assignment and contains your finished work.

**Rubric:**

|                      Item                      | Points Possible |
|:----------------------------------------------:|:---------------:|
| <div style="text-align: right">**Total**</div> |        5        |

---

The following is not a part of the rubric, but specifies how you can lose points. For example: if you fail to upload your file correctly.

| **Reasons for Points Lost** |    **Amount**     |  
|:---------------------------:|:-----------------:|
|  File uploaded incorrectly  |       -10%        |
|  Turned in late (per week)  | -10% (up to -50%) |