#  Final Project Design

**Purpose:** Choose a problem, then design your app before you build it: set up your team's repository, write the spec, have the agent review it, and plan how you will prove the app's answers are right.

Work with your [team](final_pro_class.md#your-team).

In the homework, you wrote a short spec, had the agent review it, and had the agent build from it. For a project several times larger, the same process needs more care at each step, and a validation plan written before any code. This part covers everything up to the code. [Part 2](final_pro_prompt.md#building-the-app) covers the build.

## Step 1: Choose a Problem

Your team chooses the problem. We recommend one from your major: civil engineering, construction management, or facilities and property management. You are also free to be creative. Teams have built games and other apps outside their majors, and those work well too if they meet the guidelines below. The best final projects solve a problem someone actually has, and the hardest part of the project is finding one. Spend real time on it before you commit.

**Where to look:**

- **Work you've done by hand.** Think about internships, summer jobs, and other classes. What did you calculate over and over, look up in tables, schedule by hand, or track in a messy spreadsheet?
- **People you know.** Ask a professor, a TA, an engineer, contractor, or property manager you've worked for, or a classmate in another major what they wish they had a tool for.
- **Your surroundings.** Campus, your apartment complex, a construction site you walk past, Utah's water, roads, snow, and earthquakes. What would be useful to measure, map, predict, track, or explain?
- **Businesses you know.** Running a crane rental company, maintaining an apartment complex, tracking equipment on a jobsite, or scheduling crews. What would make the work easier?
- **Things you're curious about.** A good app can also make an idea visible or turn it into a game: how a structure carries load, how water moves through a basin, how a schedule slips.

**Kinds of apps that work well:**

- **Calculators and design tools,** such as sizing a beam, estimating concrete, or comparing bids
- **Simulations,** such as traffic at an intersection or water moving through a basin
- **Maps,** such as snow loads across Utah, building conditions across campus, or active job sites
- **Management tools,** such as scheduling a crane company's fleet, tracking work orders for an apartment complex, or keeping a project budget
- **Games** built around an idea from your field

**What makes a problem a good one:**

- **A real user.** You can name who would use the app and what it helps them do.
- **Substance.** The app does real work for its users, such as calculating, simulating, mapping, scheduling, tracking, or managing something. A page that only shows fixed information isn't enough.
- **Checkable answers.** You can work at least three cases by hand or find them in a reference, so you can prove the app is right.
- **The right size.** Your team can build a working first version in a week and spend the rest of the time improving and validating it. If you can't describe the first version in two sentences, narrow the problem.

Before you go on, describe your problem to a TA or the instructor in a few sentences and get their approval. They will help you scale it up or down.

## Step 2: Set Up the Team Repository

Your whole team works in one GitHub repository, for the design and for the build. You set it up once, and after that the agent handles almost all of the Git work.

### Write the Team's Rules

You have used `AGENTS.md` since the web apps section to have the agent keep your prompt log. In a team, it does more: everyone's agent reads the same file, so put your team's rules there and every agent follows them, whichever agent each person uses. (Codex reads it only when it starts, so restart it after you change the file.) Start with rules like these, and add your own as you go:

```markdown
- Read spec.md before making any change.
- After each request, add an entry to prompts.md: who entered the prompt (use the name from `git config user.name`), what they asked, what you changed, and whether it worked.
- Pull before starting work, and push after every change that passes validation.
- Units are US customary; label every number shown to the user.
- Rerun the validation cases in spec.md after every change.
```

### Share the Repository

1. Choose one person to be the **owner**. The owner makes a folder named for your app, such as `crane_scheduler` (use underscores, not spaces). The folder name becomes the repository's name on GitHub, and for a web app, part of its GitHub Pages address. The owner opens the folder in VS Code, creates `AGENTS.md` with your team's rules, and asks the agent:

    !!! prompt "Prompt"
        Initialize a Git repository here, commit AGENTS.md, and publish it to GitHub as a public repository.

2. The owner opens the repository on GitHub, goes to **Settings → Collaborators**, and adds each teammate by GitHub username.
3. Each teammate accepts the invitation from their email or GitHub notifications, then clones the repository, the same way you cloned Alien Invasion in [Using Python Locally](../04_local_python/local_py_class.md#exercise-3-clone-and-run-a-game):
    1. On the repository's page on GitHub, click the green **Code** button and copy the URL.
    2. In VS Code, choose **File → New Window**. On the Welcome tab, click **Clone Git Repository**.
    3. Paste the URL and press Enter.
    4. Choose your class folder as the location. When VS Code offers to open the cloned repository, click **Open**.
    5. If a Restricted Mode banner appears, click **Manage**, then click **Trust**.

### Every Work Session

From now until the end of the project, start every work session by getting your teammates' latest work:

!!! prompt "Prompt"
    Pull the latest changes from GitHub and summarize what my teammates changed since my last session.

Work the way you have all along: one change at a time, checked before you move on. When a change is done, share it:

!!! prompt "Prompt"
    Commit these changes and push them to GitHub.

Push soon after each change instead of at the end of the day. The longer you wait, the more likely you and a teammate have changed the same lines.

### When Two People Change the Same Lines

If you and a teammate change the same lines, Git can't tell which version to keep. This is called a **merge conflict**, and it shows up when you pull or push.

The best way to handle merge conflicts is to avoid them. Coordinate so that two people aren't changing the same part of the project at the same time. Agree on who is working on what before each work session, split the work by feature or by file, and tell your teammates when you start and finish something. If two of you need to change the same file, such as `spec.md`, take turns: pull before you start, and push as soon as you finish.

If a conflict happens anyway, don't try to untangle it by hand. Ask the agent:

!!! prompt "Prompt"
    There is a merge conflict. Explain what my version and my teammate's version each do, and recommend how to combine them. Don't change anything until I approve.

Read its explanation. If the two versions do different things that both matter, check with your teammate before you approve. Then have the agent resolve the conflict, rerun the validation cases (once you have code), commit, and push.

## Step 3: Write the Spec

As a team, start with an outline of your idea in `spec.md`. Use the sections you have used all along (Purpose, Inputs, Calculations, Outputs, and Out of scope), plus these:

- **Users:** Who will use the app, and what do they already know?
- **Screens:** What the user sees first, what they click, and what happens. A photo of a paper sketch is fine.
- **Platform and structure:** A web app (a single `index.html` file on GitHub Pages) or a desktop app (a Python app built with Tkinter, CustomTkinter, or PySide6 and started with `python app.py`), and the files the project will have.

Each section can start as a rough list. If your app schedules, tracks, or follows rules instead of calculating, put those rules under Calculations.

Then have the agent help you get the spec ready to build, the same way you did in the [web apps homework](../05_ai_web_apps/web_read.md#2-write-and-review-the-spec-with-the-agent):

!!! prompt "Prompt"
    Read spec.md. Don't write any code. Help us finish the spec so it's ready to build.

## Step 4: Have the Agent Review the Design

Before any code is written, ask the agent to critique your spec:

!!! prompt "Prompt"
    Read spec.md and review the design. Don't write any code. Point out any problems and suggest improvements.

Read the review as a team and decide which suggestions to take. You don't have to take any of them, but you need a reason for each one you reject. Update the spec, and add a section at the end called **Design review** that lists each suggestion and what you decided.

## Step 5: Plan the Validation

Before you build, decide how you will prove the app's results are right, so you aren't tempted to accept whatever the app produces. The agent can do most of this. Ask it to draft the plan:

!!! prompt "Prompt"
    Read spec.md. Don't write any code. Add a Validation plan section with at least three test cases (exact inputs and expected outputs), property checks, and edge cases.

- **Test cases** give exact inputs and the outputs the app must produce.
- **Property checks** are things that must be true even without an exact answer, such as totals adding up, or an output that should increase when an input increases.
- **Edge cases** are inputs at the limits, such as zero, very large values, or missing data, and what the app should do with each.

Your team's job is to check the test cases. Work each one by hand, or find it in a textbook, a manual, or a previous homework, and write down where each expected value came from. If an expected value is wrong, the agent will build the app to match it.

## Step 6: Plan the Teamwork

Everyone on the team works on the app. That is the point of sharing a Git repository. Graders will check the commit history and the prompt log to see that every team member entered their own prompts and made their own commits, from their own computer and GitHub account, throughout the project.

Add a **Team workflow** section to the spec that says who is responsible for which features and other parts of the project.

---

# Turning In/Rubric

Only one team member needs to turn in the design. Upload `spec.md` to Learning Suite, and paste your team repository's GitHub address in the submission comments.

|                                    **Item**                                     | **Amount** |
|:-------------------------------------------------------------------------------:|:----------:|
|  Spec: Purpose, Users, Inputs, Calculations, Outputs, Screens, Out of scope     |     10     |
|                 Design review: suggestions and team decisions                   |     6      |
|      Validation plan: 3+ hand-worked cases with sources, property checks, edge cases |  10     |
|                  Platform, structure, and team workflow                         |     4      |
|                 <div style="text-align: right">**Total**</div>                  |   **30**   |

---

The following is not a part of the rubric, but specifies how you can lose points.

|          **Reasons for Points Lost**          |    **Amount**     |  
|:---------------------------------------------:|:-----------------:|
|           File uploaded incorrectly           |       -10%        |
|           Turned in late (per week)           | -10% (up to -50%) |
