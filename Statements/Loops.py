myList = [1, 2, 3, 4, 5]

# FOR loops
for ele in myList:
    if ele % 2:
        print('%d is ODD' %ele)

for _ in 'Samrat':      #repeat len('Samrat') times
    print('Repeat')

for _ in myList:
    pass    # does nothing at all

# Tuple unpacking
tupList = [(1, 2), (3, 4), (5, 6)]
for (a, b) in tupList:
    print('%d -- %d' %(a, b))



# WHILE loops
x = 0
while x < 5:
    print(x)
    x += 1

while x < 7:
    print(x)
    x += 1
else:
    print('x is > 7')
