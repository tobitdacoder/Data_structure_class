#QUEUE: its principle is FIFO (FIRST IN, FIRST OUT)
#STACK: its principle is LIFO (LAST IN, LAST OUT)

from collections import deque
#this "collections" is a library used for datastructure, we are going to use one of its functions or module called "deque" and this module or function will help us implement the queues and the stacks


linked=deque()
linked.append(56) #first appended
linked.append(45.3) #second appended
linked.append(20) #third appended (at the end of the list coz, remember, the append function adds at the end of list)
linked.pop() #this function is used to remove the last element added in a list (hee it is 20)
linked.popleft() #this will remove the last element but at the left side (beginnig of the list)
print(linked) #here we print that object after added some elements in it


#!!!! LET US IMPLEMENT THE QUEUE NOW:

queue=deque() #here we are now creating a queue. and for that we first store the deque function in the variable we called queue.
for i in range(0,10): #then here we create this loop so that it will print the index from 0 to 9 [10 is not printed coz in the range function, the last element of the range is excluded]
   queue.append(i) #here we will add the index number to our list in the queue everytime we append, until we reaches the last index which is 9
   print(queue) #then here, since this print function is in the loop, everytime we apend, a queue list will be printed with the value appended added in, so we are going to jave 10 lists created where each following list will have one element more than the previous one.
   

for i in range(len(queue)): #now here we are implementing the FIFO logic, where the first element to be added previously in the list, will be the first one to be removed (this is the logic of the queue)
   queue.popleft() #here we are using the "popleft" to implement that idea of removing first the element which came in the first in the previous loop
   print(queue) #then, in this same loop we print the queue (there will be 9 queues printed since we putted the print in the loop in purpose of seeing what is appening)









   