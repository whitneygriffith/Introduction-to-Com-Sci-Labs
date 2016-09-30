def max_of_nights():
    sum_nights= sum(reservations)
    for i in reservation:
        while nights <= sum_nights:
            nights = i + 2
        return nights




#variables used

reservations = [5, 7, 10, 3]
nights = 0
max_of_nights([5, 7, 10, 3])
reservations = [5, 7, 10, 3]
