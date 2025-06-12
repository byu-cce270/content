# Exercise - Employee Data

The following exercise is based on the Pivot Table and Query Functions we have just covered. For this exercise, open the in-class workbook, make a copy, and follow the instructions.

You can find the Employee Data starter sheet here: [Pivot Tables/Query Starter Sheet](https://docs.google.com/spreadsheets/d/19msUPf9DYVBAMNnoIhYO6RMpdSlKobbJM3Ul7W-qiCU/edit?usp=sharing){:target="_blank"}.

## Instructions
1. Navigate to the **high_salary** sheet.
2. Create a query in cell **A1** that references the employee data in the data sheet that finds all incidents involving 
   employees earning over $150,000 per year and returns 
   the columns (Full Name, Job Title, Department, Business Unit, Gender, and Annual Salary). Structure the query so that the results are sorted by salary in descending order.
3. Navigate to the **senior_us_employees** sheet.
4. Create a query in cell **A1** that references the employee data in the data sheet that returns all active employees 
   in the United States that have worked for the company for at least 20 years. Return the following columns 
   (EEID, Full Name, Job Title, Hire Date, Age, and Yrs Since Hire) and sort the results by hire date.

    **HINT**: An employee is active if the value in the Exit Date column is empty. Sometimes we can check for an empty value with (N = ") but in this case you have to use (N is null) because it is a date field.

5. Navigate to the sheet titled "Pivot Table" and create a pivot table that includes the Job Title and Department rows.
6. Using the pivot table just created, provide a count of the number of people with each job title and calculate the average salary for each job title.

## Turning in/Rubric
Turn sharing and editing on, then submit the link to Learning Suite in the feedback box. In-class assignment scores are based on valid effort and completion.
