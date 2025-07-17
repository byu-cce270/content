#  Reading: IF Statements and Goal Seek

---

# Pre Class Reading Assignment

Before class, you will learn about a few types of IF Statements: IF and IFS. You will also learn about Goal Seek.

---

## IF Statements

**IF Statements** are a function within Google Sheets that can compare two values and determine if they are true or false. This type of two-outcome expression in programming is known as a boolean.

### Syntax

The syntax for an IF statement is as follows:

    =IF(logical_expression, value_if_true, value_if_false)

An IF statement has three arguments:

- **logical_expression**: This is what is known as the conditional statement. This function can compare whether a number is greater than (**>**), less than (**<**), or if a number or text is equal to (**=**) in the given condition
- **value_if_true**: This is a placeholder for what will be returned if the given condition is found to be true.
- **value_if_false**: This is a placeholder for what will be returned if the given condition is found to be false.

### Example Problem - IF Statement

Let's look at a simple example of an IF statement using strings. Here are a few fictional locations that have different types of material their driveways are made out of. Using an IF statement, we can quickly differentiate for specifically a concrete driveway.

![readingex1.png](images/readingex1.png)

We can write a single statement in cell C2, drag it down, and watch it populate with either a "Yes" or a "No" depending on the conditional statement we gave the function.

![readingex2.png](images/readingex2.png)

One more example is using a number. Using the length of a driveway, we can find which of the driveways are longer than the given distance of 75 ft.

![readingex3.png](images/readingex3.png)

Again, we can see that we can quickly populate the rest of the table by dragging the corner of the cell down.

![readingex4.png](images/readingex4.png)

---

## IFS Statements

**IFS Statements** are an even more powerful version of an IF statement that can allow for multiple conditional statements to take place within one function. This type of function allows for easy categorization by testing a given number or string against one found in a table

### Syntax

The syntax for an IFS statement is as follows:

    =IFS(logical_expression1, value_if_true1, [logical_expression2, value_if_true2], [logical_expression3, ...)

An IFS statement only technically requires two arguments, both of which are nearly the same as the IF statement. However, there can be any number of logical expressions within one IFS statement.

**Note**: More than one condition can be true so the function will always return the value for the first condition that is found true.

### Example Problem - IFS Statement

Using the same premise as the IF statement, we can utilize the table we used before. This time around, we will categorize the different lengths of driveways into three tiers: short, medium, and long.

![readingex5fixed.png](images/readingex5fixed.png)

**Note**: The third condition ```<=50``` includes ```=``` so that 50 is included in "less than or **equal** to 50

Dragging them down, we can see the final result. Now each driveway is nicely categorized by its length.

![readingex6.png](images/readingex6.png)

---

## Goal Seek

There are many cases when performing computations in Excel where we need to solve an equation that is either difficult or impossible to solve directly. Therefore, we need to solve it using some sort of iterative process. This is often done using a trial-and-error approach where we enter our formula and then experiment with different input values to the formula until the formula returns the desired output. **Goal Seek** is an add-on plugin for Google Sheets that automates this process. It is a powerful tool that utilizes an algorithm that plugs in different calculations to find a solution for an unknown variable using a known end-goal value. One example of this is often found in sales when determining how many units need to be sold to break even or meet a certain quota.

### Using Goal Seek

To use Goal Seek, head to **Data** > **What-If Analysis** > **Goal Seek.** This will open the Goal Seek dialog box, 
where you can enter your desired values and the cells you want to change.

Goal Seek has three basic components: 
- **Set Cell**
- **To Value**
- **By Changing Cell**

### Example Problem 
Let's use the example of a contractor wanting to find what he would have to charge to make a profit of **\$1250** by 
building his friend a 12' x 12' deck. Given the cost of materials (\$6000) and the $22/hr of pay for each employee, we 
can calculate the project cost. Using Goal Seek, we can allow the computer to do the rest of the work for us.

First, select the cell you want to set by 1) selecting the cell (B11) and 2) clicking the **Set Cell** grid icon on the goal seek tab. 

**Hint**: This cell should **almost always** be the cell that contains your formula.

![GoalSeekExcel1.png](images/GoalSeekExcel1.png)

Then, set the **To Value** to whatever value you are trying to find. In our case, this number would be 1250.

Finally, select the cell that would need to change to evaluate the final part of the question. In this instance, this would be cell B9.

![GoakSeekExcel2.png](images/GoakSeekExcel2.png)

When all three inputs are filled on the Goal Seek tab, the Solve button will light up blue. If you press the button, the computer should start jumping between values trying to find the solution to what gets a profit of $1250.

In this example, our solution is $8240.000057, or **$8240**!

### How does this work?

Each attempt by the computer tries to get closer and closer by guessing a number.

**Attempt 1**

![guess1.jpg](images/guess1.jpg)

**Attempt 2**

![guess2.jpg](images/guess2.jpg)

**Attempt 3**

![guess3.jpg](images/guess3.jpg)

**Attempt 4 and onwards**

![guessTo6.jpg](images/guessTo6.jpg)

---

# Pre-Class Quiz Challenge

Here is a link for the pre-class starter sheet: [IF Statement Pre-Class](https://docs.google.com/spreadsheets/d/1THgXpQWhGptdaxTNjyA9lHC3aBrUcUookT472WKRKFk/edit?usp=sharing){:target="_blank"}

## Instructions

1. In column D, use RANDBETWEEN to give points to Students randomly. Points should be between 0 and 100. Then copy and paste-special (as values) the results to lock in the values. This overwrites the formula with the values it generated.
2. In column E, write a simple IF statement in the Pass/Fail column to indicate "Pass" or "Fail" depending on whether they scored over 60/100.
3.  In column F, write a complex IF statement in the "Grade" column to assign a letter grade to each student based on their points:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;90-100 = A, 80-89 = B, 70-79 = C, 60-69 = D, < 60 = F
