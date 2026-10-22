# In-Class Exercise: Team Git and Project Kickoff

Sit with your final project team for this exercise. You will set up a shared repository, cause a merge conflict on purpose and have the agent resolve it, and then start your project's spec.

## Part 1 - Share a Repository

1. Choose one person to be the **owner**. The owner makes a folder named after your team, opens it in VS Code, creates a file named `team.md` containing the line `# Team members`, and asks the agent:

    !!! prompt "Prompt"
        Initialize a Git repository here, commit team.md, and publish it to GitHub as a public repository.

2. The owner opens the repository on GitHub, goes to **Settings → Collaborators**, and adds each teammate by GitHub username.
3. Each teammate accepts the invitation from their email or GitHub notifications, then clones the repository in VS Code (**Clone Git Repository** on the Welcome tab).

## Part 2 - Take Turns

One at a time, each person adds a line to `team.md` with their name and one thing they hope the app will do, then asks the agent:

!!! prompt "Prompt"
    Pull the latest changes, then commit my change to team.md and push it.

When everyone has had a turn, everyone pulls. Every copy of `team.md` should now list the whole team.

## Part 3 - Cause a Merge Conflict

1. Everyone pulls, so all copies match.
2. **At the same time**, everyone changes the first line of `team.md` to a different team name of their own invention and asks the agent to commit and push.
3. The first person's push works. Everyone else's agent will report that the push was rejected, or that pulling caused a merge conflict.
4. Each person who has a conflict asks:

    !!! prompt "Prompt"
        There is a merge conflict. Explain what my version and my teammate's version each do, and recommend how to combine them. Don't change anything until I approve.

5. Agree on a team name out loud, tell the agent which version to keep, and have it finish the merge and push.
6. When everyone has pushed, everyone pulls and checks that all copies match.

## Part 4 - Start Your Spec

Use the rest of class to start on your [project proposal](final_pro_proposal.md):

1. Decide whether you will build a web app or a desktop app, and how you will split the work: one driver, everyone coding, or a mix.
2. Create `spec.md` in your team repository and write a first draft of the Purpose, Users, Inputs, and Outputs sections.
3. Ask the agent for a design review of what you have so far, as described in the [reading](final_pro_read.md#step-2-have-the-agent-review-the-design). Discuss its suggestions as a team.
