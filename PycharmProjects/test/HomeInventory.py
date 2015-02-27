#-------------------------------------------------------------------------------
# Name: Homework 03
# Purpose: Complete Homework 3
# Author: AZSilverman
# Created: 10/12/2014
# Desc: Asks the user for the name of a household item and its estimated value.
# then stores both pieces of data in a text file called HomeInventory.txt
#-------------------------------------------------------------------------------

#1. Declare amd note the variables we are going to use
# objFile = "An object that represents a file"
# strData = "A row of text data from the file"

# asks the user for the name of a household item,
# and then asks for its estimated value.

while(True):
  print('Type in a "Name" and replacement "Value" for your household items')
  print('Enter the word "Done" to quit!)')
  strName = str(input('Enter the name of an item: '))
  if(str(strName).lower() = 'done'):
    break
  else:
    strValue = str(input('Enter a replacement Value for that Item: ')
    objFile.write(strName + ',' + '/n/r')
    objFile.close()
    print('Data was saved!')
print('Thank You!')


