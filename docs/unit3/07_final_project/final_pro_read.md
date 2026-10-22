# Reading: Building a Team Project with an AI Agent

---

For your final project, your team will design and build an app using an AI coding agent. You may build either a web app or a desktop app. This reading covers the two things that are new compared to your homework: a more careful design process, because the project is bigger, and working on the same code as a team.

## The Design Process

In the homework, you wrote a short spec, had the agent review it, and had the agent build from it. For a project several times larger, the same process needs more care at each step, and a validation plan written before any code. Follow these four steps, in order.

### Step 1: Write a detailed spec

Write `spec.md` with the same sections you have used all along (Purpose, Inputs, Calculations, Outputs, Validation, Out of scope), plus these:

- **Users:** Who will use the app, and what do they already know? A spec for a structural engineer can assume different things than one for a homeowner.
- **Screens:** Describe each part of the interface, or sketch it on paper and include a photo. What does the user see first? What do they click, and what happens?
- **Platform and structure:** Web or desktop, and which files the project will have.

Be as specific as you can. Every decision you leave out, the agent will make for you, and it won't ask.

### Step 2: Have the agent review the design

Before any code is written, ask the agent to critique your spec:

> Read spec.md. Don't write any code. Review this design as an experienced software engineer and civil engineer would. List anything that is ambiguous, missing, or inconsistent, any calculations that look wrong or incomplete, and any features that will be much harder to build than they look. Suggest improvements.

Read the review as a team and decide which suggestions to take. You don't have to take any of them, but you need a reason for each one you reject. Update the spec, and add a section at the end called **Design review** that lists each suggestion and what you decided.

### Step 3: Plan the validation

Decide how you will prove the app's answers are right before you build it, so that you aren't tempted to accept whatever the app produces. Add a **Validation plan** section to the spec:

- **Hand-worked cases:** At least three test cases with exact inputs and expected outputs, worked by hand or taken from a textbook, a design manual, or a previous homework. Write down where each expected value came from.
- **Property checks:** Things that must be true even without an exact answer, such as symmetric inputs giving symmetric results, totals adding up, or outputs that should increase when an input increases.
- **Edge cases:** Inputs at the limits, such as zero, very large values, or missing data. Decide what the app should do with each.
- **Automated tests:** For a desktop app, which of the cases above become pytest tests (at least 5). For a web app, you will check the cases by hand and record the results in a table.

You can ask the agent to suggest additional test cases, but the expected values must come from your team.

### Step 4: Build, review, and test

Now have the agent build the app, the way you did in the homework. Get a plan from the agent first, build one feature at a time, run your validation cases after every change, and commit after each working step. Read the code the agent writes for your calculations. You are responsible for every line of it, and in your presentation you may be asked to explain any part of it.

## Working as a Team

### Two ways to split the work

Your team can choose either approach, or switch between them.

- **One driver.** One person runs the agent and commits code, while the others write the spec, work the validation cases by hand, test the app, and write the documentation. Rotate the driver each work session so that everyone takes a turn. This is the simplest approach, because only one person changes the code at a time.
- **Everyone codes.** Each person works on a different feature at the same time on their own computer, and Git combines the work. This is faster once it works, but you will have to handle **merge conflicts**, described below.

Either way, everyone on the team should be able to clone the repository and run the app.

### Sharing a repository

1. One team member creates the repository and publishes it to GitHub, with at least `spec.md` in it.
2. On GitHub, that person goes to **Settings → Collaborators** and adds each teammate by GitHub username. Each teammate accepts the email invitation.
3. Each teammate clones the repository (**Clone Git Repository** on the VS Code Welcome tab).

Now everyone has a copy, and everyone can push to GitHub.

### The team workflow

Every time you sit down to work:

1. **Pull** first, to get your teammates' latest commits. In the Source Control panel, click **…** and then **Pull**, or click **Sync Changes**.
2. Make one change, test it, and commit.
3. **Push** (click **Sync Changes**) soon after you commit, so your teammates get your work.

Small, frequent commits make merging much easier than one big commit at the end of the day.

### Merge conflicts

If you and a teammate both change the same lines of the same file, Git can't tell which version to keep. When you pull, VS Code will mark the file with a **!** and open it in the **merge editor**, which shows both versions side by side. For each conflict, choose **Accept Current** (your version), **Accept Incoming** (your teammate's), or **Accept Both**, or edit the result by hand. Then click **Complete Merge**, commit, and push.

If you don't understand why the two versions differ, talk to your teammate before choosing. You can also ask the agent: "There is a merge conflict in index.html. Explain what each version does and recommend how to combine them."

### Branches

To avoid stepping on each other, each person can work on a **branch**, which is a separate line of commits that doesn't affect anyone else until it is merged.

1. Click the branch name at the bottom left of VS Code and choose **Create new branch**. Name it after the feature, such as `cost-report`.
2. Work and commit as usual. Click **Publish Branch** to push it to GitHub.
3. When the feature works, open the repository on GitHub. It will offer to create a **pull request** for your branch. Create it, and have a teammate look over the changes and merge it.
4. Switch back to the `main` branch (click the branch name again) and pull to get the merged work.

### Give the agent the team's rules

Each agent reads a standing instructions file from the top of your repository at the start of every conversation: Copilot reads `.github/copilot-instructions.md` or `AGENTS.md`, Codex reads `AGENTS.md`, and Claude Code reads `CLAUDE.md`. Put your team's rules there so that everyone's agent follows them. For example:

```markdown
- Read spec.md before making any change.
- Calculations go in calcs.py, never in the interface code.
- Units are US customary; label every number shown to the user.
- Run pytest after every change. Never change an expected value in a test.
```
