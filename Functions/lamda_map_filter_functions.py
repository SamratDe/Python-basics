# map function -

def square(n):
    return n ** 2

my_nums = [1, 2, 3, 4]

# map function syntax -> map(function, elements on which the function is applied)
myList = list(map(square, my_nums))
print(myList)



# filter function -
# it returns the iterator yielding those items of the iterable for which when you pass 
# in the item into the function it's true

def check_even(n):
    return not (n % 2)

my_nums = [1, 2, 3, 4, 5, 6]

myList = list(filter(check_even, my_nums))
print(myList)



# lamda expression -
# also known as anonymous function coz it's some functionality that you intent only use one time,
# so we don't give it a name 

# lambda exp of square
square_num = lambda n: n ** 2
print(square_num(5))

# lambda exp are used with map & filter
myList = list(map(lambda n: n ** 2, my_nums))
print(myList)

myList = list(filter(lambda n: not (n % 2), my_nums))
print(myList)