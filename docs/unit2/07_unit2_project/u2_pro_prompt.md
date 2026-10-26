#  Unit 2 Project

**Purpose:** The purpose of this assignment is to showcase how much you have learned during this Python unit of the class. You will get to choose with your team between 3 different prompts listed below.

## Instructions

!!! note "Grading is done from the rubric on this page"
    Your project will be graded using the rubric and the "Reasons for Points Lost" table at the bottom of this page.
    Use them as a checklist before you turn your project in.

1. Assemble your team. Here is the google sheet where you declared this in case you forget:
</br>(If you need to change teams for any reason, please contact the head TA or the professor)

   - [Section 1 (Tue/Thur) F26 Team Sign up Sheet](https://docs.google.com/spreadsheets/d/1wuC_wtIl35VIJQPS_9wqFshkSZB9AH3bdgrOphxBbao/edit?gid=2018473579#gid=2018473579){:target="_blank"}
   - [Section 2 (Mon/Wed) F26 Team Sign up Sheet](https://docs.google.com/spreadsheets/d/1BbOlW3br0eThzIEGwqug39G6jgy3ZJRTF82djzRp0IA/edit?gid=2018473579#gid=2018473579){:target="_blank"}

2. You will then choose one of the three prompts listed below.

3. Complete the project using all the following requirements (this is where your grade will come from):

      - An introductory text block with:
        - instructions on how to use your code
        - link to your external file
        - group name
        - members of your group
        - a report on how each team member contributed (with rubric items that they did)
        - Links to any out of class resources you used **(Please don't forget this part. If there are no links you will lose points)**
      - At least 1 if-elif-else statement
      - Use file reading and or writing. Should be a file that your code creates or one that you upload to your Colab session and use in your code or both.
      - At least 1 loop (for or while)
      - Use numeric and string variables 
      - At least 1 list or dictionary
      - Use comments throughout your code explaining what is happening
      - At least 3 functions that you write/define
      - At least 1 class that has attributes and methods that you write/define
      - Use of forms or input statements.
        - For a refresher on adding a form click [here](https://www.tutorialspoint.com/google_colab/google_colab_adding_forms.htm){:target="_blank"} or about the different types of forms [here](https://colab.research.google.com/notebooks/forms.ipynb){:target="_blank"}
      - Use markdown to organize code
        - Give each code cell a title with `# @title` (for example `# @title Imports`, `# @title Get Data`)
        - [Markdown Guide](https://colab.research.google.com/notebooks/markdown_guide.ipynb#scrollTo=Lhfnlq1Surtk){:target="_blank"}
      - Your program is bug free and runs without error. Code that crashes or shows errors when it is run loses 10%.
      - If you use AI to help write any of your code, add comments explaining where AI was used and what the code it gave you does. **Leaving these comments out costs 50% of your score.**

4. After you have completed your project, create a video that demonstrates what your project does and how it works. You can use ScreenPal (formerly ScreenCast-O-Matic) [https://screenpal.com/](https://screenpal.com/){:target="_blank"} or any other screen recorder that records your screen and your voice. The main purpose of this video is to make grading these projects easier.
   - **Turn in a link to your video, not the video file.** Use ScreenPal's "share" link, or upload the video to YouTube, Google Drive, Box, or OneDrive and copy its link.
   - Make sure the link can be viewed by anyone who has it. A private link can't be graded.
   - Keep it short (ideally under 4 min)
   - Show how your group completed every element in the rubric
   - Have each group member share one thing they learned. 

---

## The Prompts

Whichever prompt you choose, your program should **load its saved file when it starts and save to it before it ends**, so the data is still there the next time you run it. If the file isn't there yet (the first run, or a new Colab session), your program should start with empty data instead of crashing.

### Prompt 1 - Rock, Paper, Scissors
Create the game “Rock, Paper, Scissors” using python. The user will be playing against the computer who will choose a result randomly and it will be compared to the user's input. Incorporate the use of storing and accessing data from a file in this project. The user should be able to play as many times as desired until they ask to stop. Create a file that stores the results of each game played (who won, what the user chose, what the computer chose, etc). At the end of the session, display to the user how many games they won, how many games the computer won, and how many ties there were. Be sure to include the items in the grading rubric below.

Your program should:

- Ask the user again if they type something that isn't rock, paper, or scissors
- Let the user keep playing until they choose to stop
- Add each game's result to the results file
- At the end, show this session's wins, losses, and ties, **and** the all-time record read from the results file

### Prompt 2 - Inventory Management
Create an inventory management system, for example for a construction materials yard. Your code should be able to add, remove, and modify the different inventory items. Store the inventory in a separate file.

Your program should:

- Use a menu that repeats until the user quits, with options to add an item, remove an item, change an item's quantity, and view the inventory
- Give each item a name, a quantity, and a unit price
- Warn the user when an item's quantity drops below a low-stock amount that you choose
- Show the total value of the inventory (quantity × unit price for every item)
- Save the inventory to a file, and load it again the next time the program runs

### Prompt 3 - To Do List
Create a code that will allow a user to take a current to-do list and be able to create, update, and delete tasks. Also include code that will allow the user to store tasks on a file.

Your program should:

- Use a menu that repeats until the user quits, with options to add a task, update a task's status, delete a task, view all tasks, and view the tasks in one category
- Give each task a name, a category, a due date, and a status
- Show how many tasks are overdue and how many are due in the next 3 days
- Save the tasks to a file, and load them again the next time the program runs

---

## Turning in/Rubric

Only one team member needs to turn in the project. That team member should submit both of the following on the
assignment in Learning Suite:

   - **A single `.zip` archive** containing your completed notebook and every file your code uses to run and/or generates
   - The link to watch the video (not the video file), pasted into the feedback box

To build the zip archive:

1. Rename your notebook in Colab something like "(Your-Team-Name)-Unit-2-Project.ipynb".
2. Run all of your cells so that your output is saved in the notebook, then download it from Colab with **File | Download | Download .ipynb**.
3. Put the downloaded `.ipynb` file and all of your data files together in one folder. Name the folder something like "(Your-Team-Name)-Unit-2-Project".
4. Compress the folder into a single `.zip` file:
    - **Windows:** right-click the folder and choose **Send to | Compressed (zipped) folder**
    - **Mac:** right-click the folder and choose **Compress "(Your-Team-Name)-Unit-2-Project"**
5. Upload the resulting `.zip` file to the assignment in Learning Suite.

**Rubric:**

|                                  Item                                  | Points Possible |
|:----------------------------------------------------------------------:|:---------------:|
| An introductory text block with all the relevant information asked for |        3        |
|                      Uses if-elif-else statement                       |        5        |
|                    Uses file reading and or writing                    |        5        |
|                               Uses loops                               |        5        |
|                   Uses numeric and string  variables                   |        2        |
|                      Uses a dictionary or a list                       |        5        |
|                    Uses comment to explain the code                    |       15        |
|                 Writes and defines 3 custom functions                  |       15        |
|         Writes and defines 1 class with attributes and methods         |        5        |
|                  Uses colab forms or input statements                  |        5        |
|                   Use markdown to organize your code                   |        5        |
|                            Prompt completed                            |       10        |
|                Video uploaded (link to video, not the file)            |       10        |
|                          Participation points                          |       10        |
|             <div style="text-align: right">**Total**</div>             |       100       |

---

The following is not a part of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to upload your file correctly.

|                       **Reasons for Points Lost**                       |    **Amount**     |  
|:-----------------------------------------------------------------------:|:-----------------:|
|                        File uploaded incorrectly                        |       -10%        |
|                        Turned in late (per week)                        | -10% (up to -50%) |
|               Code crashes or shows errors when it is run               |       -10%        |
| No comments explaining where AI is used and what its provided code does |       -50%        |