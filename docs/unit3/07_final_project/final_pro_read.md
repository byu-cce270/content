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

!!! prompt "Prompt"
    Read spec.md. Don't write any code. Review this design as an experienced software engineer and civil engineer would. List anything that is ambiguous, missing, or inconsistent, any calculations that look wrong or incomplete, and any features that will be much harder to build than they look. Suggest improvements.

Read the review as a team and decide which suggestions to take. You don't have to take any of them, but you need a reason for each one you reject. Update the spec, and add a section at the end called **Design review** that lists each suggestion and what you decided.

### Step 3: Plan the validation

Decide how you will prove the app's answers are right before you build it, so that you aren't tempted to accept whatever the app produces. Add a **Validation plan** section to the spec:

- **Hand-worked cases:** At least three test cases with exact inputs and expected outputs, worked by hand or taken from a textbook, a design manual, or a previous homework. Write down where each expected value came from.
- **Property checks:** Things that must be true even without an exact answer, such as symmetric inputs giving symmetric results, totals adding up, or outputs that should increase when an input increases.
- **Edge cases:** Inputs at the limits, such as zero, very large values, or missing data. Decide what the app should do with each.
- **How you will check them:** Plan to have the agent run every case and report a table of expected versus actual values, and to rerun that check after every change. Also plan to confirm some cases yourself in the app.

You can ask the agent to suggest additional test cases, but the expected values must come from your team.

### Step 4: Build, review, and test

Now have the agent build the app, the way you did in the homework. Get a plan from the agent first, build one feature at a time, run your validation cases after every change, and commit after each working step. Read the code the agent writes for your calculations. You are responsible for every line of it, and in your presentation you may be asked to explain any part of it.

## Working as a Team

Your whole team works in one GitHub repository. You set it up once on GitHub, and after that the agent handles almost all of the Git work.

### Set up the shared repository

1. One team member creates the repository and publishes it to GitHub, with at least `spec.md` in it.
2. On GitHub, that person goes to **Settings → Collaborators** and adds each teammate by GitHub username. Each teammate accepts the email invitation.
3. Each teammate clones the repository (**Clone Git Repository** on the VS Code Welcome tab).

### Every work session

Start by getting your teammates' latest work:

!!! prompt "Prompt"
    Pull the latest changes from GitHub and summarize what my teammates changed since my last session.

Work the way you have all along: one change at a time, validated before you move on. When a change works, share it:

!!! prompt "Prompt"
    Commit these changes and push them to GitHub.

Push soon after each change instead of at the end of the day. The longer you wait, the more likely you and a teammate have changed the same code.

### When two people change the same code

If you and a teammate change the same lines, Git can't tell which version to keep. This is called a **merge conflict**, and it shows up when you pull or push. Don't try to untangle it by hand. Ask the agent:

!!! prompt "Prompt"
    There is a merge conflict. Explain what my version and my teammate's version each do, and recommend how to combine them. Don't change anything until I approve.

Read its explanation. If the two versions do different things that both matter, check with your teammate before you approve. Then have the agent resolve the conflict, rerun the validation cases, commit, and push.

### Splitting the work

Your team can split the work either of these ways, or switch between them:

- **One driver.** One person runs the agent while the others write the spec, work the validation cases by hand, test the app, and write the documentation. Rotate the driver each work session so everyone takes a turn. Merge conflicts can't happen, because only one person changes the code.
- **Everyone codes.** Each person works on a different feature at the same time. To keep from stepping on each other, each person can work on their own **branch**, a separate copy of the code that is merged back when the feature is done:

    !!! prompt "Prompt"
        Create a branch named cost-report for the cost report feature, and switch to it.

    When the feature works and passes validation:

    !!! prompt "Prompt"
        Merge the cost-report branch into main, resolve any conflicts with my approval, rerun the validation cases, and push.

### Give the agent the team's rules

Copilot, Codex, and Claude Code all read a file named `AGENTS.md` at the top of your repository when a conversation starts. Put your team's rules there so that everyone's agent follows them, whichever agent they use. (Codex reads it only when it starts, so restart it after you change the file.) For example:

```markdown
- Read spec.md before making any change.
- Pull before starting work, and push after every change that passes validation.
- Units are US customary; label every number shown to the user.
- Rerun the validation cases in spec.md after every change. Never change an expected value.
```
