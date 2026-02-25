#  HW: Introduction to Classes

**Objective:** Learn how to create and use classes, add methods, validate input, and practice inheritance.

In this assignment, you will complete a three-part exercise. In Part 1, you will create a **Material** class for tracking construction materials. In Part 2, you will create a **ConstructionProject** class that manages a project with multiple materials and labor costs. In Part 3, you will use inheritance to create a **RoadProject** class that extends **ConstructionProject** with road-specific attributes and methods.

## Getting Started

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit2/06_classes/(Starter_Workbook)_HW_Intro_Classes.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

2. Rename it something like "(Your_Name)_HW_Intro_Classes.ipynb".

---

## Part 1 - Material Class

In this part, you will create a class called **Material** that represents a construction material (e.g., concrete, rebar, lumber). This class will track the material's name, cost, unit of measurement, and quantity.

1. In Code Block 1, define a class called **Material** with an **\_\_init\_\_** method that takes the following parameters:

    | Parameter       | Description                              | Default |
    |:---------------:|:----------------------------------------:|:-------:|
    | **name**        | Name of the material (e.g., "Concrete")  | None    |
    | **unit_cost**   | Cost per unit (e.g., 125.00)             | None    |
    | **unit**        | Unit of measure (e.g., "cubic yards")    | None    |
    | **quantity**    | Amount of material on hand               | 0       |

2. Add **validation** in the **\_\_init\_\_** method:
    - If **unit_cost** is less than or equal to 0, print an error message and set **unit_cost** to 1.
    - If **quantity** is less than 0, print an error message and set **quantity** to 0.

3. Add a method called **total_cost()** that returns **unit_cost \* quantity**.

4. Add a method called **add_quantity(amount)** that adds the given amount to the current quantity. If the amount is less than or equal to 0, print an error message and do not change the quantity.

5. Add a method called **use_quantity(amount)** that subtracts the given amount from the current quantity. If the amount is greater than the current quantity, print an error message that includes the material name and current quantity, and do not change the quantity. If the amount is less than or equal to 0, print an error message.

6. Add a **print_description** method that returns a formatted string like:

```
Concrete: 50 cubic yards @ $125.00/cubic yards = $6,250.00
```

7. Test your **Material** class in the Code Block 1 Test cell by doing the following:
   - Create a material and print it.
   - Add quantity using the **add_quantity()** method and print it. 
   - Use quantity using the **use_quantity()** method and print it.
   - Try to use more quantity than available with the **use_quantity()** method.
   
   Your output should look similar to this:

```
Concrete: 50 cubic yards @ $125.00/cubic yards = $6,250.00
After adding 20: Concrete: 70 cubic yards @ $125.00/cubic yards = $8,750.00
After using 30: Concrete: 40 cubic yards @ $125.00/cubic yards = $5,000.00
Error: Not enough Concrete available. Current quantity: 40 cubic yards.
```

---

## Part 2 - ConstructionProject Class

In this part, you will create a class called **ConstructionProject** that manages a construction project. It will use **Material** objects from Part 1 to track materials and calculate costs.

1. In Code Block 2, define a class called **ConstructionProject** with an **\_\_init\_\_** method that takes the following parameters:

    | Parameter          | Description                         | Default |
    |:------------------:|:-----------------------------------:|:-------:|
    | **project_name**   | Name of the project                 | None    |
    | **budget**         | Total project budget in dollars     | None    |
    | **labor_rate**     | Labor cost per hour in dollars      | None    |

2. In **\_\_init\_\_**, also initialize the following attributes:
    - **materials** as an empty list (this will hold Material objects)
    - **hours_worked** as 0

3. Add a method called **add_material(material)** that appends a **Material** object to the **materials** list.

4. Add a method called **log_hours(hours)** that adds hours to **hours_worked**. If hours is less than or equal to 0, print an error message.

5. Add a method called **total_material_cost()** that loops through all materials in the **materials** list and returns the sum of each material's **total_cost()**.

6. Add a method called **total_labor_cost()** that returns **labor_rate \* hours_worked**.

7. Add a method called **total_project_cost()** that returns the sum of **total_material_cost()** and **total_labor_cost()**.

8. Add a method called **is_under_budget()** that returns **True** if **total_project_cost()** is less than or equal to **budget**, and **False** otherwise.

9. Add a method called **summary()** that prints a formatted project summary. The summary should include:
    - Project name and budget
    - A list of all materials (use each material's **\_\_str\_\_** method)
    - Total material cost
    - Labor hours, rate, and total labor cost
    - Total project cost
    - Remaining budget (budget minus total project cost)
    - Whether the project is under or over budget

10. Test your **ConstructionProject** class in the Code Block 2 Test cell by doing the following:
    - Create three materials (concrete, rebar, and lumber) using the **Material** class.
    - Create a project using the **ConstructionProject** class you just created.
    - Add the three materials to the project using the **add_material()** method.
    - Log hours using the **log_hours()** method.
    - Print the summary using the **summary()** method.
    
    Use the following test data:

     | Material   | Unit Cost | Unit         | Quantity |
     |:----------:|:---------:|:------------:|:--------:|
     | Concrete   | 125.00    | cubic yards  | 50       |
     | Rebar      | 0.85      | lbs          | 5000     |
     | Lumber     | 6.50      | board feet   | 2000     |

     | Project               | Budget      | Labor Rate | Hours  |
     |:---------------------:|:-----------:|:----------:|:------:|
     | Campus Parking Garage | 500,000.00  | 45.00      | 1200   |

Your output should look similar to this:

```
--- Project Summary: Campus Parking Garage ---
Budget: $500,000.00
Materials:
  - Concrete: 50 cubic yards @ $125.00/cubic yards = $6,250.00
  - Rebar: 5000 lbs @ $0.85/lbs = $4,250.00
  - Lumber: 2000 board feet @ $6.50/board feet = $13,000.00
Total Material Cost: $23,500.00
Labor: 1200 hours @ $45.00/hr = $54,000.00
Total Project Cost: $77,500.00
Remaining Budget: $422,500.00
Status: UNDER BUDGET
```

---

## Part 3 - RoadProject (Inheritance)

In this part, you will create a class called **RoadProject** that **inherits** from **ConstructionProject**. This class adds road-specific attributes and methods while reusing all the functionality from the parent class.

1. In Code Block 3, define a class called **RoadProject** that inherits from **ConstructionProject**. The **\_\_init\_\_** method should take the following parameters:

    | Parameter          | Description                              | Default |
    |:------------------:|:----------------------------------------:|:-------:|
    | **project_name**   | Name of the road project                 | None    |
    | **budget**         | Total project budget in dollars          | None    |
    | **labor_rate**     | Labor cost per hour in dollars           | None    |
    | **length_miles**   | Length of the road in miles              | None    |
    | **num_lanes**      | Number of lanes                          | None    |

    Use **super().\_\_init\_\_()** to call the parent class constructor with **project_name**, **budget**, and **labor_rate**. Then set **length_miles** and **num_lanes** as additional attributes.

2. Add a method called **cost_per_mile()** that returns the total project cost divided by **length_miles**.

3. Add a method called **cost_per_lane_mile()** that returns **cost_per_mile()** divided by **num_lanes**.

4. **Override** the **summary()** method to print a road-specific summary. It should include everything from the original summary plus:
    - Road length and number of lanes
    - Cost per mile
    - Cost per lane-mile

5. Test your **RoadProject** class in the Code Block 3 Test cell by doing the following: 
    - Create three materials (asphalt, gravel, and rebar) using the **Material** class.
    - Create a road project using the inherited **RoadProject** class.
    - Add the three materials to the project using the **add_material()** method.
    - Log hours using the **log_hours()** method.
    - Print the summary using the **summary()** method.
    
    Use the following test data:

    | Material   | Unit Cost | Unit  | Quantity |
    |:----------:|:---------:|:-----:|:--------:|
    | Asphalt    | 95.00     | tons  | 800      |
    | Gravel     | 28.00     | tons  | 1500     |
    | Rebar      | 0.85      | lbs   | 20000    |

    | Project                 | Budget       | Labor Rate | Hours | Length | Lanes |
    |:-----------------------:|:------------:|:----------:|:-----:|:------:|:-----:|
    | Highway 89 Expansion    | 2,000,000.00 | 52.00      | 5000  | 3.5    | 4     |

Your output should look similar to this:

```
--- Road Project Summary: Highway 89 Expansion ---
Road: 3.5 miles, 4 lanes
Budget: $2,000,000.00
Materials:
  - Asphalt: 800 tons @ $95.00/tons = $76,000.00
  - Gravel: 1500 tons @ $28.00/tons = $42,000.00
  - Rebar: 20000 lbs @ $0.85/lbs = $17,000.00
Total Material Cost: $135,000.00
Labor: 5000 hours @ $52.00/hr = $260,000.00
Total Project Cost: $395,000.00
Cost per Mile: $112,857.14
Cost per Lane-Mile: $28,214.29
Remaining Budget: $1,605,000.00
Status: UNDER BUDGET
```

!!! Note
    While this problem can be solved using AI, we strongly encourage you to first attempt to write it without AI. If you get stuck, you may use AI tools like ChatGPT or Gemini (the AI inside Colab notebooks) to help you debug or complete these classes. If you do use AI tools, be sure to examine the code provided by the AI tool and try to understand how it works. Add comments to the code to explain what each part of the code does.

---

## Turning in/Rubric

**_REMINDER_** - For this class, **you will only turn in the links to your colab notebooks**. You will get a 0 for this assignment if you turn in a python file or a link that is not correct, wrong assignment, or does not give editor permission.

**Rubric:**

|                          **Item**                           | **Amount** |
|:-----------------------------------------------------------:|:----------:|
|    Material **\_\_init\_\_** with validation is correct     |     2      |
|           **total_cost()** method works correctly           |     2      |
|          **add_quantity()** method works correctly          |     2      |
|     **use_quantity()** with validation works correctly      |     2      |
|    **project_description** method returns formatted string    |     2      |
|       ConstructionProject **\_\_init\_\_** is correct       |     2      |
|    **add_material()** and **log_hours()** work correctly    |     2      |
|     **total_material_cost()** loops and sums correctly      |     2      |
| **total_labor_cost()** and **total_project_cost()** correct |     2      |
|        **is_under_budget()** returns correct boolean        |     1      |
|            **summary()** prints formatted output            |     3      |
|        RoadProject inherits from ConstructionProject        |     2      |
|          **super().\_\_init\_\_()** used correctly          |     2      |
|  **cost_per_mile()** and **cost_per_lane_mile()** correct   |     2      |
|     **summary()** override includes road-specific info      |     3      |
|       <div style="text-align: right">**Total**</div>        |   **31**   |

---

The following is not a part of the rubric, but specifies how you can lose points. For example: if you do not explain your code when using AI to help you create it or fail to share your link correctly.

|                       **Reasons for Points Lost**                       |    **Amount**     |
|:-----------------------------------------------------------------------:|:-----------------:|
|                         Link shared incorrectly                         |       -10%        |
|                        Turned in late (per week)                        | -10% (up to -50%) |
| No comments explaining where AI is used and what its provided code does |       -50%        |
