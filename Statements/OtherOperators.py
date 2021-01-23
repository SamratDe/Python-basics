# Useful Operators in Python

# range -
for num in range(10):       # prints numbers from 0-9
    print(num)

for num in range(3, 10):    # prints numbers from 3-9
    print(num)

for num in range(4, 10, 3):     # prints numbers from 4-9 with steps of 3
    print(num)

# generating a list
myList = list(range(2, 10, 2))



# enumerate - 
str = 'Hello'
for indx, letter in enumerate(str):     # enumerate output as tuples -> (index val, str character)
    print('At %d is the letter %s' % (indx, letter))



# zip - 
myList = [1, 2, 3]
myList2 = [5, 6, 7, 8]
# zip together 2/more lists together and return as tuple
for first, second in zip(myList, myList2):
    print('First = %d, Second = %d' % (first, second))
    


# in - 
# used for checking if an ele is present or not
7 in [1, 2, 4]  # returns False
'x' in ['x', 'y', 'z']  # returns True



# min & max -
# returns minimum and maximum values respectively
print(min(myList))
print(max(myList))



# random library -
from random import shuffle
shuffle(myList2)    # randomly shuffles the list
print(myList2)

from random import randint
val = randint(0, 100)   # returns random integer from 0-100
print(val)



# input -
# takes input from user
res = input('Enter string: ')     # always accepts input as string
print('You entered: %d' % res)

# taking integer input
res = int(input('Enter number: '))
print(res)