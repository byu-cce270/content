#  Final Project

**Purpose:** As a team, design, build, validate, and present an app that solves a real problem, using an AI coding agent.

Do [Part 1: Design](final_pro_proposal.md) first. This page picks up where it leaves off: building the app from your spec as a team, presenting it, and turning it in. You will work with your [team](final_pro_class.md#your-team) in the repository you set up in Part 1.

## What Your Project Must Include

- **A working app,** built as the web app or desktop app your spec describes.
- **Substance:** The app must do real work for its users, such as calculating, simulating, mapping, scheduling, tracking, or managing something. A page that only shows fixed information is not enough.
- **A final spec** (`spec.md`) updated to match what you actually built, including the Design review and Validation plan sections from Part 1.
- **Validation results:** A **Validation results** section in the spec showing each hand-worked case, the app's output, and whether they match, plus your property checks and edge cases.
- **Documentation:** A `README.md` at the top of the repository with:
    - What the app does and who it is for
    - How to use it, with at least two screenshots
    - How to run it: the GitHub Pages address, or the packages to install and the command to start it
    - A report of how each team member contributed
    - Links to any outside resources and data sources you used
- **A prompt log** (`prompts.md`) kept by the agent throughout the project, and read and corrected by the team
- **Each team member's agent chats:** a `chats/` folder with every team member's exported conversations with the AI agent, in a file or subfolder named for that person (for example, `chats/jane-smith.md`). In VS Code, you can save a Copilot chat by opening the Command Palette and running **Chat: Export Chat...**.
- **A GitHub repository** containing all of the above, with every team member added as a collaborator

## Building the App

Have the agent build the app from your spec, the way you did in the homework. Build one feature at a time, run your validation cases after every change, and commit after each working step. Read the code the agent writes for the app's core logic, such as its calculations, cost totals, or scheduling rules. You are responsible for every line of it, and in your presentation you may be asked to explain any part of it.

Keep working in the team repository the way you did in Part 1: pull at the start of [every work session](final_pro_proposal.md#every-work-session), push after every change that passes validation, and have the agent resolve any merge conflicts with your approval.

## How Teamwork Is Graded

This is a team project, and we grade it that way:

- **Every team member commits and prompts.** Graders will look at the commit history and the prompt log to see that each team member made their own commits and entered their own prompts throughout the project, from their own computer and GitHub account. A repository where one person made all of the commits will lose points, even if the whole team met together.
- **Every team member turns in their chats.** The chats in `chats/` show how each person worked with the agent. A team member with no chats loses points for the team.

!!! warning "Work with your group"
    If you do not work with your group, **50% will be taken off your final project grade**. If you are having trouble working with a group member, tell your professor and the Head TA **as soon as possible**, not at the end of the project. We can help while there is still time to fix it.

## Presentation

Sign up for a time to present your project to the class:

- [Section 1 (Tue/Thur) W26 Final Project Presentation Time](https://docs.google.com/spreadsheets/d/1nDVYvtjEuYaGbyBVqcca9jvJ2Bi295bQr9OErrtKDKI/edit?gid=161779235#gid=161779235){:target="_blank"}
- [Section 2 (Mon/Wed) W26 Final Project Presentation Time](https://docs.google.com/spreadsheets/d/1VF3Kz6_FpXtXYWbdA36d2gVFDtvJPrkBni9LlTZ56Tg/edit?gid=1979404871#gid=1979404871){:target="_blank"}

Your presentation should include a live demonstration of the app and a walkthrough of how you validated it. Be prepared to explain how any part of your code works.

Every team member must be present for the presentation. Being present is worth 5 points (5%) of the Presentation and demo score, and a team member who is not there loses those 5 points.

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

!!! warning "Everything is due before presentations start"
    The whole project is due **before the first presentation in your section starts**, even if your team presents later. That includes the `.zip` upload in Learning Suite, every team member's chats in `chats/`, and your final commits pushed to GitHub. Commits pushed after presentations start will not be graded.

**Rubric:**

|                                  Item                                   | Points Possible |
|:-----------------------------------------------------------------------:|:---------------:|
|        App works as described in the final spec, without bugs           |       16        |
|            Substance: the real, useful work the app does                |       10        |
|      Final spec, with design review and validation plan                 |       10        |
|                       Validation results                                |       13        |
|          README: description, usage, screenshots, how to run            |        6        |
|                             Prompt log                                  |        5        |
|                     **Teamwork:**                                       |                 |
|   Commit history and prompt log show every team member working throughout the project |    10        |
|              Every team member's agent chats turned in                  |        5        |
|           Report of each team member's contribution                     |        5        |
|   Presentation and demo (5 of these points are for being present)      |       10        |
|                             TA wow factor                               |       10        |
|             <div style="text-align: right">**Total**</div>              |       100       |

---

The following is not a part of the rubric, but specifies how you can lose points.

|                     **Reasons for Points Lost**                      | **Amount** |  
|:--------------------------------------------------------------------:|:----------:|
|          Files not turned in before presentations start               |     10     |
|                      File uploaded incorrectly                       |     10     |
|                       No prompt log submitted                         |     50     |
|     Not working with your group (taken off that team member's grade)  |     50     |
