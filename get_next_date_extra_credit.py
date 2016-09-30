def GetNextDate(day, month, year, num_days_forward):
    if month == 1 and day < 31:
        print(month, '/', day + 1, '/', year)
    elif month == 1 and day == 31:
        print(month + 1, '/', '1', '/', year)
    elif month == 2 and day < 28:
        print(month, '/', day + 1, '/', year)
    elif month == 2 and day == 28:
        print(month + 1, '/', '1', '/', year)
    elif month == 3 and day < 31:
        print(month, '/', day + 1, '/', year)
    elif month == 3 and day == 31:
        print(month + 1, '/', '1', '/', year)
    elif month == 4 and day < 30:
        print(month, '/', day + 1, '/', year)
    elif month == 4 and day == 30:
        print(month + 1, '/', '1', '/', year)
    elif month == 5 and day < 31:
        print(month, '/', day + 1, '/', year)
    elif month == 5 and day == 31:
        print(month + 1, '/', '1', '/', year)
    elif month == 6 and day < 30:
        print(month, '/', day + 1, '/', year)
    elif month == 6 and day == 30:
        print(month + 1, '/', '1', '/', year)
    elif month == 7 and day < 31:
        print(month, '/', day + 1, '/', year)
    elif month == 7 and day == 31:
        print(month + 1, '/', '1', '/', year)    
    elif month == 8 and day < 31:
        print(month, '/', day + 1, '/', year)
    elif month == 8 and day == 31:
        print(month + 1, '/', '1', '/', year)
    elif month == 9 and day < 30:
        print(month, '/', day + 1, '/', year)
    elif month == 9 and day == 30:
        print(month + 1, '/', '1', '/', year)
    elif month == 10 and day < 31:
        print(month, '/', day + 1, '/', year)
    elif month == 10 and day == 31:
        print(month + 1, '/', '1', '/', year)
    elif month == 11 and day < 30:
        print(month, '/', day + 1, '/', year)
    elif month == 11 and day == 30:
        print(month + 1, '/', '1', '/', year)
    elif month == 12 and day < 31:
        print(month, '/', day + 1, '/', year)
    elif month == 12 and day == 31:
        print('1', '/', '1', '/', year + 1)

GetNextDate(20, 7, 2016)
GetNextDate(31, 12, 2016)
GetNextDate(30, 5, 2016)
