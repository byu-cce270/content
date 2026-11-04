# In-Class Exercise: Beam Designer on the Desktop

In this exercise, you will have the agent build the [Beam Designer](../05_ai_web_apps/web_class.md#beam-designer) as a Python desktop app, with numpy for the calculations and matplotlib for the diagrams, then add features that a desktop app does well, such as saving designs as files. Along the way, you will practice the three habits from the reading: getting a plan before any code, having the agent check its own work, and changing an existing program.

## Step 1 - Set Up the Project

1. Make a folder named `beam_desktop` in your class folder.
2. Copy the Beam Designer spec from the [web apps in-class exercise](../05_ai_web_apps/web_class.md#beam-designer) into a file named `spec.md` in `beam_desktop`. If your class built Beam Designer as its web app, copy your own `spec.md` and `index.html` from your `first_app` folder instead. The agent will use `index.html` as a reference for how the app should behave.
3. Copy `AGENTS.md` from your `first_app` folder, so the agent keeps a prompt log for this project too.
4. Open `beam_desktop` in VS Code, initialize a repository, and ask the agent to commit.
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
    - Calculations with numpy, kept in their own module, separate from
      the window code
    - Diagrams drawn with matplotlib, embedded in the window
    ```

2. Change the **Look and feel** section for a desktop window: inputs in a panel on the left, the beam and diagrams on the right, and a window that can be resized. Remove the lines about phones.

3. Add this case to the **Validation** section:

    ```markdown
    5. Simply supported, 30 ft, W18x35, uniform 2 kips/ft from 0 to 15 ft
       only: reactions 22.5 k (left) and 7.5 k (right); max moment
       126.6 kip-ft at 11.25 ft.
    ```

    Check it by hand before you commit it. Find the reactions with statics, then find where the shear is zero.

Ask the agent to commit.

## Step 3 - Get a Plan

In the Copilot chat panel, choose **Plan** from the picker and enter:

!!! prompt "Prompt"
    Read spec.md. I want to build this app as the Python Tkinter desktop app described in spec.md. Before writing any code, describe your plan: which files you will create, what each one does, and how the beam calculations are organized.

Read the plan and check that:

- Nothing in it contradicts the spec
- The beam calculations are kept apart from the window code, so the agent can check them without opening the app
- It isn't more complicated than it needs to be

If something is off, say so and ask for a revised plan.

## Step 4 - Build It

Switch the picker to **Interactive** and enter:

!!! prompt "Prompt"
    Build the app following your plan and spec.md.

When the agent finishes, run the app:

```
python app.py
```

Try every input. If something doesn't work, describe what you did and what happened, and ask the agent to fix it.

## Step 5 - Have the Agent Check Its Work

Enter:

!!! prompt "Prompt"
    Run all of the validation cases in spec.md against the app's beam calculations and report a table of expected versus actual values.

Read the table. Every value should match to the number of digits given in the spec. If a case fails, tell the agent to fix the app. Never let it change an expected value. If you think an expected value is wrong, check it by hand yourself.

Then enter case 1 in the app yourself and confirm that you see the same values the agent reported.

When everything matches, ask the agent to commit.

## Step 6 - Add Desktop Features

Add these features **one at a time**:

1. **Save and Open:** A File menu with **Save** and **Open** that saves the beam (support type, span, section, deflection limit, and loads) to a file and opens it again. Remove "Saving designs" from the **Out of scope** section of the spec first.
2. **Export results:** A button that saves a table of x, V, M, and deflection along the beam to a CSV file that opens in Excel.
3. **Calculation sheet:** A button that saves the diagrams and checks as a PDF, with the inputs listed at the top, ready to hand in with a design.

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
