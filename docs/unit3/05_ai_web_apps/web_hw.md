# HW: Build a Web App

**Purpose:** Use an AI coding agent to build, validate, and publish a web app for an engineering problem of your choice.

---

## Overview

Choose one of the five problems below and build it as a single-file web app, following the workflow from the [reading](web_read.md) and the [in-class exercise](web_class.md):

1. Write the spec, including a validation case you have worked by hand
2. Have the agent review the spec, and revise it
3. Have the agent build the app
4. Validate it against your hand calculation
5. Add features one at a time, committing after each one
6. Publish it on GitHub Pages

Each problem lists features the app must have, a validation check, and ideas for going further. The must-have features are the minimum. The best apps will go well past them, and the "Going further" ideas are a place to start.

Set up a new folder and repository for this assignment, with `spec.md`, `prompts.md`, and `index.html` at the top level.

---

## The Problems

### 1. Shake Table

Draw a building and shake it. The app models a building of 1 to 5 stories, where each floor is a mass connected to the floor below by a spring that represents the columns. The ground moves back and forth, and the app animates the building swaying.

**Must have:**

- Number of stories (1–5), and the mass and stiffness of each story, set by the user
- Ground motion as a sine wave with an adjustable amplitude and frequency
- An animation of the building moving, with the displacements exaggerated enough to see
- A plot of roof displacement over time
- The building's natural period (for a 1-story building) displayed in seconds
- A "pluck" button that displaces the roof and lets the building vibrate freely with no ground motion

**Validation:** For a 1-story building, the natural period is $T = 2\pi\sqrt{m/k}$. Pick a mass and stiffness, compute $T$ by hand, then set the ground motion frequency to $1/T$ and confirm that the building resonates: the roof displacement keeps growing. Set the frequency to half of that and confirm that it doesn't. Finally, pluck the building and measure the period of free vibration from your plot (the time between peaks), and compare it to your hand value.

**Going further:** Add damping and show how it limits resonance. Add a tuned mass damper on the roof. Use a real earthquake record, such as the 1940 El Centro ground motion, instead of a sine wave.

---

### 2. Traffic Signal Tuner

Animate cars moving through a four-way intersection with a traffic signal. The user sets the arrival rate on each approach and the green time for each direction, and watches queues build or clear.

**Must have:**

- Arrival rates (vehicles per hour) for the north-south and east-west approaches
- Cycle length and green time for each direction
- Cars that arrive at random, stop at red lights, and leave at a steady rate during green
- The current queue length on each approach, and the average delay per vehicle

**Validation:** The capacity of an approach is $c = s \cdot g / C$, where $s$ is the saturation flow rate (use 1800 vehicles per hour per lane), $g$ is the green time, and $C$ is the cycle length. Compute the capacity by hand for one set of inputs. Then run the app with an arrival rate 20% below that capacity and confirm that the queue clears every cycle. Run it with an arrival rate 20% above capacity and confirm that the queue keeps growing.

**Going further:** Add left-turn lanes or a protected left-turn phase. Add a button that finds the green split that minimizes total delay. Compare the app's average delay to Webster's delay formula.

---

### 3. Bid War

A construction bidding game. For each project, the player and four computer contractors estimate the cost and submit bids. The lowest bid wins the job, and then the true cost is revealed. After 20 projects, the player sees whether they made money.

**Must have:**

- A true project cost that is hidden until the job is awarded
- Each bidder's cost estimate equals the true cost plus a random error (for example, ±15%)
- The player sees their own estimate and enters a markup percentage, which sets their bid
- The computer contractors bid using their own estimates and a fixed markup
- A table showing every round: the bids, the winner, the true cost, and the winner's profit or loss
- The player's total profit at the end of the game

**Validation:** Set the estimate error to 0%. Every bid should equal the true cost times (1 + markup), the bidder with the lowest markup should win every round, and the winner's profit should equal the markup times the true cost. Check one round by hand. Then turn the error back on, run the game, and look at the winners' profits. You should find that the winner usually underestimated the cost, which is called the **winner's curse**. Explain in your spec why that happens.

**Going further:** Give the computer contractors different strategies. Add bid bonds or a limit on how much work a contractor can carry at once. Let several players compete on one screen.

---

### 4. Crane Placement

Plan a tower crane on a construction site. The user drags a crane onto a site plan that shows pick points, such as where steel, rebar, and HVAC units have to be lifted, and the app checks whether the crane can reach and lift each one.

**Must have:**

- A site plan with at least 6 pick points, each with a load weight. The user can add, move, and delete pick points.
- A crane the user can drag to any position, with its reach drawn as a circle
- A load chart (capacity vs. radius) for the crane. Use this one, which is an example and not from a real crane:

    | Radius (ft) | Capacity (lb) |
    |:-----------:|:-------------:|
    |     50      |    20,000     |
    |     75      |    13,000     |
    |     100     |     9,000     |
    |     125     |     7,000     |
    |     150     |     5,500     |

- Each pick point colored green if the crane can lift it and red if it can't, with the radius and the capacity at that radius shown

**Validation:** Decide in your spec how the app reads the load chart between table values. Using the next larger radius in the table is conservative, and interpolating is less so. Then compute the radius and capacity by hand for three pick points and compare them to the app. Include one pick that is just inside a radius in the table and one that is just outside it.

**Going further:** Offer several crane models with different load charts and costs, and find the cheapest one that covers every pick. Allow two cranes. Add obstructions, such as an existing building, that the boom can't swing through.

---

### 5. Provo River Float Check

A dashboard that downloads live streamflow data from a USGS gauge on the Provo River and tells the user whether conditions look good for floating the river.

**Must have:**

- The current flow (cubic feet per second) at a USGS gauge on the Provo River, downloaded when the page loads. Gauge 10163000, Provo River at Provo, is a good choice, and the [USGS Water Data](https://waterdata.usgs.gov/) site lists the others.
- A chart of the flow over the past 7 days
- A green, yellow, or red rating based on flow thresholds that you choose. Research and cite your thresholds in your spec.
- A clear statement on the page that the rating is not a safety guarantee
- The time of the most recent reading

USGS data services change from time to time. Have the agent find the current way to download instantaneous discharge (USGS parameter code 00060) for your gauge, and record what it used in your spec.

**Validation:** Compare the current flow in your app to the value on the gauge's USGS web page at the same time. Then download the past 7 days of data from the USGS site as a CSV file, compute the 7-day average in Excel, and compare it to an average shown by your app.

**Going further:** Add other gauges, such as the Weber River or Hobble Creek. Show how today's flow compares to the historical average for this date. Add a snowmelt season outlook.

---

## Turning in/Rubric

!!! note "Do not put your name or NetID in the file"
    Learning Suite records who submitted each file, so your name is not needed
    inside the file itself. Leaving it out means your work can be graded
    anonymously, which keeps grading fair. Your GitHub Pages address will show
    your GitHub username, which is fine for this assignment.

Upload these three files to Learning Suite:

1. `index.html` - your app
2. `spec.md` - your final spec, including your validation case, your hand calculation, and the app's results
3. `prompts.md` - your prompt log

Paste your GitHub Pages address (for example, `https://your-username.github.io/your-repo-name/`) in the Learning Suite submission comments.

**Rubric:**

|                                         **Items**                                          | **Amount** |  
|:------------------------------------------------------------------------------------------:|:----------:|
|      Spec has all six sections, with equations and a hand-worked validation case           |     5      |
|                         All must-have features work                                        |     10     |
|              Validation check passes and is documented in the spec                         |     5      |
|                    App is published and works at the GitHub Pages address                  |     4      |
|        App is easy to use: clear labels, units on every number, looks finished            |     3      |
|              Prompt log is complete, and the repository has at least 5 commits            |     3      |
|                         <div style="text-align: right">**Total**</div>                    |   **30**   |

---

The following is not a part of the rubric, but specifies how you can lose points.

|          **Reasons for Points Lost**          |    **Amount**     |  
|:---------------------------------------------:|:-----------------:|
|           File uploaded incorrectly           |       -10%        |
|           Turned in late (per week)           | -10% (up to -50%) |
|            No prompt log submitted            |       -50%        |
