# Working with Excel Files in Python

Spreadsheets are a fundamental tool in civil engineering and construction management. In Unit 1, we learned some advanced techniques for working with spreadsheets. We used Google Sheets, but Microsoft Excel is another popular tool for working with spreadsheets. In this unit, we will learn how to work with Excel files in Python.

## Reading Excel Files Using Pandas

In the previous section, we learned how to use the `pandas` library. Pandas is a powerful data manipulation library that provides data structures and functions to work with structured data. The `pandas` library makes it easy to work with Excel files. We can easily read data from an Excel file into a pandas dataframe and/or export a pandas dataframe to an Excel file. 

To read an Excel file in Python, you need to install the `pandas` library. You can install the `pandas` library using the following command:

```python
!pip install pandas
```
There is a method in Pandas called `read_excel()` that reads an Excel file and returns a dataframe. As you may recall, a DataFrame is a two-dimensional data structure that is similar to a table in a database. You can think of a DataFrame as a spreadsheet in Python.

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

# Write data to the worksheet
worksheet.write('A1', 'Name')
worksheet.write('B1', 'Age')
worksheet.write('C1', 'City')

worksheet.write('A2', 'John')
worksheet.write('B2', 25)
worksheet.write('C2', 'New York')

worksheet.write('A3', 'Jane')
worksheet.write('B3', 30)
worksheet.write('C3', 'Los Angeles')

worksheet.write('A4', 'Alice')
worksheet.write('B4', 35)
worksheet.write('C4', 'Chicago')

# Add a formula to the worksheet to compute the average age
worksheet.write_formula('B5', '=AVERAGE(B2:B4)')

# Define a format for the header row
header_format = workbook.add_format({'bold': True, 'bg_color': '#F0F8FF', 'border': 1})

# Apply the format to the header row
worksheet.set_row(0, None, header_format)

# Center justify the columns
worksheet.set_column('A:C', None, None, {'align': 'center'})

# Close the workbook
workbook.close()
```

As you can see, the `xlsxwriter` library provides more control over the Excel file's formatting and content. The basic steps to create an Excel file using the `xlsxwriter` library are as follows:

1. Create a new Excel file using the `Workbook` class.
2. Add a worksheet to the Excel file using the `add_worksheet()` method.
3. Write data to the worksheet using the `write()` method.
4. Add formulas to the worksheet using the `write_formula()` method.
5. Define formats for cells using the `add_format()` method.
6. Apply formats to cells using the `set_row()` and `set_column()` methods.
7. Close the workbook using the `close()` method.

### Creating an Excel File with Charts

You can create more complex Excel files with charts, images, and other elements using the `xlsxwriter` library. Here is an example of how to create a chart in an Excel file using the `xlsxwriter` library:

```python
import xlsxwriter

# Create a new Excel file
workbook = xlsxwriter.Workbook('output.xlsx')

# Add a worksheet
worksheet = workbook.add_worksheet()

# Write data to the worksheet
worksheet.write('A1', 'Name')
worksheet.write('B1', 'Age')
worksheet.write('C1', 'City')

worksheet.write('A2', 'John')
worksheet.write('B2', 25)
worksheet.write('C2', 'New York')

worksheet.write('A3', 'Jane')
worksheet.write('B3', 30)
worksheet.write('C3', 'Los Angeles')

worksheet.write('A4', 'Alice')
worksheet.write('B4', 35)
worksheet.write('C4', 'Chicago')

# Add a chart to the worksheet
chart = workbook.add_chart({'type': 'column'})

# Configure the chart
chart.add_series({'values': '=Sheet1!$B$2:$B$4'})

# Insert the chart into the worksheet
worksheet.insert_chart('E1', chart)

# Close the workbook
workbook.close()
```

### Saving a DataFrame to an Excel File with xlsxwriter

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

# Format the header row
header_format = writer.book.add_format({'bold': True, 'bg_color': '#F0F8FF', 'border': 1})

# Apply the format to the header row
writer.sheets['Sheet1'].set_row(0, None, header_format)

# Close the workbook
writer.close()
```

This is just the tip of the iceberg! You can read more about the `xlsxwriter` library in the [official documentation]
(https://xlsxwriter.readthedocs.io/){target='blank'}. 

# Pre-Class Quiz Challenge

Open a new Colab notebook and do the following:

1. Click here to download the [data.xlsx](./data.xlsx) file.
2. Upload the file to your colab notebook by clicking on the folder icon on the left side of the screen and then 
   clicking on the upload icon. Or you can drag and drop the file into the notebook.
1. Import the file to a dataframe using the `pandas` library and display the contents of the dataframe.
3. Change the name of the first column to **Date** and display the updated dataframe.
3. Add a new column to the dataframe called **Sum** that is the sum of columns 2-4. Display the updated dataframe.
4. Save the updated dataframe to a new Excel file called **output.xlsx** using the `pandas` library. In a few seconds, 
   the file will appear in your notebook's file list. Download the file to your computer and check the contents.

Save changes to your Google Drive and submit the link to the notebook in your Pre-Class Quiz.