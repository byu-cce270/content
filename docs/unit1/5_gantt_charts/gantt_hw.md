# Homework: Gantt Chart and Project Scheduling

## Purpose

Extend the Gantt chart started in class into a schedule for developing a landscape-invoice workbook. The assignment tests whether you can maintain an existing spreadsheet model by adding rows, extending formulas and formatting, and checking the resulting schedule.

Do not start over and do not use a separate homework starter. Open the workbook you completed in class and save a copy as the homework file you will turn in. Save the file before you start making changes, use a new name (follow the standard naming convention). If you start making changes, you might overwrite the in-class file.

## Project Scenario

A landscaping company needs a spreadsheet that can generate client invoices. The proposed spreadsheet would include:

- at least three foliage, soil, and rock materials with unit costs,
- client quantity or area inputs,
- formulas for material costs and invoice totals,
- an input for required person-hours, and
- the labels and checks needed for a clear client invoice.

You are **not** building an invoice workbook. You are planning the work required to build and verify it. You are identifying the tasks required to build the workbook, assigning tasks to your staff, and visualizing the project. You are creating a Gantt chart that represents the project. You can then use the Gantt chart to manage the work (if you did create the workbook)

Assume a three-person team and a two-week project. Use these anonymous role labels:

- `Project Manager`
- `Team Member 2`
- `Team Member 3`

The project starts on the date stored in `project_start`.

## Required Work

### 1. Expand the Class Workbook

Insert enough formatted rows to create three phase rows with three or four task rows under each phase. Insert rows before entering the new formulas and conditional-formatting ranges. Copy the format of an existing phase or task row into each new row.

Possible phases include planning, workbook development, and verification and delivery. You may use different phases if they represent a logical workflow.

<details>
<summary><b>Hint: Why add all rows first?</b></summary>

Adding the final row structure first lets you define formulas and conditional-formatting ranges once. If rows are added later, some formulas or rules may omit them and the displayed chart can become inconsistent with the task data.

</details>

### 2. Define the Work

- Enter three clearly labeled phases.
- Enter three or four specific tasks under each phase, for a total of 9–12 tasks.
- Use WBS numbers and descriptive task names, such as `2.1 Build material-cost formulas`.
- Assign every task in column B to one of the three role labels.
- Assign at least three tasks to each role.
- Record important dependencies in the task name, for example `2.2 Build invoice summary (after 2.1)`. Include dependencies where they affect sequence; do not add one to every task.

The task list should describe how the team would plan, build, test, and deliver the invoice workbook. It should not describe landscaping construction work.

### 3. Schedule the Tasks

- Enter a Monday-through-Friday start date and positive whole-number work-day duration for every task.
- Calculate every task end date with the same `IF`, `OR`, and `WORKDAY` structure used in class.
- Allow tasks to overlap when different team members can work in parallel.
- Calculate phase start dates with `MIN` and phase end dates with `MAX`.
- Calculate each phase's unweighted average task progress with `AVERAGE`.
- Update `F3` so the project-end formula includes every phase and task row.
- Keep the project end no later than 14 calendar days after `project_start`.

<details>
<summary><b>Check the formulas after inserting rows</b></summary>

Select representative task, phase, and project-summary cells and inspect their formulas in the formula bar. Confirm that each range includes all intended rows and does not include tasks from an adjacent phase.

</details>

### 4. Extend the Visual Model

- Extend every conditional-formatting **Applies to** range through the final phase or task row.
- Preserve separate rules for task bars and phase bars.
- Preserve the current-day marker.
- Extend the weekend rule through the final row.
- Enter a progress value for every task. Use 0% for a defined task that has not started; do not use a blank as a substitute for 0%.
- Preserve task progress data bars and phase-average progress values.
- Confirm that the dynamic four-week timeline still responds to `display_week`.

!!! note "Ranges must include the complete model"
    Formulas and formatting can become out of sync when newly inserted rows are outside their source or Applies to ranges. After adding rows, check every phase-summary formula, the project-end formula, and all conditional-formatting ranges.

### 5. Verify the Schedule

Before submitting, make the following tests:

1. Change one task duration and confirm that the task end date, task bar, phase end, phase bar, and project end update.
2. Change `display_week` and confirm that the timeline moves while task dates remain unchanged.
3. Confirm that each Saturday and Sunday is identified correctly.
4. Confirm that the current day is marked when it falls within the displayed four weeks.
5. Check that all 9–12 task rows appear in the chart and in their phase calculations.
6. Confirm that the three team roles have reasonable workloads. A task marked as occurring after a predecessor must start no earlier than the next workday after the predecessor's calculated end date.

## Turning In

!!! note "Do not put your name or NetID in the file"
    Learning Suite records the student who submitted each file. Use the three role labels instead of personal names so the workbook can be graded anonymously.

Upload the completed `.xlsx` file directly to Learning Suite.

1. Save and close the workbook.
2. Upload it to the correct homework assignment.
3. Reopen or preview the uploaded file and confirm that it contains your completed work.

**Rubric:**

| Item | Points Possible |
|:-----|:---------------:|
| Project title, organization, and three role labels are clear | 2 |
| Three phases and 9–12 specific tasks form a complete workflow | 5 |
| Tasks are assigned across the three roles as required | 3 |
| Important dependencies are identified and scheduled logically | 2 |
| Task start, duration, and calculated end dates are correct | 5 |
| Phase dates and the calculated project end are correct | 4 |
| Project fits within the two-week limit | 1 |
| Dynamic timeline and `display_week` control are functional | 3 |
| Task and phase bars are correct and visually distinct | 3 |
| Task progress, data bars, and phase averages are correct | 3 |
| Current-day and weekend formatting are functional | 1 |
| Headers and layout are readable | 1 |
| **Total** | **33** |

The following deductions are separate from the rubric.

| Reason for Points Lost | Amount |
|:-----------------------|:------:|
| File uploaded incorrectly | -10% |
| Turned in late, per week | -10% up to -50% |
