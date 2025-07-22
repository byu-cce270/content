# HW: Pivot Tables & Query

**Purpose:** Learn how to use pivot tables and query functions to summarize data.

## Instructions
1. First make a copy of the starter sheet here:
   [Starter Sheet - HW Pivot Tables & Query](https://docs.google.com/spreadsheets/d/1__eHBgjb9pZAlpfAtQ35LTMt8a-BroQ79vLmHEwzdzU/edit?gid=0#gid=0){:target="_blank"}
2. Rename it something like "[Your Name] HW Pivot Tables & Query"
 
---

#### Part 1
1. Navigate to the **2021_med_claims** sheet.
2. Create a query in cell **A1** that references the safety data in the Data sheet that returns the columns **Date**, **Plant**,
   **Shift**, and **Department**.
3. Find all incidents in 2021 involving a medical claim (hint: look in column H).
4. Sort the results by plant.

---

#### Part 2
1. Navigate to the **days_lost_claims** sheet.
2. Create a query in cell **A1** that references the safety data in the Data sheet that returns the columns **Incident 
   Type**, **Days Lost**, **Age Group**, **Gender**, and **Incident Cost**.
3. Find all incidents where the number of days lost > 0 and the incident cost > 0.
4. List the results in reverse order by cost (highest to lowest).

---

#### Part 3

In this part, you will create a pivot table that summarizes the incident data found in the Data tab. We will 
be checking to see if there are any noticeable trends in the accident data relative to gender and age group.

1. Create a pivot table on the **pivot_table_1** sheet that references the incident data found in the **data** tab. 
2. Use the **Rows|Add** feature to add a row for the **Gender** and then **Age Group** fields.
2. Use the **Values|Add** feature to add a value for the **Days Lost** (Average) and **Incident Cost** (Average) fields. 

Are there any noticeable trends in the data?

**FULL DISCLOSURE**: This is a fake dataset and the data is not real.

---

### Part 4

In this part, we want you to create another pivot in the **pivot_table_2** sheet, but in this case we want you to 
examine the data and create a pivot table that explores data correlations that **YOU** find interesting. Make sure to 
use at least two combinations of fields in the **Rows** section and at least two combinations of fields in the **Values** 
section.

For example, are there are plants that have more incidents than others? What are the more common incident types?

---

## Submission/Rubric
Turn sharing and editing on. Turn in the link to Learning Suite in the feedback box.

---

**Rubric**

|                              Item (Query)                              | Points Possible |
|:----------------------------------------------------------------------:|:---------------:|
|          Query is created in cell A1 on 2021_med_claims sheet          |        2        |
|      Query returns the Date, Plant, Shift, and Department columns      |        2        |
|           All incidents involving a medical claim were found           |        2        |
|                      Results are sorted by plant                       |        2        |
|         Query is created in cell A1 on days_lost_claims sheet          |        2        |
|       Query returns the 5 columns specified in the instructions        |        2        |
| All incidents where # of days lost > 0 and incident cost >0 were found |        2        |
|              Results are sorted in reverse order by cost               |        2        |
|             <div style="text-align: right">**Total**</div>             |       16        |

|                            Item (Pivot Tables)                            | Points Possible |
|:-------------------------------------------------------------------------:|:---------------:|
|                   Pivot table is created on a new sheet                   |        2        |
|               Table created using the data in the Data tab                |        2        |
|                   Table includes month and year columns                   |        2        |
|        Column created showing the count of the number of incidents        |        4        |
|            Column created showing the sum of the incident cost            |        4        |
|              <div style="text-align: right">**Total**</div>               |       14        |

The following is not a part of the rubric, but specifies how you can lose points. For example: if you fail to share your link correctly.

|                      **Reasons for Points Lost**                      | **Amount** |  
|:---------------------------------------------------------------------:|:----------:|
|                        Link shared incorrectly                        |     3      |
|       Turned in late. 10% or 3 points for every week it's late.       |    3-15    |
