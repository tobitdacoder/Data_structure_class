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
      
      
      
ll=LinkedList()
ll.insert_at_begining(34) #this will be the first element to be inserted in the linkedlist
ll.insert_at_begining(23) #this will be the second and will push the (34) value and become the head
ll.insert_at_begining(44) #then this will come and push the (23) and then become the head
ll.insert_at_begining(20) #then this (20) will be inserted at the beginning too and push the (44) and become the head. 

#notice that the one which is inserted after the other is the one which become the head (so it is aded at the beginning of the linked list)
ll.print() #then this function comes and print the linked list while itterating through all the values until it reaches the value which does not have another value in after it (in front of it)