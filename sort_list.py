def SortList(lists):
    # length of list
    length = len(lists)

    # length = 0 or lentgh =1
    if length == 0 or length == 1:
        print(lists)
        return


    #minimum value in list
    minimum = min(lists)

    #new minimum
    new_minimum = minimum

    #old minimum
    old_minimum = minimum

    # new lists
    sorted_list = [minimum]

    # loop
    for i in lists:
        if i == minimum:
            continue
        if i > new_minimum:
            sorted_list += [i]
            new_minimum = i
        elif i < new_minimum:
            sorted_list.remove(new_minimum)
            if old_minimum != minimum:
                sorted_list.remove(old_minimum)
            sorted_list.append(i)
            if old_minimum != minimum:
                sorted_list.append(old_minimum)
            sorted_list.append(new_minimum)
            old_minimum = new_minimum
            new_minimum = i
    print(sorted_list)


SortList([6, 4, 2, -1])
SortList([6, 3, 9, 2, 3])
