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

print(type(student1))

   
      
      


