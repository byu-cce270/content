#  Reading: Combining & Grouping Data Sets in Python

---

# Pre-Class Reading Assignment

On the O'Reilly's website read the following chapters in the Python Data Science Handbook, 2nd Edition:

[Chapter 18: Combining Datasets: Concat and Append](https://learning.oreilly.com/library/view/python-data-science/9781098121211/ch18.html){:target="_blank"} (Section titled: Simple Concatenation with pd.concat)<br>
[Chapter 19: Combining Datasets: Merge and Join](https://learning.oreilly.com/library/view/python-data-science/9781098121211/ch19.html){:target="_blank"} (from 'Categories of Joins' to the end of the chapter)<br>
[Chapter 20: Aggregation and Grouping](https://learning.oreilly.
com/library/view/python-data-science/9781098121211/ch20.html#ch_0308-aggregation-and-grouping_planets-data){:target="_blank"} (everything up to the "Iteration over Groups" heading)

Remember that you may have to sign in with your byu netid to access the reading content.

# Optional Reading
Here are some additional chapters in other O'Reilly books that may be helpful for this assignment:

- Plotting with Pandas directly (Learning pandas)
    - [Chapter 11: Visualizaton](https://learning.oreilly.com/library/view/learning-pandas/9781783985128/ch11s02.html){:target="_blank"} (Read through the end of Chapter 11) 
- Groupby (Pandas for Everyone: Python Data Analysis, First Edition)
    - [Chapter 10:Data Aggregation and Group Operations](https://learning.oreilly.
    com/library/view/python-for-data/9781491957653/ch10.html#groupby_mech_iteration){:target="_blank"}. (Read 10.1 
    to 10.4)

Both books are available on the O'Reilly website and provide good overviews and examples of using pandas for data 
analysis.. 

## Things to look out for
- What is the .concat method and what does it do?
- How is the .merge method used and what does it do?
- What does the 'on' keyword do when merging DataFrames?
- What is the .groupby operation and when do you use it?


## NaNs and Missing Values in Pandas

In Python, sometimes a dataset has values that are empty or missing. These values are represented as NaN (Not a Number) in Pandas. If this happens, you typically need to do something with the NaN values before you can operate on the dataset. You can use the `.isna()` method to find NaN values in a DataFrame and the `.fillna()` method to replace NaN values with a specified value. Here is an example of how to use these methods:


```python
import pandas as pd
import numpy as np

data = pd.DataFrame(np.array([[1, 2, np.nan], [3, np.nan, 6], [np.nan, 8, 9]]), columns=['A', 'B', 'C'])
print(data)
# Output:
     A    B    C
0  1.0  2.0  NaN
1  3.0  NaN  6.0
2  NaN  8.0  9.0

# Find NaN values
print(data.isna())

# Output:
       A      B      C
0  False  False   True
1  False   True  False
2   True  False  False

# Replace NaN values with 0
data_filled = data.fillna(0)
print(data_filled)

# Output:
     A    B    C
0  1.0  2.0  0.0    
1  3.0  0.0  6.0
2  0.0  8.0  9.0
```
You can replace the NaN's with any value, but typically you will replace them with 0 or the mean of the column.

For numeric columns you can also use the `.fillna()` method with the `method` parameter to propagate non-NaN values forward or backward.

Here is an example of how to use the `method` parameter with `.fillna()` using the mean value of the column:
```python
df['A'].fillna(df['A'].mean(), inplace=True)  # Fill with mean
```
And here is using the backfill and forword fill methods:

```python
import pandas as pd
import numpy as np
data = pd.DataFrame(
    np.array([[1, 2, np.nan], [np.nan, np.nan, 6], [7, 8, np.nan]]),
    columns=['A', 'B', 'C'])       
print(data)
# Output:
#      A    B    C
# 0  1.0  2.0  NaN
# 1  NaN  NaN  6.0
# 2  7.0  8.0  NaN


# Forward fill NaN values
data_ffill = data.fillna(method='ffill')
print(data_ffill)
# Output:
    
#      A    B    C
# 0  1.0  2.0  NaN
# 1  1.0  2.0  6.0
# 2  7.0  8.0  6.0


# Backward fill NaN values
data_bfill = data.fillna(method='bfill')
print(data_bfill)
# Output:
#      A    B    C
# 0  1.0  2.0  6.0
# 1  7.0  8.0  6.0
# 2  7.0  8.0  NaN
```


You can also drop rows or columns with NaN values using the `.dropna()` method. Here is an example:
```python
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.array([[1, 2, 3], [4, np.nan, 6], [7, 8, 9]]),
    columns=['A', 'B', 'C'])

print(data)
# Output:
#      A    B  C
# 0  1.0  2.0  3.0
# 1  4.0  NaN  6.0
# 2  7.0  8.0  9.0

# Drop rows with NaN values
data_dropped = data.dropna()
print(data_dropped)
# Output:
#      A    B  C
# 0  1.0  2.0  3.0
# 2  7.0  8.0  9.0

# Drop columns with NaN values
data_dropped_cols = data.dropna(axis=1)
print(data_dropped_cols)
# Output:
#      A  C
# 0  1.0  3.0
# 1  4.0  6.0
# 2  7.0  9.0
```
This command drops any row (or column) that contains at least one NaN value. Be careful, you may drop more data than you intend to if you have many NaN values in your dataset.

---

## Pandas append and concat

Pandas has a method called `.append()` that allows you to add rows to a DataFrame.  This is useful when you want to combine data from multiple sources or add new data to an existing DataFrame.  Here is an example of how to use the `.append()` method:

```python
import pandas as pd

data1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
data2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
combined_data = data1.append(data2, ignore_index=True)
print(combined_data)

# Output:
   A  B 
0  1  3
1  2  4
2  5  7
3  6  8
```
The `ignore_index=True` parameter is used to reset the index of the combined DataFrame. If you don't use this parameter, the index of the original DataFrames will be preserved. But in this case you want the new index to be continuous to add the additional rows. 

Pandas also has a method called `.concat()` that allows you to concatenate two or more DataFrames along a particular axis. This is useful when you want to combine data from multiple sources or add new data to an existing DataFrame. Here is an example of how to use the `.concat()` method:

```python
import pandas as pd

data1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
data2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
combined_data = pd.concat([data1, data2], ignore_index=True)
print(combined_data)

# Output:
   A  B
0  1  3
1  2  4
2  5  7
3  6  8
```
In this case the ignore_index=True parameter is used to reset the index of the combined DataFrame. If you don't use this parameter, the index of the original DataFrames will be preserved. You want to create a continuous index for the new DataFrame.

As you can see, `.append()` and `.concat()` are similar, and can often be used interchangeably.

## Pandas groupby

One of the most useful methods in pandas is the `.groupby()` method. It is similar to a pivot table in Excel or Google Sheets in that it allows you to group data based on one or more columns and then perform operations on the groups. Here is an example of how to use the `.groupby()` method:

```python
import pandas as pd

data = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar'],
                     'B': [1, 2, 3, 4],
                     'C': [5, 6, 7, 8]})
print(data)
grouped_data = data.groupby('A').sum()
print(grouped_data)

# first print statement output:
     A  B  C
0  foo  1  5
1  bar  2  6
2  foo  3  7
3  bar  4  8

# second print statement output:
     B   C 
A
bar  6  14
foo  4  12
```
The code groups the data by the values in column 'A' and then sums the values in columns 'B' and 'C' for each group.  You can also group by multiple columns by passing a list of column names to the `.groupby()` method.

```python
import pandas as pd

data = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar'],
                     'B': [1, 2, 3, 4],
                     'C': [5, 6, 7, 8]})

print(data)
grouped_data = data.groupby(['A', 'B']).sum()
print(grouped_data)

# first print statement output:
     A  B  C
0  foo  1  5
1  bar  2  6
2  foo  3  7
3  bar  4  8

# second print statement output:
A   B  C
bar 2  6
    4  8
foo 1  5
    3  7
``` 

In this case there are two levels of grouping: first by column 'A' and then by column 'B'.  The resulting DataFrame shows the sum of column 'C' for each group. The column has the values of 'foo' and 'bar' as the first level of the index, and the column 'B' values as the second level of the index which are 1, 2, 3, and 4. The command groups them together by the values in column 'A' and then by the values in column 'B'. The value 'foo' from column 'A' has two values 1 and 3 from column 'B' and the sum of column 'C' for those values is 12. The value 'bar' from column 'A' has two values 2 and 4 from column 'B' and the sum of column 'C' for those values is 14. The 'sum' command isn't really used since there is only a single value in each group. But with large datasets, you can use the sum command to aggregate the data in each group based on multiple category combinations.

## Pandas datetime

Pandas has a powerful set of tools for working with dates and times. In engineering and construction, it is common to deal with data associated with a particular date. For example, when reading datasets from Excel or CSV files, the first column in a table is often a date. When you import such a column to a DataFrame, the date values are imported as strings. However, we need to convert the strings to actual datetime objects in order to fully utilize Pandas for analyzing and plotting the data associated with dates. Fortunately, you can use the `.to_datetime()` function to convert a column of strings to datetime objects. Here is an example dataset with a datetime column and two other columns:

```python   
import pandas as pd
data = pd.DataFrame({'date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                     'value1': [1, 2, 3],
                     'value2': [4, 5, 6]})
data['date'] = pd.to_datetime(data['date'])
print(data)
# Output:
        date  value1  value2
0 2022-01-01       1       4
1 2022-01-02       2       5
2 2022-01-03       3       6
```
You often want the datetime column to be the index of the DataFrame so you can access the data by date. We can achieve this using the `.set_index` method. So when we import a dataset with a date column, we first convert to datetime, then set it to be the index of the DataFrame. Here is an example using the previous data frame:

```python  
import pandas as pd

# use the 'data_range' command to create a date range
data = pd.DataFrame({
    'date': pd.date_range(start='2022-01-01', end='2022-01-10'),
    'value1': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'value2': [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
})

# Convert the 'date' column to datetime objects
data['date'] = pd.to_datetime(data['date'])

# Set the 'date' column as the index
data.set_index('date', inplace=True)

print(data)
```

The output would be as follows:

```python
    #output:
                value1  value2
    date                      
    2022-01-01      10      15
    2022-01-02      20      25
    2022-01-03      30      35
    2022-01-04      40      45
    2022-01-05      50      55
    2022-01-06      60      65
    2022-01-07      70      75
    2022-01-08      80      85
    2022-01-09      90      95
    2022-01-10     100     105
```

Now the date column is the index of the DataFrame, and we can access the data by date. For example, to select data for a specific date or a range of dates, you can use the `.loc` method. Here is an example:

```python
# Select data for a specific date
selected_data = data.loc['2022-01-02']
print("data for 2022-01-02:")
print(selected_data)

# Select data for a range of dates
date_range_data = data.loc['2022-01-02':'2022-01-03']
print("\ndata from 2022-01-02 to 2022-01-03:")
print(date_range_data)
```

The output would be as follows:

```text
Data for 2022-01-02:
value1    20
value2    25
Name: 2022-01-02 00:00:00, dtype: int64

Data from 2022-01-02 to 2022-01-03:
            value1  value2
date                      
2022-01-02      20      25
2022-01-03      30      35
```

If you have a DataFrame with a datetime index, you can easily resample the data to a different frequency using the `.resample()` method. For example, you can resample daily data to monthly data or hourly data to daily data. Here is an example:

```python
# Resample daily data to monthly data
monthly_data = data.resample('M').sum()
print("Monthly data:")
print(monthly_data)
```

The output would be as follows:

```text
Monthly data:
            value1  value2
date
2022-01-31     550     600
```

In this example, the `.resample('M')` method resamples the daily data to monthly data by summing the values for each month. You can also resample the data to other frequencies such as 'D' for daily, 'H' for hourly, 'W' for weekly, etc.

A datetime index is also useful for plotting time series data. You can use the `.plot()` method to plot the data directly from the DataFrame. Here is an example:

```python
import matplotlib.pyplot as plt

# Plot the data
data.plot()
plt.show()
```
Each of the columns are then plotted against the date index.

---


# Pre-Class Quiz Challenge
Open the following notebook and complete the instructions in the markdown:

<a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit3/03_continuing_pandas/(Starter_Notebook)_Pre_Continuing_with_Pandas.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Rename it something like "(Your_Name)_Pre_Continuing_with_Pandas.ipynb".

Save changes to your Google Drive and submit the link to the notebook in your Pre-Class Quiz.

---

## Turning in/Rubric

**_REMINDER_** - For this class, **you will only turn in the links to your colab notebooks**. You will get a 0 for this assignment if you turn in a python file or a link that is not correct, wrong assignment, or does not give editor permission.

**Rubric:**

|                      Item                      | Points Possible |
|:----------------------------------------------:|:---------------:|
| <div style="text-align: right">**Total**</div> |        3        |

---

The following is not a part of the rubric, but specifies how you can lose points. For example: if you fail to share your link correctly.

| **Reasons for Points Lost** |    **Amount**     |  
|:---------------------------:|:-----------------:|
|   Link shared incorrectly   |       -10%        | 
