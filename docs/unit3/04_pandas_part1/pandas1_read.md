#  Reading: Pandas Series and DataFrame

---

# Pre-Class Reading Assignment

Read the following chapters and sections in the
Python Data Science Handbook, 2nd Edition:

[Chapter 13: Introducing Pandas Objects](https://learning.oreilly.
com/library/view/python-data-science/9781098121211/ch13.html){:target="_blank"} (up to the Pandas Index Object subheading)
</br>[Chapter 14: Data Indexing and Selection](https://learning.oreilly.
com/library/view/python-data-science/9781098121211/ch14.html){:target="_blank"} (just the Data Selection in 
DataFrames section)
</br>[Chapter 20: Aggregation and Grouping](https://learning.oreilly.
com/library/view/python-data-science/9781098121211/ch20.html#ch_0308-aggregation-and-grouping_planets-data)
{:target="_blank"} (stop at the "Iteration over Groups" section)

Remember that you may have to sign in with your byu netid.

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

# Pre-Class Quiz Challenge
Open the following notebook and complete the instructions in the markdown:

<a href="https://colab.research.google.com/drive/1KnfUY_SD_SPUh0HjIvaLvqic42LhMXwT#scrollTo=YZjJdSzBaBLK" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Save changes to your Google Drive and submit the link to the notebook in your Pre-Class Quiz.
