'''
Problem 2: Get location path
Download the starter files locations.py and get_location_path.py (link here). locations.py containns a dictionary of geographical location pairs (e.g. city and state, state and country, country and continent, etc). Open that file and make sure you understand how the dictionary is structured.


Your job is to write a program in get_location_path.py that ask the user for a location and prints the "location path" -- all of the locations from that location to the top level location. For example, if the user enters chicago, the program should print "chicago, illinois, united states, north america, earth". For this problem, you only need to modify get_location_path.py. If you want, you can add more location pairs to locations.py.


Some notes:
Everything should be in lowercase (e.g. 'chicago' instead of 'Chicago')
A comma should separate each location in the printed output. However, there shouldn't be a comma after the last location (e.g. no "united states, north america, earth,").
If the user enters a location not in the dictionary, you can output whatever you want.


See below for examples.


        = user input


Example
>>> 
Enter a location:  chicago 
>>> chicago, illinois, united states, north america, earth


Example
>>> 
Enter a location:  illinois
>>> illinois, united states, north america, earth


Example
>>> 
Enter a location:  lagos 
>>> lagos, nigeria, africa, earth


Example
>>> 
Enter a location:  tharsis 
>>> tharsis, mars


Example
>>> 
Enter a location:  earth 
>>> earth
'''

from locations import location_dict

#user entered location

input1 = input('Enter a location: ')

#variable for four other possible outputs
var1 = ''
var2 = ''
var3 = ''
var4 =''


#finding the starting key

for key, value in location_dict.items():
    if key == input1:
        var1 = value        
        print('%s, %s' % (input1, var1), end='')
            
for key, value in location_dict.items():
    if key == var1:
        var2 = value
        print(', %s' %(var2), end='')

for key, value in location_dict.items():
    if key == var2:
        var3 = value
        print(', %s' % (var3), end='')
        
for key, value in location_dict.items():
    if key == var3:
        var4 = value
        print(', %s' % (var4))

if input1 == 'earth' or input1 == 'mars':
    print(input1)
