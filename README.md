#Python Assignments from Introduction to Programming and Application Development
#--- Make the class ---
class Person(object):
    """ Base Class for Personal data """
    #-------------------------------------#
    #Desc:  Holds Personal data
    #Dev:   RRoot 
    #Date:  12/12/2012
    #ChangeLog:(When,Who,What)
    #-------------------------------------#
    
    #--Fields--
    FirstName = ""

    #--Constructor--
    def __init__(self, FirstName):
        #Attributes
        self.FirstName = FirstName
    
    #--Properties--   
    
    #--Methods--
    def ToString(self):
        return self.FirstName 

#--End of class--

# --- Use the class ----
# by making an object!
objP1 = Person("Bob")
#objP1.FirstName = "Bob"

objP2 = Person("Sue")
#objP2.FirstName = "Sue"

print(objP1.ToString())
print("-------------")
print(objP2.ToString())
