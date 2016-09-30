def GetIntersectionSize(range_1_min, range_1_max, range_2_min, range_2_max):
    if range_1_min == range_1_max or range_2_min == range_2_max:
        return 0
    elif range_1_min < range_2_min < range_1_max:
        intersection_min = range_2_min
        if intersection_min < range_1_max < range_2_max:
            intersection_max = range_1_max
        elif intersection_min < range_2_max < range_1_max:
            intersection_max = range_2_max
        return intersection_max - intersection_min
    elif range_2_min < range_1_min < range_2_max:
        intersection_min = range_1_min
        if intersection_min < range_1_max < range_2_max:
            intersection_max = range_1_max
        elif intersection_min < range_2_max < range_1_max:
            intersection_max = range_2_max
        return intersection_max - intersection_min
    elif range_1_min == range_2_min and range_1_max == range_2_max:
        return 0
    elif range_2_min > range_1_max:
        return -1
    elif range_2_max < range_1_min:
        return -1


# You don't need to change anything below this line.
range_1_min = int(input('Enter the min number for range 1: '))
range_1_max = int(input('Enter the max number for range 1: '))
range_2_min = int(input('Enter the min number for range 2: '))
range_2_max = int(input('Enter the max number for range 2: '))


intersection_size = GetIntersectionSize(
    range_1_min, range_1_max, range_2_min, range_2_max)
print('The intersection size is', intersection_size)
