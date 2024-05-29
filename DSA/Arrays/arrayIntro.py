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

## Problem 2
## SPlit an array in three equal sum subarrays
'''
Consider an array A of n integers. Determine if array A can be split into three consecutive parts such that sum of each part is equal. If yes then print any index pair(i, j) such that sum(arr[0..i]) = sum(arr[i+1..j]) = sum(arr[j+1..n-1]), otherwise print -1. 

Examples: 

Input : arr[] = {1, 3, 4, 0, 4}
Output : (1, 2)
Sum of subarray arr[0..1] is equal to
sum of subarray arr[2..3] and also to
sum of subarray arr[4..4]. The sum is 4. 

Input : arr[] = {2, 3, 4}
Output : -1
No three subarrays exist which have equal
sum.

#SOLUTION:
Check if this sum is divisible by 3 or not.
This is because if sum is not divisible then the sum cannot be split in three equal sum sets.
If there are three contiguous subarrays with equal sum, then sum of each subarray is S/3. 
Suppose the required pair of indices is (i, j) such that sum(arr[0..i]) = sum(arr[i+1..j]) = S/3. 
Also sum(arr[0..i]) = preSum[i] and sum(arr[i+1..j]) = preSum[j] – preSum[i]. 
This gives preSum[i] = preSum[j] – preSum[i] = S/3. This gives preSum[j] = 2*preSum[i]. 
Thus, the problem reduces to find two indices i and j such that preSum[i] = S/3 and preSum[j] = 2*(S/3). 
For finding these two indices, traverse the array and store sum upto current element in a variable preSum. 
Check if preSum is equal to S/3 and 2*(S/3).
'''
def findSplit(arr, n):
    # variable to store prefix sum
    preSum = 0
 
    # variables to store indices which have prefix sum divisible by S/3.
    ind1 = -1
    ind2 = -1
 
    # variable to store sum of entire array. S
    # Find entire sum of the array.
    S = arr[0]
    for i in range(1, n):
        S += arr[i]
 
    # Check if array can be split in three equal sum sets or not.
    if(S % 3 != 0):
        return 0
     
    # Variables to store sum S/3 and 2*(S/3).
    S1 = S / 3
    S2 = 2 * S1
 
    # Loop until second last index as S2 should not be at the last
    for i in range(0,n-1):
        preSum += arr[i]
         
        # If prefix sum is equal to S/3 store current index.
        if (preSum == S1 and ind1 == -1):
            ind1 = i
        # If prefix sum is equal to 2*(S/3) store current index.        
        elif(preSum == S2 and ind1 != -1):
            ind2 = i
             
            # Come out of the loop as both the required indices are found.
            break   
 
    # If both the indices are found then print them.
    if (ind1 != -1 and ind2 != -1):
        print ("({}, {})".format(ind1,ind2))
        return 1
     
    # If indices are not found return 0.
    return 0
 
# Driver code
arr = [ 1, 3, 4, 0, 4 ]
n = len(arr)
if (findSplit(arr, n) == 0) :
    print ("-1") 

#SUBSEQUENCE
'''
A subsequence is a sequence that can be derived from another sequence by removing zero or more elements,
 without changing the order of the remaining elements.
 More generally, we can say that for a sequence of size n, we can have (2^n – 1) non-empty sub-sequences in total.
For the same above example, there are 15 sub-sequences. They are:
(1), (2), (3), (4), (1,2), (1,3),(1,4), (2,3), (2,4), (3,4), (1,2,3), (1,2,4), (1,3,4), (2,3,4), (1,2,3,4).
'''

## Problem
## Longest subsequence having equal numbers of 0 and 1
''' Given a binary array, the task is to find the size of the largest sub_sequence which having equal number of zeros and one. 

Examples : 

Input : arr[] = { 1, 0, 0, 1, 0, 0, 0, 1 } 
Output: 6

Input : arr[] = { 0, 0, 1, 1, 1, 1, 1, 0, 0 }
Output : 8
'''
def generateSubsequences(a, n):
	result = 0
	
	# Number of subsequences is (2**n -1)
	opsize = 2**n
	
	# Run from counter 000..1 to 111..1
	for counter in range(opsize):
		
		# store count of zeros and one
		countzero, countone = 0, 0
		current_size = 0
		
		for j in range(n):
			
			# Check if jth bit in the counter is set. If set then 
			# print jth element from arr[]
			if counter & (1 << j):
				if arr[j] == True:
					countone += 1
				else:
					countzero += 1
				current_size += 1
		
		# update maximum size
		if countzero == countone:
			result = max(current_size, 
						result)
	return result 

# Driver code
arr = [ 1, 0, 0, 1, 0, 0, 0, 1 ]
n = len(arr)
print("largest Subsequences having" +
		" equal number of 0 & 1 is ",
		generateSubsequences(arr, n))



#SUBSET
'''
If a Set has all its elements belonging to other sets, this set will be known as a subset of the other set.
A Subset is denoted as “⊆“. If set A is a subset of set B, it is represented as A ⊆ B.

For example, Let Set_A = {m, n, o, p, q}, Set_ B = {k, l, m, n, o, p, q, r}
Then, A ⊆ B.
'''

## Problem
## Find if there is any subset of size K with 0 sum in an array of -1 and +1
'''
Given an integer K and an array arr containing only 1 and -1, the task is to find if there is any subset of size K sum of whose elements is 0.

Examples: 

Input: arr[] = {1, -1, 1}, K = 2 
Output: Yes 
{1, -1} is a valid subset

Input: arr[] = {1, 1, -1, -1, 1}, K = 5 
Output: No 

Approach: 

In order for the sum to be 0, there has to be equal number of 1 and -1 in the subset.
If K is odd then no subset will satisfy the given condition.
Else if K is even then we need to choose exactly (K / 2) 1’s and (K / 2) -1’s in order to form the subset so that the sum of all of it’s elements is 0
So, if K is even and number of 1’s ≥ K / 2 and number of -1’s ≥ K / 2 then print Yes else print No.
'''
def countOnes(n, a): 
 
    count = 0
    for i in range(0, n): 
        if a[i] == 1: 
            count += 1
    return count 
 
def isSubset(arr, n, k): 
 
    countPos1 = countOnes(n, arr) 
    countNeg1 = n - countPos1 
 
    # If K is even and there are 
    # at least K/2 1's and -1's 
    return (k % 2 == 0 and countPos1 >= k // 2 and
                           countNeg1 >= k // 2) 
 
# Driver Code
if __name__ == "__main__": 
 
    a = [1, 1, -1, -1, 1] 
    n = len(a) 
    k = 5
     
    if isSubset(a, n, k) == True: 
        print("Yes") 
    else:
        print("No") 