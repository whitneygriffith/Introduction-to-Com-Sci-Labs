'''
Create a file named anagram.py. In it, write a function named IsAnagram that takes two strings as input and returns True if they are anagrams and returns False otherwise. An anagram is a word, phrase, or sentence formed from another by rearranging its letters. For example, the string 'astronomer' is an anagram of the string 'moon starer' because they have the same letters, just in different order.

Below are examples of what should be returned for different calls to IsAnagram:
IsAnagram('mall', 'lama') -> False
IsAnagram('astronomer', 'moon starer') -> True
IsAnagram('astronomer', 'moon starrer') -> False
IsAnagram('cinema', 'iceman') -> True
IsAnagram('cinema', 'icemen') -> False
IsAnagram('i matthias', 'i am that is') -> True
IsAnagram('i am lord voldemort', 'tom marvolo riddle') -> True
IsAnagram('hot dog', 'potato') -> False
'''

def IsAnagram(string1, string2):
    # count to keep track of differences
    count = 0

    # loop iterating through string
    for i in string1:        
        #ignoring spaces
        if i == ' ':
            continue
            
        #if i is not in string it's definitely not an anagram     
        if i not in string2:
            count += 1
            
        # num times i occurs in the string1
        num1 = string1.count(i)
        num2 = string2.count(i)

        if num1 != num2:
            count += 1
    if count > 0:
        print('False')
    else:
        print('True')

IsAnagram('mall', 'lama')
IsAnagram('astronomer', 'moon starer')
IsAnagram('astronomer', 'moon starrer')
IsAnagram('cinema', 'iceman')
IsAnagram('cinema', 'icemen')
IsAnagram('i matthias', 'i am that is')
IsAnagram('i am lord voldemort', 'tom marvolo riddle') 
IsAnagram('hot dog', 'potato')





