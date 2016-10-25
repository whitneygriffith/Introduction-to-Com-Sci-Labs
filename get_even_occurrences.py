'''
Problem 1: Get even number of occurrences
Create a file named get_even_occurrences.py. In it, write a function named GetEvenNumOccurrences that returns all the values in a list that occur an even number of times. For example, if the list is: [3, 2, 'pie', 4, 3, 'pie' 4, 3], your function should return the list ['pie', '4']. GetEvenNumOccurrences should take a single parameter, a list of values, and it should return a list of values.


Below are examples of what should be returned for different calls to GetEvenNumOccurrences:
GetEvenNumOccurrences([1, 1, 1, 2, 2, 2, 2, 3, 3]) -> [2, 3]
GetEvenNumOccurrences(['fa', 'la', 'pa', 'la', 'fa']) -> ['fa', 'la']
GetEvenNumOccurrences(['pizza']) -> [ ]
GetEvenNumOccurrences([ ]) -> [ ]


Some notes:
You are not allowed to use the count function.
The values in the input list may be in any order (i.e. do not assume they're sorted)
You can assume the values in the input list are of the following types: int, float, string.


'''

def GetEvenNumOccurrences(lists):
	#length of lists
	length = len(lists)
	
	if length == 0:
		print([])
		return
	
	#my_dict
	my_dict= {}
	
	#adding first element to my_dict
	my_dict = {lists[0] : 0}
	
	#list contaaining my_dict items
	my_values = []
	my_keys = []
	
	#list containing answeer
	evenNum = []
	
	#for loop to create dictionary
	for i in lists:
		if i in my_dict:
			my_dict[i] += 1
		if i not in my_dict:
			my_dict[i] = 1

	my_values = list(my_dict.values())
	my_keys = list(my_dict.keys())
	
	#loop to remove the keys that do not have an even occurrence 
	
	for i in my_values:
		if i % 2 != 0:
			#index of i
			index = my_values.index(i)
			my_keys.pop(index)
			
		
	print(my_keys)
	
	
GetEvenNumOccurrences([ ]) 
