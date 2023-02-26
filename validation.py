while True:
   #here the loop will continue until there is not invalid input after we tried 
   # we like this aproche because it will keep asking until it breaks after a certain condition
   try:
      #here we try the input of the user to see if it is valid or not
      age=int(input("what is your age: "))
   except ValueError:
      #the loop will come here once the try statement signal that there is an invalid input
      print("this is not valid as input") #this message will be prompted to tell that the input is not valid
      continue #then this continue will help us jump the [else statement] until the input is valid  
   if age<0: #this is just to make sure that the user will not attemp to put deliberately a negative age
      print("age cannot be negative please")
      continue
   else: #this else will be lauched once the input is valid so that it will break the while loop we created before
      break #this break will break the loop and takes us to the "if condition to check the valid input"
#here now we are out of the loop and we can now check the input to see its condition
if age>18: #first condition
   print("you are an adult")
else: #second condition
   print("you are not an adult")
   
   
   
################################################################################


#we can try the samething for a string:

while True:
   name=input("What is your name in upper case?:")
   if not name.isupper():
      print("i said, ALL THE NAME IN UPPER CASE")
   else:
      break
   
   
################################################################################


#ANOTHER ONE:

while True:
   vawels=['a','e','i','o','u']
   vawel=input("gimme a valid vawel: ")
   if vawel.lower() not in vawels:
      print("not a valid vawel")
   else:
      print("it is a valid one ")
      break
    
   
