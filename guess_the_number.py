def GuessTheNumber(mystery_num):
    #count for guesses
    count = 0

    #variable for input
    input1 = 0
    
    #while loop for guesses
    while input1 != mystery_num: 
        #variable for input
        input1 = int(input("Enter a guess:"))
        if input1 < mystery_num:
            print("Too low!")
            count += 1
        elif input1 > mystery_num:
            print("Too high!")
            count += 1
    # variable to whole the string guess
    if count == 1:
        guess = "guess."
    else:
        guess = "guesses."
    #output if guess is correct
    if input1 == mystery_num:
        print("You're correct! It took you ", count, guess)



GuessTheNumber(8)
