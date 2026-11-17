# In-Class Exercise: Running Python Locally

Before class, you should have installed Python, VS Code, and Git and applied for the GitHub Student Developer Pack, as described in the [reading](local_py_read.md). If any of that didn't work, get a TA's help before starting Exercise 2.

On a Mac, type `python3` and `pip3` wherever this page says `python` and `pip`. If a command gives an error, find the message under [Troubleshooting](#troubleshooting) at the end of this page.

## Sign In to GitHub

Open VS Code and click the **Sign In** button. Choose GitHub and follow the prompts in your browser. Signing in lets VS Code push your code to GitHub and turns on Copilot. If you already signed in as part of the reading, your account name appears there instead and you can skip this step.

## Exercise 1 - Find Your Way Around the Terminal

1. In VS Code, choose **File → Open Folder** and open your class folder (for example, `Documents/cce270`). If you don't have one yet, make it first.
2. A blue banner may appear at the top of the window saying VS Code is in **Restricted Mode**. In Restricted Mode, VS Code turns off features such as running code and Copilot, so you need to trust the folder. Click **Manage** on the banner:

    ![The Restricted Mode banner with the Manage link](images/vscode_restricted_banner.png){:width="700px"}

    Then click **Trust**:

    ![The Trust button in the In a Trusted Folder panel](images/vscode_trust_folder.png){:width="400px"}

    Only trust folders whose contents you know, such as your own class folder or code from your course.

3. Open the terminal with **Terminal → New Terminal**.

    ![VS Code with a class folder open and the terminal panel at the bottom](images/vscode_terminal.png){:width="800px"}

4. Check where you are with `pwd`. It should be your class folder.
5. Make a folder for today and move into it:

    ```
    mkdir local_python
    cd local_python
    ```

6. Create the Python file:

    - Choose **File → New File** and select **Python File** from the list.
    - Choose **File → Save As**, browse to the `local_python` folder you just created, name the file `beam.py`, and click **Save**.

    Paste this code into `beam.py` and save it. The code computes the maximum moment and deflection of a simply supported beam with a uniform load:

    ```python
    # Simply supported beam with a uniform load
    w = float(input("Uniform load w (kip/ft): "))
    L = float(input("Span L (ft): "))
    E = 29000      # ksi, steel
    I = 510        # in^4, W18x35

    M_max = w * L**2 / 8                                  # kip-ft
    delta = 5 * (w / 12) * (L * 12)**4 / (384 * E * I)    # in

    print(f"Maximum moment: {M_max:.1f} kip-ft")
    print(f"Maximum deflection: {delta:.2f} in")
    print(f"L/360 limit: {L * 12 / 360:.2f} in")
    ```

    The pasted code may come in indented, and Python will report an error if it is. To fix it, select all the lines (**Ctrl+A** on Windows, **Cmd+A** on Mac) and press **Shift+Tab** until every line starts at the left edge. Then save the file.

7. Run it from the terminal with `python beam.py` (or `python3 beam.py` on a Mac). Try a 1.0 kip/ft load on a 25 ft span, then 1.5 kip/ft on a 30 ft span. Check the first answer by hand: $M = wL^2/8 = 78.1$ kip-ft.
8. Run `ls` (Mac) or `dir` (Windows) to see your file, then `cd ..` to move back up to your class folder.

## Exercise 2 - Your First GitHub Repository

Now you will put your own code on GitHub.

When you initialize a repository, Git tracks your folder on your own computer. That is a **local repository**. Publishing it copies the repository to GitHub, where it is a **remote repository**. Once your code is on GitHub, you can get to it from any other computer, share it with others by sending them the link, and keep a backup in case something happens to your laptop. Each time you push, GitHub's copy is updated to match your local one.

1. In VS Code, open your `local_python` folder from Exercise 1 (**File → Open Folder**).
2. Open the **Source Control** panel (the branching icon on the left sidebar, or **Ctrl+Shift+G** / **Cmd+Shift+G**) and click **Initialize Repository**. Git now tracks this folder.
3. Your `beam.py` file is listed under **Changes**. Type a message in the box at the top, such as `Add beam calculator`, and click **Commit**. If VS Code asks whether to stage all your changes, click **Yes**.
4. Click **Publish Branch**. Choose **public repository** and accept the suggested name. If VS Code asks you to sign in to GitHub, do so.

    ![Source Control panel after the first commit, showing the Publish Branch button](images/vscode_publish_branch.png){:width="600px"}

5. Click the link VS Code shows (or go to your GitHub profile) and find your repository. Your code is now on GitHub.

Now make a second commit:

1. Change `beam.py` to also print whether the beam passes the L/360 deflection check. For example:

    ```python
    if delta <= L * 12 / 360:
        print("Deflection OK")
    else:
        print("Deflection too large - choose a stiffer beam")
    ```

2. Run it to make sure it works.
3. Commit with the message `Add deflection check`.
4. Click **Sync Changes** to push the commit to GitHub.
5. Refresh your repository page on GitHub and click the commit count (the clock icon) to see both commits.

That is the whole Git workflow you will use for the rest of the semester: **change, test, commit, push**.

Pushing only sends your commits up to GitHub. If you or a teammate pushed commits from another computer, your local repository is now behind GitHub's copy. Before you start working, **pull** to catch up: click the **...** menu at the top of the Source Control panel and choose **Pull**. This downloads the new commits and updates your files. **Sync Changes** also pulls before it pushes.

## Exercise 3 - Clone and Run a Game

Python Crash Course, the textbook we've used this semester, builds a game called "Alien Invasion" in Chapters 12–14. Someone has posted a complete version on GitHub, and you will download it with Git, run it, and change it.

### Clone the Repository

1. Browse to the repo: [https://github.com/bryanmacgo/Alien-Invasion](https://github.com/bryanmacgo/Alien-Invasion)

2. Click the green **Code** button and copy the URL.

    ![aliens_clone_repo.png](images/aliens_clone_repo.png)

3. In VS Code, choose **File → New Window**. On the Welcome tab, click **Clone Git Repository**.

    ![vscode_clone.png](images/vscode_clone.png)

4. Paste the URL:

    ![vscode_clone2.png](images/vscode_clone2.png)

5. Choose your class folder as the location. VS Code will clone the repo and offer to open it. Click **Open**.

6. Trust the new folder the same way you did in Exercise 1: click **Manage** on the Restricted Mode banner, then click **Trust**.

7. You now have two VS Code windows open: the `local_python` window from Exercise 2 and the new one with the Alien Invasion project. You can close the `local_python` window.

### Install pygame and Run the Game

1. Open the terminal (**Terminal → New Terminal**) and install pygame (`pip3` on a Mac):

    ```bash
    pip install pygame-ce
    ```

    The game is built on pygame, so if you skip this step it stops with `ModuleNotFoundError: No module named 'pygame'`. `pygame-ce` is the community edition of pygame. It uses the same `import pygame` statement, and unlike the original package it supports the newest versions of Python.

2. The project files appear in the Explorer panel on the left. `alien_invasion.py` starts the game, and the other files hold the ship, the aliens, the scoreboard, and the settings.

    ![vscode_main.png](images/vscode_main.png)

3. Run the game (`python3` on a Mac):

    ```bash
    python alien_invasion.py
    ```

    ![aliens_game.png](images/aliens_game.png){width=800}

    Use the arrow keys to move, the space bar to fire, and **Q** to quit.

### Change the Game

Open `settings.py`. Every number that controls how the game plays is defined here. Make these changes, saving and rerunning the game after each one:

- Set `bullet_width` to `300` so your bullets clear a whole section of aliens at once
- Change `bullets_allowed` from `3` to `10`
- Change `bullet_color` to something bright, such as `255, 0, 0`
- Speed up the aliens by changing `alien_speed_factor`

Now open the **Source Control** panel. It lists `settings.py` as changed. Click the file name to see a side-by-side comparison: red lines are what you removed and green lines are what you added. This view will matter a great deal once an AI agent is making the changes.

![Source Control panel listing settings.py, with the side-by-side comparison of the bullet_width change](images/vscode_scm_diff.png){:width="800px"}


## Exercise 4 - Meet Your Coding Agent

If your Copilot student license hasn't been approved yet, use the free plan for this exercise.

1. In the Alien Invasion window from Exercise 3, open the Source Control panel and discard your changes to `settings.py` (right-click the file and choose **Discard Changes**) so the game is back to its original state.
2. Open the Copilot chat panel (the chat icon at the top of VS Code) and make sure the mode is set to **Plan**.

     ![The Copilot chat panel with the mode picker open](images/vscode_mode_picker.png){:width="500px"}

    Ask it:

    !!! prompt "Prompt"
        Explain how this game is organized. Which file handles keyboard input, and how does the main loop work?

    Compare its answer to what you see in the files.

3. Switch the mode to **Interactive** and ask:

    !!! prompt "Prompt"
        Add a pause feature. Pressing P should pause the game and show the word "PAUSED" in the middle of the screen. Pressing P again should resume.

4. When the agent finishes, go to the **Source Control** panel and look at what it changed. Which files did it edit? Can you find the new code that checks for the P key?
5. Run the game and test the feature. Does it work? Does anything else break?
6. If it works, commit it. This commit goes into your **local** copy of the repository only. The Alien Invasion repository on GitHub belongs to someone else, so you can't push to it, and you should not click **Sync Changes** here. If it doesn't work, describe the problem to the agent and let it try again. If it makes things worse, discard all the changes in the Source Control panel and start over.

Steps 4–6 are the habit to build: **ask the agent, review what it changed, test it, then commit or throw it away.**

!!! note "Optional: Put Your Version of the Game on GitHub"
    This is not required. If you want your modified game in your own GitHub account do the following:

    1. In the Alien Invasion window, open the terminal and run:

        ```
        git remote remove origin
        ```

        When you cloned the game, Git remembered where it came from and named that location `origin`. This command disconnects your local copy from the original repository. Your files and commits stay on your computer.

    2. Open the Source Control panel. Because your copy is no longer connected to any GitHub repository, it now shows a **Publish Branch** button, just like in Exercise 2.

    3. Click **Publish Branch** and choose **public repository**. You may want to give it a new name, such as `my-alien-invasion`. This creates a new repository in your GitHub account and makes it the new `origin`.

    4. Go to your GitHub profile and open the new repository. Your version of the game, including all of your commits, is there. From now on, **Sync Changes** pushes your commits to your own repository.

## Troubleshooting

Find the message you see below. Most problems come from a skipped step, from typing `python` where a Mac expects `python3`, or from running a command in the wrong folder. If none of these fixes the problem, ask a TA.

### `python` or `pip` Isn't Found

**Mac:** `zsh: command not found: python` or `zsh: command not found: pip`

Use `python3` and `pip3`:

```
python3 beam.py
pip3 install pygame-ce
```

**Windows:** `Python was not found` or `The term 'python' is not recognized`

Quit VS Code completely and reopen it. The terminal only finds programs that were installed before VS Code started, so this clears the error if you installed Python while VS Code was open.

If the error is still there, Python was installed without the **Add Python to PATH** box checked. Use `py` in place of `python` for today:

```
py beam.py
py -m pip install pygame-ce
```

To fix it for good, uninstall Python and reinstall it using the [Setup Guide](local_py_read.md#setup-guide), checking the box this time.

### Python Can't Find Your File

```
python: can't open file '/Users/you/Documents/cce270/beam.py': [Errno 2] No such file or directory
```

Python looks for the file in the folder the terminal is in, and your file is in a different folder. In this example, the terminal is in `cce270`, but `beam.py` is in `cce270/local_python`. The terminal prompt also shows the folder: the whole path on Windows, such as `PS C:\Users\you\Documents\cce270>`, and only the last folder on a Mac, such as `cce270 %`.

To open a terminal in the folder that holds your file:

1. Find the file in the Explorer panel on the left side of VS Code. If it's inside a folder, click the folder name to show the files in it.
2. Right-click the file and choose **Open in Integrated Terminal**. A new terminal opens in the folder that holds the file.
3. Type the command again in the new terminal.

If the file isn't in the Explorer panel, VS Code has a different folder open. Hover over the file's tab at the top of the editor to see where you saved it. Then choose **File → Open Folder**, open that folder, and open a new terminal with **Terminal → New Terminal**.

The game shows the same problem with a different message:

```
FileNotFoundError: No file 'images/ship.bmp' found in working directory '...'
```

The game loads its pictures from the `images` folder, and it finds them only when the terminal is in the game's folder. Right-click `alien_invasion.py` in the Explorer panel, choose **Open in Integrated Terminal**, and run the game from the new terminal.

### `ModuleNotFoundError: No module named 'pygame'`

You skipped step 1 of [Install pygame and Run the Game](#install-pygame-and-run-the-game). Run the install command there, then run the game again.

If pip says it installed `pygame-ce` and you still get this error, pip installed it for a different copy of Python than the one running the game. This happens most often on Macs that have more than one Python. Run pip through the same command you use to run the game:

```
python3 -m pip install pygame-ce
```

On Windows, use `python -m pip install pygame-ce`, or `py -m pip install pygame-ce` if `python` isn't found.

If the error appears only when you click the ▷ Run button, VS Code is using a different Python than your terminal. Run the game from the terminal.

### `pip install pygame` Ends with `Failed to build`

You installed `pygame` instead of `pygame-ce`. The original pygame package doesn't support the newest versions of Python, so it fails to install. Run `pip install pygame-ce`.

### `IndentationError: unexpected indent`

The pasted code came in indented. Select all the lines (**Ctrl+A** on Windows, **Cmd+A** on Mac), press **Shift+Tab** until every line starts at the left edge, and save.

### Your Changes Don't Show Up

Save the file with **Ctrl+S** (**Cmd+S** on a Mac). Python runs the saved version, and a dot on the file's tab means it has unsaved changes. The game reads `settings.py` only when it starts, so quit with **Q** and run it again after each change.

### Committing Fails with `Make sure you configure your "user.name" and "user.email" in git`

Git needs your name and email before it can commit ([Tell Git who you are](local_py_read.md#2-tell-git-who-you-are) in the reading). Run these in the terminal, using your own name and the email on your GitHub account, then commit again:

```
git config --global user.name "Your Name"
git config --global user.email "you@byu.edu"
```

### Source Control Offers to Install Git

If the Source Control panel shows a button to download Git where **Initialize Repository** should be, VS Code can't find Git. If you installed Git while VS Code was open, quit VS Code and reopen it. Otherwise, install Git using the [Setup Guide](local_py_read.md#setup-guide). On a Mac, run `git --version` in the terminal and click **Install** when it offers the Command Line Tools.

### Changes Lists Files Other Than `beam.py`

You initialized the repository in your class folder instead of `local_python`, so Git is tracking everything in your class folder. Don't commit or publish. Ask a TA to help you remove the repository, then open `local_python` with **File → Open Folder** and start Exercise 2 again.

### Copilot or the ▷ Run Button Doesn't Work

Look at the left end of the status bar at the bottom of the window. If it says **Restricted Mode**, you haven't trusted the folder. Click **Restricted Mode**, then click **Trust**. Each folder you open needs this once, including the Alien Invasion folder.
