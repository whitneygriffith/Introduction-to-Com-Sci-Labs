def is_prime(i):
    factor = 2

    if i == 2:
        return True
    elif i <= 1:
        return False
    while factor < i:
        if i % factor == 0:
            factor += 1
            return False
        elif i % factor != 0:
            factor += 1
    return True

def CountPrimeNumbers(nums):
    # count for prime
    count_prime = 0

    # for loop to add to count
    for i in nums:
        if is_prime(i) == True:
            count_prime += 1
            i +=1
        else:
            i += 1
    print(count_prime)

CountPrimeNumbers([-3, -2, -1, 0, 1, 2, 3])
