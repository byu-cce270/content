# In-Class Exercise: Team Git and Project Kickoff

Sit with your final project team for this exercise. You will practice sharing a repository, cause a merge conflict on purpose and resolve it, and then start your project's spec.

## Part 1 - Share a Repository

1. Choose one person to be the **owner**. The owner makes a folder named after your team, opens it in VS Code, creates a file named `team.md` containing the line `# Team members`, commits it, and publishes it to GitHub as a public repository.
2. The owner opens the repository on GitHub, goes to **Settings → Collaborators**, and adds each teammate by GitHub username.
3. Each teammate accepts the invitation from their email or GitHub notifications, then clones the repository in VS Code.

## Part 2 - Take Turns

1. One at a time, each person pulls, adds a line to `team.md` with their name and one thing they hope the app will do, commits, and pushes.
2. After everyone has had a turn, everyone pulls. Every copy of `team.md` should now list the whole team.

## Part 3 - Cause a Merge Conflict

1. Everyone pulls, so all copies are identical.
2. **At the same time**, everyone changes the first line of `team.md` to a different team name of their own invention, then commits. Don't push yet.
3. One person pushes. That push works.
4. The next person tries to push. Git refuses, because GitHub has a commit their copy doesn't have. They pull, and VS Code reports a merge conflict.
5. Resolve it: open `team.md` from **Merge Changes** in the Source Control panel, pick a team name using the **Accept** buttons above the conflict (or edit it by hand), click **Complete Merge**, commit, and push.
6. Repeat until everyone has pushed. Then everyone pulls and checks that all copies match.

## Part 4 - Use a Branch

1. One person creates a branch named `add-goals`, adds a `## Goals` section to `team.md`, commits, and clicks **Publish Branch**.
2. On GitHub, that person creates a pull request for the branch.
3. A different teammate reviews the change on GitHub and clicks **Merge pull request**.
4. Everyone switches to `main` and pulls.

## Part 5 - Start Your Spec

Use the rest of class to start on your [project proposal](final_pro_proposal.md):

1. Decide whether you will build a web app or a desktop app, and how you will split the work: one driver, everyone coding, or a mix.
2. Create `spec.md` in your team repository and write a first draft of the Purpose, Users, Inputs, and Outputs sections.
3. Ask the agent for a design review of what you have so far, as described in the [reading](final_pro_read.md#step-2-have-the-agent-review-the-design). Discuss its suggestions as a team.
