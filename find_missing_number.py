'''
Problem 2: Find missing number
Create a file named find_missing_number.py. In it, write a function named FindMissingNumber that finds the missing number in a list of numbers ranging from A to B. For example, the missing number in the list [45, 51, 47, 46, 50, 49] is 48. FindMissingNumber should take a single parameter, a list of numbers, and it should return a single number.


Below are examples of what should be returned for different calls to FindMissingNumber:
FindMissingNumber([-6, -11, -8, -9, -10]) -> -7
FindMissingNumber([45, 47]) -> 46


Some notes:
You are not allowed to use any Python sort functions.
You are not allowed to import any modules.
The input list will contain all the numbers within an arbitrary range except for one. The input will never be something like: [7, 4, 6, 5], and it will always have at least 2 numbers.
You can assume that the input list only contains whole numbers.

'''
def FindMissingNumber(lists):
	#creating dictionary to hold pairs
	dict1 = {}

	#missing number
	missing = -0

	#range for missing number
	range1 = 0
	
	for i in lists:
		var = i
		for i in lists:
			if var - i == 1 or var - i == -1:
				dict1[var] = i
	for i in lists:
		if i not in dict1:
			range1 = i
	for i in lists:
		if i - range1 == 2 or i - range1 == -2:
			range2 = i
	
	missing = range1 + 1
	if missing > range1 and missing < range1:
		missing = missing
	elif missing < range1 and missing > range2:
		missing = missing
	else: 
		missing = range1 - 1

	print(missing)

FindMissingNumber([45, 47])
FindMissingNumber([-6, -11, -8, -9, -10]) 
