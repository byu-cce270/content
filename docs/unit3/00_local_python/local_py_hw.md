# HW: Using Python Locally

**Purpose:** Gain experience coding and running your code in a local environment.

---

## Getting Started

In Unit 2 we primarily used Google Colab, which runs Python in the cloud. In this assignment you will practice running Python locally on your own computer.

Running Python locally allows you to:

- Work offline
- Use your own files directly
- Run larger programs more efficiently
- Begin working like real software developers

You should already have installed Python locally during class or shortly after class. If not, go back to the reading or get help from a TA. 

This assignment has two parts. **Part 1** will be due like normal (the night after your next class). **Part 2** will complete later in Unit 3.

---

## Part 1 - Run a Previous Assignment Locally

For this part you will download an old Unit 2 assignment from Google Colab and run it on your own computer. The goal is simply to confirm that your local Python environment works correctly.

### Step 1: Download an Old Unit 2 Homework from Google Colab

1. Open the Unit 2 assignment in Google Colab. If you don't remember where they are saved, you can find them in your Google Drive under "Colab Notebooks" or search for the assignment name in Google Drive.
2. Click File → Download → **Download .ipynb** or File → Download → **Download .py**. If you intend to run the notebook as a Jupyter notebook, download it as a .ipynb. If you want to run it as a Python script in an IDE, download it as a .py file.
3. Save the file somewhere on your computer (for example, a folder for this class).

This will download the notebook file to your local machine.

### Step 2: Open the Notebook Locally

Open the downloaded notebook on your computer using either Jupyter Lab or VS Code that we installed.

General steps:

1. Locate the downloaded .ipynb notebook file on your computer.
2. Open Jupyter Lab or VS Code.
3. Open the notebook file within that environment.

You can also run the *.ipynb* file in VS Code, but it works better in Jupyter Lab.

### Step 3: Run the Notebook

Once the notebook is open in your environment, run the notebook. 

#### Jupyter Lab

If you are using Jupyter Lab, you can run cells by clicking the "Run" button in the toolbar or by using the keyboard shortcut:

```
Shift + Enter
```

1. Run the code cells in the notebook.
2. Continue executing cells until the entire notebook runs successfully.

#### VS Code

If you are using VS Code, open the *.py file and run it using the Run option in the top right corner of the editor or by using the terminal.

```
python filename.py
```

This will run the entire script. If you downloaded the notebook as a .ipynb file, you can also open it in VS Code and run cells similarly to Jupyter Lab.

#### Packages

If you encounter errors about missing packages, you will need to install those packages locally. You can do this using pip in your terminal or command prompt.

```
pip install package_name
```

After installing any required packages, run the notebook or python code again until it executes without errors.

### Step 4: Take a Screenshot

Take a screenshot showing:

- The notebook running on your local machine
- Code cells executed successfully
- Output visible

The screenshot should clearly show that the notebook is not running in Colab. You will turn this in on Learning Suite and finish part 2 later. 

---

## Part 2 - Complete a Future Unit 3 Assignment Locally

For this part, you will complete a future Unit 3 homework assignment, but instead of using Colab you will complete it entirely in your local Python environment. You can pick from homework 3.2-3.7.

### Step 1: Choose a Unit 3 Assignment

Select any future homework assignment from Unit 3. You don't have to complete that assignment until we have covered it in class. 

### Step 2: Download the Starter Notebook (if applicable)

On the homework assignment you are working locally, open up the starter sheet (if there is one) and instead of makeing a copy like you normally would, download the .ipynb file. 

### Step 3: Open the Assignment in Your Local Environment

Open the downloaded notebook or create your file in VS Code or Jupyter Lab.

You may complete the assignment in either of these formats unless your instructor says otherwise:

- A Jupyter notebook (.ipynb)
- A Python script (.py)

### Step 4: Complete the Assignment Locally

Write and run your code locally instead of in Google Colab.

Your file should:

- Include all code required for the assignment
- Run successfully in your local environment
- Show the same work you would normally complete in Colab

If needed, install any required packages using pip or conda.

### Step 5: Save and Submit Your File

When you complete the Unit 3 assignment, submit your work as a local file on Learning Suite.

Acceptable file types are:

- .ipynb
- .py

Make sure the file you submit is the actual file you used locally and that it opens correctly.

---

## Turning in/Rubric

**_REMINDER_** - For this class, **only for this assignment** will you turn in a screenshot and later a .ipynb/.py file. You will not get a 0 for the future assignment that you chose when your turn in a python file.

**Rubric:**

|                                   **Items**                                    | **Amount** |  
|:------------------------------------------------------------------------------:|:----------:|
| Part 1: Screenshot of old unit 2 assignment and shows IDE and the code results |     5      |
|  Part 2: A unit 3 assignment was completed in an IDE and file turned in works  |     25     |
|                 <div style="text-align: right">**Total**</div>                 |   **30**   |

---

The following is not a part of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                       **Reasons for Points Lost**                       |    **Amount**     |  
|:-----------------------------------------------------------------------:|:-----------------:|
|                         Link shared incorrectly                         |       -10%        |
|                        Turned in late (per week)                        | -10% (up to -50%) |
| No comments explaining where AI is used and what its provided code does |       -50%        |




