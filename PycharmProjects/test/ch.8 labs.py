class Person(object):
    """Doc String """
    #-------------------------------------#
    #Desc:
    #Dev:
    #Date:
    #ChangeLog: (When,Who,What)
    #-------------------------------------#

    #--Fields--
    #__FirstName = ""
    #LastName = ""

    #--Constructor--
    def __init__(self,FirstName,LastName):
        self.__FirstName = FirstName
        self.LastName = LastName
	#Attributes
    #--Properties--
    #--Methods--
    def SetFirstName(self,FirstName):
        self.__FirstName = FirstName
    def GetFirstName(self):
        return self.__FirstName

    def ToString(self):
        return self.__FirstName + "," + self.__LastName
#--End of class--

objP1 = Person("Bob","Smith")
objP1.SetFirstName("Rob")
#objP1.LastName = "Smith"
print(objP1.GetFirstName())
__