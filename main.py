"""
File Name: main.py
Author: Abilash Bodapati
Version: 20200606
Description:
    This is a Main file to test if the Sorting and Search algorithms work
    as they supposed to. 
"""

from Sorting import *

if __name__ == "__main__":
    example = [5, 2, 4, 6, 1, 3]
    print("Before Sorting: ")
    print (example) 
    print('\n')
    insertionSort(example)
    print("After Sorting: ")
    print (example) 
    print('\n')
    
    example = [5, 2, 4, 6, 1, 3]
    print("Before Sorting: ")
    print (example) 
    print('\n')
    mergeSort(example)
    print("After Sorting: ")
    print (example) 
    print('\n')

    example = [5, 2, 4, 6, 1, 3]
    print("Before Sorting: ")
    print (example) 
    print('\n')
    heapSort(example)
    print("After Sorting: ")
    print (example) 
    print('\n')

    example = [5, 2, 4, 6, 1, 3]
    print("Before Sorting: ")
    print (example) 
    print('\n')
    quickSort(example)
    print("After Sorting: ")
    print (example) 
    print('\n')

    example = [5, 2, 4, 6, 1, 3]
    print("Before Sorting: ")
    print (example) 
    print('\n')
    bubbleSort(example)
    print("After Sorting: ")
    print (example) 
    print('\n')

    example = [5, 2, 4, 6, 1, 3]
    print("Before Sorting: ")
    print (example) 
    print('\n')
    countingSort(example)
    print("After Sorting: ")
    print (example) 
    print('\n')

    example = [5, 2, 4, 6, 1, 3]
    print("Before Sorting: ")
    print (example) 
    print('\n')
    radixSort(example)
    print("After Sorting: ")
    print (example) 
    print('\n')

    example = [5, 2, 4, 6, 1, 3]
    print("Before Sorting: ")
    print (example) 
    print('\n')
    bucketSort(example)
    print("After Sorting: ")
    print (example) 
    print('\n')

    example = [5, 2, 4, 6, 1, 3]
    print("Before Sorting: ")
    print (example) 
    print('\n')
    topoSort(example)
    print("After Sorting: ")
    print (example) 
    print('\n')