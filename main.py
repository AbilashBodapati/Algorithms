"""
File Name: main.py
Author: Abilash Bodapati
Version: 20200606
Description:
    This is a Main file to test if the Sorting and Search algorithms work
    as they supposed to. 
"""

from Sorting import insertionSort

if __name__ == "__main__":
    example = [5, 2, 4, 6, 1, 3]
    print("Before Sorting: ")
    print (example)
    print("")
    insertionSort(example)
    print("After Sorting: ")
    print (example)
    print("")
