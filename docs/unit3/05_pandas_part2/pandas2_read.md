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
Here are some chapters in other O'Reilly books that may be helpful for this assignment:

- Plotting with Pandas directly (Learning pandas)
    - [Chapter 11: Visualizaton](https://learning.oreilly.com/library/view/learning-pandas/9781783985128/ch11s02.html) 
   {:target="_blank"} (Read through the end of Chapter 11) 
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


---

Pandas can help with missing data which are typically represented in your data frames as NaN values.  Here is a short example of using Panda's to find and replace NaN values.

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

---
#Panda's append and concat
Pandas has a method called .append() that allows you to add rows to a DataFrame.  This is useful when you want to combine data from multiple sources or add new data to an existing DataFrame.  Here is an example of how to use the .append() method:

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
The ignore_index=True parameter is used to reset the index of the combined DataFrame.  If you don't use this parameter, the index of the original DataFrames will be preserved."
But in this case you want the new index to be continuous to add the additional rows. 

# Concatenating DataFrames
Pandas also has a method called .concat() that allows you to concatenate two or more DataFrames along a particular axis.  This is useful when you want to combine data from multiple sources or add new data to an existing DataFrame.  Here is an example of how to use the .concat() method:

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
In this case the ignore_index=True parameter is used to reset the index of the combined DataFrame.  If you don't use this parameter, the index of the original DataFrames will be preserved. You want to create a continuous index for the new DataFrame.

#

#Panda's groupby
The .groupby() method in Pandas is used to group data by one or more columns.  This is useful when you want to perform operations on groups of data within a DataFrame.  Here is an example of how to use the .groupby() method:

```python
import pandas as pd
data = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar'],
                     'B': [1, 2, 3, 4],
                     'C': [5, 6, 7, 8]})
print(data)
grouped_data = data.groupby('A').sum()
print(grouped_data)
# Output:
# first print statement
     A  B  C
0  foo  1  5
1  bar  2  6
2  foo  3  7
3  bar  4  8

# second print statement
     B   C 
A
bar  6  14
foo  4  12
```
The code groups the data by the values in column 'A' and then sums the values in columns 'B' and 'C' for each group.  You can also group by multiple columns by passing a list of column names to the .groupby() method.

```python
import pandas as pd
data = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar'],
                     'B': [1, 2, 3, 4],
                     'C': [5, 6, 7, 8]})
grouped_data = data.groupby(['A', 'B']).sum()
print(grouped_data)
# Output:
# first print statement
     A  B  C
0  foo  1  5
1  bar  2  6
2  foo  3  7
3  bar  4  8

# second print statement
        C
A   B
bar 2  6
    4  8
foo 1  5
    3  7
``` 

In this case there are two levels of grouping: first by column 'A' and then by column 'B'.  The resulting DataFrame shows the sum of column 'C' for each group. The column has the values of 'foo' and 'bar' as the first level of the index, and the column 'B' values as the second level of the index which are 1, 2, 3, and 4. The command groups them togehter by the values in column 'A' and then by the values in column 'B'. The value 'foo' from column 'A' has two values 1 and 3 from column 'B' and the sum of column 'C' for those values is 12. The value 'bar' from column 'A' has two values 2 and 4 from column 'B' and the sum of column 'C' for those values is 14. The 'sum' command isn't really used since there is only a single value in each group. 

# Panda's datetime
Pandas has a powerful set of tools for working with dates and times.  You can use the pd.to_datetime() function to convert a column of strings to datetime objects.  Here is an with a datetime column and two other columns:

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
````
YOu often want the datetime column to be the index of the DataFrame so you can access the data by date. Here is an example using the previous data frame:

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

```python
# Select data for a specific date
selected_data = data.loc['2022-01-02']
print("Data for 2022-01-02:")
print(selected_data)

# Select data for a range of dates
date_range_data = data.loc['2022-01-02':'2022-01-03']
print("\nData from 2022-01-02 to 2022-01-03:")
print(date_range_data)
```

# Output:
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



We can now select the data by date. 
```python
import pandas as pd
data = pd.DataFrame({'date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                     'value1': [1, 2, 3],
                     'value2': [4, 5, 6]})
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)
print(data.loc['2022-01-02'])
# Output:
value1    2
value2    5
Name: 2022-01-02 00:00:00, dtype: int64

```












# Pre-Class Quiz Challenge
Open the following notebook and complete the instructions in the markdown:

<a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit3/04_pandas_part2/preclass_pandas_part2.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>


Save changes to your Google Drive and submit the link to the notebook in your Pre-Class Quiz.
