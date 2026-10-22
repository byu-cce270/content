# HW: Build a Desktop App

**Purpose:** Use an AI coding agent to build a Python desktop app with a graphical interface, and check its calculations with automated tests.

---

## Choose Your Project

Choose **one** of these two options.

**Option A - Port your web app.** Rebuild the app from your [web app homework](../05_ai_web_apps/web_hw.md) as a Tkinter desktop app, as you did with Bridge Builder in class. Then add **at least two features** that the web version didn't have. Look for features that use what Python and a desktop app do well, for example:

- Saving and opening work as files
- Reading input data from a CSV or Excel file with pandas
- Exporting results to CSV or Excel
- matplotlib plots that the user can zoom and save
- Running many cases at once, such as a parameter sweep that plots how an output changes with an input

**Option B - Build a new problem.** Choose a problem from the [web app homework](../05_ai_web_apps/web_hw.md) that you did not build, and build it as a Tkinter desktop app. Shake Table, Traffic Signal Tuner, Bid War, Crane Placement, and Provo River Float Check all work as desktop apps. Use the problem's must-have features and its validation check.

## Requirements

Whichever option you choose, your app must:

1. **Use Tkinter** for its interface and start with `python app.py`.
2. **Keep calculations separate from the interface.** Put the engineering calculations in plain functions that don't use tkinter, preferably in their own file. The interface code calls those functions.
3. **Have at least 3 automated tests** in a file named `test_*.py`, and all of them must pass when you run `pytest`. At least two of the tests must use expected values that you worked by hand or took from a reference. Write a comment in each of those tests saying where the expected value came from. The third can check a property the answer must have, such as a symmetry or a proportionality.
4. **Have a spec** (`spec.md`) with all six sections from the [web apps reading](../05_ai_web_apps/web_read.md#1-write-a-spec), plus a **Platform and structure** section that lists your files and what each one does. For Option A, also list the features you added.
5. **Have a prompt log** (`prompts.md`) and a `README.md` that says how to install and run the app.
6. **Be in a GitHub repository** with at least 5 commits.

Follow the workflow from class: get a plan before the agent writes code, write the test expected values yourself, add one feature at a time, and run `pytest` after every change.

---

## Turning in/Rubric

!!! note "Do not put your name or NetID in the file"
    Learning Suite records who submitted each file, so your name is not needed
    inside the file itself. Leaving it out means your work can be graded
    anonymously, which keeps grading fair. Your GitHub repository address will
    show your GitHub username, which is fine for this assignment.

Upload a **`.zip` of your project folder** to Learning Suite. It should contain `app.py`, your calculation file (if separate), your test file, `spec.md`, `prompts.md`, `README.md`, and any data files your app needs. On Windows, right-click the folder and choose **Send to → Compressed (zipped) folder**. On a Mac, right-click the folder and choose **Compress**.

Paste your GitHub repository address in the Learning Suite submission comments.

The TA will grade your app by unzipping it, installing the packages in your README, running `pytest`, and running `python app.py`. Before you submit, unzip your own file into a new folder and do the same thing to make sure it works.

**Rubric:**

|                                         **Items**                                          | **Amount** |  
|:------------------------------------------------------------------------------------------:|:----------:|
|     Spec has all required sections, including Platform and structure (and added features)  |     4      |
|      App works: all must-have features (Option B) or the port plus 2 new features (Option A) |     9      |
|   At least 3 tests pass, with at least 2 using hand-worked or referenced expected values   |     6      |
|               Calculations are in plain functions, separate from the interface             |     3      |
|        App is easy to use: clear labels, units on every number, looks finished            |     3      |
|                  Prompt log is complete                                                    |     3      |
|            README works, and the GitHub repository has at least 5 commits                  |     2      |
|                         <div style="text-align: right">**Total**</div>                    |   **30**   |

---

The following is not a part of the rubric, but specifies how you can lose points.

|          **Reasons for Points Lost**          |    **Amount**     |  
|:---------------------------------------------:|:-----------------:|
|           File uploaded incorrectly           |       -10%        |
|           Turned in late (per week)           | -10% (up to -50%) |
|            No prompt log submitted            |       -50%        |
