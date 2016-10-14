def GetSecondLargestNumber(nums):
    #length
    length = len(nums)

    #case of empty lists
    if length == 0:
        print("None")
        return

    #largest number
    large = max(nums)

    #smallest number
    small = min(nums)

    #case of no distinct number
    if small == large:
        print("None")
        return

    #loop to find second largest
    for i in nums:
        if (i > small) and (i < large):
            small = i
    print(small)



GetSecondLargestNumber([])
