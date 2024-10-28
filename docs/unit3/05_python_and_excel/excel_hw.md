# Homework - Working with Excel Files in Python

**Objective:** Learn how to export data and charts to an Excel file.

In this homework assignment, you will import an Excel file containing monthly precipitation data for a set of weather stations in Utah. You will read the data into a pandas dataframe, perform some data analysis, and write the results back to a new Excel file. You will also create a chart of the data and include it in the Excel file.

To begin, create a new Colab notebook and name it '**[yourname]_excel_hw.ipynb'**. Then follow the instructions below. Create and organize your code in cells in the notebook as you go.

## Part 1: Import your data

Do the following to import the data:

1. Install the **xlsxwriter** package and import the required packages (**xslxwriter**, **pandas**, and **matplotlib.pyplot**).
2. Download the Excel file with the precip data from [precip_data.xlsx](precip_data.xlsx). Open the file in Excel to 
   see what the data looks like. You will see that there are three sheets, one for Salt Lake City, one for Utah 
   State, and one for BYU. Each sheet contains monthly precipitation data going back several years. For this 
   exercise, we will focus on the BYU data.
3. Upload the file to your Colab environment. You can do this by clicking on the folder icon on the left sidebar, then clicking on the upload icon. Or you can drag and drop the file into the file browser.
4. Read the data into a pandas dataframe. Use the `read_excel` method and read the sheet named **'BYU'**.
5. Display the first few rows of the dataframe to see what the data looks like.
6. 

## Instructions

