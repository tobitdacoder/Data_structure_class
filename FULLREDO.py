# SO GUYZ, HERE IS THE FULL SUCCESFULL REDO OF EVERY NEW MODULE OR FUNCTION WE'VE IMPLEMENTED SO FAR.... TRY ALSO TO RECALL ALL THE FUNCTIONS WEVE COVERED SO FAR TO MAKE SURE YOU'VE IMPLEMENTED EVERYTHING WELL BEFORE TO ATTEMPT THE EXERCICES ... THIS IS HOW WE ARE GOING TO DO FROM NOW SO THAT WE CAN EASILY UNDERSTAND WHERE WE ARE 



class Node:
   def __init__(self,data=None,next=None):
      self.data=data
      self.next=next
class LinkedList:
   def __init__(self):
      self.head=None
   
   def Insert_at_begining(self,data):
      node=Node(data,self.head)
      self.head=node
      
   def print(self):
      if self.head==None:
         print("empty array")
         return
      
      itr=self.head
      lstr=''
      while itr:
         lstr+=str(itr.data)+ ' --> '
         itr=itr.next
         
         
      print(lstr)
      
   def insert_at_end(self,data):
      node=Node(data,None)
      if self.head==None:
         self.head=node
         return
      itr=self.head
      while itr.next:
         itr=itr.next
      itr.next=node      
      
   def insert_value(self,data_list):
      self.head=None
      for data in data_list:
         self.insert_at_end(data)  
         
   def get_length(self):
      count=0
      itr=self.head
      while itr:
         count+=1
         itr=itr.next
      return count 
   
   def insert_at(self,index,data):
      if index<0 or index>=self.get_length():
         raise Exception("out of index range") 
      if index==0:
         self.Insert_at_begining(data)
         return
      
      count=0
      
      itr=self.head
      while itr:
         if count==index-1:
            node=Node(data,itr.next)
            itr.next=node
            break
         itr=itr.next
         count+=1
   def remove_at(self,index):
      if index<0 or index>=self.get_length():
         raise Exception("out of range")
      if index==0:
         self.head=self.head.next
      count=0
      itr=self.head
      while itr:
         if count==index-1:
            itr.next=itr.next.next
         itr=itr.next
         count+=1
         
         
   def insert_after_value(self,data_after,data_to_insert):
      #we have first to search for first occurance of "data_after" value in linked list
      #Now insert "data_to_insert" after data_after node (try first, then look for the answer after in the description of the video by code basics)
      if self.head is None:
         return
      if self.head.data==data_after:
         self.head.next=Node(data_to_insert,self.head.next)
         return
      itr=self.head
      while itr:
         
         if itr.data == data_after:
               itr.next = Node(data_to_insert, itr.next)
               break
         itr=itr.next
         
      
      
      
      
      
ll=LinkedList()
ll.Insert_at_begining(45)
ll.Insert_at_begining(65)
ll.Insert_at_begining(54.6)
ll.Insert_at_begining(54.5)
ll.Insert_at_begining(94.6)

length=ll.get_length()
ll.insert_at(1,777)
ll.remove_at(1)
ll.insert_after_value(65,100)
ll.print()
print(length)


def gen(m, n):

    while m < n:

        yield m

        m *= 2

    yield n

lst = []

g1 = gen(2, 5)

g2 = gen(4, 20)

while True:

    try:

        lst.append(next(g1))

        lst.append(next(g2))

    except StopIteration:

        break
res=gen(g1,g2)
print(res)