# Reading: Working with Excel Files in Python

---

Spreadsheets are a fundamental tool in civil engineering and construction management. In Unit 1, we learned some advanced techniques for working with spreadsheets. We used  Microsoft Excel which is the main  tool used for working with spreadsheets. In this unit, we will learn how to work with Excel files in Python.

## Reading Excel Files Using Pandas

In the previous section, we learned how to use the `pandas` library. Pandas is a powerful data manipulation library that provides data structures and functions to work with structured data. The `pandas` library makes it easy to work with Excel files. We can easily read data from an Excel file into a pandas dataframe and/or export a pandas dataframe to an Excel file. 

With Pandas we used a  method  called `read_excel()` that reads an Excel file and returns a dataframe. As you may recall, a DataFrame is a two-dimensional data structure that is similar to a table in a database. We will now look at this in more detail. 

You can think of a DataFrame as a spreadsheet in Python.

Here is an example of how to read an Excel file using the `read_excel()` method:

```python
import pandas as pd

# Read the Excel file
df = pd.read_excel('data.xlsx')

# Display the DataFrame
print(df)
```
The read_excel() method has one essential parameter, which is the path to the Excel file. In this example, we are reading an Excel file named `data.xlsx`. The `read_excel()` method reads the Excel file and returns a DataFrame. We store the DataFrame in a variable called `df` (which is a really bad variable name - you should use something more descriptive - by convention, we name variables that contain Panda's data structures as _df with the descriptive name before the _df part). 

The read_excel() method has a number of optional arguments. For example, if the Excel file has multiple sheets, you can specify which sheet to read using the `sheet_name` parameter. Here is an example:

```python   
# Read the second sheet of the Excel file, if the name of the second sheet is 'Sheet2'
df = pd.read_excel('data.xlsx', sheet_name='Sheet2')
```

In each of the examples thus far, we are reading the entire contents of a sheet into the dataframe. In some cases, you may want to start reading on a particular row. You can also specify the header row using the `header` parameter. For example:
    
```python
# Read the Excel file starting from the second row
df = pd.read_excel('data.xlsx', header=1)
```

Note that the header row is zero-indexed, so the first row is 0, the second row is 1, and so on.

You can also specify the columns to read using the `usecols` parameter. For example:

```python
# Read only the first two columns of the Excel file
df = pd.read_excel('data.xlsx', usecols='A:B')
```

The `usecols` parameter accepts a string or a list of column names. In this example, we are reading only the first two columns of the Excel file. Here is an example of reading the same two specific columns (the first two columns) by index:

```python
# Read only the first two columns of the Excel file
df = pd.read_excel('data.xlsx', usecols=[0, 1])
```
You can read more about the pandas `read_excel()` method in the [official documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html){target='_blank'}. **We suggest you look through the documentation to see all the available parameters.**

## Writing Data to Excel Files Using Pandas

In addition to reading Excel files, you can also write data to Excel files using the `pandas` library. The `pandas` library provides a `to_excel()` method that allows you to write a DataFrame to an Excel file. Here is an example:

```python
import pandas as pd

# Create a dictionary with the data
data = {
    'Name': ['John', 'Jane', 'Alice', 'Bob'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)
```

As you can see, the `to_excel()` method takes the path to the Excel file as a parameter. In this example, we are writing the DataFrame to an Excel file named `output.xlsx`. The `index` parameter is set to `False` to prevent pandas from writing row indices to the Excel file. You can also specify the sheet name using the `sheet_name` parameter. Here is an example:

```python
# Write the DataFrame to an Excel file with a specific sheet name
df.to_excel('output.xlsx', sheet_name='MySheet', index=False)
```


## Using the xlsxwriter Library 

When saving a dataframe using the 'to_excel' method in pandas, the resulting Excel file contains a simple 
unformatted table. However,
in cases where you need more control over the Excel file, you can use the `xlsxwriter` library. The `xlsxwriter` 
library is a Python module that allows you to create and save Excel files with formatting and charts. Note that xlsxwriter is a write-only library -- it can only create new Excel files, not read existing ones. You can write data to the cells of the Excel document, including formulas.

The documentation for the `xlsxwriter` library can be found [here](https://xlsxwriter.readthedocs.io/){target='_blank'}. It includes many examples of how to use the library to create Excel files with formatting and charts. Look through it to see all the available features. You can use it with Pandas as well as standalone. Below we have a Pandas example and several standalone examples.

Panda uses xlsxwriter to create Excel files in the background, but only provides limited options for formatting. If you use xlsxwriter to create Excel files, you have much more control over the formatting and content of the Excel file. You can create different formats for different types of data, add charts and images, and even add formulas to the Excel file.


### Installing the xlsxwriter Library

You can 
install the `xlsxwriter` library using the following command:

```python
!pip install xlsxwriter
```
This is **not** one of the default packages installed with Google Colab, so you need to explicitly install it before using. 

After you install it (i.e., load it on the computer) you also need to import it:

```python
import xlsxwriter
```

### Creating an Excel File with Formatting

Here is an example of how to use the `xlsxwriter` library to create an Excel file with formatting. xlsxwriter uses an object approach, where you first create a workbook object and then add worksheets to the workbook. Then apply formatting to the cells of the worksheets and add data to the worksheets. 

Here is an example:

```python
import xlsxwriter

# Create a new Excel file object called "workbook"
workbook = xlsxwriter.Workbook('output.xlsx')

# Add a worksheet to the workbook object
worksheet = workbook.add_worksheet()

# Define formats for different workbook areas such as the header and data sections
# We haven't applied these formats yet, but we will apply them when we write data to the worksheet
# You can create a number of formats, and then apply them to different areas of the worksheet as needed.
header_format = workbook.add_format({'bold': True, 'bg_color': '#F0F8FF', 'border': 1})
data_format = workbook.add_format({'align': 'center', 'border': 1})

# Write data for the headers to the worksheet and apply the header format
worksheet.write('A1', 'Name', header_format)
worksheet.write('B1', 'Age', header_format)
worksheet.write('C1', 'City', header_format)

worksheet.write('A2', 'John', data_format)
worksheet.write('B2', 25, data_format)
worksheet.write('C2', 'New York', data_format)

worksheet.write('A3', 'Jane', data_format)
worksheet.write('B3', 30, data_format)
worksheet.write('C3', 'Los Angeles', data_format)

worksheet.write('A4', 'Alice', data_format)
worksheet.write('B4', 35, data_format)
worksheet.write('C4', 'Chicago', data_format)

# Add a formula to the worksheet to compute the average age
worksheet.write_formula('B5', '=AVERAGE(B2:B4)', data_format)

# You could have created a 'results_format' and applied to the formula cell as well, but we just used the data_format for simplicity. 
# You can create as many formats as you want and apply them to different areas of the worksheet as needed.


# Close the workbook - since this is an object, you need to close it to save the file
# You can continue writing to the workbook until it is closed, but once it is closed, you cannot write to it anymore.
workbook.close()
```

As you can see, the `xlsxwriter` library provides more control over the Excel file's formatting and content. Also 
notice that you apply formatting by creating a format object using the `add_format()` method and then passing the 
object each time you write data to the worksheet. You can create different format objects for different types of data.

To create a format, you simply create a dictionary with the formats you want to apply. Click [here](https://xlsxwriter.readthedocs.io/format.html#format-methods-and-format-properties){target='_blank'} to see a complete list of the properties you can apply to a format object. It includes things like fonts, bold, italic, locked cells, foreground or background colors, borders, number formats, alignments, and many more. 

### Creating an Excel File with Charts

You can create more complex Excel files with charts, images, and other elements using the `xlsxwriter` library. Here 
is an example of how to create a **column** chart in an Excel file using the `xlsxwriter` library:

```python
import xlsxwriter

# Create a new Excel file object
workbook = xlsxwriter.Workbook('output.xlsx')

# Add a worksheet to the workbook object
worksheet = workbook.add_worksheet()

# Create some data to add to the worksheet. Something that we can plot with a column chart
data = [
    ['Category', 'Values'],
    ['A', 10],
    ['B', 70],
    ['C', 30],
    ['D', 60],
    ['E', 50],
    ['F', 90],
]

# Create formats
header_format = workbook.add_format({
    'bold': True,
    'align': 'center'
})

data_format = workbook.add_format({
    'align': 'center'
})

# Write the header row using the header format
worksheet.write_row(0, 0, data[0], header_format)

# Write the rest of the data using a loop, start on row 2 since we already wrote the header
row_num = 1
for row_data in data[1:]:
    worksheet.write_row(row_num, 0, row_data, data_format)
    row_num += 1

# Add a chart to the worksheet
chart = workbook.add_chart({'type': 'column'})

# Configure the chart
# Configure the first series.
# In this section we use Excel sheet and column references to specify the data.
# Above we used a loop to write the data to the worksheet without specifying the row numbers.
# By default, these start at A1 and go to the last cell required to hold the data
# In this section we hardcoded the data locations

chart.add_series(
    {
        "name": "=Sheet1!$B$1",
        "categories": "=Sheet1!$A$2:$A$7",
        "values": "=Sheet1!$B$2:$B$7",
    }
)

# Insert the chart into the worksheet
worksheet.insert_chart('D2', chart)

# Close the workbook
workbook.close()
```
This same example could be used to create a **line** chart simply by changing the chart type to 'line'. 

Here is an example of how to create an **xy scatter** plot in an Excel file using the `xlsxwriter` library.
In this case we need numbers for the x-axis:

```python
import xlsxwriter

# Create a new Excel file object
workbook = xlsxwriter.Workbook('output.xlsx')

# Add a worksheet to the workbook object
worksheet = workbook.add_worksheet()

# Create data  to add to the worksheet. Something that we can plot with an xy scatter plot
data = [
    ['X', 'Y'],
    [5.0, 8.5],
    [20.7, 32.8],
    [37.1, 35.3],
    [54.0, 40.7],
    [63.1, 51.3],
]

# Add the data to the workbook object
data_format = workbook.add_format({'align': 'center'})

# Write the data to the worksheet
for row_num, row_data in enumerate(data):
    worksheet.write_row(row_num, 0, row_data, data_format)
    
# Add a chart to the worksheet, include markers
chart = workbook.add_chart({'type': 'scatter', 'subtype': 'smooth_with_markers'})

# Configure the chart
# Configure the first series.
chart.add_series(
    {
        "name": "=Sheet1!$B$1",
        "categories": "=Sheet1!$A$2:$A$6",
        "values": "=Sheet1!$B$2:$B$6",
    }
)

# Insert the chart into the worksheet
worksheet.insert_chart('D2', chart)

# Close the workbook and save the file
workbook.close()
```

### Saving a Pandas DataFrame to an Excel File with xlsxwriter

You can also save a pandas DataFrame to an Excel file with formatting using the `xlsxwriter` library. Here is an example:

```python
import pandas as pd
import xlsxwriter

# Create some data for a DataFrame
data = {
    'Name': ['John', 'Jane', 'Alice', 'Bob'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Create a Pandas Excel writer object using XlsxWriter as the engine.
# Using a "with" block ensures the file is properly saved when the block ends.
with pd.ExcelWriter('output.xlsx', engine='xlsxwriter') as writer:

    # Write the dataframe to an XlsxWriter Excel object. Name the sheet "Sheet1"
    df.to_excel(writer, sheet_name='Sheet1')

    # Get the xlsxwriter workbook and worksheet objects so we can add formatting
    workbook = writer.book
    worksheet = writer.sheets["Sheet1"]

    # Create a format for the header row
    header_format = workbook.add_format({'bold': True, 'bg_color': '#F0F8FF', 'border': 1})

    # Apply the format to the header row
    worksheet.set_row(0, None, header_format)

# The file is automatically saved when the "with" block ends
```

### Saving Data to an Excel File with xlsxwriter Using Write Methods

Note that this example uses the `pd.ExcelWriter()` method to create an Excel writer object. The `to_excel()` method 
is then used to write the DataFrame to the Excel file. This is easier than looping over data
Another way to write the contents of a DataFrame to an Excel 
file is to write them out one column at a time using the `write` and `write_column` methods in xlsxwriter. Here is an 
example:

```python
import pandas as pd
import xlsxwriter

# Create data for a DataFrame
data = {
    'Name': ['John', 'Jane', 'Alice', 'Bob'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Create a new Excel file object
workbook = xlsxwriter.Workbook('output.xlsx')

# Add a worksheet to the object
worksheet = workbook.add_worksheet()

# Create some format objects
header_format = workbook.add_format({'bold': True, 'align': 'center', 'border': 1})
data_format = workbook.add_format({'align': 'center', 'border': 1})

# Write the column headers
worksheet.write('A1', 'Name', header_format)
worksheet.write('B1', 'Age', header_format)
worksheet.write('C1', 'City', header_format)

# Write the column values - notice we are writing the full column from the data frame
# without using a loop. 
# The write_column method takes care of writing the data to the correct rows and columns.
worksheet.write_column('A2', df['Name'], data_format)
worksheet.write_column('B2', df['Age'], data_format)
worksheet.write_column('C2', df['City'], data_format)

# Close the workbook and save the file
workbook.close()
```


This is just the tip of the iceberg! You can read more about the `xlsxwriter` library in the [official documentation](https://xlsxwriter.readthedocs.io/){target='_blank'}. 

# Pre-Class Quiz Challenge

Open a new Colab notebook and do the following:

1. Rename the notebook something like '**(Your_Name)_Pre_xlswriter.ipynb'**
2. Click here to download the [data.xlsx](data.xlsx) file.
2. Upload the file to your Colab notebook by clicking on the folder icon on the left side of the screen and then 
   clicking on the upload icon. Or you can drag and drop the file into the notebook.
1. Import the file to a dataframe using the `pandas` library and display the contents of the dataframe.
3. Add a new column to the dataframe called **Sum** that is the sum of columns 2-4. Display the updated dataframe.
4. Save the updated dataframe to a new Excel file called **output.xlsx** using the `pandas` library. In a few seconds, 
   the file will appear in your notebook's file list. Download the file to your computer and check the contents.

Save changes to your Google Drive and submit the link to the notebook in your Pre-Class Quiz.

---

## Turning in/Rubric

**_REMINDER_** - For this class, **you will only turn in the links to your Colab notebooks**. You will get a 0 for this assignment if you turn in a python file or a link that is not correct, wrong assignment, or does not give editor permission.

**Rubric:**

|                      Item                      | Points Possible |
|:----------------------------------------------:|:---------------:|
| <div style="text-align: right">**Total**</div> |        3        |

---

The following is not a part of the rubric, but specifies how you can lose points. For example: if you fail to share your link correctly.

| **Reasons for Points Lost** |    **Amount**     |  
|:---------------------------:|:-----------------:|
|   Link shared incorrectly   |       -10%        | 