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
stack_list.append(34)
stack_list.append(54)
stack_list.append(81)
stack_list.append(27)
print(stack_list)
