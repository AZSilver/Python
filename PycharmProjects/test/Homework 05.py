# -------------------------------------------------------------------------------
# Name: Homework 05
# Purpose: Complete Homework 5
# Author: AZSilverman
# Created: 10/21/2014
# Desc: Asks the user for the name of a household item and its estimated value.
# then stores both pieces of data in a text file called HomeInventory.txt
# -------------------------------------------------------------------------------
import json

# 1: Create new manages a "ToDo list." The ToDo file will contain two columns of data, separated by a comma, called:
# Task, Priority. Use a Python Dictionary to work with the data while the program is running.
# Also use Try - Catch blocks to manage user input errors.
toDoFile = "An object that represents a file"
toDoFile = open('ToDo.txt', 'r')


#
# When the program starts, load the any data you have in a text file called ToDo.txt into a python Dictionary.
data = {}
with open("ToDo.txt") as f:
    for line in f:
        (key, val) = line.split()
        data[key] = val
# Display the contents of the file to the user
def displayData():
    for key, value in data.items():
        print(key, ",", value)


displayData()
#
# .
# Allow the user to Add tasks, Remove, and save the task to a file using numbered choices like this:
#     print "1. Add task"
def addTask():
    taskName = str(input('What is the name of the task? '))
    priorityName = str(input('What is the priority of this task? '))
    data.update({taskName, priorityName})
    displayData()
#
#     print "2. Remove task"
def removeTask():
    taskName = str(input('What is the name of the task you would like to delete? '))
    try:
        del data['taskName']
    except KeyError:
        pass
#     print "3. Save tasks to file"
def saveTask():
    with open("ToDo.txt") as f:
        f.write(json.dumps(data))

while inputString != 3:
    inputString = str(input('Please select from one of the following options'))
    print('1. Add task')
    print('2. Remove task')
    print('3. Save tasks to file (and quit)')
    if (inputString == '1'):
        addTask()
    elif (inputString == '1'):
        removeTask()
    elif (inputString == '3'):
        saveTask()
    else:
        print('I don\'t understand an option besides 1,2 or 3. Please try again' )

toDoFile.close()
exit()
