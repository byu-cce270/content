# In-Class Exercise: Bridge Builder on the Desktop

In this exercise, you will have the agent turn your Bridge Builder web app into a Python desktop app, then add features that a desktop app does well, such as saving designs as files. Along the way, you will practice the three habits from the reading: getting a plan before any code, having the agent check its own work, and changing an existing program.

## Step 1 - Set Up the Project

1. Make a folder named `bridge_desktop` in your class folder.
2. Copy `spec.md` and `index.html` from your `bridge_builder` folder into `bridge_desktop`. The agent will use `index.html` as a reference for how the app should behave.
3. Open `bridge_desktop` in VS Code, initialize a repository, and ask the agent to commit.
4. Copy `AGENTS.md` from your `bridge_builder` folder, so the agent keeps a prompt log for this project too.
5. In the terminal, install the packages you'll need:

    ```
    pip install numpy matplotlib
    ```

6. Check that Tkinter works by running `python -m tkinter`. A small window should open. If you get `No module named '_tkinter'` on a Mac, your Python came from Homebrew; run `brew install python-tk@3.x` with your Python version (for example, `python-tk@3.14`), or ask a TA for help.

## Step 2 - Update the Spec

Edit `spec.md` to describe the desktop version.

1. Add this section near the top:

    ```markdown
    ## Platform
    - Python desktop app using Tkinter, started with `python app.py`
    - The truss is solved with numpy (np.linalg.solve), the same method
      used in the Numpy homework.
    ```

2. In the **Calculations** section, replace the line about Gaussian elimination with:

    ```markdown
    - Solve the system with np.linalg.solve.
    - Treat a nearly singular matrix (condition number above 1e12) as
      unstable, as well as an exactly singular one.
    ```

    The second line matters more than it looks. When joints are almost in a straight line, numpy doesn't report an error. It returns forces in the billions of pounds, and the app would show them as if they were real.

3. Add these cases to the **Validation** section, below the Numpy homework case:

    ```markdown
    Symmetric truss:
    - Joints: (0, 0) pin, (5, 5), (10, 0) roller, with three members
      connecting them. Load -1000 lb at (5, 5).
    - Expected: both vertical reactions are +500 lb.

    Square with no diagonal:
    - Joints: (0, 0) pin, (10, 0) roller, (10, 10), (0, 10), with the four
      sides as members. Load -1000 lb at (10, 10).
    - Expected: reported as unstable, with no forces shown.

    Joints in a straight line:
    - Joints: (0, 0) pin, (5, 0), (10, 0) roller, with a member between
      each pair. Load -1000 lb at (5, 0).
    - Expected: reported as unstable, with no forces shown.
    ```

Ask the agent to commit.

## Step 3 - Get a Plan

In the Copilot chat panel, choose **Plan** from the picker and enter:

!!! prompt "Prompt"
    Read spec.md and index.html. I want to rebuild this app as the Python Tkinter desktop app described in spec.md. Before writing any code, describe your plan: which files you will create, what each one does, and how the truss calculations are organized.

Read the plan and check that:

- Nothing in it contradicts the spec
- It says what the app will show for a truss it can't solve
- The truss calculations are kept apart from the window code, so the agent can check them without opening the app

If something is off, say so and ask for a revised plan.

## Step 4 - Build It

Switch the picker to **Agent** and enter:

!!! prompt "Prompt"
    Build the app following your plan and spec.md.

When the agent finishes, run the app:

```
python app.py
```

Draw a truss and check that it behaves like your web version. If something doesn't work, describe what you did and what happened, and ask the agent to fix it.

## Step 5 - Have the Agent Check Its Work

Enter:

!!! prompt "Prompt"
    Run the four validation cases in spec.md against the app's truss calculations and report a table of expected versus actual values.

Read the table. Every case should match within 1 lb, and the two unstable trusses should be reported as unstable. If a case fails, tell the agent to fix the app. Never let it change an expected value. If you think an expected value is wrong, check it by hand yourself.

Then build the Numpy homework truss in the app yourself and confirm that you see the same forces the agent reported.

When everything matches, ask the agent to commit.

## Step 6 - Add Desktop Features

Add these features **one at a time**:

1. **Save and Open:** A File menu with **Save** and **Open** that saves the truss (joints, members, supports, and loads) to a file and opens it again. Remove "Saving or loading designs" from the **Out of scope** section of the spec first.
2. **Export results:** A button that saves a table of member forces (member, length, force, T or C) to a CSV file that opens in Excel.
3. **Force plot:** A matplotlib bar chart of the member forces next to the truss, with tension in blue and compression in red.

For each feature:

1. Add it to the spec.
2. Ask the agent to build it.
3. Try it in the app.
4. Have the agent rerun the validation cases:

    !!! prompt "Prompt"
        Rerun the validation cases in spec.md and confirm they still pass.

5. Ask the agent to commit.

## Step 7 - Push to GitHub

1. Ask the agent for a README:

    !!! prompt "Prompt"
        Write a short README.md that says what this app does, which packages to install, and the command that starts it.

2. Ask the agent to commit, then click **Publish Branch** and publish a public repository.
3. Trade repository addresses with a neighbor. Clone their repository (**File → New Window**, then **Clone Git Repository**), follow their README, and run their app. If the README left anything out, tell them.
