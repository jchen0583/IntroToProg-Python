#-------------------------------------------------#
# Title: Working with Dictionary and List
# Developer: J. Chen
# Date: Oct. 30, 2016
# Description: See Objective below
# ChangeLog: NA

'''
Objective:
1.	Create a text file called Todo.txt using the following data:
        Clean House,Low
        Pay Bills,High
2.	When the program starts, load each row of data from the ToDo.txt text file into a Python dictionary.
3.	After you get a row of data stored in a Python dictionary, add the new “row” into a Python.
4.	Display the contents of the List to the user.
5.	Allow the user to Add or Remove tasks from the list using numbered choices.
6.	Save the data from the table into the ToDo.txt file when the program exits.
'''


#objective 1: create a file and use the write function to enter the data into a file
f = open('C:\_PythonClass\Assignment05\ToDo.txt', 'w')
f.write('Clean House,Low\n')
f.write('Pay Bills,High')
f.close ()

#objective 2: load the data into a python dictionary
strQ1 = input("Would you like to open and add to your 'To Do' list? (y/n): ")
if strQ1.lower() == 'n':
    print("Good Bye!") #allows user to exit program right away
else:
    objFile = open('C:\_PythonClass\Assignment05\ToDo.txt', 'r') #opens data file
    print("\nYour 'To Do' list includes the following item(s):\n")
    dicTable = {} #create an empty dictionary name dicTable
    for line in objFile: #store the data from the file into the dicTable
        task, priority = line.strip().split(',')
        dicTable[task] = priority
        print('\t',line) #print the data in a readable format for the user

 #objective 3: prompts user to add new data
    strTask = input("\nEnter a new task: ")
    strPriority = input('Enter the priority of the new task: ')
    dicAdd = {strTask.strip().title(): strPriority.strip().title()}  #add the new task to the dictionary format
    dicTable.update(dicAdd) #update the dicTable
    print("\nThe following task has been added to your 'To Do' list:")
    print("\t",dicAdd)

 #objective 4: print content
    print("\nYour task list includes the following:")
    for key in dicTable:
        print("\t",key)

 #objective 5: allow user choices
    print("\nWhat would you like to do next?")
    print("\tChoose '1' to add another task")
    print("\tChoose '2' to remove an existing task")
    print("\tChoose '3' to save all tasks to the Todo.txt file and exit!")
    strQ2 = input("Next: ")

    while strQ2 == '1': #use the loop function
        strTask = input("\nEnter a new task: ")
        strPriority = input('Enter the priority of the new task: ')
        dicAdd = {strTask.title(): strPriority.title()} #add new task
        dicTable.update(dicAdd) #update the dicTable
        print("\nThe following task has been added to your 'To Do' list:")
        print("\t",dicAdd)

        print("\nWhat would you like to do next?")
        print("\tChoose '1' to add a new task")
        print("\tChoose '2' to remove an existing task")
        print("\tChoose '3' to save all tasks to the ToDo.txt file and exit!")

        strQ2 = input("Next: ")

    while strQ2 == '2':  #use the loop function
        print("\nYour 'To Do' list includes the following task(s): ")
        for key in dicTable:
            print("\t",key)
        strTask = input("\nWhat task do you want to remove?: ")
        try: #use a try-except to avoid error messages if a user enters a non-existing task
            del dicTable[strTask.strip().title()]
            print("'",strTask.title(), "' has been removed.")
            print("\nYour 'To Do' list has the remaining task(s):")
            for key in dicTable:
                print("\t",key)
        except:
            print("That task cannot be found.")

        print("\nWhat would you like to do next?")
        print("\tChoose '2' to remove another existing task")
        print("\tChoose '3' to save all tasks to the ToDo.txt file and exit!")
        strQ2 = input("Next: ")

 # objective 6: save the edits upon exit of the program
    if strQ2 == '3':
        objFile = open('C:\_PythonClass\Assignment05\ToDo.txt', 'w')
        lstTable = [dicTable]
        objFile.write(str(lstTable))
        objFile.close ()
        print("\nThe following data has been saved to the 'ToDo' file:\n\r", lstTable, "\nThank you and Good Bye!")
    else: print("\nYou have entered an invalid choose. Your data has not been saved. Good Bye.") #a catch all feature