var_1=float(input('Minutes:'))
num_hours= int(var_1 // 60)
num_minutes = int(var_1 % 60)
num_seconds = int(float(var_1 - (num_hours * 60)  - num_minutes) * 60)

print(num_hours, 'hours,', num_minutes, 'minutes',  num_seconds, 'seconds')
