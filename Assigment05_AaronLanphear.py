# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ALanphear,2.13.21,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
dicRowNew = {}  # A row of new data inputted by user
lstRow = []  # A list of rows to help create dictionary rows
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # To capture the user option selection
strTaskNew = ""  # User input for new task
strPriorityNew = ""  # User input for new task priority
strTaskRemove = ""  # User task to remove
strTable = ""  # String of data to add to file
strNewRow = ""  # New string row to add to strTable data

# -- Processing -- #
# Step 1 - When the program starts, load the data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open(strFile, "r")

for row in objFile:
    lstRow = row.split("\t")
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)

objFile.close()  # Close connection so you can open in write mode later

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = input("Which option would you like to perform? [1 to 5] - ")
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == "1":
        print("Task", "|", "Priority")
        for row in lstTable:
            print(row["Task"], "|", row["Priority"])
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == "2":
        strTaskNew = input("What task would you like to add? - ")
        strPriorityNew = input("What priority would you like to assign it? - ")
        dicRowNew = {"Task": strTaskNew, "Priority": strPriorityNew}
        lstTable.append(dicRowNew)
        print("\nTask has been added to your list!")
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == "3":
        count = 0
        strTaskRemove = input("Which task would you like to remove? - ")
        for dicRow in lstTable:
            if dicRow["Task"].lower() == strTaskRemove.lower():
                lstTable.remove(dicRow)
                count += 1
        if count > 0:
            print("\nTask removed from your list!")
        else:
            print("\nThat task is not your list! Please try again.")
    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == "4":
        objFile = open(strFile, "w")
        for row in lstTable:
            strNewRow = row["Task"] + "\t" + row["Priority"] + "\n"
            strTable += strNewRow
        objFile.write(strTable)
        print("Current list saved to your file!")
        objFile.close()
    # Step 7 - Exit program
    elif strChoice.strip() == "5":
        break  # and Exit the program
    else:
        print("'" + strChoice + "'" + " is not an available option. Please try again.")
