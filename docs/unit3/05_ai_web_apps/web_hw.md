# HW: Build a Web App

**Purpose:** Use an AI coding agent to build, validate, and publish a web app for an engineering problem of your choice.

---

## Overview

Choose one of the seven problems below and build it as a single-file web app, following the workflow from the [reading](web_read.md) and the [in-class exercise](web_class.md):

1. Write the spec, including a validation case you have worked by hand
2. Have the agent review the spec, and revise it
3. Have the agent build the app
4. Validate it against your hand calculation
5. Add features one at a time, committing after each one
6. Publish it on GitHub Pages

Each problem lists features the app must have, a validation check, and ideas for going further. The must-have features are the minimum. The best apps will go well past them, and the "Going further" ideas are a place to start.

Set up a new folder and repository for this assignment, with `spec.md`, `prompts.md`, and `index.html` at the top level. Have the agent commit at each step: the spec, the revised spec after review, the first working version, the validated version, and each feature. Graders will look at the commit history to see that you worked in steps, so committing everything at the end will lose points.

---

## The Problems

### 1. Bear River Gage Explorer

An interactive map of every USGS stream gage in the Bear River basin, which drains parts of Utah, Idaho, and Wyoming into the Great Salt Lake. The app downloads the gage locations and the basin boundary live, and clicking a gage shows its hydrograph and information about the stream.

**Must have:**

- A map (Leaflet works well) showing the Bear River basin boundary
- Every active USGS stream gage in the basin, downloaded from the [USGS Water Data API](https://api.waterdata.usgs.gov/docs/ogcapi/) when the page loads, shown as a marker
- Clicking a gage shows its name, site number, drainage area, the most recent flow (cfs), and a hydrograph of daily flow for the past year
- The date and time of the most recent reading, and a link to the gage's USGS page

The older `waterservices.usgs.gov` service is being shut down during the 2026–27 school year, so tell the agent not to use it.

**Validation:** For three gages, compare the most recent flow and the drainage area in your app to the gage's page on [USGS Water Data](https://waterdata.usgs.gov/). Then download a year of daily flow for one gage from the USGS site, compute the mean annual flow in Excel, and compare it to a mean flow shown by your app.

**Going further:** Color each marker by how today's flow compares to the median for this date (well below normal, normal, well above). Add a slider that replays a spring runoff season. Click two gages on the same river to compare their hydrographs and see the flood wave travel downstream.

---

### 2. Roller Coaster Designer

Draw a roller coaster track and ride it. A car starts at the top of the first hill and rolls along the track under gravity, and the app shows its speed and the g-forces on the riders as it goes.

**Must have:**

- A track the user draws or shapes by dragging control points, with a smooth curve through them
- An animated car that follows the track, with its speed computed from conservation of energy
- Live readouts of speed (mph) and vertical g-force, and a plot of both along the track
- Failure when the car doesn't have enough energy to reach the next crest (it rolls back) or when the g-force goes above 4 g or below -1 g, with the failure point marked on the track

**Validation:** With no friction, the speed at any point is $v = \sqrt{2g(h_0 - h)}$, where $h_0$ is the height of the starting crest. Compute the speed by hand at the bottom of the first drop and compare it to the app. Then, for a valley with radius of curvature $R$, check the app's g-force against $n = 1 + v^2/(gR)$.

**Going further:** Add rolling friction and air drag, and a lift hill that pulls the car to the top. Add loops. Score designs by thrill (time spent above 3 g) while keeping every ride safe.

---

### 3. Earthquake Shake-Down

Build a tower from columns, beams, and braces, set it on a shake table, and turn up the shaking until it falls. Use a 2D physics engine such as Matter.js, which handles the collisions and collapse.

**Must have:**

- Building pieces (columns, beams, braces, and floor masses) that the user places on the shake table, with joints that break when overloaded
- A shake table that moves back and forth with an amplitude and frequency the user sets, or a button that plays an earthquake ground motion
- A cost for each piece and a total cost
- A score: the strongest shaking the building survived for 10 seconds without any floor touching the ground

**Validation:** Physics engines use their own units, so check that yours behaves like the real world. Drop a single block from a known height and compare its fall time to $t = \sqrt{2h/g}$. Then measure the table's motion from the animation (the time for 10 cycles and the distance between the extremes) and compare it to the frequency and amplitude you set.

**Going further:** Add base isolation (a layer that lets the building slide) or a tuned mass damper on the roof, and show how much more shaking the building survives. Play a real earthquake record. Add a challenge mode: the most floors that survive a given earthquake for a given budget.

---

### 4. Stadium Evacuation

Lay out a floor plan, fill it with a crowd, and time how long it takes everyone to get out. Each person walks toward the nearest exit, and people slow down and queue when it gets crowded.

**Must have:**

- A floor plan editor with walls, exits, and obstacles such as rows of seats
- A crowd of 100 to 2,000 people placed randomly or in a region the user draws
- An animation of the evacuation, with people moving toward exits and queuing at doors
- The total evacuation time and the time when 50% and 90% of people are out, and a plot of people remaining over time

**Validation:** For a crowded room with one door, the time to empty is controlled by how fast people can pass through the door. A commonly used maximum flow through a door is about 24 people per minute per foot of door width (from the *SFPE Handbook of Fire Protection Engineering*). Compute by hand how long 500 people need to get through a 6 ft door and compare it to your app. The app should take longer, because people first have to walk to the door, but it should be close.

**Going further:** Model the Marriott Center or another real venue. Add stairs, which are slower than level floors. Find the exit layout that minimizes evacuation time for a fixed total exit width.

---

### 5. Crane Operator

Run a tower crane with the keyboard. Pick up loads from the staging area and set them on a building under construction before time runs out, without tipping the crane.

**Must have:**

- A side view of a tower crane, with keys to swing the jib (or move the trolley in and out) and to raise and lower the hook
- Loads of different weights to pick up and target locations on the building to set them
- The crane's load chart (allowed load vs. radius) shown on screen, with the current load and radius marked on it. Use this one, which is an example and not from a real crane:

    | Radius (ft) | Capacity (lb) |
    |:-----------:|:-------------:|
    |     50      |    20,000     |
    |     75      |    13,000     |
    |     100     |     9,000     |
    |     125     |     7,000     |
    |     150     |     5,500     |

- A warning when the load reaches 90% of capacity at the current radius, and a dramatic tip-over when it passes 100%
- A timer and a score

**Validation:** Decide in your spec how the app reads the load chart between table values. Using the next larger radius in the table is conservative, and interpolating is less so. Then compute the allowed load by hand at three radii, including one just inside a table radius and one just outside, and check that the app warns and tips at the right points.

**Going further:** Add wind, which makes the load swing. Add a second crane and avoid collisions. Make levels, each with a different site layout.

---

### 6. Utah Snowpack Map

Most of Utah's water supply falls as snow. Build a map of the SNOTEL snow-monitoring sites in Utah that shows how this year's snowpack compares to normal.

**Must have:**

- A map of all Utah SNOTEL sites, downloaded from the NRCS snow survey data service when the page loads
- Each site colored by its snow water equivalent (SWE) as a percent of the median for today's date
- Clicking a site shows its name and elevation, today's SWE and median SWE, and a plot of this water year's SWE with the median for comparison
- A statewide summary: the average percent of median across all sites

**Validation:** Compare today's SWE and percent of median for three sites to the NRCS [Utah Snow Survey](https://www.nrcs.usda.gov/conservation-basics/conservation-by-state/utah/utah-snow-survey) reports. Then compute the percent of median by hand for one site from the two numbers the app downloaded.

**Going further:** Group the sites by river basin and show each basin's percent of median. Add a date slider to replay past water years, such as the record snow of 2023. Estimate how much water is stored in the snowpack above a reservoir.

---

### 7. Jobsite Weather Planner

Click a jobsite on a map and get a 7-day forecast showing which days are safe for the work that weather can stop: crane lifts, concrete pours, and roofing.

**Must have:**

- A map where the user clicks to choose a jobsite
- A 7-day hourly forecast for that location from the free [Open-Meteo](https://open-meteo.com/) API, which needs no key
- A calendar view with a go, caution, or no-go rating for each day and each activity:
    - **Crane lifts:** sustained wind and gusts compared to a crane wind limit
    - **Concrete pours:** low temperatures compared to cold-weather concreting limits
    - **Roofing:** chance of rain
- Your thresholds in the spec, with a source for each, and the reason for each day's rating shown when the user clicks it

**Validation:** For one location and one day, read the raw hourly forecast numbers the app downloaded, apply your thresholds by hand, and confirm the app gave the same rating. Also compare the app's forecast to the National Weather Service forecast for the same place.

**Going further:** Let the user enter the crew's working hours, so overnight conditions don't count. Add activities such as asphalt paving or excavation in frozen ground. Show the best three-day window for a large pour.

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
|   Prompt log is complete, and at least 5 commits match the workflow steps (spec, review, first version, validation, features)   |     3      |
|                         <div style="text-align: right">**Total**</div>                    |   **30**   |

---

The following is not a part of the rubric, but specifies how you can lose points.

|          **Reasons for Points Lost**          |    **Amount**     |  
|:---------------------------------------------:|:-----------------:|
|           File uploaded incorrectly           |       -10%        |
|           Turned in late (per week)           | -10% (up to -50%) |
|            No prompt log submitted            |       -50%        |
