def CountVowels(string):
    count = 0
    for i in string:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' :
            count += 1
    print(count)


CountVowels('pizza')
CountVowels('i like ike')
CountVowels('today was a good day')
CountVowels('grrrrrrrrrr')
CountVowels('')
