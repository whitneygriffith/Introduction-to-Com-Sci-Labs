def PrintMultiples(start, end, multiple):
    count = 0
    if multiple <= 0:
        print ('Input multiple must be greater than 0')
    elif start > end:
               
        #pass end as start and start as end
        for i in range(end, start + 1):
            while (i % multiple) == 0 or multiple == 1:
                print(i)
                count += 1
                i += 1
        if count == 0:
            print('There are no multiples of {} in the range of {} to {}'.format(multiple, start, end))
                        
                
    
    elif start == end:
       
        while start == end and ((start % multiple) == 0 or multiple == 1):
            
            print(start)
            count += 1
            start += 1
        if count == 0:
            print('There are no multiples of {} in the range of {} to {}'.format(multiple, start, end))


    elif start < end:
        
                
        for i in range(start, end + 1):
            
            while (i % multiple) == 0 or multiple == 1:
                print(i)
                i += 1
                count += 1
                
        if count == 0:
            print('There are no multiples of {} in the range of {} to {}'.format(multiple, start, end))

    


PrintMultiples(1, 5, 0)


