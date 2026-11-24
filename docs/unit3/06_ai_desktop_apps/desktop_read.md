# Reading: Building Desktop Apps with an AI Agent

---

In the last section, you had an agent build a web app. In this section, the agent builds a desktop app in Python, using the same process. You will not need to learn a new library. The agent handles the details. You decide what gets built, in what order, and whether it is right.

## Desktop Apps

A desktop app runs in its own window on your computer, with buttons, input boxes, and plots, the way Excel or AutoCAD does. We will build ours in Python with **Tkinter**, a library that comes with Python, so the app runs on any computer that has Python with nothing extra to install. That includes your TA's computer, which matters when your homework is graded.

The agent writes all of the interface code, just as it wrote the HTML and JavaScript for your web app. Because the code is Python, you can open it and follow what it does, and you can ask the agent to use numpy, pandas, or matplotlib wherever they help.

Tkinter windows look a little dated. For your final project, you may prefer **CustomTkinter**, which gives Tkinter a modern look, or **PySide6** (Qt), which is used for many professional engineering programs but is a large install. Switching is mostly a matter of naming the library you want in your spec. For the homework in this section, use Tkinter.

## Managing the Process

Use the same process as the web app: write the spec, work through it with the agent, build in stages, validate, commit, and add one feature at a time. In the spec, add a **Platform** section saying the app is a Python desktop app built with Tkinter, and describe a desktop window instead of a web page in **Look and feel**.

Validation gets easier, because the agent can run the cases in Python instead of you typing them into the app:

!!! prompt "Prompt"
    Run the validation cases in spec.md against the app's calculations and report a table of expected versus actual values.

Ask it to rerun them after every change. A change that breaks a calculation that used to work is one of the most common problems in agent-built code, and this catches it right away.

The agent is also good at finding cases worth testing, including edge cases and property checks you might not think of. Ask it for more:

!!! prompt "Prompt"
    Suggest validation cases that test every calculation in spec.md, including edge cases and property checks such as symmetry. Work out the expected values from the equations in the spec, show your work, and add the cases to the Validation section. Don't change the app.

## Sharing a Desktop App

GitHub Pages can't run a desktop app, because a desktop app runs on the user's own computer. Instead, push the code to a GitHub repository, and anyone who wants to use it clones the repository and runs it. Have the agent write a short `README.md` at the top of the repository that says what the app does, which packages to install, and the command that starts it.

---

# Pre-Class Quiz Challenge

Practice having the agent check its own work. This Python function computes the flow in an open channel using Manning's equation, $Q = \frac{1.49}{n} A R^{2/3} S^{1/2}$, in US units:

```python
def manning_flow(n, A, R, S):
    """Flow (cfs) from Manning's n, area A (ft^2), hydraulic radius R (ft), and slope S (ft/ft)."""
    return 1.49 / n * A * R ** (2 / 3) * S ** 0.5
```

1. Make a new folder, open it in VS Code, and save the function in a file named `manning.py`.
2. Work two cases with a calculator, using any reasonable values of n, A, R, and S.
3. Ask the agent to check `manning_flow` against your two cases and report a table of expected versus actual values.
4. Take a screenshot of the agent's table.

Upload your screenshot and your two hand-worked cases with your Pre-Class Quiz.

---

## Turning in/Rubric

**Rubric:**

|                      Item                      | Points Possible |
|:----------------------------------------------:|:---------------:|
| <div style="text-align: right">**Total**</div> |       15        |

---

The following is not a part of the rubric, but specifies how you can lose points. For example: if you fail to upload your file correctly.

| **Reasons for Points Lost** |    **Amount**     |  
|:---------------------------:|:-----------------:|
|  File uploaded incorrectly  |       -10%        | 
