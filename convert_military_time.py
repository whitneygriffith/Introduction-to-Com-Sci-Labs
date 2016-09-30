hour1 = int(input('Enter the hour (ranging from 0 to 23): '))
min1 = int(input('Enter the minute (ranging from 0 to 59): '))
hour2 = int(hour1 - 12)

if (hour1 > 0 and hour1 <= 11) and (min1 >= 10 and min1 <= 59):
    print(hour1, ':', min1, 'am')
elif (hour1 > 0 and hour1 <= 11) and (min1 >= 0 and min1 <= 9):
    print(hour1, ':0', min1, 'am')
elif hour1 == 0  and (min1 >= 10 and min1 <= 59):
    print('12:', min1, 'am')
elif hour1 == 0  and (min1 >= 0 and min1 <= 9):
    print('12:0', min1, 'am')
elif (hour1 > 12 and hour1 <= 23 ) and (min1 >= 10 and min1 <= 59):
    print(hour2, ':', min1, 'pm')
elif (hour1 > 12 and hour1 <= 23 ) and (min1 >= 0 and min1 <= 9):
    print(hour2, ':0', min1, 'pm')
elif hour1 == 12 and (min1 >= 10 and min1 <= 59):
    print(hour1, ':', min1, 'pm')
elif hour1 == 12 and (min1 >= 0 and min1 <= 9):
    print(hour1, ':0', min1, 'pm')
