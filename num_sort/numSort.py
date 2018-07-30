"""A function that uses the bubble sort algorithm to sort the user input"""
def bubbleSortDesc(List):
    nums = list(List)
    for i in range(len(List)):
        for y in range (i+1, len(List)):
            if List[y] > List[i]:
                List[y], List[i] = List[i], List[y]
    return List
                
"""An array for the user input"""
numList = []
print("This program will ask you to input ten numbers of your choosing and sort them.")
"""A for loop that gathers the user input and puts into an array"""
for x in range(10):
    numbers=int(input())
    numList.append(numbers)

"""This block of code outputs the user input unsorted and sorted"""
print("Numbers before sorting")
print(numList)
print("--------------------------------------------------")
"""Calls an instance of the bubbleSortDesc function """
bubbleSortDesc(numList)
print("Numbers after sorting")
print(numList)

