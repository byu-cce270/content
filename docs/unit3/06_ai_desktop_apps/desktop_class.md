# In-Class Exercise: Beam Designer on the Desktop

In this exercise, you will have the agent build the [Beam Designer](../05_ai_web_apps/web_class.md#beam-designer) as a Python desktop app, with numpy for the calculations and matplotlib for the diagrams, then add features that a desktop app does well, such as saving designs as files. The process is the same as for the web app. You change the spec to describe a desktop app, and the agent runs the validation cases for you.

<!-- TEMPORARY: added mid-semester because BYU's ChatGPT Edu access was new.
     Remove next semester and fold it into the Using Python Locally reading. -->

!!! note "New: Codex with your BYU ChatGPT account"
    BYU now gives every student **CES ChatGPT Edu**, the university's managed ChatGPT environment, at no cost, and it includes **Codex**, OpenAI's coding agent. You can use Codex for this exercise instead of Copilot. Copilot still works for everything in this class, and you will not lose points for using it.

    If you already have a personal ChatGPT account on your `netID@byu.edu` address, move that account to a personal email first, as described on BYU's [CES ChatGPT Edu page](https://ai.byu.edu/ces_chatgpt_edu){:target="_blank"}, so the two don't collide. Your CES ChatGPT Edu account is for academic purposes.

    **To set up Codex:**

    1. Activate your account if you haven't yet, following the steps on the same BYU page.
    2. In VS Code, open the Extensions panel and search for **Codex**. Install **Codex – OpenAI's coding agent**, published by **OpenAI**. Check the publisher before you install it. Several extensions use the Codex name and a similar icon, but only one is OpenAI's: the publisher reads **OpenAI** with a blue verified check mark, and the identifier is `openai.chatgpt`. If you installed the wrong one, uninstall it and try again.
    3. Click the **Codex** icon in the sidebar. If it isn't there, open the Command Palette (**Ctrl+Shift+P**, or **Cmd+Shift+P** on a Mac) and run **Codex: Open Codex Sidebar**.
    4. Click **Sign in with ChatGPT** and finish in the browser. If you are asked which workspace to use, choose the **CES ChatGPT** one.

    You don't need the Codex CLI or the ChatGPT desktop app. The extension works on its own.

    Where this page says to use the Copilot chat panel, use the Codex sidebar instead, and enter the same prompts.

## Step 1 - Set Up the Project

1. Make a folder named `beam_desktop` in your class folder.
2. Open `beam_desktop` in VS Code, then click **Initialize Repository** in the **Source Control** panel.
3. Copy the polished Beam Designer spec from the [web apps in-class exercise](../05_ai_web_apps/web_class.md#beam-designer) into a file named `spec.md` in `beam_desktop`. If your class built Beam Designer as its web app, copy your own `spec.md` and `index.html` from your `first_app` folder instead. The agent will use `index.html` as a reference for how the app should behave.
4. Make an `AGENTS.md` so the agent keeps a prompt log for this project too. In the Copilot chat panel, enter:

    !!! prompt "Prompt"
        Create an AGENTS.md at the top level of this project containing this line: "After each request, add an entry to prompts.md: what I asked, what you changed, and whether it worked." Don't build anything else.

    !!! note "If you copy AGENTS.md from first_app instead"
        You can reuse the file from your web app if you added your own rules to it and want them back. Be careful, though: that file describes a web app. It may name folders that don't exist here, or tell the agent that `index.html` goes at the top level, and the agent follows those rules in every conversation. Ask the agent what is in it:

        !!! prompt "Prompt"
            Read AGENTS.md and list the rules it contains. Tell me which ones apply to a Python desktop app and which ones only make sense for a web app.

        Then have it update the file for this project:

        !!! prompt "Prompt"
            Update AGENTS.md for this project, a Python desktop app built with Tkinter, numpy, and matplotlib, started with `python app.py`. Remove the rules that only apply to a web app. Keep the prompt log rule. Don't build anything else.

        Read the result yourself before you move on. You are responsible for what the agent is told to do.

5. Ask the agent to commit.
6. In the terminal, install the packages you'll need:

    ```
    pip install numpy matplotlib
    ```

7. Check that Tkinter works. Tkinter draws the app's window:

    ```
    python -m tkinter
    ```

    A small window should open. Close it and carry on.

    On many Macs the command is `python3` rather than `python`, so use `python3 -m tkinter` if `python` isn't found or starts the wrong version. The same is true of every `python` command on this page, and of `pip` above, which is `pip3` on those machines.

    !!! note "You probably don't need to install anything"
        Tkinter is part of Python itself, not a package you add with `pip`. The Python you installed from [python.org](https://www.python.org/downloads/) in Using Python Locally includes it, on both Windows and Mac, so for most of you the window just opens and there is nothing more to do.

    If you get `No module named '_tkinter'` on a Mac, your Python came from Homebrew rather than python.org, and Homebrew keeps Tkinter in a separate package. Install it, matching your Python version:

    ```
    brew install python-tk@3.14
    ```

    If that doesn't work, ask a TA for help.

## Step 2 - Update the Spec

Edit `spec.md` to describe the desktop version.

1. Add this section near the top:

    ```markdown
    ## Platform
    - Python desktop app using Tkinter, started with `python app.py`
    - Calculations with numpy, kept in their own module, separate from
      the window code
    - Diagrams drawn with matplotlib, embedded in the window
    ```

2. Change the **Look and feel** section for a desktop window: inputs in a panel on the left, the beam and diagrams on the right, and a window that can be resized. Remove the lines about phones.

3. Add this case to the **Validation** section:

    ```markdown
    5. Simply supported, 30 ft, W18x35, uniform 2 kips/ft from 0 to 15 ft
       only: reactions 22.5 k (left) and 7.5 k (right); max moment
       126.6 kip-ft at 11.25 ft.
    ```

    Read the spec all the way through before you commit it.

Ask the agent to commit.

## Step 3 - Build It

Ask the agent to build the app:

!!! prompt "Prompt"
    Read spec.md and build the desktop app it describes. If index.html is in this folder, use it as a reference for how the app should behave.

When the agent finishes, run the app:

```
python app.py
```

You can run this in a VS Code terminal or in a command terminal. If you use a command terminal, you have to be in the directory that contains your Python file, or Python won't find it.

Try every input. If something doesn't work, describe what you did and what happened, and ask the agent to fix it.

## Step 4 - Have the Agent Check Its Work

Enter:

!!! prompt "Prompt"
    Run all of the validation cases in spec.md against the app's beam calculations and report a table of expected versus actual values.

Read the table. Every value should match to the number of digits given in the spec. If a case fails, ask the agent to find out whether the app or the expected value is wrong, and to show its work.

Then enter case 1 in the app yourself and confirm that you see the same values the agent reported.

Ask the agent for more cases:

!!! prompt "Prompt"
    Suggest validation cases that test every calculation in spec.md, including edge cases and property checks such as symmetry. Work out the expected values from the equations in the spec, show your work, and add the cases to the Validation section. Don't change the app.

Read what it suggests, keep the cases you agree with, and have it rerun the full set.

When everything matches, ask the agent to commit.

## Step 5 - Add Desktop Features

Add these features **one at a time**:

1. **Save and Open:** A File menu with **Save** and **Open** that saves the beam (support type, span, section, deflection limit, and loads) to a file and opens it again. Remove "Saving designs" from the **Out of scope** section of the spec first.
2. **Export results:** A button that saves a table of x, V, M, and deflection along the beam to a CSV file that opens in Excel.
3. **Calculation sheet:** A button that saves the diagrams and checks as a PDF, with the inputs listed at the top, ready to hand in with a design.

    Expect to iterate on the layout. Open the PDF, decide what would make it easier to read, and tell the agent what to change, or talk through the options with it if you aren't sure. Keep going until the sheet looks like something you would be willing to hand to an engineer.

For each feature:

1. Add it to the spec.
2. Ask the agent to build it.
3. Try it in the app.
4. Have the agent rerun the validation cases:

    !!! prompt "Prompt"
        Rerun the validation cases in spec.md and confirm they still pass.

5. Ask the agent to commit.

## Step 6 - Push to GitHub

1. Ask the agent for a README:

    !!! prompt "Prompt"
        Write a short README.md that says what this app does, which packages to install, and the command that starts it.

2. Ask the agent to commit, then click **Publish Branch** and publish a public repository.
3. Trade repository addresses with a neighbor. Clone their repository (**File → New Window**, then **Clone Git Repository**), follow their README, and run their app. If the README left anything out, tell them.

## Optional Step - Just for Fun

!!! note "Not required, not graded"
    Nothing in this section is worth points. It is here because it is a good way to practice everything above on something you actually want to build.

In [Using Python Locally](../04_local_python/local_py_class.md#exercise-3-clone-and-run-a-game) you cloned Alien Invasion, the Pygame game from *Python Crash Course*, and ran it as a Python app on your own machine. You have now built a desktop app from a spec. The same workflow turns that game into a web app that runs in a browser.

1. Make a new folder in your CCE 270 folder, such as `alien_invasion_web`, and open it in VS Code. Don't copy the game's files into it. You are building a new version, not editing the old one.
2. Ask the agent to initialize it as a Git repository, and to create an `AGENTS.md` with the prompt log line, as you did in Step 1.
3. Work out the spec with the agent before any code. You can name the technology yourself, or ask the agent to recommend one and explain the trade-offs. Ask whether a single file is realistic, because that shapes everything else:

    !!! prompt "Prompt"
        I want to rebuild the Alien Invasion game from Python Crash Course as a web app that runs in a browser. I want the whole game contained in a single .html file. Is that possible? If so, what would it take, and what are the trade-offs? Then help me write a spec.md for it, and don't write any game code yet.

4. Once you have a spec you believe in, build it the same way you built the beam app: build it, try it, and have the agent fix what doesn't work. Commit as you go.

When it runs, keep going if you want to. Add levels, a scoreboard, better graphics, or sound. Or throw it out and build a different game of your own from scratch. Everything you need is in the workflow you just practiced: write the spec, build in stages, and check the result.

## Turning in/Rubric

Upload a **`.zip` of your `beam_desktop` folder** to Learning Suite. On Windows, right-click the folder and choose **Send to → Compressed (zipped) folder**. On a Mac, right-click the folder and choose **Compress "beam_desktop"**. Paste your GitHub repository address in the submission comments.

**Rubric:**

|                      Item                      | Points Possible |
|:----------------------------------------------:|:---------------:|
| <div style="text-align: right">**Total**</div> |        5        |

The following is not a part of the rubric, but specifies how you can lose points. For example: if you fail to upload your file correctly.

| **Reasons for Points Lost** |    **Amount**     |  
|:---------------------------:|:-----------------:|
|  File uploaded incorrectly  |       -10%        |
|  Turned in late (per week)  | -10% (up to -50%) |
