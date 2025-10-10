#  HW: Introduction to Functions

**Objective:** Learn how to create and use functions.

In this assignment, you will complete a two-part exercise. In the first part, you will create a set of functions 
that converts a text string from standard text to Morse code and back again. In the second part, you will create a 
set of functions that optimize how to cut a set of concrete reinforcing bar (rebar) from standard lengths.

## Getting Started

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/04_intro_functions/(Starter_Notebook)_functions_intro_hw.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "(Your_Name)_functions_intro_hw.ipynb".

## Part 1 - Morse Code

Morse code is a method used in telecommunication to encode text characters as standardized sequences of two 
different signal durations, called dots and dashes. It is named after Samuel Morse, one of the inventors of the 
telegraph. Here is an example of Morse code:

```
.... . .-.. .-.. ---   .-- --- .-. .-.. -..
```
This translates to "HELLO WORLD" in English. Note that each Morse character is separated by a space, and each word is
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
   the **.split("   ")** method of a string to split the 'words' (sequences of morse characters separated by three 
   spaces) into an array. You can then split each word into morse characters using **.split(" ")**. Then you loop 
   through each morse character and look it up in the dictionary. As you convert each morse character to text, you 
   can build a new string that contains the text. Separate each word with a space.
4. Write code to test your functions. First, enter a text string and call the **text_to_morse()** function to 
   convert it to morse code. Print the morse 
   code. 
5. Write code to test the **morse_to_text()** function to convert the morse code back to text. Print the text 
   string. Verify that the original text string and the final text string are the same.

!!! Note
    While this problem can be easily solved using AI, we strongly encourage you to first attempt to write it without 
    AI. If you get stuck, you may use AI tools like ChatGPT or Gemini (Colab AI) to help you debug or complete these 
    functions. If you do use AI tools, be
    sure to examine the code provided by the AI tool and try to understand how it works. Add comments to the code to 
    explain what each part of the code does.


## Part 2 - Optimizing Rebar Cuts

When constructing concrete structures, steel reinforcing bars (rebar) are used to provide tensile strength. Rebar is 
often delivered in standard lengths, such as 20 ft or 60 ft. When a contractor needs to cut rebar to 
specific lengths for a project, they want to minimize waste and maximize efficiency. Being able to model and 
optimize this process can lead to significant cost savings, more sustainable construction practices, and improve 
construction efficiency. In this assignment, you will create a function that calculates the waste and efficiency of 
cutting rebar from standard lengths. You will also create a function that finds the stock length that minimizes waste and 
maximizes efficiency for a given set of required lengths.

1. Write a function called **sort_cuts()#** that takes a list of rebar cut lengths (cut_lengths) and a rebar stock 
   length (stock_length) as input parameters. The function should create list called **cut_plan** where each item in the 
   list represents a set of cuts that can be made from a single stock length. The length of this list is the number of 
   stock lengths needed. The function should return the cut_plan list. For example, if the cut_lengths are [8, 6, 6, 
   4, 3, 2] and the stock_length is 20, the cut_plan could be [[8, 6, 6], [4, 3, 2]]. Note that the order of the 
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
      science. Since the solution can be a little complex, we encourage you to use AI tools like ChatGPT or Gemini 
      (Colab AI) to help you write this function. Be sure to examine the code provided by the AI tool and try to understand
      how it works. Add comments to the code to explain what each part of the code does. 

2. There are two code blocks below that define a list of cut lengths and a list of stock lengths. Run these code blocks to define 
   the lists in your environment. One is for generating a random set of cut lengths and the other is a fixed set of 
   cut lengths. Both sets contain 100 cuts. You can use either set for testing your function, but the specific cut 
   lengths will be used to test your function for grading. 
3. Write code to test your sort_cuts() function. Pass one of the cut_lengthts lists and use a stock length of 20. Print the 
   waste and efficiency returned by the function using f-strings to format the output. Also print the total number 
   of rebar stock required which is the length of your cut_plan list. Then display 
   the contents of the cut_plan list by simply writing the name of the list as the last line of the code block. Your oputput should look something like this:

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
4. Write a function called **optimize_rebar()** that takes four arguments as parameters: a list of cut lengths 
   (cut_lengths), a minimum stock length (min_stock), a maximum stock length (max_stock), and a stock length 
   increment (increment). The function should loop through all stock lengths from min_stock to max_stock, incrementing by 
   increment each time. For each stock length, the function should call the **sort_cuts()** function to get the cut plan, waste, and 
   efficiency. The function should keep track of the stock length that produces the minimum waste and maximum 
   efficiency and corresponding cut_plan list. The 
   function should return the optimal  cut plan and corresponding stock length. As you loop through the stock 
   lengths, print the stock length, waste, and efficiency for each stock length using f-strings to format the output. 

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

# Turning In/Rubric

Turn on sharing and editing. Turn in the link to the Learning Suite feedback box

|                    **Item**                    | **Amount** |  
|:----------------------------------------------:|:----------:|
|  optimize_rebar function is defined correctly  |     4      |
|     The function includes 2 if statements      |     4      |
|         waste is calculated correctly          |     3      |
|       efficiency is calculated correctly       |     3      |
|       print_results is defined correctly       |     4      |
|  print_results calls function optimize_rebar   |     4      |
|        Prints the correct rebar lengths        |     2      |
|         Prints the total stock lengths         |     2      |
|        Prints the total wasted material        |     2      |
|     Prints the total efficiency in percent     |     2      |
| <div style="text-align: right">**Total**</div> |   **30**   |

The following is not part of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                      **Reasons for Points Lost**                         | **Amount** |  
|:------------------------------------------------------------------------:|:----------:|
|  No comments explaining why AI is used and what its provided code does   |     2-3    |
|                       Link shared incorrectly                            |      3     |
