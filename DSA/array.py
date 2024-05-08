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
