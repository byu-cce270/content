#  Reading: NumPy Library

!!! note "Start your GitHub application this week"
    This topic's homework has you create a GitHub account and apply for a free student Copilot license. GitHub takes a few days to review each application, and longer at the start of a semester, so don't leave it until the night the homework is due. The steps are in [Setting Up GitHub and Copilot](#setting-up-github-and-copilot) further down this page. Read them before class so you can ask questions while a TA is there to help.

---

# Pre-Class Reading Assignment

Read the [NumPy chapter](numpy_chapter.md). It takes about 45 minutes. Open a blank Google Colab notebook and run the examples as you read.

The *Python Data Science Handbook* chapters this page used to assign are now optional. They're listed under [Going Further](numpy_chapter.md#going-further) at the end of the chapter.

## Things to look out for
- What is the difference between a list and a NumPy array?
- How to turn a list into a NumPy array?
- How to append 2 NumPy arrays together?
- The different functions you can do with a NumPy array
- How to pick out a single value, a row, or a column of a 2-D array?
- How to solve a system of equations with `np.linalg.solve()`?

---

<!-- Keep in sync with Part 5 of numpy_hw.md, which repeats these steps. -->

# Setting Up GitHub and Copilot

Later in Unit 3 you will use an AI coding agent called GitHub Copilot, which is free for verified students. Setting this up is part of the Numpy homework, but read through it now so you can ask questions in class or of a TA before you do it.

GitHub reviews each application, which usually takes a few days and can take longer at the start of a semester, so start as soon as you can. Follow the steps in order, because an application can be rejected if Steps 1 to 3 are incomplete.

**Step 1: Create a GitHub account**

1. Go to [github.com](https://github.com/) and click **Sign up**. Use your **@byu.edu** email address.
2. Choose your username with care. It appears in the address of every web page you publish from GitHub, and many engineers use their GitHub profile as part of their résumé.
3. Open the email from GitHub and verify your address.

If you already have a GitHub account, keep it. Add your @byu.edu address under **Settings → Emails** and verify it.

!!! warning "Four things to check before you apply"
    GitHub's own application page does not mention these, but we have tested it: applications without them are rejected, and applications with them are accepted. Before you click **Start an application**, make sure all four are true:

    1. Your **@byu.edu email** is on your account and verified (Step 1).
    2. **Two-factor authentication** is turned on (Step 2).
    3. Your **name** on GitHub matches the name BYU has for you (Step 3).
    4. Your **billing information** is filled in — name and address, no credit card (Step 3).

**Step 2: Turn on two-factor authentication**

1. Install an authenticator app on your phone, such as Google Authenticator or Microsoft Authenticator.
2. On GitHub, click your profile picture, then go to **Settings → Password and authentication**.
3. Click **Enable two-factor authentication**.
4. Scan the QR code with the app, and enter the six-digit code it shows.
5. Click **Download** to save your recovery codes, and keep the file somewhere safe. If you lose your phone, these codes are how you get back into your account.
6. Click **I have saved my recovery codes**.

**Step 3: Add your name and billing information**

Your name on GitHub has to match the name BYU has on record for you — the same name that appears on your BYU ID and on whatever document you upload in Step 4. This is the step that catches people out:

- Use your full legal name, not a nickname. If BYU has you as "David," don't put "Dave."
- Include your middle name or initial if it appears on your ID.
- Look at your BYU ID while you type it rather than going from memory.

1. Go to **Settings → Public profile**, enter your name in the **Name** box, and click **Update profile**.
2. Go to **Settings → Billing & Licensing → Payment information**.
3. Add your first name, last name, and address.

!!! danger "Do not enter a credit card"
    GitHub asks for billing information, but everything you are applying for is free. Enter your first name, last name, and address only. Leave the payment method empty — you do not need a credit card, and you should not add one.

**Step 4: Apply for student benefits**

Before you start, have your BYU ID with you and turn off any VPN. Apply from campus if you can, because GitHub checks your location.

1. Go to [github.com/settings/education/benefits](https://github.com/settings/education/benefits) and click **Start an application**.
2. Select your @byu.edu email and **Brigham Young University**.
3. Allow your browser to share your location and use your camera when it asks.
4. When asked for proof, upload a picture of your BYU ID. Your full name, Brigham Young University, and the expiration date must all be easy to read, because GitHub needs to see a date. A class schedule, transcript, or enrollment verification letter also works.
5. Click **Submit application**.
6. Take a screenshot showing that your application was submitted. You will turn this in with the Numpy homework.

**Step 5: Turn on Copilot after you are approved**

Approval alone doesn't turn Copilot on. GitHub will email you when you are approved, and the benefit can take several more days to finish applying to your account. Then:

1. Go to [github.com/settings/education/benefits](https://github.com/settings/education/benefits).
2. Under **Free GitHub developer resources for students and teachers**, click **Learn more**.
3. Follow the prompts to activate **Copilot Student**.

If your account still shows the free plan after a few days, try [github.com/settings/copilot](https://github.com/settings/copilot) and follow the prompts. **If you are only offered paid plans, do not buy anything.** Wait a few days and try again, and contact GitHub Support if it still doesn't work.

If your application is rejected, read the reason in the email, fix it, and apply again. The most common problems are a name that doesn't match the name BYU has for you, missing billing information, two-factor authentication turned off, an unverified BYU email, location sharing turned off, a VPN, or a blurry photo. If you are still waiting when we start using Copilot, you can use Copilot's free plan, which is limited to 2,000 code completions per month.

---

# Pre-Class Quiz Challenge
The challenge has two parts, and both are done in the same notebook:

- **Part 1 - Quiz Questions:** Answer the questions below in the **Quiz Answers** text block at the top of the notebook. Double-click the text block to edit it, and type your answer after each **Answer:**.
- **Part 2 - Code Blocks:** Complete Code Blocks 1-3 by following the instructions in the notebook.

<a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit3/00_numpy/Pre_Numpy.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Save your changes, then download the completed notebook with **File | Download | Download .ipynb** and upload it to Learning Suite.

## Part 1 - Quiz Questions
Each question lists the section of the [NumPy chapter](numpy_chapter.md) that covers it.

**Question 1.** Did you do the reading?

- T) Yes, I did
- F) No

**Question 2.** What is the first thing you should always do if you intend to use NumPy in your code?

- A) `import np as numpy`
- B) `import numpy as np`
- C) `upload numpy as np`
- D) `import np`

*Where to look: [Importing NumPy](numpy_chapter.md#importing-numpy).*

**Question 3.** What is the output of the following code?

```python
import numpy as np
ary = np.array([1, 2, 3, 5, 8])
ary = ary + 1
print(ary[1])
```

- A) 0
- B) 1
- C) 2
- D) 3

*Where to look: [Math on a Whole Array](numpy_chapter.md#math-on-a-whole-array) and [Picking Values Out of an Array](numpy_chapter.md#picking-values-out-of-an-array).*

**Question 4.** What will be the output of the following code?

```python
import numpy as np
nums = [2,3,4,5]
updatednums = np.array(nums)
print(updatednums)
```

- A) `['2' '3' '4' '5']`
- B) `[2,3,4,5]`
- C) `[2 3 4 5]`
- D) `[5 4 3 2]`

*Where to look: [From Lists to Arrays](numpy_chapter.md#from-lists-to-arrays).*

**Question 5.** What is the syntax for changing a list called `mylist` into an array using NumPy?

- A) `array(mylist)`
- B) `mylist.np_array()`
- C) `np.array(mylist)`
- D) `array(mylist).np`

*Where to look: [From Lists to Arrays](numpy_chapter.md#from-lists-to-arrays).*

**Question 6.** True or False: given the array below, the syntax `my_array[1]` returns `[1 2 3]`.

```python
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
```

- T) True
- F) False

*Where to look: [Two-Dimensional Arrays](numpy_chapter.md#two-dimensional-arrays), under [Selecting Rows, Columns, and Values](numpy_chapter.md#selecting-rows-columns-and-values).*

**Question 7.** What is the output of the following code?

```python
import numpy as np
a = np.arange(10)
print(a[2:5])
```

- A) `[2 3 4]`
- B) `[0 1 2]`
- C) `[5 6 7]`
- D) `[2 4 6]`

*Where to look: [Making Arrays from Scratch](numpy_chapter.md#making-arrays-from-scratch) (for `np.arange`) and [Picking Values Out of an Array](numpy_chapter.md#picking-values-out-of-an-array).*

**Question 8.** What syntax would you use to solve the system of linear equations containing arrays `A` and `B`?

- A) `np.linalg.solve(A, B)`
- B) `linalg.solve.np(A, B)`
- C) `np.solve(A, B)`
- D) `linalg.solve(A, B)`

*Where to look: [Solving Systems of Equations](numpy_chapter.md#solving-systems-of-equations).*

## Part 2 - Code Blocks
Complete Code Blocks 1-3 in the notebook. The instructions are in the text block above each code block.

---

## Turning in/Rubric

**_REMINDER_** - For this class, **you will download your completed Colab notebook and upload the `.ipynb` file to Learning Suite**. Make sure the notebook you upload is for the correct assignment and contains your finished work.

**Rubric:**

|                             Item                             | Points Possible |
|:------------------------------------------------------------:|:---------------:|
|        Part 1 - Question 1 (Did you do the reading?)        |        2        |
| Part 1 - Questions 2-8 (10 points split evenly, correct answers) |       10        |
|            Part 2 - Code Blocks 1-3 (1 point each)            |        3        |
|        <div style="text-align: right">**Total**</div>         |       15        |

---

The following is not a part of the rubric, but specifies how you can lose points. For example: if you fail to upload your file correctly.

| **Reasons for Points Lost** |    **Amount**     |  
|:---------------------------:|:-----------------:|
|  File uploaded incorrectly  |       -10%        | 