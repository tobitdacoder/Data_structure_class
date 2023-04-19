#1. here is the implementation of the binary search algorythm 

def binary_searh(arr,x):
    low=0
    high=len(arr)-1
    while low <= high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
    return -1

arr=[2,5,7,8,67,79]
x=8
result=binary_searh(arr,x)
print(result)
