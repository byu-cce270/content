
#  Reading: Gspread and API's

---

There are many ways to interact with data in Python. Last time we learned about how to read in a txt or csv files. There are many other ways to interact with data, and one of the most powerful ways is through APIs. Some include using libraries like gspread to interact with Google Sheets.

### Thing to Look Out For
 - What is an API and how it is used.
 - How to allow API access for a project.
 - What is gspread and how to use it.

---

## What is an API

API stands for Application Programming Interface. It is a set of rules and protocols that allow one software application to interact with another. APIs are used to allow different software applications to communicate with each other. APIs are everywhere, from social media to weather apps, from payment services to authentication services.

Watch this video bellow to learn more about APIs:

<iframe width ="560" height="315" src="https://www.youtube.com/embed/s7wmiS2mSXY?si=8KPdJAYfLwC1Hxht" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Think to yourself: How are APIs us in the as a civil engineer or construction management career?

---

## How to Allow API Access for a Project

1. Head to this link: [Google Dashboard](https://console.developers.google.com/){:target="_blank"}

2. Click on the link that says "+ Enable APIs and Services".

3. Find the box labeled "search for APIs & Services", it should look like this: 

![apilibrary](https://github.com/user-attachments/assets/ab05f2cb-aaae-4e6e-a456-c2ff19cccbbc)

4. Search for "Google Sheets API" and enable it. 

![googlesheetsapi](https://github.com/user-attachments/assets/e1be68aa-7ffa-403f-a384-ec11ec3036f1)

5. Search for ""Google Drive API" and enable it as well.

![googledriveapi](https://github.com/user-attachments/assets/683ffac4-f0f9-4999-9d05-85abfb64233a)

---

## What is Gspread

Gspread is a Python library that allows you to interact with Google Sheets. It allows you to read, write, and share data in Google Sheets. It is a powerful tool that can be used to automate tasks and create reports. With gspread we can:

 - Open a spreadsheet by title or url
 - Read data from sheets into python
 - Use python to change the data in a sheet
 - Create new sheets
 - Share sheets with others
 - And much more!

All the documentation for gspread can be found [here](https://gspread.readthedocs.io/en/latest/){:target="_blank"}. 

Now let's see how to use gspread.

---

## Installing Gspread

To use gspread, you will normally need to install the library. However, since we are working in Google Colab, this library is already installed. If you are working in another coding environment, you can install this library this by running the following command in your terminal:

```bash
!pip install gspread
```

---

## Importing and Authenticating Gspread

To use gspread, you need to import it. You can do this by using the following command:

```python
import gspread
```

Then you need to authenticate your account. This is done by running the following command:

```python
from google.auth import default
creds, _ = default()
gc = gspread.authorize(creds)
from google.colab import auth
from google.auth import default
from google.colab import auth
auth.authenticate_user()
```

If you prefer, you can do all of this in one cell or code block as follows:

```python
import gspread
from google.auth import default
creds, _ = default()
gc = gspread.authorize(creds)
from google.colab import auth
from google.auth import default
from google.colab import auth
auth.authenticate_user()
```

---

## Reading Data from Google Sheets

To read data from a Google Sheet, you need to open the spreadsheet. This is the entire google sheet document that has several pages or worksheets with data and information. Then select the worksheet or page that you want to read. Once you have selected the worksheet, you can read the data from the worksheet.

### Opening a Google Sheet

To read data from a Google Sheet, you need to open the sheet and then read the data. There are several ways to read in the data from a Google Sheet. Here is an example of how to read in the data from a Google Sheet:

```python
spreadsheet = gc.open('Name of your Google Sheet')
``` 

In this example, 'Name of your Google Sheet' is the name of the Google Sheet that you want to open. **Note that the name of the Google Sheet is case-sensitive. If you have multiple Google Sheets with the same title, only the latest sheet will be opened by this method without throwing an error.** 

For this class, we will be sharing google sheets for use with gspread by providing you with a public URL for the 
sheet. Therefore, we ask that you open the sheets using the 
URL method. Here is an 
example of 
how to open a sheet by URL:

```python
spreadsheet = gc.open_by_url('URL of your Google Sheet')
```

### Selecting a Worksheet

Once you have opened the sheet, you can read the data from the sheet. To select a Worksheet, you can use the following commands:

By index. Worksheet indexes start from zero:

```python
worksheet = spreadsheet.get_worksheet(0)
```

Or by title:

```python
worksheet = spreadsheet.worksheet("January")
```

Or the most common case: Sheet1:
    
```python
worksheet = spreadsheet.sheet1
```

To get a list of all worksheets:
```python
worksheet_list = spreadsheet.worksheets() 
```

### Creating a spreadsheet and worksheet 

Sometime you will want to create your own spreadsheet from scratch with your code. To create a new spreadsheet, you can use the following command:

```python
spreadsheet = gc.create('A new spreadsheet')
```

Then to create a worksheet in the spreadsheet, you can use the following command:

```python
worksheet = spreadsheet.add_worksheet(title="A worksheet", rows="100", cols="20")
```

### Important Naming Tip

In all the examples above, you can see that the variable names are `spreadsheet` and `worksheet`. You can name these variables whatever you want. However, it is important to remember that these variables are objects that represent the Google Sheet and the Worksheet. So it is a good idea to name them something that makes sense. For example, if you are reading in data from a Google Sheet that contains sales data, you could name the variables `sales_sheet` and `sales_worksheet`.

---

## Reading Data

Once you have selected the worksheet, you can read the data from the worksheet. To read the data from a worksheet, you can use the following command:

```python
data = worksheet.get_all_values()
```

This will return a list of lists, where each sub-list represents a row in the worksheet. For example, if the worksheet contains the following data:

| Name  | Age
|-------|-----
| Alice | 25
| Bob   | 30
| Carol | 35

The `data` variable will contain the following list of lists:

```python
[['Name', 'Age'], ['Alice', '25'], ['Bob', '30'], ['Carol', '35']]
```

You can also get all values from a worksheet and return it as a list of dictionaries. This is useful when you have a header row in your worksheet. To do this, you can use the following command:

```python
data = worksheet.get_all_records()
```

This will return a list of dictionaries, where each dictionary represents a row in the worksheet. For example, if the worksheet contains the following data:

| Name  | Age
|-------|-----
| Alice | 25
    
The `data` variable will contain the following list of dictionaries:

```python
[{'Name': 'Alice', 'Age': '25'}]
```

There are many other ways to read data from a Google Sheet, including from specific cells, ranges, row, or columns. You can find more information in the [gspread documentation](https://docs.gspread.org/en/latest/user-guide.html#getting-a-cell-value){:target="_blank"}.

---

## Handling large data sets

At this point we already know to loop through the data and run and print it out. We can use loop to go in and extra data from the list of lists or list of dictionaries to get the data we need and use it how we want.  

Later in this unit, we will learn about the libraries pandas and numpy which will allow us to work with data in a more efficient way. Pandas and numpy are powerful libraries for data manipulation and analysis. We can use them to read in the data from the Google Sheet and manipulate it. The simplest way to get data from a sheet to a pandas or numpy DataFrame is with get_all_records():

```python
dataframe = pd.DataFrame(worksheet.get_all_records())
```

```python
array = np.array(worksheet.get_all_values())
```

We will go over this in more detail in the later but you may see some code we provide use these libraries.

---

## Writing Data to Google Sheets

To write data to a Google Sheet, you need to select the worksheet that you want to write to and then write the data. There are several ways to write data to a Google Sheet. Here is an example of how to write data to a Google Sheet:

```python
worksheet.update('A1', 'Hello World!')
```

In this example, 'A1' is the cell that you want to write to, and 'Hello World!' is the data that you want to write. You can also write data to a range of cells:

```python
worksheet.update('A1:B2', [['Hello', 'World'], ['Goodbye', 'World']])
```

This will write the data 'Hello' to cell A1, 'World' to cell B1, 'Goodbye' to cell A2, and 'World' to cell B2. You can also write data to a specific row or column by using coordinates:

```python
worksheet.update_cell(1, 1, 'Hello')
```

This will write the data 'Hello' to cell A1. Antoher way to write data to a Google Sheet is to append data to the end of the worksheet. This is useful when you want to add new data to the sheet without overwriting existing data. Say we have a worksheet that looks like this:

| Name  | Age
|-------|-----
| Alice | 25

We can append data to a Google Sheet, you can use the following command:

```python
worksheet.append_row(['Hello', 'World'])
```

The sheet will look like this:

| Name  | Age
|-------|-----
| Alice | 25
| Hello | World

This will append the data 'Hello' to cell A1 and 'World' to cell B1. You can also append multiple rows at once:

```python
worksheet.append_rows([['Hello', 'World'], ['Goodbye', 'World']])
```

This will append the data 'Hello' to cell A1 and 'World' to cell B1, and 'Goodbye' to cell A2 and 'World' to cell B2. You can also append a dictionary to the worksheet:

```python
worksheet.append_row({'Name': 'Alice', 'Age': 25})
```

The sheet will look like this:

| Name  | Age
|-------|-----
| Alice | 25

This will append the data 'Alice' to cell A1 and '25' to cell B1. You can also append multiple dictionaries at once:

```python
worksheet.append_rows([{'Name': 'Alice', 'Age': 25}, {'Name': 'Bob', 'Age': 30}])
```

The sheet will look like this:

| Name  | Age
|-------|-----
| Alice | 25
| Bob   | 30

**For most of the HW and In Class assignments, we will be using the append_row method to write data to the Google Sheet.**

There are many other ways to write data to a Google Sheet, including to specific cells, ranges, rows, or columns. You can find more information in the [gspread documentation](https://docs.gspread.org/en/latest/user-guide.html#updating-cells){:target="_blank"}. You can also look here to see how to code in data validation, formatting, and other features.

---

## Pre-Class Quiz Challenge

For your pre-class quiz, you need to follow the instructions to Allow API Access for a Project. Then you will create a new Google doc and put screenshot of the Google API Dashboard showing that you have enabled the Google Sheets API and Google Drive API. Your image should look like this but the blue botton should say "Manage" instead of "Enable":

![googlesheetsapi](https://github.com/user-attachments/assets/e1be68aa-7ffa-403f-a384-ec11ec3036f1)

Submit a link to the completed Google Doc in your Pre-Class Quiz. If you have any questions, please reach out in Teams or met with a TA before class to make sure you are set up correctly. We will not be taking time in class to help you set up your API access.
