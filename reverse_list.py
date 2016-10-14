def ReverseList(lists):
    # count for the while
    count = -1

    # length of list (negative of the number)
    length = len(lists)
    length = -1 * length

    # new reverse list
    reverse_list = []

    #while loop to iterate through the lists starting from the last index (-1)
    while count >= length:
        reverse_list += [lists[count]]
        count -= 1
    print(reverse_list)


ReverseList([1, 2, 3, 4])
