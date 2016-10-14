def IsPalindrome(lists):
    #length of list
    length = len(lists)

    #count for the positive direction (index value)
    count = 0

    #count for the negative direction
    neg_count = -1

    #always true if there is only one element
    if length == 1:
        print("True")
        return

    #while loop comparing elements of opposite ends
    while (count < length):
        if lists[count] != lists[neg_count]:
            print("False")
            return
        count += 1
        neg_count -= 1
    print("True")

IsPalindrome([10])
IsPalindrome(['pizza', 14, 'corn', 14, 'pizza']) 
