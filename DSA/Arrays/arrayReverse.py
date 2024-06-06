## 1. Array Reverse Using an Extra Array (Non In-place) ##
'''
- Create a new array of the same size as the original array.
- Copy elements from the original array to the new array in reverse order. '''

def reverse_array_extra_array(arr):
    reversed_arr = arr[::-1]

    # Print reversed array
    print("Reversed Array:", end=" ")
    for i in reversed_arr:
        print(i, end=" ")

''' 
Time Complexity: O(n)
    Copying elements to a new array is a linear operation.
Auxiliary Space Complexity: O(n)
    Additional space is used to store the new array. '''

## 2. Array Reverse Using a Loop (In-Place)
''' 
- Iterate through the array using two pointers (start and end).
- Swap elements at the start and end pointers.
- Move the start pointer towards the end and the end pointer towards the start until they meet or cross each other.'''

def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
''' 
Time Complexity: O(n)
    The loop runs through half of the array, so it’s linear with respect to the array size.
Auxiliary Space Complexity: O(1)
    In-place reversal, meaning it doesn’t use additional space. '''        

## 3. Array Reverse Inbuilt Methods (Non In-Place)
'Using inbuilt methods like reverse in Python'
original_array = [1, 2, 3, 4, 5]
reversed_array = list(reversed(original_array))
''' 
Time Complexity: O(n) The reverse method typically has linear time complexity.
Auxiliary Space Complexity: O(n)
    Additional space is used to store the reversed array.'''

## 4. Array Reverse Recursion (In-Place or Non In-Place)
''' 
- Define a recursive function that takes an array as input.
- Swap the first and last elements.
- Recursively call the function with the remaining subarray.'''

def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)
''' 
Time Complexity: O(n). The recursion goes through each element once, so it’s linear.
Auxiliary Space Complexity: O(n) for non in-place, O(log n) for in-place (due to recursion stack).'''

## 5. Array Reverse Stack (Non In-Place)
''' 
- Push each element of the array onto a stack.
- Pop elements from the stack to form the reversed array.'''

def reverse_array_using_stack(arr):
    stack = []
    
    # Push elements onto the stack
    for element in arr:
        stack.append(element)
    
    # Pop elements from the stack to reverse the array
    for i in range(len(arr)):
        arr[i] = stack.pop()
''' 
Time Complexity: O(n)
    Pushing and popping each element onto/from the stack requires linear time.
Auxiliary Space Complexity: O(n)
    Additional space is used to store the stack.'''
