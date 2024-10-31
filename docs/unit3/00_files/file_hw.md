#  HW: Reading and Writing Files

**Purpose:** In this assignment you are given a csv file from the UDOT. You are going to go through the file and count how many speed limit signs there are of the various speed limits. You can find where to access this data [here](https://data-uplan.opendata.arcgis.com/datasets/uplan::speed-limit-signs-1/explore?location=40.705286%2C-111.838968%2C12.49 )

## Instructions

1. First, make a copy of the starter sheet here: <a href="https://colab.research.google.com/github/byu-cce270/content/blob/main/docs/unit3/00_files/3_1_Files_HW.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
2. Rename it something like "[Your Name] 3_1_Files_HW"

___

### Uploading your file to the Colab Notebook
1. Open this link to a Google spreadsheet called [Signs](https://docs.google.com/spreadsheets/d/1BZ7EEaaEOXzzgQUbLKVCEBnU4SpjnjWYlR34aQlz4F0/edit?gid=1541112318#gid=1541112318). It contains Speed limit sign data such as the condition of the sign, the speed, and other info.
2. Once opened, go to the file tab --> download --> select Comma Separated Files (.csv)
3. Go back to your Colab notebook and upload your file. For reference, the preclass reading for files has a step-by-step guide on how to upload a file to a Colab notebook

---
### Read in your file
1. In the first code block, read in the 'signs' file in reading mode.
2. In a new line, read your file into a list of strings where there is one string for each line in the file. Save this as a variable. This will allow us easier access to read our data later.

---

### Sign Counter Code
1. Now time to do the real work! In the second code block, you are given a dictionary named "Sign_counter" where the keys are the MPH of the signs and the value is the signs with the corresponding MPH. Note they are all initialized to zero. The objective is to read our given file and find the total number of each sign. This will be WAY faster than counting it on our own!
2. In a new line underneath the given dictionary, write code that will loop through the list of strings you imported from the file. For each line (string) you will loop through the items in the dictionary to see if the speed limit is in the string. If so, increment the corresponding counter. 

      - For example, since Sign_counter has a key value of "10" if the file contains an MPH sign with a speed limit of 10, then I would add 1 to the corresponding value of "10" in Sign_counter for EACH occurrence of "10" in the file. This process would be the same for each key value of Sign_counter.
     - HINT: Refer back to HW 2.4 (IF statements) for how to compare lists, and HW 2.5 (Dictionaries) for how to access the values of the keys in a dictionary.
   
3. In the next code block, print each MPH speed limit sign in Sign_counter with its NEW value.
4. When done, here are the values you should get:

![Sign_Counter_HW](https://github.com/user-attachments/assets/5c6e7b82-2895-4a98-b600-915254db8fb0)

### Creating Your New File 
1. In the last code block you will be creating a new file and put in the new values of Sign_counter.
2. In the first line, open a new file in writing mode and name it something like "sign_values". Make sure to make the file a .txt as we just want a text file.
3. Now, write each key and its corresponding value of Sign_counter into your new file. You will need to write each key and its value line by line. Make sure to insert the values on a new line into your file.
     - HINT:  When writing, you can use \n to make a new line in your file. Look at the textbook section from the pre-class reading for examples of using "\n" with files.
4. To check and make sure the file has been created, click on the folder icon on the far left of your screen. Look for a new ".txt" file
   
![FILEHWPRACTICE](https://github.com/user-attachments/assets/0eacbc96-4e6d-49be-a8d7-4aba055a4ef8)

5. Open the file and **double-check that your values are on separate lines**. Here's an example of what your file should look like:

![Screenshot 2024-10-31 134127](https://github.com/user-attachments/assets/f04fea9a-024d-4922-a118-752ea23572cc)


# Turning In/Rubric

Turn on sharing and editing. Turn in the link to the Learning Suite feedback box. ONLY turn in the workbook. **You don't need to turn in the file you created. **


| Description                          | Points |
|--------------------------------------|--------|
| File is imported correctly to a list | 6      |
| Sign counters are properly calculated  | 12     |
| Results are correctly printed        | 6      |
| Results are saved to a text file  and on separate lines   | 6      |
| Total                                | 30     |





