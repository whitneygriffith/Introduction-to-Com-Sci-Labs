'''
Problem 2: Queue
Create a file named queue.py. In it, write a class named Queue that represents a new data type called a queue. A queue is is like a list. It's a container, so it can store any number of values. You can add and remove values from it. However, the order of the values removed depends on the order in which they were added. The value removed is the one that was added earliest. For example, if I add the values 5, 7, 11 to a queue (in that order), the first value to be removed will be 5, the second would be 7, and the last would be 11. You can read more about the queue data type here.


Queue should have the following functions defined inside it:
add(value)
Adds the value to the queue.
remove()
Removes and returns the value in the queue that was added earliest.
print_values()
Prints all the values inside the queue in the order that they were added.


Some notes:
You are not allowed to import any modules.
Remember to have remove() return the value that is removed.
print_values() can print the values in any format. They just need to be printed in the order that they were added.


Below is an example of how an object of this class should work.


Example
>>> my_queue = Queue()
>>> my_queue.add(5)
>>> my_queue.add('pizza')
>>> my_queue.add(False)
>>> my_queue.add('sunshine')
>>> my_queue.print_values()
5, 'pizza', False, 'sunshine'
>>> my_queue.remove()
>>> my_queue.print_values()
'pizza', False, 'sunshine'
>>> my_queue.add(42)
>>> my_queue.remove()
>>> my_account.print_values()
False, 'sunshine', 42

'''

class Queue:
  def __init__(self):
    #variable to hold list
    self.queueList = []
  def add(self, value):
    self.queueList += [value]
  def print_values(self):
      #returning list as individual items i converted the list to a string and stripped the string of the []
      strings = str(self.queueList)
      strings = strings.strip('[')
      strings = strings.strip(']')
      print(strings)
  def remove(self):
    return self.queueList.pop(0)
      
    
my_queue = Queue()
my_queue.add(5)
my_queue.add('pizza')
my_queue.add(False)
my_queue.add('sunshine')

my_queue.print_values()

my_queue.remove()
my_queue.print_values()

my_queue.add(42)
my_queue.remove()
my_queue.print_values()
