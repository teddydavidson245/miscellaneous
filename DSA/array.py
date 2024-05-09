import array

arr = array.array('i', [1, 2, 3, 4, 5])
# Traversing over arr[]
for x in arr:
    print(x, end=" ")

#Insertion in Array - at a specific postion

def insertElement(arr, n, x, pos):

    # shift elements to the right
    # which are on the right side of pos
    for i in range(n-1, pos-1, -1):
        arr[i + 1] = arr[i]

    arr[pos] = x

insertElement(arr, 4, 10, 2)
print (arr)

#Deletion in Array

#1.Function to search for a key in the array
def findElement(arr, n, key):
    for i in range(n):
#return the index if the key is found
        if arr[i] == key:
            return i
    return -1 #if key is not found

#2.Function to delete an element from the array
def deleteElement (arr, n, key):
    #find position of the element to be deleted
    pos = findElement(arr, n, key)

    if pos == -1:
        print("Element not found")
        return n
#Deleting the element
    for i in range(pos, n-1):
        arr[i] = arr[i+1]
    return n-1

#SUBARRAY
'''A subarray is a contiguous part of array, i.e. an array inside another array
in general, for an array of size n, there are n*(n+1)/2 non-empty subarrays.
For example, consider the array [1,2,3,4], there are 10 non-empty subarrays. These are:
(1), (2), (3), (4), (1,2), (2,3), (3,4), (1,2,3), (2,3,4), and (1,2,3,4)'''

## Problem 1
## Split an array into two equal sum subarrays
'''
Given an array of integers greater than zero, find if it is possible to split it in two subarrays (without reordering the elements),
such that the sum of the two subarrays is the same. Print the two subarrays.

Examples : 
Input : Arr[] = { 1 , 2 , 3 , 4 , 5 , 5  }
Output :  { 1 2 3 4 } 
          { 5 , 5 }

Input : Arr[] = { 4, 1, 2, 3 }
Output : {4 1}
         {2 3}

Input : Arr[] = { 4, 3, 2, 1}
Output : Not Possible'''

def findSplitPoint(arr, n) : 
    leftSum = 0 
    
    # traverse array element 
    for i in range(0, n) : 
        # add current element to left Sum 
        leftSum += arr[i]  
    
        # find sum of rest array elements (rightSum) 
        rightSum = 0 
        for j in range(i+1, n) : 
            rightSum += arr[j]  
    
        # split point index 
        if (leftSum == rightSum) : 
            return i+1 
         
    # if it is not possible to split array into two parts 
    return -1
   
# Prints two parts after finding split point using findSplitPoint() 
def printTwoParts(arr, n) : 
   
    splitPo = findSplitPoint(arr, n) 
    
    if (splitPo == -1 or splitPo == n ) : 
        print ("Not Possible") 
        return
       
    for i in range(0, n) : 
        if(splitPo == i) : 
            print ("") 
        print (str(arr[i]) + ' ',end='') 
   
# driver program 
arr = [1 , 2 , 3 , 4 , 5 , 5] 
n = len(arr) 
printTwoParts(arr, n) 

#SUBSEQUENCE
'''
A subsequence is a sequence that can be derived from another sequence by removing zero or more elements,
 without changing the order of the remaining elements.
 More generally, we can say that for a sequence of size n, we can have (2^n – 1) non-empty sub-sequences in total.
For the same above example, there are 15 sub-sequences. They are:
(1), (2), (3), (4), (1,2), (1,3),(1,4), (2,3), (2,4), (3,4), (1,2,3), (1,2,4), (1,3,4), (2,3,4), (1,2,3,4).
'''

#SUBSET
'''
If a Set has all its elements belonging to other sets, this set will be known as a subset of the other set.
A Subset is denoted as “⊆“. If set A is a subset of set B, it is represented as A ⊆ B.

For example, Let Set_A = {m, n, o, p, q}, Set_ B = {k, l, m, n, o, p, q, r}
Then, A ⊆ B.


'''