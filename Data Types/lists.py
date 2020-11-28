# --------- LISTS ---------
# Lists are ordered sequence that can hold a variety of objects types
# Supports indexing & slicing

myList = [1, 2, 3, 4, 5]
myList = [1, 'Samrat', 34.56, 'De']   # flexible
print(myList)

# checking length
print(len(myList))

# indexing
print(myList[1])

# slicing
print(myList[1:])
print(myList[2:3])

# concatenate
myList2 = [1, 2, 3]
newList = myList + myList2
print(newList)

# List is Mutable
myList[0] = 100
print(myList)


# Functions -

# append
myList.append('LastElement')
print(myList)

# pop
print(myList.pop())     # by default removes the last element
print(myList.pop(0))    # removing using index position
