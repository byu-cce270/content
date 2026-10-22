#AI Unit Edits

 we are looking to make some changes to the last part of the class. For unit two and most of unit three we are teaching the students the basics of both python and computer programming. We want to end the class with introduction to agent based coding and have them build some applications.

  I want to prototype how this would look. This would involve the current four sections: using python locally, special topic, E.P. widgets, final project.

 We will update and modify, using python locally, I will provide the contact for special topics, we will replace pi widgets, and modify the final project. More detail details below.

 ## Using Python Locally

For this section, we will teach them how to run python locally and how to install and use an IDE. We will also teach them how to use the command line to run python scripts. This will be a hands-on section where students will be able to practice running python code on their own machines.  We will focus on VS code. We will also introduce GitHub and have them create a GitHub account. As part of that, we will ask them to apply for a free copilot student license through their hub account. We will tell them that another option is to pay $20 to get either an entry-level Claude code account or a ChatGPT code X account. This will be in preparation for the subsequent lessons. We need to do this with sufficient lead time that they can get their copilot account approved.

We need to make sure the in class exercise and the corresponding homework assignment are well structured. For the homework assignment, we could have them download one of the Call notebooks that they've generated as a.PY file and have them open it and run it in the IDE and make some modifications. Your suggestions are welcome here. The homework could also include creating the hub account and signing up for an agent, but again that would need to be done well in advance.

## Agent-based coding, part 1

This section will replace the current section marked as special topic. The objective here will be to teach them how to use agent based programming to build a web application. We will have them run the web application locally and then show them how to put it on their get up account and run it have the Web App posted as a webpage from their hub account. We will need to have one or more problems that we could go through in the in class exercise to build a web application. We need to have some problems appropriate for the class. This class is taken by undergraduate students in Civil Engineering and construction and facilities management. So the problem should be related to those fields. 

For the homework assignment, want to present them with 4-5 problems and have them select one to build a web application. We will need to provide them with some guidance on how to do this. We will also need to provide them with some guidance on how to put the web application on their GitHub account and run it as a webpage. These should be problems that get them excited about the possibilities of agent based programming and how it can be used to solve problems in their field. We will need to develop a rubric on how to grade the homework assignment. 

We will need to give them instructions on how to submit the assignment. We would require the entire assignment to be a single HTML file. This would also teach them how easy this is to build something like this and how easy it is to share it with others. 

## Agent-based coding, part 2

 this section will replace what is currently labeled as ipywidgets in the course content. This will be another section on agent base programming, but rather than building a web application, we will have them create an application in Python. That includes a a user a full user interface using Qt or Tkinter. We could  we could then have them build one or more of the same applications that we built on a for a Webb application in the previous unit, but this time it is a desktop application. We will show them how to run the application locally and then how to put it on their GitHub account and run it from there. 

 Once again, for the homework assignment, we will present them with 4-5 problems and have them select one to build a desktop application. Perhaps we could provide the same applications that we built for the web application, but this time they will build them as desktop applications. Part of the assignment would be to make additional features or enhancements to the problem. 

 Again, we will need a rubric and instructions on how to submit the assignment. We could have them put it on their GitHub account and submit a link to the assignment. The TA's could then just clone the account to grade the assignment. Or it might be easier to have them submit a zip file of the application. We will need to decide on that.

 ## Final Project

 For this part, we we will continue our discussion of agent base programming, but in the context of their final project, which we will ask them to do using agent base programming. As part of this, we will teach them good practices for agent base programming, including using the following strategy:

 1) we will teach them to write a markdown file that has a detailed outline of the application that they want to build.
   
2) next they will point their agent to the markdown file and ask the agent to review their design and give suggestions for how to improve it.

3) then they will need to consider how they will validate the application and how they will test it. They should modify the markdown file accordingly with a validation plan. They can use the agent to help them with the validation and testing process.

4) then they will have the agent generate the code for the application. They will need to review the code and make any necessary modifications. They will also need to test the application and make any necessary modifications.

We will let them do either a web application or a desktop application for their final project. In either case, they will need to create documentation for the application and submit it as part of their final project. 

Again, we will need details on submission and rubric.

## Decisions

1. **Paid agent tools:** Optional but mildly encouraged, since Claude Code and Codex work better than Copilot. All graded work must be doable with the free GitHub Copilot student license (or Copilot's free tier while the student license is pending).
2. **Desktop app submission (Part 2):** A single `.py` file, or a `.zip` if the app needs data files, uploaded to Learning Suite.
3. **Part 2 problem:** Students may either port their own Part 1 web app to a desktop app and add features, or pick a new problem from the list.
4. **Final project team workflow:** Teach basic team git (clone, pull, commit, push, branches, resolving a merge conflict), then let each team decide whether everyone commits or one "driver" commits while the others write the spec and tests.

## Candidate Problems

Each problem has engineering underneath that students can check against a hand calculation. All of them fit in a single HTML file, using CDN libraries (Leaflet, three.js, Chart.js) where needed.

### Simulations and games

- **Bridge builder.** Click to place joints and members, add a truck load, and the app solves the truss. Members turn red (tension) or blue (compression), and the bridge collapses when a member exceeds its capacity. Score by cost or weight. Check against a hand-solved truss from statics.
- **Shake table.** Draw a 3–5 story building with adjustable floor masses and stiffnesses, then animate it shaking under a real earthquake record (El Centro 1940 or a synthetic Wasatch event). Add a damper and compare roof drift with and without it.
- **Traffic signal tuner.** Cars animate through a four-way intersection. Set green times and arrival rates, watch queues build or clear, and report average delay.
- **Bid war (CFM).** Bid against 4 computer contractors whose cost estimates are uncertain. After 20 rounds, the low bidder tends to lose money (the winner's curse).
- **Crane placement.** Drag a tower crane onto a site plan with pick points and load weights. The app checks each pick against a load chart for radius and capacity and flags the picks that fail. Find the cheapest crane that covers every pick.
- **Block stacking.** Stack blocks to maximize overhang past a table edge. The app tracks the combined center of mass and topples the stack when it is unstable. The harmonic-series answer makes a good reveal.

### Live data

These APIs are free, need no key, and work from the browser.

- **Provo River float check.** Pull live flow from the USGS stream gauges on the Provo River and show a green, yellow, or red "safe to float?" rating with a 7-day trend chart. Extensions: Hobble Creek, the Weber River, snowmelt season.
- **Wasatch earthquake map.** Plot the USGS real-time earthquake feed on a Leaflet map with the Wasatch Fault drawn in, filtered by magnitude and time window. Clicking a quake estimates shaking intensity at the BYU campus.

### Design tools

- **Roof solar planner.** Draw a roof, place panels, and set the date and time. The app computes the sun path for Provo, shows shading, and estimates annual energy and payback.
- **Tiny house configurator (CFM).** Drag walls on a grid while a 3D view (three.js) updates alongside a live material takeoff and cost estimate.

### Notes on using the problems

- **In-class demo (Part 1):** Bridge builder or shake table. Both look impressive when they run, and both give the agent chances to get the physics wrong that the class can catch together.
- **Part 2 (Tkinter):** The games, the traffic simulation, the crane planner, and both live-data apps translate well to Tkinter. The 3D configurator and the map do not, so leave them off the Part 2 list.

## Decisions: Using Python Locally

1. **Student Pack timing:** Students create a GitHub account and apply for the Student Developer Pack in the Numpy homework (Part 5, 2 points). The Using Python Locally pre-class quiz checks their application status.
2. **Anonymous grading:** GitHub usernames will be visible in this section's homework and in Agent Parts 1 and 2. Each of those pages says so in its anonymity note.
3. **Verification before class:** A TA follows the reading and In-Class Exercise 4 on a fresh GitHub account a week before class, fixes any steps that don't match the current GitHub and VS Code screens, and replaces each "Screenshot needed" placeholder with a real screenshot.
4. **AI comment penalty:** Keep the −50% penalty for the Using Python Locally homework. In the agent sections, replace it with a required spec file plus a short log of the prompts the student used.
