# HW: Pivot Tables & Query

**Purpose:** Learn how to use pivot tables and query functions to summarize data.

## Instructions
1. First make a copy of the starter sheet here:
   [Starter Sheet - HW Pivot Tables & Query](https://docs.google.com/spreadsheets/d/1pGdgsPzEM5ut-0GVPKQJ8Kz7nSL1OHsaVC_KOrr0MKk/edit?usp=sharing){:target="_blank"}
2. Rename it something like "[Your Name] HW Pivot Tables & Query"
 
---

#### Part 1
3. Navigate to the **2021_med_claims** sheet.
4. Create a query in cell **A1** that references the safety data in the Data sheet that returns the columns **Date**, **Plant**,
   **Shift**, and **Department**.
5. Find all incidents in 2021 involving a medical claim (hint: look in column H).
6. Sort the results by plant.

---

#### Part 2
7. Navigate to the **days_lost_claims** sheet.
8. Create a query in cell **A1** that references the safety data in the Data sheet that returns the columns **Incident 
   Type**, **Days Lost**, **Age Group**, **Gender**, and **Incident Cost**.
9. Find all incidents where the number of days lost > 0 and the incident cost > 0.
10. List the results in reverse order by cost (highest to lowest).

---

#### Part 3
11. Create a pivot table that references the incident data found in the Data tab. The table should include Month and Year columns.
12. For each year/month combo, include a count of the number of incidents during that time and a sum of the incident cost.

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

|                           Item (Pivot Tables)                             | Points Possible |
|:-------------------------------------------------------------------------:|:---------------:|
|                  Pivot table is created on a new sheet                    |        2        |
|               Table created using the data in the Data tab                |        2        |
|                 Table includes month and year columns                     |        2        |
|        Column created showing the count of the number of incidents        |        4        |
|            Column created showing the sum of the incident cost            |        4        |
|  <div style="text-align: right">**Total**</div>                           |       14        |
