def PrintMultiplicationTable(num_1, num_2):
    #count for num_1
    count_1 = 1
    
    #count for num_2
    count_2 = num_2 + 1
    
    #while loop for table, iterating through count_1
    while count_1 <= num_1:
        #for loop to iterate through num_2
        for i in range(1, count_2):
            #variable for multiplication
            mult = count_1 * i
            print(count_1, 'X', i, '=', mult)
        count_1 += 1


PrintMultiplicationTable(4, 3)
PrintMultiplicationTable(2, 4)
PrintMultiplicationTable(3, 1)
