def AreStringsSimilar(string1, string2):
    # in case the strings are equal
    if string1 == string2:
        print('True')
        

    # variables
    length1 = len(string1)
    length2 = len(string2)

    # count to keep track of the number of elements that differ
    count = 0

    # looping based on the longer string
    if (length1 - length2) == 1:
        count += 1
        # loop to loop through shorter string
        for i in string2:
            # membership check for if i is in the other string
            if i not in string1:
                count += 1
        # if count is more than 1 then it differs in more than one way
        if count > 1:
            print('False')
            
        else:
            print('True')
    elif (length2 - length1) == 1:
        count += 1
        for i in string1:
            if i not in string2:
                count += 1
        if (count > 1):
            print('False')
        else:
            print('True')

    elif length1 == length2:
        for i in string1:
            if i not in string2:
                count += 1
        if count > 1:
            print('False')
            
        else:
            print('True')
    else:
        print('False')
        
AreStringsSimilar('potato', 'potatoe')
AreStringsSimilar('potato', 'potatoes') 
AreStringsSimilar('turkey', 'tuken')
AreStringsSimilar('turkey', 'tukey')
AreStringsSimilar('', 'a')
AreStringsSimilar('spot', 'pot')
