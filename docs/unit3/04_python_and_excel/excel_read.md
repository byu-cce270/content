# Bons Material: Working with Excel Files in Python

Spreadsheets are a fundamental tool in civil engineering and construction management. In Unit 1, we learned some advanced techniques for working with spreadsheets. We used Google Sheets, but Microsoft Excel is another popular tool for working with spreadsheets. In this unit, we will learn how to work with Excel files in Python.

## Reading Excel Files Using Pandas

In the previous section, we learned how to use the `pandas` library. Pandas is a powerful data manipulation library that provides data structures and functions to work with structured data. The `pandas` library makes it easy to work with Excel files. We can easily read data from an Excel file into a pandas dataframe and/or export a pandas dataframe to an Excel file. There is a method in Pandas called `read_excel()` that reads an Excel file and returns a dataframe. As you may recall, a DataFrame is a two-dimensional data structure that is similar to a table in a database. You can think of a DataFrame as a spreadsheet in Python.

Here is an example of how to read an Excel file using the `read_excel()` method:

```python
import pandas as pd

# Read the Excel file
df = pd.read_excel('data.xlsx')

# Display the DataFrame
print(df)
```
The read_excel() method has one essential parameter, which is the path to the Excel file. In this example, we are reading an Excel file named `data.xlsx`. The `read_excel()` method reads the Excel file and returns a DataFrame. We store the DataFrame in a variable called `df`. 

The read_excel() method has a number of optional arguments. For example, if the Excel file has multiple sheets, you can specify which sheet to read using the `sheet_name` parameter. Here is an example:

```python   
# Read the second sheet of the Excel file
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

The `usecols` parameter accepts a string or a list of column names. In this example, we are reading only the first two columns of the Excel file. Here is an example of reading specific columns by index:

```python
# Read only the first two columns of the Excel file
df = pd.read_excel('data.xlsx', usecols=[0, 1])
```
You can read more about the pandas `read_excel()` method in the [official documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html){target='blank'}.

## Writing Data to Excel Files Using Pandas

In addition to reading Excel files, you can also write data to Excel files using the `pandas` library. The `pandas` library provides a `to_excel()` method that allows you to write a DataFrame to an Excel file. Here is an example:

```python
import pandas as pd

# Create a DataFrame
data = {
    'Name': ['John', 'Jane', 'Alice', 'Bob'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)
```
## Using the xlsxwriter Library

When saving a dataframe using the 'to_excel' method in pandas, the resulting Excel file contains a simple 
unformatted table. However,
in cases where you need more control over the Excel file, you can use the `xlsxwriter` library. The `xlsxwriter` 
library is a Python module that allows you to create and save Excel files with formatting and charts. You can even 
create 
data on the cells of the Excel document, including formulas.

### Installing the xlsxwriter Library

You can 
install the `xlsxwriter` library using the following command:

```python
!pip install xlsxwriter
```
### Creating an Excel File with Formatting

Here is an example of how to use the `xlsxwriter` library to create an Excel file with formatting:

```python
import xlsxwriter

# Create a new Excel file
workbook = xlsxwriter.Workbook('output.xlsx')

# Add a worksheet
worksheet = workbook.add_worksheet()

# Define a format for the header row
header_format = workbook.add_format({'bold': True, 'bg_color': '#F0F8FF', 'border': 1})
data_format = workbook.add_format({'align': 'center', 'border': 1})

# Write data to the worksheet
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

# Close the workbook
workbook.close()
```

As you can see, the `xlsxwriter` library provides more control over the Excel file's formatting and content. Also 
notice that you apply formatting by creating a format object using the `add_format()` method and then passing the 
object each time you write data to the worksheet. You can create different format objects for different types of data.

### Creating an Excel File with Charts

You can create more complex Excel files with charts, images, and other elements using the `xlsxwriter` library. Here 
is an example of how to create a **column** chart in an Excel file using the `xlsxwriter` library:

```python
import xlsxwriter

# Create a new Excel file
workbook = xlsxwriter.Workbook('output.xlsx')

# Add a worksheet
worksheet = workbook.add_worksheet()

# Add data to the worksheet. Something that we can plot with a column chart
data = [
    ['Category', 'Values'],
    ['A', 10],
    ['B', 70],
    ['C', 30],
    ['D', 60],
    ['E', 50],
    ['F', 90],
]

data_format = workbook.add_format({'align': 'center'})

# Write the data to the worksheet
for row_num, row_data in enumerate(data):
    worksheet.write_row(row_num, 0, row_data, data_format)

# Add a chart to the worksheet
chart = workbook.add_chart({'type': 'column'})

# Configure the chart
# Configure the first series.
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

Here is an example of how to create an **xy scatter** plot in an Excel file using the `xlsxwriter` library:

```python
import xlsxwriter

# Create a new Excel file
workbook = xlsxwriter.Workbook('output.xlsx')

# Add a worksheet
worksheet = workbook.add_worksheet()

# Add data to the worksheet. Something that we can plot with an xy scatter plot
data = [
    ['X', 'Y'],
    [5.0, 8.5],
    [20.7, 32.8],
    [37.1, 35.3],
    [54.0, 40.7],
    [63.1, 51.3],
]

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

# Close the workbook
workbook.close()
```

### Saving a Pandas DataFrame to an Excel File with xlsxwriter

You can also save a pandas DataFrame to an Excel file with formatting using the `xlsxwriter` library. Here is an example:

```python
import pandas as pd
import xlsxwriter

# Create a DataFrame
data = {
    'Name': ['John', 'Jane', 'Alice', 'Bob'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# Create a Pandas Excel writer using XlsxWriter as the engine
writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

workbook = writer.book
worksheet = writer.sheets["Sheet1"]

# Format the header row
header_format = workbook.add_format({'bold': True, 'bg_color': '#F0F8FF', 'border': 1})

# Apply the format to the header row
worksheet.set_row(0, None, header_format)

# Close the workbook
workbook.close()
```

### Saving Data to an Excel File with xlsxwriter Using Write Methods

Note that this example uses the `pd.ExcelWriter()` method to create an Excel writer object. The `to_excel()` method 
is then used to write the DataFrame to the Excel file. Another way to write the contents of a DataFrame to an Excel 
file is to write them out one column at a time using the `write` and `write_column` methods in xlsxwriter. Here is an 
example:

```python
import pandas as pd
import xlsxwriter

# Create a DataFrame
data = {
    'Name': ['John', 'Jane', 'Alice', 'Bob'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# Create a new Excel file
workbook = xlsxwriter.Workbook('output.xlsx')

# Add a worksheet
worksheet = workbook.add_worksheet()

# Create some format objects
header_format = workbook.add_format({'bold': True, 'align': 'center', 'border': 1})
data_format = workbook.add_format({'align': 'center', 'border': 1})

# Write the column headers
worksheet.write('A1', 'Name', header_format)
worksheet.write('B1', 'Age', header_format)
worksheet.write('C1', 'City', header_format)

# Write the column values
worksheet.write_column('A2', df['Name'], data_format)
worksheet.write_column('B2', df['Age'], data_format)
worksheet.write_column('C2', df['City'], data_format)

# Close the workbook
workbook.close()
```

This is just the tip of the iceberg! You can read more about the `xlsxwriter` library in the [official documentation](https://xlsxwriter.readthedocs.io/){target='blank'}. 
anges to your Google Drive and submit the link to the notebook in your Pre-Class Quiz.