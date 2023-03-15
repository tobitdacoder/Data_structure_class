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
      
      
ll=LinkedList()
ll.insert_at_begining(34)
ll.insert_at_begining(23)
ll.insert_at_begining(44)
ll.print()