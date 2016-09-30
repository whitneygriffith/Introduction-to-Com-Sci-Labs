def GetDayOfYear(month, day):
    if month == 'january' or month == 'January':
        print(day)
    elif month == 'february' or month == 'February':
        print (31 + day)
    elif month == 'march' or month == 'March':
        print (59 + day)
    elif month == 'april' or month == 'April':
        print (90 + day)
    elif month == 'may' or month == 'May':
        print (120 + day)
    elif month == 'june' or month == 'June':
        print (151 + day)
    elif month == 'july' or month == 'July':
        print (181 + day)
    elif month == 'august' or month == 'August':
        print (212 + day)
    elif month == 'september' or month == 'September':
        print (243 + day)
    elif month == 'october' or month == 'October':
        print (273 + day)
    elif month == 'november' or month == 'November':
        print (304 + day)
    elif month == 'december' or month == 'December':
        print (334 + day)

GetDayOfYear('February' , 2)
GetDayOfYear('february' , 2)
GetDayOfYear('March' , 2)
