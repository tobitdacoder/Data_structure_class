# what is a stack
# stacks in python
# using a list as a stack 
# using deque as a stack
#exercices

'''first, stacks are usualy used in places like websites where, when we are on a website and we keep opening pages of that website, by clicking on the arrow (top-left) to come back to the previous page, there we are using stacks data structure (Last In First Out - LIFO)... those links are in a stack where the last link we click on is the first to be closed once we click on that arrow to go back to the previous page (link)'''

'''we are going to talk about queues just after this topic so stay tuned guyz 😊😁'''

# first we have to know that push/pop are constant time operations O(1) 

#when u are using the "undo" CTRL+Z functionality in any editor, u are using the stack to track down last set of operations

# import deque as dq
# stk=deque()
# stk.append(45)
# stk.append(65)
# stk.pop()

stack_list=[]
stack_list.append('https://www.cnn.com/')
stack_list.append('https://www.cnn.com/world')
stack_list.append('https://www.cnn.com/DRC')
stack_list.append('https://www.cnn.com/GOMA')
stack_list.pop() #this pop will remove the last element from the list "...GOMA"
print(stack_list)
# print(stack_list[-1]) this is to print the last element of the list without poping it out 

# here we are starting to implement the stack notion, and here the idea is to implement it in the logic of a website and its pages, so , when we open a new page of a website, that page is added to our list (is appended to our list) and here when we will click to the return arrow, the last page which we oppenned willl be the first on to be closed (LIFO)

#the problem of implementing the stack using a dynamic array is that, when its full, it will copy all the elelemts from the list and paste it into a new location and add the double of the previous space that we have, so the best way to use stack and queues is to use the "collections.deque" ... deque is a generalization of stacks and queues (pronounced "deck" and is short form of "double-ended queue")... memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction. 


from collections import deque #import deque from collections 
stack=deque() #then assign it to stack which is a variable (container)
# to see all the methods available in deque (which we egaled to stack, just write "stack." and this will show the list of all available method under stack)

stack.append("https://www.cnn.com/")
print(stack)


