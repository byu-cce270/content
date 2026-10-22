# Reading: Building Web Apps with an AI Agent

---

In this section, you will use an AI coding agent to build an interactive web application for an engineering problem, test it against a hand calculation, and publish it on the internet where anyone with the link can use it. You will not learn to write the code for a web page yourself. The agent writes it. Your job is the part that requires an engineer: deciding exactly what the app should do, describing it clearly, and proving that its answers are right.

You will need everything from [Using Python Locally](../04_local_python/local_py_read.md): VS Code, Git, a GitHub account, and Copilot (or Claude Code or Codex, if you use one of them).

## What a Web App Is

Every web page is built from three languages, and a single `.html` file can hold all three:

- **HTML** describes what is on the page: headings, text, buttons, input boxes, and drawing areas.
- **CSS** describes how it looks: colors, fonts, spacing, and layout.
- **JavaScript** describes what it does: the calculations, what happens when you click a button, and the animation.

Here is a complete web app in one file. It converts a flow rate from cubic feet per second to gallons per minute:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Flow Converter</title>
  <style>
    body { font-family: sans-serif; margin: 40px; }
    input { width: 80px; }
  </style>
</head>
<body>
  <h1>Flow Converter</h1>
  <input id="cfs" type="number" value="1"> cfs
  <button onclick="convert()">Convert</button>
  <p id="result"></p>

  <script>
    function convert() {
      const cfs = Number(document.getElementById("cfs").value);
      const gpm = cfs * 448.83;
      document.getElementById("result").textContent = gpm.toFixed(1) + " gpm";
    }
  </script>
</body>
</html>
```

The HTML tags in the `<body>` put a box, a button, and an empty paragraph on the page. The `<style>` section sets the font and margins. The JavaScript inside `<script>` defines a function, much like a Python `def`, that reads the input box, multiplies, and writes the answer into the paragraph. You can read most of it with the Python you already know: `const` creates a variable, `function` defines a function, and `toFixed(1)` rounds to one decimal place like `round(gpm, 1)`.

To run it, save it as `index.html` and double-click the file. It opens in your web browser. No installation and no server are required, which is why we will build every web app in this class as a **single HTML file**: it runs on any computer, and you can email it, upload it, or publish it as a web page.

A single file can still do a lot. JavaScript can draw on a canvas, animate, make charts, show maps, and download live data from public sources such as the USGS. For charts and maps, the agent can load free libraries like Chart.js or Leaflet with one line that links to a public copy online.

## The Workflow

Working with an agent goes much better if you follow the same steps every time.

### 1. Write a spec

A **spec** (short for specification) is a short document that describes what you want built. You write it in a Markdown file named `spec.md` in your project folder, using the same Markdown you have used for text cells in Colab. A good spec has these sections:

```markdown
# Bridge Builder

## Purpose
One or two sentences: what the app does and who it is for.

## Inputs
Every value the user can enter or change, with units and reasonable ranges.

## Calculations
The equations the app uses, written out. Define every variable and its units.

## Outputs
What the app shows: numbers (with units), plots, colors, animations.

## Validation
At least one test case you have worked by hand: the exact inputs,
and the outputs the app must produce.

## Out of scope
Things the app will NOT do, so the agent doesn't add them.
```

The **Calculations** and **Validation** sections make the difference between an engineering app and a toy. If you leave the equations to the agent, it will pick some, and they may be wrong in ways that are hard to see. If you write them down, you can check its work.

### 2. Have the agent review the spec

Before any code is written, ask the agent to critique your spec. Open the Copilot chat panel, switch to **Ask** mode so it can't change any files, and enter:

> Read spec.md. Don't write any code. List anything in this spec that is ambiguous, missing, or inconsistent, check the equations in the Calculations section, and point out anything that will be hard to build. Suggest improvements.

Read its suggestions and decide which ones to take. The agent is good at spotting a missing input, an undefined variable, or a unit that doesn't match, and it will often ask questions you hadn't thought of, such as what the app should do with a negative span. It is less reliable about engineering judgment, so check any change it suggests to your equations against your textbook or notes. Update the spec, and commit it before moving on.

### 3. Ask the agent to build it

Switch the chat panel to **Agent** mode and point it at your spec:

> Read spec.md and build the app it describes as a single file named index.html. Use plain HTML, CSS, and JavaScript with no build tools. You may load libraries from a CDN. Put all calculations in clearly named functions.

The last sentence keeps the calculations in their own functions, where you and the agent can find and check them.

### 4. Run it and look for errors

Double-click `index.html` to open it in your browser. After each change the agent makes, refresh the page (**Ctrl+R** or **Cmd+R**) to load the new version.

If the page is blank or a button does nothing, there is an error. Open the browser's **developer console** to see it: press **Ctrl+Shift+J** on Windows, or **Cmd+Option+J** in Chrome on a Mac. (In Safari, first turn on **Settings → Advanced → Show features for web developers**, then press **Cmd+Option+C**.) Errors appear in red. Copy the error into the chat and ask the agent to fix it.

### 5. Validate

Enter the inputs from your validation test case and compare the app's answers to your hand calculation. If they don't match, don't simply tell the agent "the answer is wrong." Tell it what you entered, what you expected, what it showed, and how you got your answer. Often the agent will find a units error or a sign convention problem. Sometimes the mistake will be in your hand calculation.

Don't skip this step. An app that looks polished and gives wrong answers is worse than no app at all, because people will believe it.

### 6. Commit

Each time the app works and passes validation, commit. Have the agent do it:

> Commit these changes.

Agents write clear, specific commit messages, because they know exactly what they changed. Before you ask, look over the changes in the Source Control panel so you know what is being saved, and read the message the agent writes. Then, if the next request goes badly, you can discard the agent's changes in the Source Control panel and you are back to a working app.

### 7. Add one feature at a time

Ask for one change per request: "Add a slider for the load," then "Color the members by force," then "Add a cost total." Test and commit after each. A long list of changes in one request is much harder to check, and when something breaks you won't know which change caused it.

## Tips for Working with the Agent

- **Be specific about what you see.** "The deflection is 12 times too large" is much more useful than "it's broken."
- **Ask it to explain.** "Explain how the solve function works, step by step" is a good way to check that the calculation matches your spec.
- **Ask it to check its own work.** "Compare the formulas in index.html to the Calculations section of spec.md and list any differences."
- **Update the spec.** When you change your mind about how something should work, change the spec first, then ask the agent to update the app to match. The spec stays the single description of what the app is supposed to do.
- **Start over when it's stuck.** If several attempts at a fix have made things worse, discard the changes and try again with a clearer request.

## Keep a Prompt Log

For every assignment in the agent sections, keep a file named `prompts.md` in your project folder. Each time you give the agent a significant request, add an entry: what you asked, and one sentence on what happened. For example:

```markdown
1. Asked it to build the app from spec.md. It worked, but forces were shown in kips instead of lb.
2. Asked it to use lb everywhere. Fixed.
3. Validation test: AB matched, BC had the wrong sign. Told it compression should be negative. Fixed.
```

The log replaces the rule from earlier homework about commenting AI-written code. Graders use it to see how you directed the agent, and you will find it useful when you write up your final project.

## Publishing with GitHub Pages

GitHub can host any HTML file in a public repository as a web page, for free. Once your app is in a repository on GitHub:

1. Make sure the file is named `index.html` and is in the top level of the repository.
2. On your repository's page on GitHub, go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**, choose the **main** branch and the **/ (root)** folder, and click **Save**.
4. Wait a few minutes, then refresh the Pages settings page. It will show your site's address, which looks like `https://your-username.github.io/your-repo-name/`.

Every time you push a new commit, GitHub updates the page within a few minutes (it can take up to 10).

---

# Pre-Class Quiz Challenge

In class, you will build a bridge truss app, and you will write the specs for your own apps from now on. For practice, write a spec for a small app that computes the concrete needed for a rectangular slab:

- The user enters the slab length and width (ft), thickness (in), a waste factor (%), and the price of concrete per cubic yard
- The app shows the volume in cubic yards (rounded up to the nearest quarter yard, which is how concrete is ordered) and the total cost

Use the six sections from [Write a spec](#1-write-a-spec). In the Validation section, work one example by hand and give its exact inputs and outputs. You do not need to build the app.

Save it as `spec.md` and upload it with your Pre-Class Quiz.

---

## Turning in/Rubric

**Rubric:**

|                      Item                      | Points Possible |
|:----------------------------------------------:|:---------------:|
| <div style="text-align: right">**Total**</div> |        3        |

---

The following is not a part of the rubric, but specifies how you can lose points. For example: if you fail to upload your file correctly.

| **Reasons for Points Lost** |    **Amount**     |  
|:---------------------------:|:-----------------:|
|  File uploaded incorrectly  |       -10%        | 
