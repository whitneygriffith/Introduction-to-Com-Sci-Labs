def IsLeapYear(year):
    if year % 100 == 0 and year % 400 == 0:
        print ('True')
    elif year % 100 == 0 and year % 400 != 0:
        print ('False')
    elif year % 100 != 0 and year % 4 == 0:
        print('True')
    elif year % 100 != 0 and year % 4 != 0:
        print('False')
    

IsLeapYear(300)


