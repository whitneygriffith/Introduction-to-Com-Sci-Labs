'''
Problem 3: Sorting frequencies
Create a file named sort_by_frequency.py. In it, write a function named SortByFrequency that sorts a list of numbers by how often they occur. The numbers that occur the most often should be placed earlier in the list. For example, the list [2, 3, 1, 2, 1, 2] should be sorted as [2, 2, 2, 1, 1, 3]. If multiple numbers occur the same number of times, then they should be put in the order of which came first. SortByFrequency should take a single parameter, a list of numbers, and should return a list of numbers.


Below are examples of what should be returned for different calls to SortByFrequency:
SortByFrequency(['pie', 6, 'pie', 9, 6, 7, 9, 9]) -> [9, 9, 9, 'pie', 'pie', 6, 6, 7]
SortByFrequency([3, -2, 6, 0, -2, 12345, 3, 7, 7, 7]) -> [7, 7, 7, 3, 3, -2, -2, 6, 0, 12345]
SortByFrequency([5]) -> [5]
SortByFrequency([ ]) -> [ ]


Some notes:
You are allowed to use Python sort functions.
You can assume that the values in the input list will be one of the following types: int, float, string.



'''
def SortByFrequency(lists):
	#length of lists
	length = len(lists)

	#sorted list (answer)
	sortedList = []
	
	#dictionary holding ocurrences and count for ocurrences
	dict1 = {}
	count = 0
	
	if length == 0:
		sortedList = []
		print(sortedList)
		return
	for i in lists:
		var = i
		count = 0
		for i in lists:
			if i == var:
				count += 1
			dict1[var] = count


	#values for the keys in dict1
	values = []
	for i in dict1.values():
		values += [i]
	values.sort()
	values.reverse()

	for i in values:
		val1 = i
		for var, i in dict1.items():

			if i == val1:
				count = i
				while count > 0:
					sortedList += [var]
					count -= 1
				del dict1[var]
				break
	print(sortedList)

SortByFrequency(['pie', 6, 'pie', 9, 6, 7, 9, 9])

