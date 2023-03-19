''' here is THE REDO FROM SCRACH of a simple program (LEARNED FROM THE INTERNET AND UNDERSTOOD ), its task is to create a linked list and insert values at the beginning of it (here the main first goal ws to be able to insert values at the front of the linked list and understand the mecanism of how it works), plus, we also know how to create a printing function in a class which helps us to print the linked list'''


class Node:
   def __init__(self,data=None,next=None):
      self.data=data
      self.next=next
class LinkedList:
   def __init__(self):
      self.head=None
      
   def insert_at_begining(self,data):
      node=Node(data,self.head)
      self.head=node #here the previous self.head became the "next" adress 
      
   def print(self):
      if self.head==None:
         print("no values in the linked list")
         return #this is to be used while we dond need to use the elif
      itr=self.head
      llist=''
      while itr:
         llist+=str(itr.data) + " --> " #here this arrow is pushing the current value too be the next value 
         itr=itr.next
         
      print(llist)
   
   def insert_at_end(self,data):
      if self.head is None: #if the list is empty, or there is not any head node in the list
                            # then the data we insert now will be the new head and after it there is not any value which can be the next (that is why we used the None)
         self.head=Node(data,None) #here we just mean that "now, the new head is the new entered
                                 # data" which does not have any next value or is not pointing at any value since it is the only value in the linked list
                                 
                                 #reemeber for the insertion at the begining we used the "node" object Node(data,self.head) whith the self head as the next value, here, since we want to ad a value at the end if the list, there is not any "next" value that has to be after the adedd value
         return #this is to show that, since there is now only one value added, we will break the condition just after we added the the single value
      itr=self.head
      
      while itr.next: #while there is another value as the "next", then we are not yet at the end of the list.
         
         itr=itr.next  #her we mean : since there is a "next" vlue to the current head, lets make that next value our new itr (self.head) and check again the condition in the loop to see if there is another value after the new itr (which was the previous itr.next), 
      itr.next=Node(data,None) #here it means that we reached the last element and for that element there is not a next value, then its next value will be the bew node we've created which does not have a next[ Node(data,None)], so after the loop is broken, which means that there is not another next value existing after, we can now add our new element (which will be the "next" of the nast element which did not have a "next" before we added the new data)
      
#!!!!! 👆👆👆UNTIL NOW, WE'VE LEARNT THE METHODS (insert_at_begining, print, insert_at_end) 😃😃
#!!!!! NOW LETS STUDY OTHER INTERESTING METHODS (OR FUNCTIONS)

# SO, THE NEXT METHOD WILL BE A METHOD THAT ALLOW US TAKE A LIST OF VALUES AS AN INPUT AND IT WILL CREATE A NEW FRESH LINKED LIST.

   def insert_values(self,data_list):
      self.head=None #here we dont use the conditional "if" to check wether the list is empty or not because we are going to wipe up all the current value from the list and input new values in that list
      for data in data_list:
         self.insert_at_end(data) #here this loop comes to use our previous function (method we created called "insert_at_end")
                                  #and it is using it so that, when we want to input a list of values at the same time, each value from that inputed list will come after another until we reach the last value which will be added at the end (coz we used the insert_at_end method)
                                  
   def get_length(self): #this function will basically help us to get the lenght of the linked list
      count=0 #here we initiate the count so that if there is a head which exist, we will incremement by one for each head
      itr=self.head
      while itr: #here is the loop that will help us find the total count of the element
         count+=1
         itr=itr.next
      return count #if the loop is broken, the count will then be retrieved
   
      
ll=LinkedList()
ll.insert_at_begining(34) #this will be the first element to be inserted in the linkedlist
ll.insert_at_begining(23) #this will be the second and will push the (34) value and become the head
ll.insert_at_begining(44) #then this will come and push the (23) and then become the head
ll.insert_at_begining(20) #then this (20) will be inserted at the beginning too and push the (44) and become the head. 
#notice that, for the "insert_at_begining" the one which is inserted after the other is the one which become the head (so it is aded at the beginning of the linked list)

ll.insert_at_end(100) #this will be the first one to be added at the end of our list
ll.insert_at_end(130) #the this will come and be addedd after the (100) and become the "next" of (100)
ll.insert_at_end(141) #then this will also come and become the "next" of (130) 
                      # NOTICE that, if we dont hadd any value after (141), then it does not have a "next" and then it is ponting at nothing "None"
ll.insert_values(["babane ","mangue ","tomato ","garlic"]) #here, as we saw, we erased all the previous content of the previous linked lists and created a new one with the inputed content,
ll.print() #then this function comes and print the linked list while itterating through all the values until it reaches the value which does not have another value in after it (in front of it)
length=ll.get_length()
print(f"the length is equal to {length} ") #now we print the length like this after weve already stored it into a variable to use it in a much easier way.





