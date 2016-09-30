print('Do not enter the same number twice')
n1 = int(input('Enter 1st number: '))
n2 = int(input('Enter 2nd number: '))
n3 = int(input('Enter 3rd number: '))

if (n1 > n2 and n1 > n3) and n2 > n3:
    print('The middle number is: ', n2, '.')
elif (n1 > n2 and n1 > n3) and n2 < n3:
    print('The middle number is: ', n3, '.')
elif (n2 > n1 and n2 > n3) and n1 < n3:
    print('The middle number is: ', n3, '.')
elif (n2 > n1 and n2 > n3) and n1 > n3:
    print('The middle number is: ', n1, '.')
elif (n3 > n1 and n3 > n2) and n1 > n2:
    print('The middle number is: ', n1, '.')
elif (n3 > n1 and n3 > n2) and n1 < n2:
    print('The middle number is: ', n2, '.')
