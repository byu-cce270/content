#  Reading: Pandas Series and DataFrame

---

# Pre-Class Reading Assignment

Read the following chapters and sections in the
Python Data Science Handbook, 2nd Edition:

[Chapter 13: Introducing Pandas Objects](https://learning.oreilly.
com/library/view/python-data-science/9781098121211/ch13.html){:target="_blank"} (up to the Pandas Index Object subheading)
</br>
[Chapter 14: Data Indexing and Selection](https://learning.oreilly.
com/library/view/python-data-science/9781098121211/ch14.html){:target="_blank"} (just the Data Selection in 
DataFrames section)

Remember that you may have to sign in with your byu netid to access the reading content.

## Things to look out for
- What is a Pandas Series and a Pandas DataFrame?
- How do you create a Pandas Series and a Pandas DataFrame?
- What does it mean to index in a Pandas DataFrame and how do you index?

## Reading CSV files into Pandas DataFrames

Pandas is a powerful data manipulation library in Python. It is built on top of NumPy and provides an easy-to-use 
data structure called a DataFrame. A DataFrame is a two-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dictionary of Series objects. It is generally the most commonly used pandas object. 

Pandas can read data from a variety of file formats, including CSV files. The `read_csv()` function in pandas is 
used to read data from a CSV file and create a DataFrame object. When working in Google Colab, you can upload a CSV file to your Colab 
file folder and then read it into a DataFrame using the following code:

```python
import pandas as pd

df = pd.read_csv('filename.csv')
```

Each of the columns in the CSV file will be read into a Series object in the DataFrame. 

## Reading Excel files into Pandas DataFrames

Pandas can also read data from Excel files. The `read_excel()` function in pandas is used to read data from an Excel file and create a DataFrame object. The `read_excel()` function has many parameters that allow you to specify how to read the data. When working in Google Colab, you can upload an Excel file to your Colab file folder and then read it into a DataFrame using the following code:

```python
import pandas as pd

df = pd.read_excel('filename.xlsx')
```

If you have multiple sheets in the Excel file, you can specify the sheet name or index using the `sheet_name` 
parameter as follows:

```python
df = pd.read_excel('filename.xlsx', sheet_name='data')
```

Once again, each of the columns in the Excel file will be read into a Series object in the DataFrame.

---

## Useful Methods for DataFrames

The following methods are useful when working with DataFrames:

| Method | Description                                                            |
| --- |------------------------------------------------------------------------|
| `head()` | Returns the first n rows of the DataFrame.                             |
| `tail()` | Returns the last n rows of the DataFrame.                              |
| `info()` | Provides a concise summary of the DataFrame.                           |
| `describe()` | Generates descriptive statistics of the DataFrame.                     |
| `shape` | Returns a tuple representing the dimensionality of the DataFrame.      |
| `columns` | Returns the column labels of the DataFrame.                            |
| `index` | Returns the index (row labels) of the DataFrame.                       |
| `set_index()` | Sets the DataFrame index using an existing column.                     |
| `to_datetime()` | Converts date strings in a series of a DataFrame to a datetime format. |
| `values` | Returns the values of the DataFrame as a 2D NumPy array.               |
| `sort_values()` | Sorts the DataFrame by the values along the specified axis.            |
| `dropna()` | Removes missing values from the DataFrame.                             |
| `fillna()` | Fills missing values in the DataFrame.                                 |
| `groupby()` | Groups the DataFrame using a mapper or by a Series of columns.         |
| `to_csv()` | Writes the DataFrame to a CSV file.                                    |
| `to_excel()` | Writes the DataFrame to an Excel file.                                 |

These methods can help you manipulate and analyze data in a DataFrame efficiently.

# Pre-Class Quiz Challenge
Open the following notebook and complete the instructions in the markdown:

<a href="https://colab.research.google.com/drive/1KnfUY_SD_SPUh0HjIvaLvqic42LhMXwT#scrollTo=YZjJdSzBaBLK" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Save changes to your Google Drive and submit the link to the notebook in your Pre-Class Quiz.
