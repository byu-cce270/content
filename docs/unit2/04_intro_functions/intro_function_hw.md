#  HW: Introduction to Functions

**Objective:** Learn how to create and use functions.

In this assignment, you will complete a two-part exercise. In the first part, you will create a set of functions 
that converts a text string from standard text to Morse code and back again. In the second part, you will create a 
set of functions that optimize how to cut a set of concrete reinforcing bar (rebar) from standard lengths.

## Getting Started

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/04_intro_functions/(Starter_Notebook)_functions_intro_hw.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "(Your_Name)_HW_Intro_Functions.ipynb".

## Part 1 - Morse Code

Morse code is a method used in telecommunication to encode text characters as standardized sequences of two 
different signal durations, called dots and dashes. It is named after Samuel Morse, one of the inventors of the 
telegraph. Here is an example of Morse code:

```
.... . .-.. .-.. ---   .-- --- .-. .-.. -..
```
This translates to "HELLO WORLD" in English. Note that each Morse character (a letter) is separated by a space, and each word is
separated by three spaces.

In this assignment, you will create a function that converts text to Morse code and another function 
that converts Morse code back to text.

1. At the top of this section you will see a code block that contains two dictionaries. The first dictionary, 
   "**TEXT2MORSE_DICT**", maps each letter and number to its corresponding Morse code representation. The second 
   dictionary, "**MORSE2TEXT_DICT**", is the reverse mapping, converting Morse code back to text. Run this code block to 
   define the dictionaries in your environment.
2. Write a function called **text_to_morse()** that takes a string in normal text and then translates it to morse code 
   and returns a string containing the translated result. Use the dictionary defined above in your code. You will 
   need to convert the text string to all uppercase to use the dictionary properly. If you encounter a morse character not in the dictionary insert '<ERROR\>' in the place of the character. You can use the **.split(" ")** method of a string to split the 'words' (sequences of text characters separated by " ") into an array. You can then split each word into characters using **list(word)**. Then you loop through each character and 
   look it up in the dictionary. As you convert each character to morse code, you can build a new string that 
   contains the morse code. Separate each morse character with a space and separate each word with three spaces.
3. Write a function called **morse_to_text()** that takes a string in morse code and then translates it to normal text and 
   returns a string containing the translated result. Use the dictionary defined above in your code. If you 
   encounter a morse character not in the dictionary insert '\<ERROR\>' in the place of the character. You can use 
   the **.split("   ")** method (**hint** there are three spaces between the quotes) of a string to split the 'words' 
   (sequences of morse characters separated by three 
   spaces) into an array. You can then split each word into morse characters using **.split(" ")** (**hint** there 
   is one space between the quotes). Then you loop 
   through each morse character and look it up in the dictionary. As you convert each morse character to text, you 
   can build a new string that contains the text. Separate each word with a space.
4. Write code to test your functions. First, enter a text string and call the **text_to_morse()** function to 
   convert it to morse code. Print the morse 
   code. 
5. Write code to test the **morse_to_text()** function to convert the morse code back to text. Print the text 
   string. Verify that the original text string and the final text string are the same.

!!! Note
    While this problem can be easily solved using AI, we strongly encourage you to first attempt to write it without 
    AI. If you get stuck, you may use AI tools like ChatGPT or Gemini (The AI inside Colab notebooks) to help you debug or complete these 
    functions. If you do use AI tools, be
    sure to examine the code provided by the AI tool and try to understand how it works. Add comments to the code to 
    explain what each part of the code does.


## Part 2 - Optimizing Rebar Cuts

When constructing concrete structures, steel reinforcing bars (rebar) are used to provide tensile strength. Rebar is 
often delivered in standard lengths, such as 20 ft or 60 ft. When a contractor needs to cut rebar to 
specific lengths for a project, they want to minimize waste and maximize efficiency. Being able to model and 
optimize this process can lead to significant cost savings, more sustainable construction practices, and improve 
construction efficiency. In this assignment, you will create a function that calculates the waste and efficiency of 
cutting rebar from standard lengths and evaluates different lengths to see which is better. You will also create a function that finds the stock length that minimizes waste and 
maximizes efficiency for a given set of required lengths.

1. Write a function called **sort_cuts()** that takes a list of rebar cut lengths (cut_lengths) and a rebar stock 
   length (stock_length) as input parameters. The function should create list called **cut_plan** where each item in the 
   list represents a set of cuts that can be made from a single stock length. The length of this list is the number of 
   stock lengths needed. The function should return the cut_plan list. For example, if the cut_lengths are [8, 6, 6, 
   4, 3, 2] and the stock_length is 20, the cut_plan could be [[8, 6, 6], [4, 3, 2]]. This means that the first 20-foot rebar is cut into pieces of 8, 6, and 6 feet (no waste), and the second 20-foot rebar is cut into pieces of 4, 3, and 2 foot lengths, which would leave a waste piece 11 feet long. **Note**  the order of the 
   cuts in each sublist does not matter. Also note that the sum of the cuts in each sublist must be less than or equal to the 
   stock_length. You can assume that all cut lengths are less than or equal to the stock_length. The function should 
   also return a **waste** variable that is the total waste for the cut plan. Waste is defined as the total length of stock 
   minus the total length of cuts. In the example above, the total length of stock is 40 (2 stock lengths of 20) and 
   the total length of cuts is 29 (8 + 6 + 6 + 4 + 3 + 2), so the waste is 11 (40 - 29). The function should also 
   return a variable called **efficiency** that is the efficiency of the cut plan. Efficiency is defined as the total length of 
   cuts divided by the total length of stock, expressed as a percentage. In the example above, the efficiency is 72.5% 
   (29 / 40 * 100).

!!! Note
      This type of problem is known as the "binpacking problem" and is a common optimization problem in computer 
      science. Since the solution can be complex, we encourage you to use AI tools like ChatGPT or Gemini 
      (Colab AI) to help you write this function. Be sure to examine the code provided by the AI tool and try to understand
      how it works. Typically, this type of code would be part of an advance optimization class. Here we don't expect you to understand how the optimization works, but realize you can solve problems like this with AI. We do want you to be able to understand what the code is doing. **Add comments to the code to explain what each part of the code does**. 

!!! Approach
    What you are learning here is how to instruct the AI to write your code. You need to be able to describe what you want the code to do in specific simple steps and the order the steps should occur. You don't need to know how to do the steps, but you do need to know what steps are required to solve the problem. 



2. There are two code blocks below that define a list of cut lengths and a list of stock lengths. Run these code blocks to define 
   the lists in your environment. One is for generating a random set of cut lengths and the other is a fixed set of 
   cut lengths. Both sets contain 100 cuts. You can use either set for testing your function, but the fixed cut 
   lengths will be used to test your function for grading as the random lengths will generate a new list everytime it is run. 


3. Write code to test your sort_cuts() function. Pass one of the cut_lengths lists and use a stock length of 20. Print the 
   waste and efficiency returned by the function using f-strings to format the output. Also print the total number 
   of rebar stock required which is the length of your cut_plan list. Then display 
   the contents of the cut_plan list by simply writing the name of the list as the last line of the code block. Your output should look something like this:

```
Waste = 16.5
Efficiency = 97.77%
Number of stock required = 37
Cut Plan:
[[12.0, 8.0],
 [12.0, 8.0],
 [12.0, 8.0],
 [11.5, 8.5],
 [11.5, 8.5],
 ...
```
The "Cut Plan:" in the above printout is a list of lists. Each sublist represents the cuts made from a single stock length. The order of the cuts in each sublist does not matter. The sum of the cuts in each sublist must be less than or equal to the stock_length.

4. Write a function called **optimize_rebar()** that takes four arguments as parameters: a list of cut lengths 
   (cut_lengths), a minimum stock length (min_stock), a maximum stock length (max_stock), and a stock length 
   increment (increment). The function should loop through all stock lengths from min_stock to max_stock, 
   incrementing by 1 each time. For each stock length, the function should call the **sort_cuts()** function to get 
   the cut plan, waste, and 
   efficiency. The function should keep track of the stock length that produces the minimum waste and maximum 
   efficiency and corresponding cut_plan list. The 
   function should return the optimal cut plan and corresponding stock length. As you loop through the stock 
   lengths, print the stock length, waste, and efficiency for each stock length using f-strings to format the output. 

!!! Hint
    You will need to clearly tell the AI the details of both the problem and what you are trying to do -- optimize the cuts to reduce the amount of waste. For example, you need to explain (or show the AI) how the cut list and the stock list are formatted, exactly what you want the function to return in both answer terms (a list of cuts for each stock piece, total waste, and efficiency) and in data types (a list of lists for the cut plan, a float for the waste, and a float for the efficiency). You also need to explain how you want the function to work. 

5. Write code to test your **optimize_rebar()** function. Use the cut_lengths list defined above and a minimum stock length of 16, 
   a maximum stock length of 30, and an increment of 2. Print the optimal stock length and the number of stock 
   required for the optimal cut plan (length of cut plan) Then 
   display the contents of the 
   optimal cut_plan 
   list by simply writing the name of the list as the last line of the code block. Your output should look something like this:

```
16.00 ft -> waste=12.50 ft, efficiency=98.30%
18.00 ft -> waste=14.50 ft, efficiency=98.04%
20.00 ft -> waste=16.50 ft, efficiency=97.77%
22.00 ft -> waste=24.50 ft, efficiency=96.72%
24.00 ft -> waste=20.50 ft, efficiency=97.24%
26.00 ft -> waste=4.50 ft, efficiency=99.38%
28.00 ft -> waste=4.50 ft, efficiency=99.38%
30.00 ft -> waste=26.50 ft, efficiency=96.47%
Best stock length = 26.0 ft
Number of stock required = 28
[[12.0, 12.0, 2.0],
 [12.0, 11.5, 2.5],
 [11.5, 11.5, 3.0],
 [11.5, 11.5, 2.5],
 [11.0, 11.0, 4.0],
 [11.0, 11.0, 4.0],
```

Note that the first part of the output shows the waste and efficiency for each stock length tested and this is 
printed by the optimize_cuts function. The second part of the output is printed by your test code.

!!! info "Additional Insight into Solving the Problem"
    One approach to solving this problem is to use a greedy algorithm. The idea is to sort the cut lengths in descending order and then try to fit each cut length into the first stock length that has enough remaining length. If no existing stock length can accommodate the cut, a new stock length is added to the cut plan. This approach does not guarantee an optimal solution but is often effective for practical purposes. 

    For example if the stock length is 20 feet, and your sorted cut-list has 3 15 foot cuts, you would pick the 1st 15 foot cut and put it in the first stock length, then the 2nd 15 foot cut would not fit in the first stock length (5 feet left) so you would put it in a 2nd stock length. The 3rd 15 foot cut would also not fit in either of the first two stock lengths (5 feet left in each) so you would put it in a 3rd stock length. Then you would move to the next shortest cut length and try to fit it in the first stock length that has enough remaining length. You would continue this process until all cut lengths are assigned to a stock length. In this case, you would need to have a cut of 5 feet or less to fit in the remaining space of any of the 3 stock lengths for the first three cuts. If you don't have any cuts of 5 feet or less, you would have 5-feet of waste material for each 15-foot cut.  The AI tool can help you write the code to implement this algorithm. 

    Above, when you solved this problem, the  AI may have used other approaches if you didn't specify the greedy algorithm. That is fine. Try to figure out what it did and expalin it with comments in the code. If you don't understand the algorithm, you do need to provide comments explaining what the each line of the  code does, even if you don't quite understand how it is solving the problem.

!!! hint "Using AI Tools"
    As you can see from the above, if you knew to use the "greedy" algorithm, you could code it yourself. We have discussed all the tools to do that. However, since this isn't an optimization class, we would not expect you to know that. The point of this exercise is to learn how to use AI tools to solve problems you don't know how to solve. You do need to be able to understand the code provided by the AI tool and explain what it does with comments in the code. If you don't understand how it works, you can still provide comments explaining what each line of the code does, even if you don't quite understand how it is solving the problem. 

    We expect AI will give you the greed algorithm, but there are other algorithms that could be used. The algorithm that the AI picks will be dependant on the "prompt" you give it. This just shows you can use AI and programing to solve problems, where you know what needs to be done, but not how to do it or code it up. 

---

## Turning in/Rubric

**_REMINDER_** - For this class, **you will only turn in the links to your colab notebooks**. You will get a 0 for this assignment if you turn in a python file or a link that is not correct, wrong assignment, or does not give editor permission.

**Rubric:**

|                           **Item**                           | **Amount** |  
|:------------------------------------------------------------:|:----------:|
|              text_to_morse() converts to upper               |     2      |
|           text_to_morse() splits the words & char            |     2      |
|             text_to_morse() error if not in dict             |     1      |
| text_to_morse() character is separated by 1 space, word by 3 |     2      |
|           morse_to_text() splits the words & char            |     2      |
|          morse_to_text() error if not in dictionary          |     1      |
|          morse_to_text() character 1 space, word 3           |     2      |
|           def sort_cuts(cut_lengths, stock_length)           |     2      |
|                cut_plan is returned correctly                |     4      |
|              sum of cuts is < or = stock_length              |     2      |
|          efficiency is calculated correctly (in %)           |     2      |
|                waste is calculated correctly                 |     2      |
|  optimize_rebar prints stock length, waste, and efficiency   |     3      |
|   optimize_rebar returns optimal cut plan and stock_length   |     3      |
|        <div style="text-align: right">**Total**</div>        |   **30**   |

---

The following is not a part of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                       **Reasons for Points Lost**                       |    **Amount**     |  
|:-----------------------------------------------------------------------:|:-----------------:|
|                         Link shared incorrectly                         |       -10%        |
|                        Turned in late (per week)                        | -10% (up to -50%) |
| No comments explaining where AI is used and what its provided code does |       -10%        |
