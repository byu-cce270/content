# Reading: Building Desktop Apps with an AI Agent

---

In the last section, you had an agent build a web app in JavaScript, a language you can mostly read but can't yet write. In this section, the agent builds a desktop app in Python. You can read every line it writes, use the libraries you already know (numpy, pandas, matplotlib), read and write files on your computer, and write **automated tests** that check your calculations every time the code changes.

You will also practice something agents are used for constantly in industry: changing an existing program instead of writing a new one from scratch.

## Desktop Apps with Tkinter

A desktop app opens in its own window, with buttons, input boxes, sliders, and plots, the way Excel or AutoCAD does. Python has a built-in library for making these windows, called **Tkinter**. It comes with Python, so there is nothing to install. Check that it works by running this in the terminal:

```
python -m tkinter
```

A small window should open. Close it. (If you get `No module named '_tkinter'` on a Mac, you probably installed Python with Homebrew rather than from python.org. Run `brew install python-tk@3.x`, using your Python version (for example, `python-tk@3.14`), or ask a TA for help.)

Here is the flow converter from the last reading, written in Python with Tkinter:

```python
import tkinter as tk


def cfs_to_gpm(cfs):
    """Convert a flow rate from cubic feet per second to gallons per minute."""
    return cfs * 448.83


def convert():
    """Read the input box, convert, and show the result."""
    cfs = float(cfs_entry.get())
    result.config(text=f"{cfs_to_gpm(cfs):.1f} gpm")


root = tk.Tk()
root.title("Flow Converter")

tk.Label(root, text="Flow (cfs):").grid(row=0, column=0, padx=10, pady=10)
cfs_entry = tk.Entry(root, width=10)
cfs_entry.grid(row=0, column=1)

tk.Button(root, text="Convert", command=convert).grid(row=0, column=2, padx=10)

result = tk.Label(root, text="")
result.grid(row=1, column=0, columnspan=3, pady=10)

root.mainloop()
```

Most of this is Python you already know:

- `root = tk.Tk()` creates the window.
- Each widget (`Label`, `Entry`, `Button`) is created and then placed with `.grid(row=..., column=...)`, which arranges widgets in rows and columns like cells in a spreadsheet.
- `command=convert` tells the button which function to call when it is clicked. Note there are no parentheses, because you are handing Tkinter the function to call later, not calling it now.
- `cfs_entry.get()` reads what the user typed, and `result.config(text=...)` changes what a label shows.
- `root.mainloop()` opens the window and waits for the user. Your program stays on this line until the window is closed.

When you look at the code an agent writes for a larger app, you will usually find all of this wrapped in a **class**, like the ones you wrote in Unit 2: the `__init__` method builds the window, the widgets are stored as attributes such as `self.cfs_entry`, and the button calls a method such as `self.convert`. A class keeps dozens of widgets and functions organized, but the pieces are the same as in this example.

The calculation, `cfs_to_gpm`, is a plain function that knows nothing about windows or buttons. That separation is the most important design decision in this section, for the reason explained in [Automated Tests](#automated-tests) below.

These are the widgets you will use most. The agent knows how to use all of them, so you only need to know they exist and ask for them by name:

| Widget              | What it does                                                    |
|:--------------------|:----------------------------------------------------------------|
| `tk.Label`          | Displays text                                                   |
| `tk.Entry`          | A box for typing one line of text or a number                   |
| `tk.Button`         | Calls a function when clicked                                   |
| `tk.Scale`          | A slider                                                        |
| `ttk.Combobox`      | A drop-down list                                                |
| `tk.Canvas`         | A drawing area for lines, shapes, and text, including animation |
| `FigureCanvasTkAgg` | Puts a matplotlib plot inside a Tkinter window                  |
| `filedialog`        | The standard Open and Save As windows                           |

### Other options

Tkinter isn't the only way to build a desktop app in Python. We use it in this class because it comes with Python, so the app runs on any computer with no installation, and a TA can run your homework without setting anything up. Its widgets look a little dated, but it handles everything the assignments need. The most common alternatives are:

- **PySide6** (Qt): the toolkit behind many professional engineering programs. It looks modern and has far more widgets, including tables, tabs, and docking panels, but it is a large install and takes more code to set up.
- **CustomTkinter**: a package that gives Tkinter a modern look with almost the same code.

Because the agent writes the interface code, switching toolkits is mostly a matter of saying which one you want in your spec. For the homework in this section, use Tkinter.

## Automated Tests

In the web app section, you validated your app by entering a test case and checking the answer by hand. That works once. But every time the agent changes the code, it might break a calculation that used to work, and you won't know unless you check again. An **automated test** is a short piece of code that runs your calculation with known inputs and checks the result against the answer you worked by hand. You can rerun every test in a second, as often as you like.

Python's most popular testing tool is **pytest**. Install it once:

```
pip install pytest
```

Suppose your app has this function in a file named `beam.py`:

```python
def max_moment(w, L):
    """Maximum moment (kip-ft) in a simply supported beam with uniform load w (kip/ft) and span L (ft)."""
    return w * L**2 / 8
```

Tests go in a separate file whose name starts with `test_`, such as `test_beam.py`. Each test is a function whose name also starts with `test_`, and it uses `assert` to state what must be true:

```python
from pytest import approx
from beam import max_moment


def test_max_moment_hand_calc():
    # 1.0 kip/ft on a 25 ft span: 1.0 * 25^2 / 8 = 78.125 kip-ft (worked by hand)
    assert max_moment(1.0, 25) == approx(78.125)


def test_max_moment_doubles_with_load():
    # Moment is proportional to load, so doubling w doubles M
    assert max_moment(2.0, 25) == approx(2 * max_moment(1.0, 25))
```

`approx` allows for the tiny rounding differences in floating-point math, so 78.12500000001 still counts as 78.125. Run all the tests in the folder by typing `pytest` in the terminal:

```
$ pytest
==================== 2 passed in 0.01s ====================
```

If a calculation is wrong, pytest tells you which test failed and shows the value it got and the value you expected.

You can only test a calculation this way if it is a plain function like `max_moment`. If the formula is buried inside a button's click method, mixed in with code that reads input boxes and updates labels, there is no way to call it with test values. That is why every app in this section keeps its calculations in separate functions, and preferably in a separate file, from the code that builds the window.

**The agent can write your tests, but you must supply the expected values.** If you ask an agent to "write tests for my code," it will read the code, compute what the code returns, and write tests that check for exactly that. Those tests will pass even if the code is wrong. Work the expected values by hand (or take them from a textbook or a previous homework) and give them to the agent.

## Changing an Existing Program

Most real programming work is changing code that already exists, and agents are good at it, but they need more direction than when they start from scratch. A few habits help:

- **Ask for a plan first.** In the Copilot chat panel, choose **Plan** from the picker and ask: "Read index.html and spec.md. I want to rebuild this app as a Python Tkinter desktop app. Before writing any code, describe how you would structure it: which files, which classes and functions, and what each one does." Read the plan, push back on anything you don't like, and only then switch to **Agent** mode and ask it to build.
- **Point it at the files that matter.** Name the files it should read and the files it is allowed to change.
- **Keep the tests passing.** After each change, run `pytest`. If a test that used to pass now fails, the agent broke something. Tell it which test failed and ask it to fix the code, not the test.
- **Update the spec first.** As in the last section, change the spec before asking for a change to the app.

## Sharing a Desktop App

GitHub Pages can't run a desktop app, because a desktop app runs on the user's own computer. Instead, you share it the way most Python programs are shared: push the code to a GitHub repository, and anyone who wants to use it clones the repository and runs it. Put a short `README.md` at the top of the repository that says what the app does, which packages to install, and the command that starts it.

---

# Pre-Class Quiz Challenge

This function computes the flow in an open channel using Manning's equation, $Q = \frac{1.49}{n} A R^{2/3} S^{1/2}$, in US units:

```python
def manning_flow(n, A, R, S):
    """Flow (cfs) from Manning's n, area A (ft^2), hydraulic radius R (ft), and slope S (ft/ft)."""
    return 1.49 / n * A * R ** (2 / 3) * S ** 0.5
```

1. Save the function in a file named `manning.py`.
2. Work two test cases by hand (or with a calculator), using any reasonable values of n, A, R, and S.
3. Write a file named `test_manning.py` with at least three tests: your two hand-worked cases, and one test that checks a property the answer must have without needing an exact value. For example, what happens to Q when you multiply the slope by 4?
4. Run `pytest` and take a screenshot showing that all of your tests pass.

Upload `test_manning.py` and your screenshot with your Pre-Class Quiz.

---

## Turning in/Rubric

**Rubric:**

|                      Item                      | Points Possible |
|:----------------------------------------------:|:---------------:|
| <div style="text-align: right">**Total**</div> |        3        |

---

The following is not a part of the rubric, but specifies how you can lose points. For example: if you fail to upload your file correctly.

| **Reasons for Points Lost** |    **Amount**     |  
|:---------------------------:|:-----------------:|
|  File uploaded incorrectly  |       -10%        | 
