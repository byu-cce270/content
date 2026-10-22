# In-Class Exercise: Will It Break?

In this exercise, you will build a bridge game. You design a truss bridge across a 60 ft gap, then drive vehicles across it, from a small car up to a fire engine. As each vehicle rolls across, every member lights up with its force, and if any member is overloaded, the bridge fails. The challenge is to build the cheapest bridge that carries every vehicle.

You will build it in stages: first a truss solver that you check against the truss from the [Numpy homework](../00_numpy/numpy_hw.md) and a hand calculation, then the bridge, the vehicles, failure, and cost. At the end, you will publish it on GitHub Pages and compete with your classmates.

Your app will not look exactly like your neighbor's, even with the same prompts. Agents don't give the same answer twice. That is fine as long as yours passes validation.

## Step 1 - Set Up the Project

1. Make a folder named `bridge_builder` in your class folder and open it in VS Code.
2. In the **Source Control** panel, click **Initialize Repository**.
3. Create a file named `AGENTS.md` containing this line, so the agent keeps your prompt log (see the [reading](web_read.md#standing-instructions-and-the-prompt-log)):

    ```markdown
    - After each request, add an entry to prompts.md: what I asked, what you changed, and whether it worked.
    ```

In Using Python Locally you made commits yourself. From here on, the agent makes them. Whenever this page says to ask the agent to commit, enter "Commit these changes" in **Agent** mode, allow the `git` command it asks to run, and read the commit message it writes.

## Step 2 - Write the Spec

The first version of the app is a truss solver: draw any truss, load it, and see the force in every member. The bridge and vehicles come later, once the solver is proven right.

Create a file named `spec.md` and paste in this spec. Read it all the way through before you go on. Every sentence in it is a decision someone had to make.

```markdown
# Will It Break?

## Purpose
A truss bridge design game for civil engineering students. The user
draws a truss, loads it, and sees the force in every member.

## Inputs
- A toolbar of modes: Joint, Member, Pin, Roller, Load, and Delete.
- Joints: placed by clicking on a grid (1 ft spacing, snap to grid), or by
  typing x and y coordinates (ft) into a joint table. Coordinates in the
  table can be any decimal value. Joints are named A, B, C, ... in the
  order they are created, and the user can rename them in the table.
- The grid shows x from -5 to 65 ft and y from -20 to 20 ft.
- Members: created by clicking one joint, then another.
- Supports: the user marks one joint as a pin (resists x and y) and one
  joint as a roller (resists y only).
- Loads: the user selects a joint and enters a vertical load in lb
  (downward is negative).
- Delete mode removes a joint (and its members, support, and load) or a
  member.

## Calculations
Method of joints, solved as one linear system.
- For each joint, sum of forces in x = 0 and sum of forces in y = 0.
- Unknowns: one axial force per member, plus 2 reactions at the pin and
  1 at the roller.
- Member force sign convention: tension positive, compression negative.
- Until one pin and one roller are placed, show "Add a pin and a roller"
  instead of solving. A joint can't be both.
- The truss is solvable only if (members + 3) = 2 x (joints). If not,
  show a message saying whether the truss is unstable or indeterminate
  and do not solve.
- If the system is singular or nearly singular (a mechanism), show
  "Truss is unstable" instead of numbers.

## Outputs
- Members colored by force: tension blue, compression red, zero-force
  (under 0.5 lb) gray. Line thickness from 2 px to 8 px, proportional to
  force magnitude.
- Each member labeled with its force in lb, with T or C.
- Reactions shown as arrows at the supports, labeled in lb.
- The solution updates automatically whenever the truss or loads change.

## Validation
Numpy homework, Test 1:
- Joints: A (0, 0) pin, B (2.5, 4.330), C (10, 0) roller
- Members: AB, BC, AC
- Load at B: -2000 lb
- Expected: AB = 1732 lb C, BC = 1000 lb C, AC = 866 lb T,
  reaction at A = 1500 lb up, reaction at C = 500 lb up,
  horizontal reaction at A = 0.

## Out of scope
- Self-weight, buckling, and 3D trusses
- Saving or loading designs
```

Ask the agent to commit.

## Step 3 - Review the Spec

Even a spec someone else wrote can be improved. In the Copilot chat panel, switch to **Ask** mode and enter:

!!! prompt "Prompt"
    Read spec.md. Don't write any code. List anything in this spec that is ambiguous, missing, or inconsistent, check the equations in the Calculations section, and point out anything that will be hard to build. Suggest improvements.

Discuss the suggestions with the people around you. Take any that make the spec clearer, and skip any that add features you don't need yet. Update `spec.md` and ask the agent to commit.

## Step 4 - Build the Solver

Switch to **Agent** mode and enter:

!!! prompt "Prompt"
    Read spec.md and build the app it describes as a single file named index.html. Use plain HTML, CSS, and JavaScript with no build tools. Put the truss solver in its own clearly named functions, separate from the drawing code.

Watch what the agent does. It will probably write the file in pieces, and it may ask permission to run commands. When it finishes, double-click `index.html` to open it in your browser.

Try drawing a truss. If something doesn't work, describe exactly what you did and what happened, and ask the agent to fix it. Check the browser's developer console for red error messages (**Ctrl+Shift+J** on Windows, or **Cmd+Option+J** in Chrome on a Mac) and paste any you find into the chat.

When you can draw a truss and see forces, ask the agent to commit.

## Step 5 - Validate the Solver

**Numpy homework truss.** Use the joint table to build the truss from the **Validation** section of the spec, add the -2000 lb load at B, and compare the app's results to the expected values. Then check the expected values yourself: sketch a free body diagram of joint B and confirm that AB = 1732 lb (compression) and BC = 1000 lb (compression) satisfy both equilibrium equations. With tension positive, the app should show them as -1732 and -1000.

**A bridge truss, by the method of sections.** Build a 60 ft Pratt truss, 10 ft tall, with six 10 ft panels:

- Bottom joints at (0, 0) through (60, 0), every 10 ft, with a pin at (0, 0) and a roller at (60, 0)
- Top joints at (10, 10) through (50, 10)
- Bottom chord, top chord, vertical members at x = 10 through 50, end posts from (0, 0) to (10, 10) and (60, 0) to (50, 10), and diagonals sloping down toward the center: (10, 10)–(20, 0), (20, 10)–(30, 0), (40, 10)–(30, 0), (50, 10)–(40, 0)

Apply these loads to the bottom joints: -12,800 lb at x = 10, -19,200 lb at x = 20, -32,000 lb at x = 30, -4,800 lb at x = 40, and -3,200 lb at x = 50. (These are the axle loads of a semi truck parked on the bridge, which you will drive across later.)

Before you look at the app, work these by hand: the two reactions, and, with a section cut through the panel from x = 20 to 30, the forces in the top chord, the bottom chord, and the diagonal in that panel. Then compare to the app. Look at the vertical member at x = 30, too. What does the app show, and why?

**An unstable truss.** Draw a square with no diagonal, put a pin and a roller at the bottom corners and a load at a top corner. The app should say the truss is unstable instead of showing forces.

If anything doesn't match, look at the sign convention, the units, and the geometry before asking the agent. Then give the agent the inputs, the expected values, and what the app showed.

Add the Pratt truss case to the **Validation** section of the spec with your hand-calculated values, and ask the agent to commit.

## Step 6 - Make It a Bridge Game

Add these features **one at a time**. For each one, add it to the spec first (Inputs, Calculations, and Outputs, as needed), then ask the agent to build it, test it, rerun your validation cases, and ask the agent to commit.

1. **The bridge site:** A **New Bridge** button that clears the screen and sets up a 60 ft gap: deck joints at (0, 0), (10, 0), ... (60, 0), with a pin at (0, 0) and a roller at (60, 0). The deck joints can't be moved or deleted. The user builds the rest of the truss above or below the deck.

2. **Vehicles:** A menu of four vehicles and a **Drive** button. The vehicle drives across the deck from left to right in 1 ft steps, from fully off the left end to fully off the right end, and the member forces update at every step. Each axle load is split between the two deck joints on either side of it in proportion to its distance from each one (as if short beams span between the deck joints). Axle loads are in lb, measured back from the front axle:

    | Vehicle                         | Axles                                      |
    |:--------------------------------|:-------------------------------------------|
    | Car                             | 2,000 at 0 ft; 2,000 at 10 ft              |
    | Loaded dump truck               | 12,000 at 0 ft; 17,000 at 14 ft; 17,000 at 18.5 ft |
    | Semi (AASHTO HS20 design truck) | 8,000 at 0 ft; 32,000 at 14 ft; 32,000 at 28 ft |
    | Fire engine                     | 20,000 at 0 ft; 27,000 at 17 ft; 27,000 at 21.5 ft |

    Also add a slider to park the vehicle at any position. To check the load splitting, park the semi with its middle axle at x = 30 on your Pratt truss. The joint loads should match the ones you entered by hand in Step 5, and so should the member forces.

3. **Failure:** Every member can carry 90,000 lb in tension and 75,000 lb in compression. A force exactly at capacity holds (allow 0.5 lb for round-off). If any member goes over capacity while a vehicle is crossing, the vehicle stops, the member turns black and dashed, and a banner says which vehicle broke the bridge and where it was. Test it with your 10 ft Pratt truss, which should carry the car and the dump truck but fail under the semi.

4. **Cost:** Members cost $100 per foot and joints cost $500 each, including the deck joints. Show the total cost, and a scoreboard of which vehicles the current design has carried.

Then compete with the people around you: **who can build the cheapest bridge that carries all four vehicles?** A taller truss carries more load but costs more. Try trusses above and below the deck, and different shapes.

The game leaves out buckling, which is why it treats every compression member the same no matter how long it is. In a real bridge, long compression members buckle at much lower loads than short ones. That is why real truss bridges usually favor designs like the Pratt, whose long diagonals are in tension, and why your best design in the game might not be the best real bridge.

## Step 7 - Publish

1. In the Source Control panel, click **Publish Branch** and choose a **public** repository.
2. On your repository's page on GitHub, go to **Settings → Pages**. Set **Source** to **Deploy from a branch**, choose your branch (**main**, or **master** on some computers) and **/ (root)**, and click **Save**.
3. After a few minutes, refresh the page to see your site's address. Open it on your phone.
4. Send the link to someone sitting near you and have them try to beat your bridge.
