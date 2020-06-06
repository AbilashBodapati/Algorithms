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

def mergeSort(self, parameter_list):
    # TODO: Implement Merge Sort
    pass

def heapSort(self, parameter_list):
    # TODO: Implement Heap Sort
    pass

def quickSort(self, parameter_list):
    # TODO: Implement Quick Sort
    pass

def bubbleSort(self, parameter_list):
    # TODO: Implement Bubble Sort
    pass

def countingSort(self, parameter_list):
    # TODO: Implement Counting Sort
    pass

def radixSort(self, parameter_list):
    # TODO: Implement Radix Sort
    pass

def bucketSort(self, parameter_list):
    # TODO: Implement Bucket Sort
    pass

def topoSort(self, parameter_list):
    # TODO: Implement Topological Sort
    pass