# In Class Exercise: Introduction to Python, Variables, and Lists

The following exercises will have you create a set of variables, formulas, and list in Python. For this exercise, open the in-class workbook, make a copy, and follow the instructions.

You can find the In Class Exercise here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/00_intro_python_variables_lists/Class_Introduction_to_Python_Variables_Lists.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

---

## Instructions

After opening the workbook, follow the instructions in the workbook to complete the exercises. There are two parts to this exercise. Part 1 will go over the basics of Python and variables. Part 2 will give you practice with the basics of Lists in Python.

Reading for this exercise: [Introduction to Python, Variables, and Lists](into_var_list_read.md) — PCC Chapter 2, *Variables and Simple Data Types*, and Chapter 3, *Introducing Lists*.

Before the list methods, there is one command you will use in nearly every exercise: `print()`. It displays a value in the output area below the code cell. Without it, your code still runs, but you see nothing.

```python
print("Hello")        # displays: Hello

items = ["a", "b", "c"]
print(items)          # displays: ['a', 'b', 'c']
print(items[0])       # displays: a
```

`print()` is also the simplest way to understand code that is not doing what you expect. List methods change a list silently, so printing the list after each step shows you what actually happened instead of what you assumed:

```python
items = ["a", "b", "c"]

items.pop(1)
print(items)          # displays: ['a', 'c']  - confirms "b" was removed

items.append("d")
print(items)          # displays: ['a', 'c', 'd']  - confirms "d" was added
```

When a result surprises you, add a `print()` after each line and work down until the displayed value stops matching what you intended. That line is where the problem is.

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

**Where to read more.** In PCC Chapter 3, `append()` and `insert()` are covered in *Adding Elements to a List* (p. 37), `pop()` and `remove()` in *Removing Elements from a List* (p. 38), and `sort()` and `reverse()` in *Organizing a List* (pp. 42-44).

!!! Note "Not in the textbook"
    `extend()`, `count()`, `index()`, and `clear()` are not covered in *Python Crash Course*, so the tables and examples on this page are your reference for them.

You will also use these built-in functions. They are not list methods, so they are called with the list inside the parentheses, as in `len(items)` rather than `items.len()`:

|  Function  | Description                                           |
|:----------:|-------------------------------------------------------|
| len(list)  | Returns the number of items in the list.              |
| sum(list)  | Adds the numbers in the list and returns the total.   |
| max(list)  | Returns the largest item in the list.                 |
| min(list)  | Returns the smallest item in the list.                |
| sorted(list) | Returns a new sorted list and leaves the original list unchanged. |

`len()` is covered in PCC Chapter 3, *Finding the Length of a List* (p. 44). `sum()`, `max()`, and `min()` are covered in Chapter 4, *Simple Statistics with a List of Numbers* (p. 59), which is next topic's reading.

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

durations = [5, 12, 3]

total = sum(durations)      # 20
longest = max(durations)    # 12
shortest = min(durations)   # 3
how_many = len(durations)   # 3

print(total, longest, shortest, how_many)   # displays: 20 12 3 3
```

!!! Note 
    The len() function and the count() method are similar, but they are not the same. len() returns the number of items in a list, while count() returns the number of times a specific item appears in a list.

### Permanent and Temporary Changes

Every list method in the table above changes the list itself and hands back `None`. The change is permanent: once you call `sort()`, the original order is gone.

`sorted()` is the temporary alternative. It is a function rather than a method, and instead of rearranging your list it builds a new one and leaves the original untouched.

```python
numbers = [3, 1, 2]

new_numbers = sorted(numbers)   # builds a new sorted list
print(new_numbers)              # displays: [1, 2, 3]
print(numbers)                  # displays: [3, 1, 2]  - the original is unchanged

numbers.sort()                  # changes the list itself
print(numbers)                  # displays: [1, 2, 3]  - the original order is gone

oops = numbers.sort()           # sort() returns None, so nothing useful is stored
print(oops)                     # displays: None
```

The last two lines show the most common mistake with these methods. Writing `new_list = my_list.sort()` looks reasonable, but `sort()` returns `None`, so `new_list` ends up holding nothing. Call `my_list.sort()` on its own line when you want the list changed, and use `sorted(my_list)` when you want a sorted copy.

PCC Chapter 3 covers both on page 43: *Sorting a List Permanently with the sort() Method* and *Sorting a List Temporarily with the sorted() Function*.

!!! Note "Looking ahead"
    Later in the course you will work with pandas DataFrames, which behave the opposite way. Their methods return a changed copy by default and leave the original alone, and you add `inplace=True` when you want the change to stick. List methods are permanent unless you use `sorted()`; DataFrame methods are temporary unless you use `inplace=True`.

### Lists Within Lists

*Python Crash Course* does not cover lists inside lists, so read this section carefully.

An item in a list can itself be a list. Reaching an item inside the inner list takes two index numbers in a row: the first finds the inner list, and the second finds the item inside it.

```python
project = [['concrete', 'steel', 'lumber'], 'Site A', ['Ann', 'Ben']]

print(project[0])       # displays: ['concrete', 'steel', 'lumber']  - the whole inner list
print(project[0][1])    # displays: steel  - item 1 of the inner list at position 0
print(project[1])       # displays: Site A  - a plain string, so no second index is needed
print(project[2][0])    # displays: Ann
```

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