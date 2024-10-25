# In Class Excersise: Working with Excel Files in Python

In this class excersise, we will learn how to work with Excel files in Python. We will read Excel files into pandas dataframes, write dataframes to Excel files, and perform some basic data manipulation tasks.

## Part 1: Streamflow Data

In Unit 1, we worked with a set of streamflow data from gauges on the Provo River. In this exercise, we will import a copy of that data in Excel format, perform some data anlysis, and write the results back to a new Excel file.

### Step 1: Uploading the Excel File to Colab.

1. Download the Excel file from [precip_data.xlsx](precip_data.xlsx).
2. Upload the file to your Colab environment by clicking on the folder icon on the left sidebar, and then clicking on the upload icon. Or you can drag and drop the file into the file browser.

### Step 1: Read the Data

 Next will use the `pandas` library to read the data into a dataframe.

```python