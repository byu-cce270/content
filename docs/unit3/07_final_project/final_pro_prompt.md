#  Final Project

**Purpose:** As a team, design, build, validate, and present an app that solves a real problem in civil engineering or construction, using an AI coding agent.

If you haven't done the proposal yet, you can find the instructions here: [Final Project Proposal](final_pro_proposal.md). The [final project reading](final_pro_read.md) describes the design process and how to work as a team.

## Instructions

1. You will work with the team you formed earlier. You can find your team here:
</br>(If you need to change teams for any reason, please contact the head TA or the professor)

    - [Section 1 (Tue/Thur) F26 Team Sign up Sheet](https://docs.google.com/spreadsheets/d/1wuC_wtIl35VIJQPS_9wqFshkSZB9AH3bdgrOphxBbao/edit?gid=2018473579#gid=2018473579){:target="_blank"}
    - [Section 2 (Mon/Wed) F26 Team Sign up Sheet](https://docs.google.com/spreadsheets/d/1BbOlW3br0eThzIEGwqug39G6jgy3ZJRTF82djzRp0IA/edit?gid=2018473579#gid=2018473579){:target="_blank"}

2. Sign up for a time to present your project to the class:

    - [Section 1 (Tue/Thur) W26 Final Project Presentation Time](https://docs.google.com/spreadsheets/d/1nDVYvtjEuYaGbyBVqcca9jvJ2Bi295bQr9OErrtKDKI/edit?gid=161779235#gid=161779235){:target="_blank"}
    - [Section 2 (Mon/Wed) W26 Final Project Presentation Time](https://docs.google.com/spreadsheets/d/1VF3Kz6_FpXtXYWbdA36d2gVFDtvJPrkBni9LlTZ56Tg/edit?gid=1979404871#gid=1979404871){:target="_blank"}

3. Build the app described in your spec, following Step 4 of the design process in the reading. You may build either:
    - **A web app:** a single `index.html` file, published on GitHub Pages, or
    - **A desktop app:** a Python Tkinter app, started with `python app.py`, with its calculations in plain functions separate from the interface

4. Your project must include:
    - **Engineering substance:** The app must perform real calculations, analysis, or modeling from civil engineering or construction. An app that only displays or organizes information is not enough.
    - **A final spec** (`spec.md`) updated to match what you actually built, including the Design review and Validation plan sections from your proposal.
    - **Validation results:** A **Validation results** section in the spec showing each hand-worked case, the app's output, and whether they match, plus your property checks and edge cases. A desktop app must also have at least 5 pytest tests that pass, at least 3 of them using hand-worked or referenced expected values.
    - **Documentation:** A `README.md` at the top of the repository with:
        - What the app does and who it is for
        - How to use it, with at least two screenshots
        - How to run it: the GitHub Pages address, or the packages to install and the command to start it
        - A report of how each team member contributed
        - Links to any outside resources and data sources you used
    - **A prompt log** (`prompts.md`) kept by the team throughout the project
    - **A GitHub repository** containing all of the above, with every team member added as a collaborator

5. Present your project to the class. Your presentation should include a live demonstration of the app and a walkthrough of how you validated it. Be prepared to explain how any part of your code works.

---

## Turning in/Rubric

Only one team member needs to turn in the project. That team member should upload **a single `.zip` archive** of your project folder to the assignment in Learning Suite, and paste the GitHub repository address (and the GitHub Pages address, for a web app) in the submission comments.

To build the zip archive:

1. Pull, so your copy has everyone's latest commits.
2. Rename the project folder something like "(Your-Team-Name)-Final-Project".
3. Compress the folder into a single `.zip` file:
    - **Windows:** right-click the folder and choose **Send to | Compressed (zipped) folder**
    - **Mac:** right-click the folder and choose **Compress "(Your-Team-Name)-Final-Project"**
4. Upload the resulting `.zip` file to the assignment in Learning Suite.

Your Learning Suite submission is due at the start of the scheduled presentations.

**Rubric:**

|                                  Item                                   | Points Possible |
|:-----------------------------------------------------------------------:|:---------------:|
|        App works as described in the final spec, without bugs           |       20        |
|               Engineering substance of the calculations                 |       10        |
|      Final spec, with design review and validation plan                 |       10        |
|  Validation results (and, for a desktop app, at least 5 passing tests)  |       15        |
|          README: description, usage, screenshots, how to run            |        8        |
|           Report of each team member's contribution                     |        5        |
|             Prompt log and commit history                               |        7        |
|                       Presentation and demo                             |       15        |
|                             TA wow factor                               |       10        |
|             <div style="text-align: right">**Total**</div>              |       100       |

---

The following is not a part of the rubric, but specifies how you can lose points.

|                     **Reasons for Points Lost**                      | **Amount** |  
|:--------------------------------------------------------------------:|:----------:|
|          Files not turned in before the presentation                  |     10     |
|                      File uploaded incorrectly                       |     10     |
|                       No prompt log submitted                         |     50     |

---

## Project Ideas

You may propose any project with real engineering substance. Here are some ideas to start from. Each is bigger than a homework problem, so plan your features carefully.

### Roof Solar Planner
Draw a roof, place solar panels, and set the date and time. The app computes the sun's path for Provo, shows which panels are shaded and when, and estimates annual energy production and the payback period.

### Wasatch Earthquake Explorer
Plot earthquakes from the USGS real-time feed on a map with the Wasatch Fault drawn in, filtered by magnitude and date. Click a quake to estimate the shaking intensity at a chosen site, such as the BYU campus, using a published attenuation relationship.

### Tiny House Configurator
Lay out the walls, doors, and windows of a tiny house on a grid and see it in 3D. The app produces a live material takeoff (studs, sheathing, drywall, roofing) and a cost estimate that updates as the design changes.

### Block Stacking Challenge
Stack blocks to reach as far as possible past the edge of a table. The app tracks the center of mass of each sub-stack and topples the stack when it becomes unstable. Compare the best stack to the theoretical answer from the harmonic series.

### Expand a Homework App
Take your web or desktop app from Unit 3 and make it a substantially bigger tool, for example by adding new analyses, real data, or a second type of user. Talk to a TA before choosing this option to make sure the expansion is big enough.

### Your Own Idea
Many of the best projects come from problems a team member has seen at an internship or a summer job. If something you did by hand in Excel took hours, it may make a great app.
