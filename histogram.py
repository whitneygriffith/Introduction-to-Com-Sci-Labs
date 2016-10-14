def PrintHistogram(nums):
    #length of list
    length = len(nums)

    #case of empty lists
    if length == 0:
        return

    #count to keep track of the number of times a number appears
    count = 0

    #value for index
    index = 0

    #old target to stop looping a previously looped number
    old_target = 0


    for i in nums:
        target = i
        if i == old_target:
            continue
        for i in nums:
            if i == target:
                count += 1
                index = i
                old_target = i
            elif i != target:
                continue
        print(index, ":" , count * "*")
        count = 0

PrintHistogram([1, 2.5, 3, 3, 4, 4, 6])

