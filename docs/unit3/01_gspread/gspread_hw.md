
# HW: Gspread
---
**Purpose:**  
    - Learn how to connect  a google sheet to Python and read the data. You can then manipulate the data in python and update into your google sheet.  
    - Practice using functions and loops with gspread.

---
## Part 1

**Objective**: Create code that will analyze the different subcontractor bids given to you in a google workbook for drywall and concrete scopes. Use python to analyze the bids, then choose a subcontractor bid based on your analysis. Afterward update the Google Workbook with the chosen bid. 

For this example, you have been given bids in a Google Workbood that were submitted for a job and it is your job as the project manager to determine which bid you will choose. 

### Steps
#### Setup
In this section we will authorize our Google account to access the Google Workbook (Steps 1 & 2). Open a the spreadsheet you were given in Colab (Step 4) (actually we will open a copy of the spreadsheet (Step 3)). Then we will read the data from the Google Workbook into the spreadsheet (Step 5). To do this we need to create a variable that represents the Workbook and a variable that represents the sheet in the Workbook we want to read from, this is code you will write (Step 5).  <br>

1. Open this Colab notebook and title it with your name: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit3/01_gspread/HW_Gspread_Starter_Sheet.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Go to the "Imports" code block. Write the proper code to import gspread and authentiate yourself. You can cut-and-paste from previous assignments.

3. Create a copy of the following worksheet and open it by url in the same code block. [Gspread Sample Data](https://docs.google.com/spreadsheets/d/1AtCbzKEuugeq9zCccWDjv9LpaLZX8ftikq6j64JJ1xc/edit?gid=0#gid=0){:target="_blank"}
   <br> You should open and look at the Google Sheet to understand the data you are working with.

4. In the code block titled "Bid Analysis" open the first worksheet in your workbook.

5. Use the .get_all_values() method to pull all the values from your spreadsheet into a list. Input the following code into your notebook:

   ```python
   headers = values1[0]
   rows = values[1:]
   ```
   
   *  Hint: Depending on what you named your values list this code might have to be modified, but the principle is the same.

#### Process the Data from the Worksheet
Now that you have the data from the Google Sheet, you will analyze the bids for the Drywall scope. We need to take the "list of lists" that we read from the Worksheet and convert the strings representing a number e.g., '10' to a number e.g., 10.0. This is harder than it looks because some of the numbers are strings like this $1,000.45. We need remove both the ''$' sign and the comma.''" 

6. Using a for loop, loop through the bid amounts in the rows list and convert the numbers into floats so you can perform an analysis on them.
<br>
   *  Hint: The following code will remove the $ and , in the bid amounts of the Google Sheet so the numbers can be converted correctly:
   ```python
   .replace('$','').replace(',','')
   # replace is a string method, so it works on strings, not lists
   ```

### Extract the Data for Analysis

Now that you have the data in a format that you can work with, you will extract the data for analysis. We  need two lists, one with all the drywall bids and one with all the concrete bids. REmember before we put items in a list, we need to create empty lists (Step 7). Then we will loop through the rows and add the row to the Drywall list if the scope is Drywall or the Concrete list if the associated scope is Concrete (Step 8).

7. Outside of the for loop, create two empty lists. One named Drywall, and the other named Concrete. This is where you will store the different bids.
8. Create a for loop that will loop through the different rows in your Google Sheet and add the row to the Drywall list if the scope is Drywall or the Concrete list if the associated scope is Concrete.

### Analyze the Bids
Now we have two lists, we want to sort the lists (using code we provide , Step 9) so you can compute both the mean and median values fo the drywall bids (Step 10 and 12). We then  remove the most expensive and cheapest bids (Step 11). 

9. Move to the "Drywall Bid Analysis" code block. Line 4 is advanced code that is provided to you for this assignment. It will sort your Drywall list in order from cheapest to most expensive bid.
10. Write code to delete the most expensive and cheapest bid from your list.
11. Write code to find the average cost for the remaining bids in your list.
12. Write code to find the median cost for the remaining bids in your list. 
    * The // operator divides a number and round the result to the lower integer. '''mid_num  = len(Drywall) // 2''' will give you the index of the middle number in the list. Remember that Python is 0-indexed.

### Choose a Bid
Then we step through the bid list and ask the user if they want to accept the remaining bids (Step 13). If the user accepts the bid, we print the bid and end the loop. If the user does not accept the bid, we remove the bid from the list and continue the loop.

13. Now that you understand your bids more, write a while loop that will loop through the remaining bids and ask you as the user if you would like to accept the given bid. If they accept the bid, stop looking, if they do not accept, go to the next bid in the list. <br>
    
    *  If you do want to accept the bid you should print something like: "Bid accepted. Your final bid for Drywall is: <br>
    *  Insert chosen here*." After accepting the bid, you should end the loop. <br>
    *  If you do not want to accept the bid you should remove the bid from your list of bids and continue the loop. <br>
    * * Hint: You can format your number as a currency by using the following code in your input statement with the f formater: 
    ```python
    "${:,.2f}"
    ```
    
### Update the Spreadsheet with the Chosen Bid
Now we will take in the information from the bid we selected, create a new sheet in the workbook, and update the sheet with the selected bidder's information.

14. Write code to add a new sheet to your Google Sheet with the selected bidder's information.

### Repeat the Process for Concrete Bids
If you are careful, you could copy and paste the code you wrote for the Drywall bids and modify it for the Concrete bids. If you want to be a better programmer, you can make several functions that you can call to do the same thing for the Concrete bids as you did for the Drywall bids. Copy-and-paste, with modifications to do concrete is what we expect from this assignment.. 

15. Move to the "Concrete Bid Analysis" code block. Line 4 is the same advanced code given for the Drywall bids.
16. Repeat steps 10-14 for the concrete bids.

---
## Part 2

**Objective**:  You will analyze data to provide estimates for two different client's  material orders.

For this part of the homework, you use the next 3 sheets in the Workbook. One sheet contains the material costs for the items you will be estimating. The other two sheets contain the quantities of materials ordered by two different clients. You will use the material costs to estimate the total cost of the materials for each client.  

### Steps
#### Get the Data
For this section, we need to open the 'Material Cost' sheet (Step 1), and read in the data (Step 2). 

1. In the "Client Estimating Portion" code block open the 'Material Cost' worksheet from your workbook to work with that data.
2. Use the .get_all_values() method to pull all the values from your spreadsheet into a list.

### Client Data
Now we need to open one of the client sheets and read in the data. We will use the data to estimate the cost of the materials for the client. The sheets are called 'Bill of Quantities 1' and 'Bill of Quantities 2'. You can hard code the sheet names in your code. For now just open one of them (Step 3).

3. Create code to open either of the client sheets to get a list of their material orders. Place this in a varible to process later. 

### Function to Estimate Costs
This time, we will create a function that will take in the quantities ordered by the clients and the list of material costs from the Google Sheet. The function will return the quantities needed by the client and the total cost of the estimate. If we do this, we can re-use the function for the other client, and not have to cut-and-paste code everytime.<br>

The function will accept two parameters, one the quantities ordered by the client (Step 3 above) and the list of material costs (Step 1&2 above). The function will do the following: 

- Remove the header row from the quantities list.
- Start an empty list for the quantities needed by the client.
- Create a variable for the total_cost of the estimate that starts at 0.
- Loop through the quantities needed by the client, convert them to floats, and add the waste factor given in the client order.
- For each material, search the list that contains the material cost to find the corresponding cost per unit.
    - If the material is found, pull the cost and convert it into a float.
    - If the material is not found, print a message indicating that the item is missing and move on to the next item in the list.
    - Calculate the material cost by multiplying the quantity with the waste factor by the cost per unit of that item.
    - Add this calculated cost to the total_cost variable.
    - At the end of the loop, store the material name and its total cost as an item in the empty list you created earlier.
    - Your list should grow to be a list of lists, where each list contains the material name and the total cost for that material.
    - Sum all the material costs to get the total cost of the estimate.
    - Print the list of materials and their total costs, then print the final total_cost.
    - Have the function return the quantities list and the total cost from the client_estimation function.

This seems complex, but if you break it down into steps, it is not too hard. We bascially look for a material in the list of materials, if we find it, we calculate the cost and add it to the total cost. If we do not find it, we print a message and move on to the next material. Keep track of things as we go, them sum them up and print everything at the end. <br>

Remember, this is a function so we can call it for each client and not have to re-write the code.

4. Create a function called client_estimation that will take 2 parameters, one for the quantities ordered by the clients and one for the list of materials costs from your Google Sheet. 
   - Your functions have to be defined above the code that calls them. <br>
5. Inside the function do the following:
    - Remove the header row from the quantities list.
    - Start an empty list for the quantities needed by the client.
    - Create a variable for the total_cost of the estimate that starts at 0.
6. Still inside the function, loop through the quantities needed by the client, convert them to floats, and add the waste factor given in the client order.
7. For each material, search the list that contains the material cost to find the corresponding cost per unit.
    - If the material is found, pull the cost and convert it into a float.
    - If the material is not found, print a message indicating that the item is missing and move on to the next item in the list.
8. Calculate the material cost by multiplying the quantity with the waste factor by the cost per unit of that item.
    - Add this calculated cost to the total_cost variable.
    - Store the material name and its total cost as an item in the empty list you created earlier.
9. After looping through all the materials, print the list of materials and their total costs, then print the final total_cost.
10. Return the quantities list and the total cost from the client_estimation function.

### Update the Google Sheet
Now we want to write out this information to the Google Workbook so we can give it to our boss. We will create a new sheet for each client and write the information to the sheet. We are going to write a function again, so we can use it for each client. <br>

To do this we need to open the workbook and create a new sheet for the client. We then write the information to the sheet. The function will take four parameters, the workbook, the client name, the quantities list, and the total cost (Step 11). The function will create a new worksheet named with the client's name, then loop through each of the material costs (from Step 10 above) and add them as rows to the worksheet, then write the total cost from step 10 at the bottom (Step 12). <br>

Next is easly, we call the function for the 1st client and then for the second client. Be careful, you need to check to see if the new workhsheet already exists, if it does, you need to delete it before you create a new one. We provide what the answer should look like in the Google Sheet (Step 15).



11. Create another function called update_sheet that takes four parameters:
    - wb (the workbook you are updating)
    - client (the client's name)
    - quantity (the list of material names and costs)
    - clientcost (the total cost of the order)
12. Inside the update_sheet function:
     - Create a new worksheet in the Google Sheet with the client's name as the title.
     - Loop through the list of materials ancd costs, appending each row to the new worksheet.
     - Append a final row the contains the final total cost for the client's order.
12. Call client_estimation for the first client using the quantities from worksheet 2 and store the results.
13. Call update_sheet to creat a new sheet for the first client and save their estimated costs.
14. Repeat steps 12-13 for the second client using data from the second bill of quantities.
15. If you've completed all the steps correctly, you should get the following answers updated into your Google Sheet for the second bill of quantities:
    
![quantities](https://github.com/user-attachments/assets/10ba9cc7-21de-4fdc-9feb-58aa8ac0500a)

         
---

**Turn sharing and editing on. Turn in the link to BOTH YOUR COLAB NOTEBOOK AND YOUR GOOGLE SHEET on Learning Suite in the feedback box**

---

**Rubric:**

|                                               Gspread                                                     | Points Possible |
|:-------------------------------------------------------------------------------------------------------:|:---------------:|
|                         Part 1 - Correct import and authentication statements                           |        2        |
|                          Part 1 - Bid analysis code block is completed correctly                        |        4        |
|         Part 1 - Drywall Bid Analysis completed correctly with chosen bid updated in Google Sheet       |        4        |
|         Part 1 - Concrete Bid Analysis completed correctly with chosen bid updated in Google Sheet      |        4        |
|                            Part 2 - Correct sheets opened for quantities and costs                      |        3        |
|                               Part 2- client_estimation function written correctly                      |        5        |
|                            Part 2 - update_sheet function written correctly                             |        5        |
|                               Part 2- Correct values updated into Google Sheet                          |        3        |
|                             <div style="text-align: right">**Total**</div>                              |       30        |

The following is not apart of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                      **Reasons for Points Lost**                      | **Amount** |  
|:---------------------------------------------------------------------:|:----------:|
| No comments explaining why AI is used and what its provided code does |    2-3     |
|                        Link shared incorrectly                        |     3      |
|       Turned in late. 10% or 3 points for every week it's late.       |    3-15    |
