#QUEUE: its principle is FIFO (FIRST IN, FIRST OUT)
#STACK: its principle is LIFO (LAST IN, LAST OUT)

from collections import deque

linked=deque()
linked.append(56) #first appended
linked.append(45.3) #second
linked.append(20) #third
linked.popleft() #this function is used to remove the last element addedd in a list (hee it is 20)
print(linked)



   