"""
File Name: Sorting.py
Author: Abilash Bodapati
Version: 20200606
Description:
    This is a Python module that implements some of the basic Sorting
    algorithms.
    This includes:
        1. Insertion sort
        2. Merge Sort
        3. Heap Sort
        4. Quick Sort
        5. Bubble Sort
        6. Counting Sort
        7. Radix Sort
        8. Bucket Sort
        9. Topological Sort
    Check out the README.md file for more information regarding the sorting
    algorithms.
"""

def insertionSort(array):
    # TODO: Implement Insertion Sort
    for iteration in range(0, len(array)):
        element = array[iteration]
        # Insert value in "element" into the sorted list array  
        insertIter = iteration - 1
        while insertIter >= 0 and array[insertIter] > element:
            array[insertIter+1] = array[insertIter]
            insertIter -= 1
        array[insertIter+1] = element

def mergeSort(array):
    # TODO: Implement Merge Sort
    if len(array) > 1:
        # Create a midpoint value
        midpoint = len(array) // 2

        # Create the left and right subarrays
        left = array[:midpoint]
        right = array[midpoint:]

        # Call the mergeSort recusively on the left and right arrays
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                array[k] = left[i] 
                i+= 1
            else: 
                array[k] = right[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
        while i < len(left): 
            array[k] = left[i] 
            i+= 1
            k+= 1
          
        while j < len(right): 
            array[k] = right[j] 
            j+= 1
            k+= 1

def heapSort(array):
    # TODO: Implement Heap Sort
    pass

def quickSort(array):
    # TODO: Implement Quick Sort
    pass

def bubbleSort(array):
    # TODO: Implement Bubble Sort
    pass

def countingSort(array):
    # TODO: Implement Counting Sort
    pass

def radixSort(array):
    # TODO: Implement Radix Sort
    pass

def bucketSort(array):
    # TODO: Implement Bucket Sort
    pass

def topoSort(array):
    # TODO: Implement Topological Sort
    pass