'''
There are several searching algorithms. The most commonly used among them are:

    Linear Search
    Binary Search
    Ternary Search
Linear Search:
Linear Search is defined as a sequential search algorithm that starts at one end and goes through each element of a list
until the desired element or group of elements is found. Otherwise, the search continues till the end of the data set. 
This has a time complexity of O(N) where ‘N’ is the length of the array

Binary Search:
Binary Search is a searching algorithm used in a sorted array. In this algorithm, the element is found by repeatedly dividing
the search interval in half and deciding the next interval to find the element. 
This searching algorithm has a time complexity of O(log 2 N) where ‘N’ is the length of the array. 
The only thing to note is that the array must be sorted in increasing or decreasing order.

Ternary Search:
Ternary search is a divide and conquer algorithm that can be used to find an element in an array. 
It is similar to binary search where we divide the array into two parts but in this algorithm, 
we divide the given array into three parts and determine which has the key (searched element). 
This algorithm also has the constraint that the array must be sorted. 
The time complexity for this algorithm is O(log 3 N) where ‘N’ is the size of the array.
'''