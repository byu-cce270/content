# In-Class Exercise: Bridge Builder on the Desktop

In this exercise, you will have the agent rebuild your Bridge Builder web app as a Python desktop app. Along the way, you will separate the truss solver from the interface, write automated tests for it using the Numpy homework truss, and add a feature that a desktop app does better than a web page: saving and opening designs as files.

## Step 1 - Set Up the Project

1. Make a folder named `bridge_desktop` in your class folder.
2. Copy `spec.md` and `index.html` from your `bridge_builder` folder into `bridge_desktop`. The agent will use `index.html` as a reference for how the app should behave.
3. Open `bridge_desktop` in VS Code, initialize a repository, and commit with the message `Start from web version`.
4. Create `prompts.md` for your prompt log.
5. Install the packages you'll need:

    ```
    pip install numpy matplotlib pytest
    ```

## Step 2 - Update the Spec

Edit `spec.md` to describe the desktop version. Add a section near the top:

```markdown
## Platform and structure
- Python desktop app using Tkinter, started with `python app.py`
- truss.py: the solver only. A function solve_truss(joints, members,
  supports, loads) that returns member forces and reactions. It uses
  numpy (np.linalg.solve) and does not import tkinter.
- app.py: the Tkinter interface. It draws on a tk.Canvas and calls
  solve_truss to get the results.
- test_truss.py: pytest tests for solve_truss.
```

Then change the **Calculations** section to say that the system is solved with `np.linalg.solve` instead of Gaussian elimination in JavaScript. This is the same method you used in the Numpy homework.

Commit with the message `Update spec for desktop version`.

## Step 3 - Get a Plan

In the Copilot chat panel, switch to **Ask** mode and enter:

> Read spec.md and index.html. I want to rebuild this app as the Python Tkinter desktop app described in spec.md. Before writing any code, describe your plan: what goes in each file, which classes and functions you will write, and what the arguments and return values of solve_truss will be.

Read the plan carefully. Check that:

- `truss.py` doesn't use tkinter
- `solve_truss` takes plain data (lists or dictionaries of joints, members, supports, and loads) and returns plain data
- Nothing in the plan contradicts the spec

If something is off, say so and ask for a revised plan. Add the plan to your prompt log.

## Step 4 - Write the Tests First

You will write the expected values for the tests before the solver exists. Then the tests check the solver against your answers rather than against whatever the solver happens to return.

Switch to **Agent** mode and enter:

> Create test_truss.py with pytest tests for solve_truss as described in your plan. Use these cases, with exactly these expected values:
>
> 1. Numpy HW Test 1: joints A (0, 0) pin, C (10, 0) roller, B (2.5, 4.330). Members AB, BC, AC. Load -2000 lb at B. Expected AB = -1732 lb, BC = -1000 lb, AC = +866 lb (tension positive), vertical reactions 1500 lb at A and 500 lb at C, horizontal reaction 0 at A. Use a tolerance of 1 lb.
> 2. A symmetric truss with a symmetric load: the two vertical reactions are equal and add up to the total load.
> 3. A truss with too few members (a four-sided frame with no diagonal) is reported as unstable instead of returning forces.
>
> Do not write truss.py yet.

Read `test_truss.py` and check that the expected values are the ones you gave. Run `pytest`. It should report an error, because `truss.py` doesn't exist yet. Commit with the message `Add solver tests`.

## Step 5 - Build It

> Now write truss.py and app.py following your plan and spec.md. Run pytest until all tests pass. Do not change the expected values in test_truss.py.

When the agent finishes, run `pytest` yourself and confirm that all the tests pass. Then run the app:

```
python app.py
```

Build a truss and check that it behaves like your web version. When it works, commit with the message `Desktop version working`.

## Step 6 - See a Test Catch a Bug

Open `truss.py` and find the line where the load is placed in the right-hand-side vector. Flip its sign on purpose (change `-` to `+` or the reverse) and run `pytest`. Look at how the failure report shows the value it got and the value you expected.

Undo the change by discarding it in the Source Control panel, and run `pytest` again to confirm everything passes.

## Step 7 - Add Desktop Features

Add these one at a time. Update the spec first, then ask the agent, then test and commit:

1. **Save and Open:** A File menu with **Save** and **Open** that writes the truss (joints, members, supports, loads) to a `.json` file and reads it back, using the standard file dialogs.
2. **Export results:** A button that writes a table of member forces (member, length, force, T or C) to a CSV file that opens in Excel.
3. **Force plot:** A matplotlib bar chart of the member forces in the window next to the truss, with tension in blue and compression in red.

After each feature, run `pytest` to confirm the solver still passes. The tests don't check the new features themselves. Ask the agent to add a test for Save and Open: save a truss, open it, and check that you get the same truss back.

## Step 8 - Push to GitHub

1. Ask the agent to write a short `README.md` that says what the app does, which packages to install, and how to start it.
2. Commit, then click **Publish Branch** and publish a public repository.
3. Trade repository addresses with a neighbor. Clone their repository (**File → New Window**, then **Clone Git Repository**), install the packages their README lists, and run their app. If their README left anything out, tell them.
