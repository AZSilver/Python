# -------------------------------------------------------------------------------
# Name: Homework 05
# Purpose: Complete Homework 5
# Author: AZSilverman
# Created: 10/21/2014
# Desc: Creates, stores and removes tasks to a file
# throw an exception on invalid input
# -------------------------------------------------------------------------------


# 1: Create new manages a "ToDo list." The ToDo file will contain two columns of data, separated by a comma, called:
# Task, Priority. Use a Python Dictionary to work with the data while the program is running.
# Also use Try - Catch blocks to manage user input errors.

#
# When the program starts, load the any data you have in a text file called ToDo.txt into a python Dictionary.
data = {}


def readTask():
    with open('ToDo.txt') as f:
        for line in f:
            inputString = line.strip().split(',')
            data[inputString[0]] = inputString[1]


readTask()
# Display the contents of the file to the user
def displayData():
    for key in data.keys():
        print(key, ",", data[key])


displayData()
#
# .
# Allow the user to Add tasks, Remove, and save the task to a file using numbered choices like this:
# print "1. Add task"
def addTask():
    taskName = str(input('What is the name of the task? '))
    priorityName = str(input('What is the priority of this task? '))
    data[taskName] = priorityName
    displayData()


#
# print "2. Remove task"
def removeTask():
    taskName = str(input('What is the name of the task you would like to delete? '))
    try:
        del data[taskName]
        displayData()
    except KeyError as e:
        print('Caught: There is no key,' + str(e))
        exit()


# print "3. Save tasks to file"
def saveTask():
    todoFile = open('ToDo.txt', 'w')
    for key in data.keys():
        encodedString = str(key) + ',' + str(data[key] + '\n')
        todoFile.write(encodedString)
    exit()


def main():
    while True:
        print('Please select from one of the following options')
        print('1. Add task')
        print('2. Remove task')
        print('3. Save tasks to file (and quit)')
        inputString = str(input())
        if inputString == '1':
            addTask()
        elif inputString == '2':
            removeTask()
        elif inputString == '3':
            saveTask()
        else:
            print('I don\'t understand an option besides 1,2 or 3. Please try again')
            print('Just kidding, there is no try again')
            raise Exception('Invalid Option')


try:
    main()
except Exception as e:
    print(e)
finally:
    print('Thank you for using my program')
    exit()
