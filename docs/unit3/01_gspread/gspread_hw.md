
# HW: Gspread
---
**Purpose:** 
- Learn how to connect read data from a google sheet to manipulate in Python and update into your google sheet.
- Practice using functions and loops with gspread.

---
## Part 1

**Objective**: Create a code that will analyze the different subcontractor bids given to you for the drywall and concrete scopes. Choose a subcontractor bid based on your analysis. 

For this example, you have been given bids that were submitted for a job and it is your job as the project manager to determine which bid you will choose. 

### Steps
1. Open this Colab notebook and title it with your name: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/03_if_statements/%5Byour_name%5D_if_statements_hw.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
2. Go to the "Imports" code block. Write the proper code to import gspread and authentiate yourself.
3. Create a copy of the following worksheet and open it by url in the same code block. [Gspread Sample Data](https://docs.google.com/spreadsheets/d/1AtCbzKEuugeq9zCccWDjv9LpaLZX8ftikq6j64JJ1xc/edit?gid=0#gid=0){:target="_blank"}
4. In the code block titled "Bid Analysis" open the first worksheet in your workbook.
5. Use the .get_all_values() method to pull all the values from your spreadsheet into a list. Input the following code into your notebook:

   ```python
   headers = values1[0]
   rows = values[1:]
   ```
   
   *  Hint: Depending on what you named your values list this code might have to be modified, but the principle is the same.
  
6. Using a for loop, loop through the bid amounts in the rows list and convert the numbers into floats so you can perform an analysis on them.

   *  Hint: The following code will remove the $ and , in the bid amounts of the Google Sheet so the numbers can be converted correctly:
   ```python
   .replace('$','').replace(',','')
   ```
7. Outside of the for loop, create two empty lists. One named Drywall, and the other named Concrete. This is where you will store the different bids.
8. Create a for loop that will loop through the different rows in your Google Sheet and add the row to the Drywall list if the scope is Drywall or the Concrete list if the associated scope is Concrete.
9. Move to the "Drywall Bid Analysis" code block. Line 4 is advanced code that is provided to you for this assignment. It will sort your Drywall list in order from cheapest to most expensive bid.
10. Write code to delete the most expensive and cheapest bid from your list.
11. Write code to find the average cost for the remaining bids in your list.
12. Write code to find the median cost for the remaining bids in your list.
13. Now that you understand your bids more, write a while loop that will loop through the remaining bids and ask you as the user if you would like to accept the given bid.
    
    *  If you do want to accept the bid you should print something like: "Bid accepted. Your final bid for Drywall is: *insert chosen here*." After accepting the bid, you should end the loop.
    *  If you do not want to accept the bid you should remove the bid from your list of bids and continue the loop.
    
14. Write code to add a new sheet to your Google Sheet with the selected bidder's information.
15. Move to the "Concrete Bid Analysis" code block. Line 4 is the same advanced code given for the Drywall bids.
16. Repeat steps 10-14 for the concrete bids.

---
## Part 2

**Objective**:  You will now be completing client estimation for different material orders.

### Steps
1. In the "Client Estimating Portion" code block open the 'Material Cost' worksheet from your workbook to work with that data.
2. Use the .get_all_values() method to pull all the values from your spreadsheet into a list.
3. Create a function called client_estimation that will take 2 parameters, one for the quantities ordered by the clients and one for the list of materials costs from your Google Sheet.
4. Inside the function do the following:
    - Remove the header row from the quantities list.
    - Start an empty list for the quantities needed by the client.
    - Create a variable for the total_cost of the estimate that starts at 0.
5. Still inside the function, loop through the quantities needed by the client, convert them to floats, and add a waste factor of 10%.
6. 
7. 
8. 
---

**Turn sharing and editing on. Turn in the link to Learning Suite in the feedback box**

---

**Rubric:**

|                                               If Statements                                                     | Points Possible |
|:-------------------------------------------------------------------------------------------------------:|:---------------:|
|                         Part 1 - Correct value for scenario 1                                           |        5        |
|                          Part 1 - Correct value for scenario 2                                          |        5        |
|                          Part 1 - Correct value for scenario 3                                          |        5        |
|                           Part 2 - Correct value for wood                                               |        3        |
|                            Part 2 - Correct value for steel                                             |        3        |
|                               Part 2- Correct value for brick                                           |        3        |
|                            Part 2 - Correct value for glass                                             |        3        |
|                               Part 2- Correct value for concrete                                        |        3        |
|                             <div style="text-align: right">**Total**</div>                              |       30        |

The following is not apart of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                      **Reasons for Points Lost**                      | **Amount** |  
|:---------------------------------------------------------------------:|:----------:|
| No comments explaining why AI is used and what its provided code does |    2-3     |
|                        Link shared incorrectly                        |     3      |
|       Turned in late. 10% or 3 points for every week it's late.       |    3-15    |
