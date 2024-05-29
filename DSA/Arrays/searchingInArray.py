'''
There are several searching algorithms. The most commonly used among them are:

    Linear Search
    Binary Search
    Ternary Search
Linear Search:
Linear Search is defined as a sequential search algorithm that starts at one end and goes through each element of a list
until the desired element or group of elements is found. Otherwise, the search continues till the end of the data set. 
This has a time complexity of O(N) where ‘N’ is the length of the array '''
def search(arr, N, x):

    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1


# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    N = len(arr)

    # Function call
    result = search(arr, N, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)
'''
Binary Search:
Binary Search is a searching algorithm used in a sorted array. In this algorithm, the element is found by repeatedly dividing
the search interval in half and deciding the next interval to find the element. 
This searching algorithm has a time complexity of O(log 2 N) where ‘N’ is the length of the array. 
The only thing to note is that the array must be sorted in increasing or decreasing order.
The search interval is halved by comparing the target element with the middle value of the search space.
The Binary Search Algorithm can be implemented in the following two ways

    Iterative Binary Search Algorithm
    Recursive Binary Search Algorithm

# Iterative Binary Search Algorithm: #
Here we use a while loop to continue the process of comparing the key and splitting the search space in two halves.'''
# It returns location of x in given array arr
def binarySearch(arr, low, high, x):

    while low <= high:

        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
        '''
# Recursive Binary Search Algorithm: #
Create a recursive function and compare the mid of the search space with the key. 
And based on the result either return the index where the key is found or call the recursive function for the next search space. ''' 
# Returns index of x in arr if present, else -1
def binarySearch(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = low + (high - low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, high, x)

    # Element is not present in the array
    else:
        return -1


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    
    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
        '''

Ternary Search:
Ternary search is a divide and conquer algorithm that can be used to find an element in an array. 
It is similar to binary search where we divide the array into two parts but in this algorithm, 
we divide the given array into three parts and determine which has the key (searched element). 
This algorithm also has the constraint that the array must be sorted. 
The time complexity for this algorithm is O(log 3 N) where ‘N’ is the size of the array.
'''
import math as mt

# Function to perform Ternary Search
def ternarySearch(l, r, key, ar):

    if (r >= l):

        # Find the mid1 and mid2
        mid1 = l + (r - l) //3
        mid2 = r - (r - l) //3

        # Check if key is present at any mid
        if (ar[mid1] == key): 
            return mid1
        
        if (ar[mid2] == key): 
            return mid2
        
        # Since key is not present at mid,
        # check in which region it is present then repeat the Search operation in that region
        if (key < ar[mid1]): 

            # The key lies in between l and mid1
            return ternarySearch(l, mid1 - 1, key, ar)
        
        elif (key > ar[mid2]): 

            # The key lies in between mid2 and r
            return ternarySearch(mid2 + 1, r, key, ar)
        
        else: 

            # The key lies in between mid1 and mid2
            return ternarySearch(mid1 + 1, 
                                 mid2 - 1, key, ar)
        
    # Key not found
    return -1

# Driver code
l, r, p = 0, 9, 5

# Get the array
# Sort the array if not sorted
ar = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# Starting index
l = 0

# end element index
r = 9

# Checking for 5

# Key to be searched in the array
key = 5

# Search the key using ternarySearch
p = ternarySearch(l, r, key, ar)

# Print the result
print("Index of", key, "is", p)

# Checking for 50
# Key to be searched in the array
key = 50

# Search the key using ternarySearch
p = ternarySearch(l, r, key, ar)

# Print the result
print("Index of", key, "is", p)
