''' 
Given an array of integers arr[] of size N and an integer, the task is to rotate the array elements to the left by d positions.
Examples:  

Input: 
N = 7, d = 2 ,arr[] = {1, 2, 3, 4, 5, 6, 7}
Output: 3 4 5 6 7 1 2

Input: N = 7, d=2 , arr[] = {3, 4, 5, 6, 7, 1, 2},
Output: 5 6 7 1 2 3 4 '''

## Approach 1 (Using temp array): 
'''
After rotating d positions to the left, the first d elements become the last d elements of the array

- First store the elements from index d to N-1 into the temp array.
- Then store the first d elements of the original array into the temp array.
- Copy back the elements of the temp array into the original array
Illustration:

Suppose the give array is arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2.
First Step:
    => Store the elements from 2nd index to the last.
    => temp[] = [3, 4, 5, 6, 7]

Second Step: 
    => Now store the first 2 elements into the temp[] array.
    => temp[] = [3, 4, 5, 6, 7, 1, 2]

Third Steps:
    => Copy the elements of the temp[] array into the original array.
    => arr[] = temp[] So arr[] = [3, 4, 5, 6, 7, 1, 2]

Follow the steps below to solve the given problem. 

- Initialize a temporary array(temp[n]) of length same as the original array
- Initialize an integer(k) to keep a track of the current index
- Store the elements from the position d to n-1 in the temporary array
- Now, store 0 to d-1 elements of the original array in the temporary array
- Lastly, copy back the temporary array to the original array 

Time complexity: O(N) 
Auxiliary Space: O(N)
'''

def rotate(L, d, n):
    d=d%n;
    k = L.index(d)
    new_lis = []
    new_lis = L[k+1:]+L[0:k+1]
    return new_lis

#Approach 2 (Rotate one by one): 
'''
At each iteration, shift the elements by one position to the left circularly (i.e., first element becomes the last).
Perform this operation d times to rotate the elements to the left by d position.

Rotate the array to left by one position. For that do the following:
- Store the first element of the array in a temporary variable.
- Shift the rest of the elements in the original array by one place.
- Update the last index of the array with the temporary variable.
Repeat the above steps for the number of left rotations required.

Time Complexity: O(N * d)
Auxiliary Space: O(1)
'''
# Function to left rotate arr[] of size n by d
def Rotate(arr, d, n):
  p = 1
  while(p <= d):
    last = arr[0]
    for i in range (n - 1):
      arr[i] = arr[i + 1]
    arr[n - 1] = last
    p = p + 1
    
# Function to print an array
def printArray(arr, size):
  for i in range (size):
    print(arr[i] ,end = " ")