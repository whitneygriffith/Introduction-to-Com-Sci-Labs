'''
Problem 1: Combine sorted lists
Create a file named combine_sorted_lists.py. In it, write a function named CombineTwoSortedLists that combines two sorted lists into a single sorted list. For example, the two list: [3, 4, 7, 9] and [1, 4, 8], would be combined to make the list [1, 3, 4, 4, 7, 8, 9]. CombineTwoSortedLists should take two list of numbers as parameters, and it should return a single list of numbers.


Below are examples of what should be returned for different calls to CombineTwoSortedLists:
CombineTwoSortedLists([6, 9, 11.5], [2, 4, 8]) -> [2, 4, 6, 9, 8, 11.5]
CombineTwoSortedLists([-3, -1, 0], [-2, 1]) -> [-3, -2, -1, 0, 1]
CombineTwoSortedLists([ ], [1, 2]) -> [1, 2]


Some notes:
You are not allowed to use any Python sort functions.
You are not allowed to import any modules.
You can assume that both input lists are sorted in ascending order.
You can assume the values in the input lists are either int or float.



'''
def CombineTwoSortedLists(listA, listB):
    #list that holds both listA and listB
    newList =[]
    
    #checking if any list is empty
    if len(listA) == 0:
    	newList = listB
    	print(newList)
    	return
    if len(listB) == 0:
    	newList= listA
    	print(newList)
    	return
    
    #variable holding minimum & max
    min = 0
    max= 0
    
    #variable holding the combined lists' maximum
    lengthA = len(listA) -1
    lengthB = len(listB) - 1
    biggest = 0
    if listA[lengthA] < listB[lengthB]:
    	biggest = listB[lengthB]
    else:
    	biggest = listA[lengthA]
		
    #transitioning list
    transList = listB
    
    for i in listA:
    	transList += [i]
	
    
    if listA[0] < listB[0]:
    	newList = [listA[0]]
    	min = listA[0]
    	max = listB[0]
    	transList.remove(min)
    	transList.remove(max)

    else:
    	newList = [listB[0]]
    	min = listB[0]
    	max = listA[0]
    	transList.remove(min)
    	transList.remove(max)

    #loop to sort transList based on minimum
    for i in transList:
    	if i < max:
    		newList += [i]
    	elif i > max:
    		newList += [max]
    		max = i
    if biggest not in newList:
    	newList += [biggest]	
    		
    print(newList)

CombineTwoSortedLists([ ], [1, 2]) 
