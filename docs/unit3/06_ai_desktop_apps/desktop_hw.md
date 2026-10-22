# HW: Build a Desktop App

**Purpose:** Use an AI coding agent to build and validate a Python desktop app, managing the development process the way you did in class.

---

## Choose Your Project

Choose **one** of these two options.

**Option A - Port your web app.** Rebuild the app from your [web app homework](../05_ai_web_apps/web_hw.md) as a Tkinter desktop app, as you did with Bridge Builder in class. Then add **at least two features** that the web version didn't have. Look for features that use what Python and a desktop app do well, for example:

- Saving and opening work as files
- Reading input data from a CSV or Excel file with pandas
- Exporting results to CSV or Excel
- matplotlib plots that the user can zoom and save
- Running many cases at once, such as a parameter sweep that plots how an output changes with an input

**Option B - Build a new problem.** Choose a problem from the [web app homework](../05_ai_web_apps/web_hw.md) that you did not build, and build it as a Tkinter desktop app. Any of them can be built as a desktop app. Name the problem in your spec and let the agent choose any extra packages it needs, such as a map package for the map problems. Use the problem's must-have features and its validation check, and add at least two features of your own design, at least one of them your own idea rather than one from the problem's list.

## Requirements

Whichever option you choose, your app must:

1. **Use Tkinter** for its interface and start with `python app.py`.
2. **Have a spec** (`spec.md`) with all six sections from the [web apps reading](../05_ai_web_apps/web_read.md#1-write-a-spec), plus a **Platform** section. For Option A, also list the features you added.
3. **Pass at least three validation cases** listed in the spec: at least two with expected values you worked by hand or took from a reference (say which), and one property check, such as a symmetry or a proportionality. Add a **Validation results** section to the spec with the table of expected versus actual values from the agent's check, and confirm at least one case yourself in the app.
4. **Have a prompt log** (`prompts.md`): a record of each request you gave the agent, what it changed, and whether it worked, kept by the agent using the `AGENTS.md` line described in the [web apps reading](../05_ai_web_apps/web_read.md#standing-instructions-and-the-prompt-log). Read and correct it before you submit. Also have a `README.md` that says how to install and run the app.
5. **Be in a GitHub repository** with at least 5 commits that follow the workflow steps: the spec, the plan, the first working version, the validated version, and each feature. Graders will look at the commit history to see that you worked in steps, so committing everything at the end will lose points.

Follow the workflow from class: get a plan before the agent writes code, have the agent rerun your validation cases after every change, and add one feature at a time.

---

## Turning in/Rubric

!!! note "Do not put your name or NetID in the file"
    Learning Suite records who submitted each file, so your name is not needed
    inside the file itself. Leaving it out means your work can be graded
    anonymously, which keeps grading fair. Your GitHub repository address will
    show your GitHub username, which is fine for this assignment.

Upload a **`.zip` of your project folder** to Learning Suite. It should contain all of your app's Python files, `spec.md`, `prompts.md`, `README.md`, and any data files your app needs. On Windows, right-click the folder and choose **Send to → Compressed (zipped) folder**. On a Mac, right-click the folder and choose **Compress**.

Paste your GitHub repository address in the Learning Suite submission comments.

The TA will grade your app by unzipping it, installing the packages in your README, and running `python app.py`. Before you submit, unzip your own file into a new folder and do the same thing to make sure it works.

**Rubric:**

|                                         **Items**                                          | **Amount** |  
|:------------------------------------------------------------------------------------------:|:----------:|
|           Spec has all required sections, including Platform (and added features)          |     4      |
|      App works: the port plus 2 new features (Option A), or the must-haves plus 2 of your own features (Option B) |     10     |
|    3+ validation cases pass, with results in the spec and sources for expected values      |     8      |
|        App is easy to use: clear labels, units on every number, looks finished            |     3      |
|                  Prompt log is complete                                                    |     3      |
|        README works, and at least 5 commits match the workflow steps                       |     2      |
|                         <div style="text-align: right">**Total**</div>                    |   **30**   |

---

The following is not a part of the rubric, but specifies how you can lose points.

|          **Reasons for Points Lost**          |    **Amount**     |  
|:---------------------------------------------:|:-----------------:|
|           File uploaded incorrectly           |       -10%        |
|           Turned in late (per week)           | -10% (up to -50%) |
|            No prompt log submitted            |       -50%        |
