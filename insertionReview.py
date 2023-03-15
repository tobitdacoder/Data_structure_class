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
ll.insert_at_begining(34)
ll.insert_at_begining(23)
ll.insert_at_begining(44)
ll.insert_at_begining(20)
ll.print()
