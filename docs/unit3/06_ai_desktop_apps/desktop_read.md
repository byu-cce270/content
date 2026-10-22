# Reading: Building Desktop Apps with an AI Agent

---

In the last section, you had an agent build a web app. In this section, the agent builds a desktop app in Python, and you will use it to practice the part of agentic programming that matters most as projects get bigger: managing the development process. You will not need to learn a new library. The agent handles the details. You decide what gets built, in what order, and whether it is right.

## Desktop Apps

A desktop app runs in its own window on your computer, with buttons, input boxes, and plots, the way Excel or AutoCAD does. We will build ours in Python with **Tkinter**, a library that comes with Python, so the app runs on any computer that has Python with nothing extra to install. That includes your TA's computer, which matters when your homework is graded.

The agent writes all of the interface code, just as it wrote the HTML and JavaScript for your web app. Because the code is Python, you can open it and follow what it does, and you can ask the agent to use numpy, pandas, or matplotlib wherever they help.

Tkinter windows look a little dated. For your final project, you may prefer **CustomTkinter**, which gives Tkinter a modern look, or **PySide6** (Qt), which is used for many professional engineering programs but is a large install. Switching is mostly a matter of naming the library you want in your spec. For the homework in this section, use Tkinter.

## Managing the Process

You already know the basic workflow from the web app section: write a spec, have the agent review it, have it build, validate, commit, and add one feature at a time. This section adds three habits.

### Ask for a plan before any code

For anything larger than a small change, ask the agent how it intends to do the work before it starts. In the Copilot chat panel, choose **Plan** from the picker:

!!! prompt "Prompt"
    Read spec.md. Before writing any code, describe your plan: which files you will create, what each one does, and how the calculations are organized.

Read the plan the way you would read a proposal from a consultant. Does it match the spec? Is anything missing? Is it more complicated than it needs to be? Push back on anything you don't like, and when you are satisfied, switch to **Agent** and tell it to build the plan.

### Make the agent check its own work

In the web app section, you validated by typing your test case into the app and comparing the result to your hand calculation. An agent can do that checking for you. Once your validation cases are in the spec, ask:

!!! prompt "Prompt"
    Run the validation cases in spec.md against the app's calculations and report a table of expected versus actual values.

The agent will write whatever code it needs to run the cases, run it, and show you the results. Keep that check, and ask the agent to rerun it after every change:

!!! prompt "Prompt"
    Rerun the validation cases and confirm they still pass.

A change that breaks a calculation that used to work is one of the most common problems in agent-built code, and this catches it right away.

Two rules keep this honest. First, **the expected values must come from you**, worked by hand or taken from a textbook or a previous homework. If the agent computes the expected values from its own code, the check will pass even when the code is wrong. Second, if a check fails, ask the agent to fix the app, never to change the expected value. If you think your expected value is wrong, rework it by hand yourself.

### Change existing code instead of starting over

Most programming work is changing a program that already exists. In this section, you will have an agent turn your web app into a desktop app, then add features to it. When you ask for a change to existing code:

- **Name the files that matter.** Tell the agent which files to read, such as your old `index.html` and `spec.md`, and which it may change.
- **Update the spec first.** Change the spec, then ask the agent to make the app match it.
- **Review the change.** Look at what the agent changed in the Source Control panel before you test and commit. If a small request changed a lot of code, ask why.

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
| <div style="text-align: right">**Total**</div> |        3        |

---

The following is not a part of the rubric, but specifies how you can lose points. For example: if you fail to upload your file correctly.

| **Reasons for Points Lost** |    **Amount**     |  
|:---------------------------:|:-----------------:|
|  File uploaded incorrectly  |       -10%        | 
