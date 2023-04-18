#The basic Python data structures in Python include list, set, tuples, and dictionary. Each of the data structures is unique in its own way. Data structures are “CONTAINERS” that organize and group data according to type. The data structures differ based on mutability and order.
#list, Tuples, Dictionaries, Sets, "Classes"

#list: mutable data structure (we can store in it different elements of differnt datatype integers,strings,floats,boolean values)... mutability refers to the ability to be modified (adding values, modifying it)

name=list()
print(type(name))

#here it means that this is a list which is an object from a class

marks=[] 
print(type(marks))

#this one is also a list which is an object from a class


# '''ILLUSTRATION OF CLASSES'''

#we make classess to make us make objects, these clases can be used by any one who want to create an object from our class

class Students:
   
   name="Mark"
   email="m@gmail.com"
   #these are the atributes of a class which are going to be for each object
   #any function that we put in the class is called a "method"
   # !!! ALWAYS PRACTICE INDENTINTION AND ALSO BY USING TAB !!!
   def __init__(self,my_name,my_access,my_regno):
      #the init method is used to create objects
      self.my_name = my_name
      self.my_access = my_access
      self.my_regno = my_regno
      
student1=Students("toby","A98591","S22B23/001")
#this is the first object we have from our class
# here we can see that we used our class in the object in order to use its structure

print(type(student1))

########################################################################

#DATASTRUCTURE REVISION:

#Text type: str
# numrical type: int, float, complex
#boolean typ: bool
#null type: Null
#sequence type: list,tuple,range
#Mapping type: dict

#LIST:

list=[1,65,22,86,93,44,81,29,52,15,18]
for i in range(len(list)):
   #this loop is printing the sentense "this is the for loop" 
   # n times (n is the number of elements of the "list")
   print("this is the for loop")
   
for i in list:
   print(i) #here we are just printing directly all the elements of the same list
            # instead of just using its length 

###########################################################

for i in range(0,100,5): 
    print(i)
    #this will print values in the range 0 and 100(excluded), notice the 5, that five is the gap to be taken between each elememt of the range... 0 5 10 15 20 25 etc

###########################################################
    
stud=[23,43,45,65,67,76,78,87]
for i in range (len(stud)):
   #this will print a numbered list of the list content : like 1-23, 2-43 etc
   print(i+1,stud[i],sep='-')
   
###########################################################

dictt={"first":1,"second":2,"third":3}
res=dictt["second"] #to print the content or the value of the given key
                    # we store the dictionry key in a variable, and by printing that
                    # variable, we will print the value of that key
print(res)
   
      
      


