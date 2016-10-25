'''
Problem 3: Find pair with target sum
Create a file named pair_with_sum.py. In it, write a function named HasPairWithTargetSum that checks whether a list of numbers has a pair of values with a given target sum. For example, if the list is: [1, 3, 7, 10] and the target sum is 10, the function should return True (3 + 7 = 10). If the target sum were 9, the function would return False. HasPairWithTargetSum should take two parameters, a list of numbers and the target sum, and should return a bool. The function definition should look like:


def HasPairWithTargetSum(nums, target_sum):


Some notes:
The input list can only contain ints and floats.
The input list can contain any range of values (e.g. negative numbers, 0, etc).
The values in the input list can be in any order (i.e. do not assume they are sorted).


Below are examples of what HasPairWithTargetSum should return given different input values:
HasPairWithTargetSum([1, 7, 3, 5], 12) -> True
HasPairWithTargetSum([1, 7, 3, 5], 9) -> False
HasPairWithTargetSum([4, -3, -1], 1) -> True
HasPairWithTargetSum([4, -3, -1], 0) -> False
HasPairWithTargetSum([2, 2, 3], 4) -> True
HasPairWithTargetSum([2, 2, 3], 6) -> False
HasPairWithTargetSum([ ], 1) -> False
'''

def HasPairWithTargetSum(nums, target_sum):
	#sort nums
	nums.sort()
	for i in nums:
		num = i
		#list not containing i
		new_list = nums
		new_list.remove(i)
		
		for i in new_list:
			if num + i == target_sum:
				print(True)
				return
	print(False)
	

HasPairWithTargetSum([1, 7, 3, 5], 12)
