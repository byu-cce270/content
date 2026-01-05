# Unit 3 Midterm Exam Study Guide

The final exam will be comprensive, but will feature a significan amount of content from Unit 3. This study guide is designed to help you review and prepare for the Unit 3 content on the exam. It includes a summary of core concepts, a practice quiz with answers, and a glossary of key terms.

!!! Note
    This study guide is not exhaustive. Be sure to review the course reading content, in-class exercises, homework assignments, and any additional materials provided by your instructor.

## Core Concepts Summary

This section provides a detailed summary of the key concepts, procedures, and functions covered in the course materials.

### NumPy

#### Chapter 5: The Basics of NumPy Arrays

This chapter introduces NumPy arrays, the foundation for data manipulation in Python.

* **Core Idea**: Data manipulation in Python, including with tools like Pandas, is built around the NumPy array.
* **Array Attributes**: Used to determine the characteristics of an array.
    * **ndim**: The number of dimensions.
    * **shape**: A tuple indicating the size of each dimension.
    * **size**: The total number of elements in the array.
    * **dtype**: The data type of the array elements (e.g., int64, float64).
* **Array Indexing**: Accessing single elements.
    * One-dimensional: Use square brackets **[]** with a zero-based index. Negative indices access elements from the end of the array.
    * Multi-dimensional: Use a comma-separated tuple of indices **[row, column]**.
    * Type Coercion: NumPy arrays have a fixed type. Assigning a float to an integer array will result in the value being silently truncated.
* **Array Slicing**: Accessing subarrays.
    * Syntax: **x[start:stop:step]**. Defaults are start=0, stop=size of dimension, step=1.
    * One-dimensional: Slicing creates subarrays. A negative step value reverses the array.
    * Multi-dimensional: Use comma-separated slices **[:2, :3]** (first two rows, first three columns). A single colon **:** is an empty slice that selects all elements in that dimension.
    * Views vs. Copies: NumPy array slices are views of the original array, not copies. Modifying a slice will change the original array. To create a copy, use the **.copy()** method.
* **Reshaping of Arrays**: Changing an array's shape.
    * **.reshape()**: Method to change the shape, e.g., **.reshape(3, 3)** for a 3x3 grid.
    * **np.newaxis**: A convenient way to convert a 1D array into a 2D row or column vector, e.g., **x[:, np.newaxis]** creates a column vector.
* **Joining and Splitting of Arrays**:
    * Concatenation:
        * **np.concatenate()**: Joins a sequence of arrays along a specified axis (axis=1 for column-wise).
        * **np.vstack()**: Stacks arrays vertically (row-wise).
        * **np.hstack()**: Stacks arrays horizontally (column-wise).
    * Splitting:
        * **np.split()**: Splits an array into multiple subarrays at specified indices. N split points result in N + 1 subarrays.
        * **np.hsplit()**: Splits an array horizontally.
        * **np.vsplit()**: Splits an array vertically.
#### Chapter 6: Computation on NumPy Arrays: Universal Functions

This chapter covers vectorized operations and universal functions that make NumPy computations fast and efficient.

* **Core Idea**: Vectorized operations, implemented through NumPy's universal functions (ufuncs), are significantly faster than Python loops for computations on arrays.
* **The Slowness of Loops**: Python's dynamic, interpreted nature (CPython) involves type-checking and function dispatches in each loop cycle, making it slow for large-scale numerical operations. Vectorized operations push the loop into the compiled layer of NumPy for massive speed gains.
* **Universal Functions (Ufuncs)**:
    * Definition: Functions that perform efficient, element-wise operations on values in NumPy arrays.
    * Types:
        * Unary ufuncs: Operate on a single input (e.g., **np.negative**, **np.abs**).
        * Binary ufuncs: Operate on two inputs (e.g., **np.add**, **np.multiply**).
* **Available Ufuncs**:
    * Array Arithmetic: Standard operators **+**, **-**, **\***, **/**, **//** , **\*\***, **%** are wrappers for ufuncs like **np.add**, **np.subtract**, etc.
    * Absolute Value: **abs()** or **np.absolute()** (**np.abs**).
    * Trigonometric Functions: **np.sin**, **np.cos**, **np.tan**, and their inverses (**np.arcsin**, etc.).
    * Exponents and Logarithms: **np.exp** (e), **np.exp2** (2^x), **np.power** (general exponentiation), **np.log** (natural log), **np.log2**, **np.log10**. Specialized versions like **np.expm1** and **np.log1p** maintain precision for very small inputs.
    * Specialized Ufuncs: Found in **scipy.special** (e.g., Gamma functions, error functions).
* **Advanced Ufunc Features**:
    * Specifying Output: The **out** argument allows you to specify an array where the result of the calculation is stored, saving memory by avoiding temporary arrays.
    * Aggregations:
        * **.reduce()**: Repeatedly applies an operation to the elements of an array until a single result remains (e.g., **np.add.reduce(x)** is equivalent to **np.sum(x)**).
        * **.accumulate()**: Stores all intermediate results of the computation (e.g., **np.add.accumulate(x)** is equivalent to **np.cumsum(x)**).
    * Outer Products: The **.outer()** method computes the output for all pairs of two different inputs, useful for creating tables like a multiplication table.
### Matplotlib

#### Chapter 15: Generating Data (and Plotting with Matplotlib)

This chapter introduces Matplotlib, Python's primary library for creating data visualizations.

* **Core Idea**: Matplotlib is a mathematical plotting library for creating data visualizations like line graphs and scatter plots.
* **Installation**: Use **pip install --user matplotlib**.
* **Plotting a Simple Line Graph**:
    * Import the library: **import matplotlib.pyplot as plt**.
    * Create a figure and axes: **fig, ax = plt.subplots()**. **fig** is the entire figure; **ax** is a single plot.
    * Plot data: **ax.plot(input_values, squares)**. If only one list is provided, it's treated as y-values with an implicit x-index starting at 0.
    * Display the plot: **plt.show()**.
* **Customization**:
    * Line Thickness: **linewidth** parameter in **ax.plot()**.
    * Titles and Labels: **ax.set_title()**, **ax.set_xlabel()**, **ax.set_ylabel()**. **fontsize** parameter controls text size.
    * Tick Marks: **ax.tick_params(labelsize=14)**.
    * Styles: Use pre-defined styles for aesthetics: **plt.style.use('seaborn')**.
* **Scatter Plots with scatter()**:
    * Plot a series of points: **ax.scatter(x_values, y_values, s=100)**. The **s** argument controls point size.
    * Custom Colors: Use the **color** argument with a color name (e.g., **'red'**) or an RGB tuple (e.g., **(0, 0.8, 0)**).
    * Colormaps: Use a gradient of colors to represent data values. Pass a list of values to the **c** argument and specify the colormap with **cmap** (e.g., **c=y_values, cmap=plt.cm.Blues**).
* **Axis Range**: Set axis limits with **ax.axis([xmin, xmax, ymin, ymax])**.
* **Saving Plots**: Save a figure to a file using **plt.savefig('filename.png', bbox_inches='tight')**. The **bbox_inches='tight'** argument trims extra whitespace.
#### Chapter 25: General Matplotlib Tips

This chapter provides essential tips and conventions for working with Matplotlib effectively.

* **Standard Imports**: **import matplotlib as mpl**, **import matplotlib.pyplot as plt**.
* **Showing Plots**:
    * In a Script: Use **plt.show()** at the end of the script to open an interactive window.
    * In IPython Shell: Use **%matplotlib** magic command to enable interactive mode.
    * In Jupyter Notebook:
        * **%matplotlib inline**: Embeds static plot images directly in the notebook.
        * **%matplotlib notebook**: Embeds interactive plots in the notebook.
* **Saving Figures**: The **fig.savefig('my_figure.png')** method saves the figure. The file format is inferred from the extension.
* **Two Interfaces**:
    * MATLAB-style (State-based): Uses **plt** functions (**plt.plot**, **plt.subplot**) that act on the "current" active figure and axes. Convenient for simple plots.
    * Object-oriented: Explicitly create and operate on Figure and Axes objects (**fig, ax = plt.subplots(); ax[0].plot(...)**). More powerful and flexible for complex plots.
#### Chapter 26: Simple Line Plots

This chapter covers the fundamentals of creating and customizing line plots in Matplotlib.

* **Figure and Axes**: A **plt.Figure** is the container for all plot elements. A **plt.Axes** is the bounding box with ticks and labels where data is plotted.
* **Plotting**: Use **ax.plot(x, y)** to create a line plot on a specific Axes object. Multiple calls to **.plot()** will overlay lines on the same axes.
* **Line Colors and Styles**:
    * **color**: Can be specified by name (**'blue'**), short code (**'g'**), grayscale (**'0.75'**), hex code (**'#FFDD44'**), RGB tuple (**1.0, 0.2, 0.3**), or HTML name (**'chartreuse'**).
    * **linestyle**: Can be specified by name (**'solid'**, **'dashed'**) or code (**'-'**, **'--'**).
    * Shorthand: A combined string can set style, color, and marker: **'-g'** for a solid green line.
* **Axes Limits**:
    * **plt.xlim()** and **plt.ylim()** set limits for x and y axes.
    * **plt.axis()**: A related method.
        * **plt.axis('tight')**: Tightens bounds around the data.
        * **plt.axis('equal')**: Sets an equal aspect ratio.
* **Plot Labels**:
    * **plt.title()**, **plt.xlabel()**, **plt.ylabel()**.
    * Object-oriented equivalents start with **set_**: **ax.set_title()**, **ax.set_xlabel()**, etc. The **ax.set()** method can set multiple properties at once.
* **Legends**:
    * **plt.legend()** creates a legend.
    * Use the **label** keyword in plot calls to define legend entries: **plt.plot(x, y, label='my line')**.
#### Chapter 27: Simple Scatter Plots

This chapter covers scatter plots, which are useful for visualizing relationships between two numerical variables.

* **Using plt.plot**: A scatter plot can be made with **plt.plot** by providing a marker style character (e.g., **'o'**, **'.'**, **'x'**) instead of a line style.
* **Using plt.scatter**: A more powerful function for creating scatter plots.
    * Key Advantage: Allows properties of each individual point (size, color, transparency) to be controlled or mapped to data.
    * Arguments:
        * **c**: Maps point color to data values. Use with **plt.colorbar()** to show the color scale.
        * **s**: Maps point size to data values.
        * **alpha**: Adjusts the transparency level.
    * Efficiency Note: For large datasets (> few thousand points), **plt.plot** is more efficient than **plt.scatter** because scatter must render each point individually.
* **Error Bars**:
    * **plt.errorbar(x, y, yerr=dy, fmt='.k')**: Creates a plot with error bars. **yerr** specifies the error size. **fmt** controls point/line appearance.
    * Customization: Can change **ecolor**, **elinewidth**, **capsize**, etc.
* **Continuous Errors**: Use **plt.fill_between(x, y_lower, y_upper)** to show a continuous error region, useful for things like Gaussian process regression fits.
#### Chapter 29: Customizing Plot Legends

This chapter explains how to create and customize legends to make plots more informative and professional.

* **Simple Creation**: **ax.legend()** automatically creates a legend for any plot elements with a label.
* **Customization**:
    * **loc**: Specifies location (e.g., **'upper left'**).
    * **frameon**: Toggles the legend frame.
    * **ncol**: Sets the number of columns.
    * **fancybox**, **shadow**, **framealpha**, **borderpad**: Control aesthetic properties.
* **Choosing Legend Elements**:
    * The legend includes all elements with a label attribute.
    * Alternatively, pass a list of line objects and a list of labels to **plt.legend()**: **plt.legend(lines[:2], ['first', 'second'])**.
* **Legends for Point Size**: Create a legend for features like point size by plotting "fake" data (empty lists) with the desired marker size and a label.
* **Multiple Legends**: Matplotlib only supports one legend per axes by default. To add more, you must create a new Legend artist from scratch and manually add it to the axes using **ax.add_artist(leg)**.
#### Chapter 32: Text and Annotation

This chapter covers adding text and annotations to plots for better communication of insights.

* **Adding Text**: Use **ax.text(x, y, "My Text", ...)** to place text at a specific data coordinate. Keywords like **ha** (horizontal alignment) and style dictionaries control appearance.
* **Coordinate Systems (Transforms)**:
    * **ax.transData**: Default. Coordinates are tied to the data.
    * **ax.transAxes**: Position is specified as a fraction of the axes size (from 0 to 1), independent of data limits.
    * **fig.transFigure**: Position is specified as a fraction of the figure size.
* **Annotation with Arrows**:
    * **ax.annotate('text', xy=(x, y), xytext=(tx, ty), arrowprops=dict(...))**.
    * **xy**: The point to annotate (data coordinates).
    * **xytext**: The position of the text.
    * **arrowprops**: A dictionary controlling the arrow's appearance (e.g., **facecolor**, **shrink**, **arrowstyle**, **connectionstyle**). This is highly flexible but often requires manual tweaking.
### Introduction to Pandas

#### Chapter 13: Introducing Pandas Objects

This chapter introduces the core data structures in Pandas: Series, DataFrame, and Index objects.

* **Core Idea**: Pandas objects are like enhanced NumPy arrays where rows and columns are identified by labels instead of just integer indices.
* **The Series Object**:
    * A one-dimensional array of indexed data.
    * Combines a sequence of values with an index.
    * As a NumPy Array: The values are a NumPy array. Can be accessed via integer index slicing (**data[1:3]**). The key difference is the explicit index in Pandas vs. the implicit index in NumPy.
    * As a Dictionary: Maps typed keys (the index) to a set of typed values. Can be created from a dictionary. Supports dictionary-style access (**data['b']**) and slicing on the explicit index (**data['a':'c']**).
    * Construction: **pd.Series(data, index=index)**.
* **The DataFrame Object**:
    * A two-dimensional array with both explicit row and column indices.
    * As a NumPy Array: Can be seen as an analog of a 2D array. The **.values** attribute returns the underlying NumPy data.
    * As a Dictionary of Series: A collection of Series objects that share the same index. Indexing with a column name (**data['area']**) returns a Series.
    * Construction: Can be created from a single Series, a list of dictionaries, a dictionary of Series, a 2D NumPy array, or a NumPy structured array.
* **The Index Object**:
    * An object that holds the axis labels for Series and DataFrame objects.
    * As an Immutable Array: Behaves like an array (supports indexing and slicing) but cannot be modified. This immutability makes it safe to share indices.
    * As an Ordered Set: Supports set operations like intersection (**.intersection()**), union (**.union()**), and symmetric difference (**.symmetric_difference()**).
#### Chapter 14: Data Indexing and Selection

This chapter covers the various methods for selecting and accessing data in Pandas Series and DataFrames.

* **Selection in Series**:
    * Acts like both a dictionary (using explicit index labels) and a NumPy array (using implicit integer indices).
    * Slicing Quirk: When slicing with an explicit index (**data['a':'c']**), the final index is included. When slicing with an implicit index (**data[0:2]**), the final index is excluded.
    * Indexers **loc** and **iloc**:
        * **data.loc[...]**: Always refers to the explicit index.
        * **data.iloc[...]**: Always refers to the implicit, Python-style integer index.
* **Selection in DataFrame**:
    * As a Dictionary: Indexing a single column name (**data['area']**) selects a Series. Attribute-style access (**data.area**) also works but can conflict with DataFrame methods.
    * As a 2D Array:
        * **data.iloc[...]**: Accesses data by implicit integer index for both rows and columns (**data.iloc[:3, :2]**).
        * **data.loc[...]**: Accesses data by explicit index for rows and columns (**data.loc[:'Florida', :'pop']**).
    * Additional Conventions:
        * Slicing: Direct slicing (**data[1:3]**) refers to rows.
        * Masking: Direct masking (**data[data.density > 120]**) is interpreted row-wise.
### Continuing with Pandas

#### Chapter 18: Combining Datasets: concat and append

This chapter covers methods for combining multiple DataFrames or Series into a single structure.

* **pd.concat()**: The primary function for simple concatenation of Series and DataFrame objects.
    * Behavior: Stacks objects along an axis (default is axis=0, row-wise).
    * Duplicate Indices: Pandas concatenation preserves indices, which can result in duplicates.
        * **verify_integrity=True**: Raises an exception if there are duplicate indices.
        * **ignore_index=True**: Creates a new integer index for the result.
        * **keys=[...]**: Creates a hierarchical index (MultiIndex) to distinguish the original data sources.
    * Concatenation with Joins: When concatenating DataFrames with different columns:
        * **join='outer'** (default): Creates a union of the columns, filling missing values with NaN.
        * **join='inner'**: Creates an intersection of the columns.
* **The .append() Method**:
    * A shortcut for **pd.concat(axis=0)**.
    * It does not modify the original object but creates a new one.
    * It is less efficient than a single concat call on a list of DataFrames.
#### Chapter 19: Combining Datasets: merge and join

This chapter covers database-style joins for combining DataFrames based on common keys.

* **Core Idea**: **pd.merge** implements high-performance, in-memory, database-style joins based on relational algebra.
* **Categories of Joins**:
    * One-to-one: Each key appears exactly once in each DataFrame.
    * Many-to-one: A key appears multiple times in one DataFrame and once in the other.
    * Many-to-many: A key appears multiple times in both DataFrames.
* **Specifying the Merge Key**:
    * Implicitly: **pd.merge** automatically uses column names that are common to both DataFrames.
    * **on**: Explicitly specify the key column name(s).
    * **left_on** and **right_on**: Specify key column names when they differ between the DataFrames.
    * **left_index=True** and **right_index=True**: Merge on the DataFrame indices.
    * **.join()** method: A convenience for performing an index-based merge.
* **Set Arithmetic for Joins (the how keyword)**:
    * **how='inner'** (default): Intersection of keys.
    * **how='outer'**: Union of keys. Fills missing data with NaN.
    * **how='left'**: Uses keys from the left DataFrame only.
    * **how='right'**: Uses keys from the right DataFrame only.
* **Overlapping Column Names**: If DataFrames have non-key columns with the same name, **pd.merge** appends **_x** and **_y** by default. This can be customized with the **suffixes** keyword.
#### Chapter 20: Aggregation and Grouping

This chapter covers aggregation operations and the powerful split-apply-combine pattern using GroupBy.

* **Simple Aggregations**: Series and DataFrames have methods like **.sum()**, **.mean()**, **.min()**, **.max()**, etc. By default, DataFrame aggregations operate column-wise. Use **axis='columns'** to aggregate row-wise.
* **.describe()**: A convenience method that computes several common aggregates for each column.
* **GroupBy: Split-Apply-Combine**:
    * Core Idea: A powerful operation for computing aggregates on subsets of data.
    1. **Split**: The data is broken up into groups based on a specified key.
    2. **Apply**: A function (aggregation, transformation, filter) is applied to each individual group.
    3. **Combine**: The results are merged into an output object.
* **The GroupBy Object**:
    * **df.groupby('key')** returns a DataFrameGroupBy object, which is a special "view" of the DataFrame. No computation happens until an aggregation is applied (lazy evaluation).
    * Supports column indexing (**.groupby('key')['column']**), iteration, and dispatching DataFrame/Series methods like **.describe()**.
* **The "Apply" Step - Key Methods**:
    * **.aggregate()**: Can take a string, function, list of functions, or a dictionary to compute multiple aggregations at once.
    * **.filter()**: Drops data based on group properties. The provided function must return True or False for each group.
    * **.transform()**: Returns a transformed version of the full data, with the same shape as the input (e.g., centering data by subtracting the group mean).
    * **.apply()**: Applies an arbitrary function to each group. The function takes a DataFrame and can return a DataFrame, Series, or scalar.
* **Specifying the Split Key**: Groups can be defined by a column name, a list or Series of the same length as the DataFrame, a dictionary mapping index values to group keys, or a function.
### Python and Excel

This section covers how to read and write Excel files using Pandas and the xlsxwriter library for advanced formatting.

* **Reading Excel with Pandas**:
    * **pd.read_excel('data.xlsx')**: Reads an Excel file into a DataFrame.
    * Key Parameters:
        * **sheet_name**: Specifies which sheet to read.
        * **header**: Specifies the row to use as the header (zero-indexed).
        * **usecols**: Specifies which columns to read (e.g., **'A:B'** or **[0, 1]**).
* **Writing to Excel with Pandas**:
    * **df.to_excel('output.xlsx', index=False)**: Writes a DataFrame to an Excel file.
    * Key Parameters:
        * **index=False**: Prevents writing the DataFrame index as a column.
        * **sheet_name**: Specifies the name of the sheet to write to.
* **The xlsxwriter Library**: A Python module for creating and formatting Excel files, offering more control than Pandas alone.
    * Installation: **!pip install xlsxwriter**.
    * Standalone Usage:
        1. Create a workbook: **workbook = xlsxwriter.Workbook('output.xlsx')**.
        2. Add a worksheet: **worksheet = workbook.add_worksheet()**.
        3. Define formats: **header_format = workbook.add_format({'bold': True, ...})**.
        4. Write data and formulas: **worksheet.write('A1', 'Name', header_format)**, **worksheet.write_formula(...)**.
        5. Close the workbook: **workbook.close()**.
    * Charts: Can create charts (**workbook.add_chart(...)**), configure them (**chart.add_series(...)**), and insert them into a worksheet (**worksheet.insert_chart(...)**).
    * Usage with Pandas:
        * Use xlsxwriter as the engine for Pandas' ExcelWriter to format a DataFrame written to Excel: **writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')**.
### ipywidgets

This section introduces ipywidgets, a library for creating interactive GUI components in Jupyter notebooks.

* **Core Idea**: ipywidgets is a Python library for creating interactive graphical user interface (GUI) components directly within Jupyter/Colab notebooks.
* **Import**: **import ipywidgets as widgets**.
* **Four-Step Process**:
    1. Create a widget: **button = widgets.Button(description='Click me')**.
    2. Set properties: **button.style = 'warning'**.
    3. Handle events: Define a function to execute on an event and link it, e.g., **button.on_click(on_button_click)**.
    4. Display the widget: **display(button)**.
* **Common Widgets**: Button, Checkbox, Dropdown, IntSlider, FloatSlider, RadioButtons, Text.
* **Handling Events**:
    * For a button click, use the **.on_click(handler_function)** method.
    * For value changes in sliders, dropdowns, etc., use the **.observe(handler_function, names='value')** method.
    * The event handler function receives an event object containing information about the interaction.
* **Getting Values**: Access the current value of a widget using its **.value** property (e.g., **current_value = slider.value**). This is often done inside an event handler for a button.
* **Layout and Arrangement**: Use **widgets.HBox([...])** to arrange widgets horizontally and **widgets.VBox([...])** to arrange them vertically.


## Midterm Practice Quiz

Sample questions to help you prepare for the midterm exam. Answers are provided at the end of the quiz.

**True/False Questions**

1. When using Pandas, df.loc[0] always selects the first row of the DataFrame.

2. In NumPy, array slices are copies of the original data by default.

3. Vectorized operations in NumPy are generally slower than equivalent Python loops.

4. The plt.show() command is required to save a figure to a file using fig.savefig().

5. In Matplotlib, ax.text() anchors text based on pixel coordinates by default.

6. The pd.merge() function can only perform inner joins.

7. The Pandas .append() method modifies the original DataFrame in place.

8. In an ipywidget, the display() function must be called before an event handler is defined for the widget.

9. The xlsxwriter library can be used to write Excel formulas into cells.

10. A GroupBy object in Pandas performs its calculations immediately upon creation.

11. When slicing a Pandas Series with an explicit string index like series['a':'d'], the element at index 'd' is included in the result.

12. The plt.scatter function is less efficient for large datasets than plt.plot with a marker style.

13. np.vstack and np.concatenate with axis=1 perform the same operation.

14. The ax.transAxes coordinate system in Matplotlib is dependent on the data limits of the plot.

15. In pd.concat, setting ignore_index=True will preserve the original indices from the concatenated DataFrames.

**Multiple Choice Questions**

1. Which attribute of a NumPy array returns the total number of elements?<br>
a) shape<br>
b) ndim<br>
c) size<br>
d) dtype

2. What is the output of np.add.reduce(np.arange(1, 5))?<br>
a) array([1, 3, 6, 10])<br>
b) 10<br>
c) array([1, 2, 3, 4])<br>
d) 24

3. Which of the following creates a Pandas Series with an explicit index?<br>
a) pd.Series([1, 2, 3])<br>
b) pd.Series([1, 2, 3], index=['a', 'b', 'c'])<br>
c) pd.Series({'a':1, 'b':2, 'c':3}, implicit=True)<br>
d) pd.Series.from_array([1, 2, 3])

4. To select rows 2 through 4 (inclusive by integer position) from a DataFrame df, which syntax is correct?<br>
a) df[2:4]<br>
b) df.loc[2:4]<br>
c) df.iloc[2:5]<br>
d) df.slice[2:4]

5. In Matplotlib's object-oriented interface, what is the common variable name for the object representing a single plot's bounding box, ticks, and labels?<br>
a) fig<br>
b) plt<br>
c) plot<br>
d) ax

6. How do you change the color of a line to red in plt.plot()?<br>
a) plt.plot(x, y, linecolor='red')<br>
b) plt.plot(x, y, 'red')<br>
c) plt.plot(x, y, color='red')<br>
d) plt.plot(x, y).color('red')

7. Which function is best suited for creating a scatter plot where each point has a unique size and color?<br>
a) plt.plot<br>
b) plt.scatter<br>
c) plt.errorbar<br>
d) plt.fill_between

8. What does pd.concat([df1, df2], join='inner') do if df1 and df2 have different columns?<br>
a) It keeps all columns from both DataFrames, filling missing values with NaN.<br>
b) It keeps only the columns that are present in both df1 and df2.<br>
c) It raises an error.<br>
d) It keeps only the columns from df1.

9. Which how argument in pd.merge() will result in a union of keys from both DataFrames?<br>
a) 'inner'<br>
b) 'left'<br>
c) 'cross'<br>
d) 'outer'

10. The "split-apply-combine" strategy is central to which Pandas operation?<br>
a) .merge()<br>
b) .concat()<br>
c) .groupby()<br>
d) .describe()

11. What does the .transform() method of a GroupBy object do?<br>
a) It returns a single aggregated value per group.<br>
b) It returns a transformed version of the full data with the same shape as the input.<br>
c) It returns a boolean indicating whether each group should be kept.<br>
d) It applies an arbitrary function and combines the results.

12. To read only columns 'A' and 'C' from an Excel file into a Pandas DataFrame, you would use:<br>
a) pd.read_excel('file.xlsx', cols=['A', 'C'])<br>
b) pd.read_excel('file.xlsx', columns='A,C')<br>
c) pd.read_excel('file.xlsx', usecols=['A', 'C'])<br>
d) pd.read_excel('file.xlsx', header=['A', 'C'])

13. How do you correctly link a function my_func to a button click event for an ipywidget named btn?<br>
a) btn.click(my_func)<br>
b) btn.on_click = my_func<br>
c) btn.on_click(my_func)<br>
d) btn.event('click', my_func)

14. What does the s parameter control in ax.scatter()?<br>
a) The style of the marker.<br>
b) The size of the marker.<br>
c) The shadow of the marker.<br>
d) The source data for the marker.

15. To create a legend in Matplotlib for specific lines, what is the recommended approach?<br>
a) Call plt.legend() with a list of string labels.<br>
b) Add a label keyword argument to each .plot() call you want in the legend.<br>
c) Manually draw the legend using plt.text().<br>
d) Create a separate plot just for the legend.

16. What is the result of x[:, np.newaxis] if x is a 1D NumPy array of size 5?<br>
a) A 1D array of size 5.<br>
b) A 2D array with shape (1, 5).<br>
c) A 2D array with shape (5, 1).<br>
d) An error.

17. If df1 and df2 have conflicting column names 'rank', what will pd.merge(df1, df2, on="name") name the columns in the output?<br>
a) 'rank', 'rank_1'<br>
b) 'rank_x', 'rank_y'<br>
c) 'rank_left', 'rank_right'<br>
d) It will raise an error.

18. To place text at the top-right corner of the axes area, regardless of data coordinates, which transform is most appropriate?<br>
a) ax.transData<br>
b) ax.transAxes<br>
c) fig.transFigure<br>
d) ax.transFigure

19. Which library is specifically designed to create formatted Excel files with charts from Python?<br>
a) pandas<br>
b) numpy<br>
c) xlsxwriter<br>
d) openpyxl

20. To arrange two ipywidgets, w1 and w2, side-by-side, you should use:<br>
a) widgets.SideBySide([w1, w2])<br>
b) widgets.Arrange([w1, w2], direction='horizontal')<br>
c) widgets.VBox([w1, w2])<br>
d) widgets.HBox([w1, w2])

21. What is the fundamental difference between a Pandas Series and a 1D NumPy array?<br>
a) A Series can only hold strings.<br>
b) A Series has an explicit index.<br>
c) A NumPy array is faster.<br>
d) A Series cannot be sliced.

22. In ax.annotate(), what does the xy parameter specify?<br>
a) The location of the text.<br>
b) The location of the point being annotated.<br>
c) The x and y limits of the axes.<br>
d) The color of the arrow.

23. Which of the following is NOT a valid line style in Matplotlib?<br>
a) '-'<br>
b) '--'<br>
c) '..'<br>
d) ':'

24. A Pandas Index object is:<br>
a) Mutable, like a Python list.<br>
b) Immutable, like a Python tuple.<br>
c) Only able to hold integers.<br>
d) The same as a Python dictionary key set.

25. The agg and aggregate methods of a GroupBy object are:<br>
a) Unrelated.<br>
b) Aliases for the same method.<br>
c) Used for filtering and transformation, respectively.<br>
d) The former is for single aggregations, the latter for multiple.

26. Which command saves a Matplotlib plot and trims whitespace from the edges?<br>
a) fig.save('plot.png', trim=True)<br>
b) fig.savefig('plot.png', tight=True)<br>
c) fig.savefig('plot.png', bbox_inches='tight')<br>
d) fig.export('plot.png', whitespace=False)

27. In pd.read_excel(), what does header=1 signify?<br>
a) Read only the first row.<br>
b) Use the second row (index 1) as the column headers.<br>
c) Skip the first row.<br>
d) Read the file as if it has no header.

28. To access the current value of an ipywidget slider named s, you would use:<br>
a) s.get_value()<br>
b) s.value<br>
c) s.current<br>
d) s.observe('value')

29. To reverse the y-axis in a Matplotlib plot, you can use:<br>
a) plt.ylim(1.2, -1.2)<br>
b) plt.axis('reversed')<br>
c) plt.ylabel.reverse()<br>
d) ax.set_ylim(reverse=True)

30. In the "split-apply-combine" pattern, which method is used for dropping groups that don't meet a certain criteria?<br>
a) aggregate<br>
b) transform<br>
c) filter<br>
d) apply

**Short Answer Questions**

1. What is the key difference between a NumPy array slice (a view) and a Python list slice (a copy)? What are the implications of this difference?

2. Explain the concept of a "universal function" (ufunc) in NumPy and why it is important for performance.

3. Describe the two main interfaces for plotting in Matplotlib and a situation where one is preferable to the other.

4. What is the purpose of the loc and iloc indexers in Pandas? Why are they useful?

5. What is the difference between an inner join and an outer join when merging two Pandas DataFrames?

6. Briefly describe the three steps of the "split-apply-combine" strategy used by groupby.

7. How can you create a legend in Matplotlib that represents the size of points in a scatter plot?

8. Explain the purpose of the transform argument in Matplotlib's ax.text() function. Name one of the available transforms besides the default.

9. When would you use the xlsxwriter library instead of Pandas' built-in to_excel() method?

10. Describe the four main steps to create and use an interactive ipywidget.

11. How do you convert a 1D NumPy array x into a 2D column vector? Provide two different methods.

12. What does it mean for a Pandas Index object to be "immutable"?

13. If you concatenate two DataFrames that have duplicate indices, what are two ways pd.concat allows you to handle the duplicates?

14. What are the on, left_on, and right_on keywords used for in pd.merge?

15. What does the .describe() method on a Pandas DataFrame return?

16. What is the purpose of plt.colorbar() when used with plt.scatter()?

17. In ipywidgets, what is the difference between the event handling for a Button (on_click) and a Slider (observe)?

18. What do the fig and ax variables represent after the call fig, ax = plt.subplots()?

19. How do you save a Pandas DataFrame to a specific sheet named "Report" in an Excel file?

20. In an ax.annotate call, what is the difference between the xy and xytext parameters?


---


**Answer Key**

**True/False Answers**

1. False. df.loc[0] selects the row with the explicit index label 0. If the index is not integer-based, this will fail. df.iloc[0] always selects the first row by integer position.

2. False. NumPy array slices are views of the original data, meaning modifications to the slice affect the original array.

3. False. Vectorized operations are significantly faster because they push loops into NumPy's compiled C layer.

4. False. plt.show() is for displaying the plot in an interactive viewer and is not necessary for saving.

5. False. ax.text() uses data coordinates by default (transform=ax.transData).

6. False. pd.merge() can perform inner, outer, left, and right joins using the how parameter.

7. False. The .append() method creates and returns a new DataFrame; it does not modify the original.

8. False. The display function can be called before or after; however, the widget must be created before it is displayed or has an event handler assigned. The handler must be defined before it is assigned.

9. True. xlsxwriter provides methods like write_formula() to insert Excel formulas.

10. False. A GroupBy object uses "lazy evaluation." No computation occurs until an aggregation or other method is called on it.

11. True. Slicing with explicit indices in Pandas is inclusive of the endpoint.

12. True. plt.plot is more efficient because the marker properties are set once for the entire series, whereas plt.scatter can render each point individually.

13. False. np.vstack stacks rows (axis 0). np.concatenate with axis=1 stacks columns.

14. False. ax.transAxes coordinates are relative to the axes bounding box (0,0 is bottom-left, 1,1 is top-right) and are independent of the data limits.

15. False. ignore_index=True creates a new integer index for the resulting DataFrame, discarding the originals.

**Multiple Choice Answers**

1. c) size

2. b) 10 (reduce performs a sum: 1+2+3+4=10).

3. b) pd.Series([1, 2, 3], index=['a', 'b', 'c'])

4. c) df.iloc[2:5] (iloc uses Python-style slicing, which is exclusive of the endpoint).

5. d) ax

6. c) plt.plot(x, y, color='red')

7. b) plt.scatter

8. b) It keeps only the columns that are present in both df1 and df2.

9. d) 'outer'

10. c) .groupby()

11. b) It returns a transformed version of the full data with the same shape as the input.

12. c) pd.read_excel('file.xlsx', usecols=['A', 'C'])

13. c) btn.on_click(my_func)

14. b) The size of the marker.

15. b) Add a label keyword argument to each .plot() call you want in the legend.

16. c) A 2D array with shape (5, 1).

17. b) 'rank_x', 'rank_y'

18. b) ax.transAxes

19. c) xlsxwriter

20. d) widgets.HBox([w1, w2])

21. b) A Series has an explicit index.

22. b) The location of the point being annotated.

23. c) '..' (The dotted style is ':').

24. b) Immutable, like a Python tuple.

25. b) Aliases for the same method.

26. c) fig.savefig('plot.png', bbox_inches='tight')

27. b) Use the second row (index 1) as the column headers.

28. b) s.value

29. a) plt.ylim(1.2, -1.2) (Reversing the order of the arguments reverses the axis).

30. c) filter

**Short Answer Answers**

1. A NumPy slice is a view, meaning it is a pointer to the original array's data. Modifying the slice changes the original array. A Python list slice is a copy, creating a new list with a copy of the data. Modifying the list slice does not affect the original list. The implication for NumPy is memory efficiency (no data is duplicated) but requires caution to avoid unintended side effects.

2. A ufunc is a function that performs fast, element-wise operations on NumPy arrays. It's important for performance because it pushes the iterative loop from slow, interpreted Python into fast, pre-compiled C code.

3. The two interfaces are MATLAB-style (state-based) and object-oriented. The MATLAB-style (plt.plot()) is convenient for simple, quick plots. The object-oriented style (ax.plot()) is preferable for more complex plots, such as those with multiple subplots, as it gives explicit control over each plot element.

4. loc selects data based on the explicit index label. iloc selects data based on the implicit, zero-based integer position. They are useful for removing ambiguity, especially when a DataFrame has an integer index, where df[0] could mean the row at position 0 or the row with label 0.

5. An inner join returns only the rows where the key exists in both DataFrames (the intersection). An outer join returns all rows from both DataFrames, placing NaN where data is missing in one of the frames (the union).

6. (1) Split: The DataFrame is broken into smaller DataFrame groups based on the values in a specified key column. (2) Apply: A function (e.g., sum, mean) is applied independently to each of these smaller groups. (3) Combine: The results of the function application on each group are combined back into a new DataFrame or Series.

7. To create a legend for point size, you plot empty lists (plt.scatter([], [], ...)) with the desired marker size (s=area) and a corresponding label. The legend picks up these labeled, "fake" plot objects.

8. The transform argument specifies the coordinate system to use for placing the text. Besides the default ax.transData (data coordinates), other options include ax.transAxes (coordinates relative to the axes bounding box) and fig.transFigure (coordinates relative to the figure).

9. You should use xlsxwriter when you need more control over the Excel output than pandas provides, such as applying custom cell formatting (colors, borders), writing formulas, creating charts, or inserting images.

10. (1) Create the widget (w = widgets.Button(...)). (2) Set its properties (w.description = 'New Text'). (3) Handle its events by defining a function and linking it (w.on_click(my_func)). (4) Display the widget (display(w)).

11. Method 1: Reshaping with .reshape(): x.reshape((5, 1)). Method 2: Slicing with np.newaxis: x[:, np.newaxis].

12. "Immutable" means that once an Index object is created, its values cannot be changed. This ensures stability and safety when the index is shared across multiple DataFrames or Series.

13. (1) ignore_index=True: This will discard the original indices and create a new, default integer index for the result. (2) keys=['df1', 'df2']: This will create a hierarchical index (MultiIndex) that preserves the original indices under a new, higher-level label.

14. They specify the columns or indices to join on. on is used when the key column has the same name in both DataFrames. left_on and right_on are used when the key column names are different in the left and right DataFrames.

15. The .describe() method returns descriptive statistics for the numerical columns of the DataFrame, including count, mean, standard deviation, min, max, and quartile values.

16. plt.colorbar() displays a color scale bar that shows the mapping between the values passed to the c argument of plt.scatter() and the colors rendered on the plot.

17. A Button's on_click event fires only when the button is explicitly clicked. A Slider's observe event (with names='value') fires every time the slider's value changes, providing continuous updates.

18. fig is an instance of plt.Figure, which is the top-level container for all plot elements. ax is an instance of plt.Axes, which is the actual plot area (the box with ticks, labels, etc.) where data is plotted.

19. df.to_excel('filename.xlsx', sheet_name='Report', index=False)

20. xy is a tuple (x, y) specifying the coordinate of the point to be annotated. xytext is a tuple (x, y) specifying the coordinate where the annotation text should be placed. An arrow is drawn from xytext to xy.


---


## Glossary of Key Terms

| Term | Definition |
| :--- | :--- |
| **Axes** | In Matplotlib, the object representing the plot area: a bounding box with ticks, grids, and labels that contains the plot elements. |
| **ax.annotate()** | A Matplotlib function for creating annotations, which consist of some text and an arrow, with flexible specification options. |
| **ax.text()** | A Matplotlib function to place text at a particular x/y value on the axes. |
| **DataFrame** | The primary two-dimensional, size-mutable, and potentially heterogeneous tabular data structure in Pandas, with labeled axes (rows and columns). |
| **DataFrameGroupBy** | The object returned by a .groupby() operation in Pandas. It is a special view of the DataFrame poised to perform operations on groups but does no actual computation until an aggregation is applied. |
| **dtype** | A NumPy attribute that describes the data type of the elements in an array (e.g., int64, float64). |
| **Figure** | In Matplotlib, the top-level object or container that holds all plot elements like axes, graphics, text, and labels. |
| **GUI** | Graphical User Interface. The visual elements of a program (buttons, text boxes, etc.) that a user interacts with. |
| **groupby** | A Pandas operation that involves splitting data into groups based on some criteria, applying a function to each group independently, and combining the results into a data structure. |
| **iloc** | An indexer in Pandas for purely integer-location based indexing for selection by position (implicit index). |
| **Index** | A fundamental Pandas object that can be thought of as an immutable array or an ordered set, holding the axis labels for Series and DataFrame objects. |
| **ipywidgets** | A Python library that provides interactive HTML widgets (like sliders, buttons, text boxes) for Jupyter notebooks and Colab. |
| **loc** | An indexer in Pandas for label-based indexing, using the explicit index labels of the Series or DataFrame. |
| **Matplotlib** | A popular and comprehensive mathematical plotting library in Python used for creating static, animated, and interactive visualizations. |
| **np.concatenate()** | A NumPy function for joining a sequence of arrays along an existing axis. |
| **np.newaxis** | A NumPy utility used to increase the dimension of an existing array by one dimension when used in slicing. |
| **pd.concat()** | A Pandas function for combining Series or DataFrame objects along a particular axis with optional set logic (union or intersection) of the other axes. |
| **pd.merge()** | A Pandas function for combining DataFrame objects using a database-style join operation based on common columns or indices. |
| **plt.scatter()** | A Matplotlib function that creates a scatter plot, which is highly flexible as the properties (size, color, etc.) of each individual point can be controlled. |
| **plt.show()** | A Matplotlib command that starts an event loop and opens interactive windows to display all active figure objects. |
| **Relational Algebra** | A formal set of rules for manipulating relational data, forming the conceptual foundation for database operations like joins, which are implemented in Pandas' pd.merge. |
| **reshape()** | A NumPy method to change the shape of an array without changing its data. |
| **Series** | The primary one-dimensional labeled array data structure in Pandas, capable of holding any data type. |
| **Slicing** | A syntax for accessing subarrays or sub-series/dataframes. In NumPy, slices are views; in Pandas, slicing with explicit indices is inclusive of the endpoint. |
| **Split-Apply-Combine** | A pattern for data analysis where data is split into groups, a function is applied to each group, and the results are combined. It is the core concept of Pandas' groupby operation. |
| **Ufunc** | Universal Function. A function that operates on NumPy arrays in an element-by-element fashion, supporting features like broadcasting and type casting. They are the key to fast, vectorized computation. |
| **Vectorization** | The process of replacing explicit for-loops with array expressions. In NumPy, this is achieved via ufuncs and leads to much faster execution. |
| **View** | In NumPy, a slice of an array that does not have its own data. It is a "view" into the memory of the original array, so modifications to the view will affect the original. |
| **xlsxwriter** | A Python library that allows you to write files in the Excel 2007+ XLSX file format, providing detailed control over formatting, charts, and other features. |