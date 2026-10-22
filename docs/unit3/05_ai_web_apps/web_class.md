# In-Class Exercise: Bridge Builder

In this exercise, the class will build a truss analysis app together. You click to place joints, connect them with members, put a load on the bridge, and the app solves for the force in every member and colors each one by tension or compression. You will check it against the truss you solved with numpy in the [Numpy homework](../00_numpy/numpy_hw.md), then publish it on GitHub Pages.

Your app will not look exactly like your neighbor's, even with the same prompts. Agents don't give the same answer twice. That is fine as long as yours passes validation.

## Step 1 - Set Up the Project

1. Make a folder named `bridge_builder` in your class folder and open it in VS Code.
2. In the **Source Control** panel, click **Initialize Repository**.
3. Create a file named `prompts.md` for your prompt log. Add an entry to it after each request you make to the agent today.

In Using Python Locally you made commits yourself. From here on, the agent makes them. Whenever this page says to ask the agent to commit, enter "Commit these changes" in **Agent** mode, allow the `git` command it asks to run, and read the commit message it writes.

## Step 2 - Write the Spec

Create a file named `spec.md` and paste in this spec. Read it all the way through before you go on. Every sentence in it is a decision someone had to make.

```markdown
# Bridge Builder

## Purpose
An interactive 2D truss analysis app for a statics or structures student.
The user draws a truss, loads it, and sees the force in every member.

## Inputs
- Joints: placed by clicking on a grid (1 ft spacing, snap to grid), or by
  typing x and y coordinates (ft) into a joint table. Coordinates in the
  table can be any decimal value.
- Members: created by clicking one joint, then another.
- Supports: the user marks one joint as a pin (resists x and y) and one
  joint as a roller (resists y only).
- Loads: the user selects a joint and enters a vertical load in lb
  (downward is negative).
- A "Delete" mode that removes a joint (and its members) or a member.

## Calculations
Method of joints, solved as one linear system.
- For each joint, sum of forces in x = 0 and sum of forces in y = 0.
- Unknowns: one axial force per member, plus 2 reactions at the pin and
  1 at the roller.
- Member force sign convention: tension positive, compression negative.
- The truss is solvable only if (members + 3) = 2 x (joints). If not,
  show a message saying whether the truss is unstable or indeterminate
  and do not solve.
- If the system is singular (a mechanism), show "Truss is unstable"
  instead of numbers.
- Solve the system with Gaussian elimination written in plain JavaScript.

## Outputs
- Members colored by force: tension blue, compression red, zero-force gray.
  Line thickness proportional to force magnitude.
- Each member labeled with its force in lb, with T or C.
- Reactions shown as arrows at the supports, labeled in lb.
- The solution updates automatically whenever the truss or loads change.

## Validation
Numpy homework, Test 1:
- Joints: A (0, 0) pin, C (10, 0) roller, B (2.5, 4.330)
- Members: AB, BC, AC
- Load at B: -2000 lb
- Expected: AB = 1732 lb C, BC = 1000 lb C, AC = 866 lb T,
  reaction at A = 1500 lb up, reaction at C = 500 lb up,
  horizontal reaction at A = 0.

## Out of scope
- Moving loads, self-weight, and 3D trusses
- Saving or loading designs
```

Ask the agent to commit.

## Step 3 - Review the Spec

Even a spec someone else wrote can be improved. In the Copilot chat panel, switch to **Ask** mode and enter:

> Read spec.md. Don't write any code. List anything in this spec that is ambiguous, missing, or inconsistent, check the equations in the Calculations section, and point out anything that will be hard to build. Suggest improvements.

Discuss the suggestions with the people around you. Take any that make the spec clearer (for example, what happens when the user deletes a support), and skip any that add features you don't need yet. Update `spec.md`, add the review to your prompt log, and ask the agent to commit.

## Step 4 - Build It

Open the Copilot chat panel, switch to **Agent** mode, and enter:

> Read spec.md and build the app it describes as a single file named index.html. Use plain HTML, CSS, and JavaScript with no build tools. Put the truss solver in its own clearly named functions, separate from the drawing code.

Watch what the agent does. It will probably write the file in pieces, and it may ask permission to run commands. When it finishes, double-click `index.html` to open it in your browser.

Try drawing a truss. If something doesn't work, describe exactly what you did and what happened, and ask the agent to fix it. Check the browser's developer console for red error messages (**F12**, or **Cmd+Option+J** in Chrome on a Mac) and paste any you find into the chat.

When you can draw a truss and see forces, ask the agent to commit.

## Step 5 - Validate

Use the joint table to build the Numpy homework truss from the **Validation** section of the spec, and add the -2000 lb load at B. Compare the app's results to the expected values.

Then check the expected values yourself. Sketch a free body diagram of joint B and confirm that AB = 1732 lb and BC = 1000 lb satisfy both equilibrium equations. The angles at A and C are 60° and 30°.

If anything doesn't match, look at three things before asking the agent:

- **Sign convention:** Is tension positive?
- **Units:** Are the forces in lb?
- **Geometry:** Is joint B where you think it is?

Then give the agent the inputs, the expected values, and what the app showed.

Next, check a truss you can't compare against the homework. Draw a symmetric truss with a symmetric load. The two vertical reactions must be equal, and they must add up to the total load. This kind of check, where you know a property the answer must have even without the exact answer, catches a surprising number of errors.

When the app passes both checks, ask the agent to commit.

## Step 6 - Make It a Game

Now make it fun. Add each of these features **one at a time**, testing and committing after each:

1. **Member failure:** Each member can carry 10,000 lb in tension and 6,000 lb in compression. Members that exceed their capacity turn black and dashed, and a banner says "Bridge failed!"
2. **Cost:** Members cost $5 per foot and joints cost $50 each. Show the total cost of the bridge.
3. **Challenge mode:** A button sets up a 40 ft gap with a pin at (0, 0), a roller at (40, 0), and a -6000 lb (downward) load at (20, 0). The user builds the cheapest bridge that holds the load.

Before you ask for each feature, add it to the spec. For example, add the capacities to the **Inputs** and **Calculations** sections before asking for member failure.

Compete with the people around you: who can build the cheapest bridge that holds 6000 lb?

## Step 7 - Publish

1. In the Source Control panel, click **Publish Branch** and choose a **public** repository.
2. On your repository's page on GitHub, go to **Settings → Pages**. Set **Source** to **Deploy from a branch**, choose **main** and **/ (root)**, and click **Save**.
3. After a minute or two, refresh the page to see your site's address. Open it on your phone.
4. Send the link to someone sitting near you and have them try to beat your bridge.
