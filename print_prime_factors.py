def is_prime(i):
    test = 2

    if i == 2:
        return True
    while test < i:
        if i % test == 0:
            test += 1
            return False
        elif i % test != 0:
            test += 1
    return True

def PrintPrimeFactors(num):
    if num == 1:
        print('There are no prime factors for 1')
        return

    # actual prime factors
    prime_factors = []

    # final prime factors with duplicates
    final_factors = []

    # all factors
    factors = []

    #range of possible factors
    numbers = range(2, num+1)


    #getting all factors of the number
    for i in numbers:
        if num % i == 0:
            factors.append(i)

    #getting all prime factors in factors
    for i in factors:
        if is_prime(i) == True:
            prime_factors.append(i)
            i += 1
        else:
            i += 1

    for i in prime_factors:

        while num % i == 0 and num > 0:
            num = num / i
            final_factors.append(i)



    output = ''

    for index, i in enumerate(final_factors):
        if(index==len(final_factors)-1):
            print(i)
        else:
            print(i, '*', end=' ')


    print(output)






# printing of return
PrintPrimeFactors(24)
PrintPrimeFactors(11)
PrintPrimeFactors(1)
PrintPrimeFactors(1650)
PrintPrimeFactors(40378)
