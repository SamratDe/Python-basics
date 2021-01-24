# Generator functions allow us to write a function that can send back a value and then
# resume to pick up where it left off.

# When generator function is compiled they become an object that supports an iteration protocol,
# means when they are called in your code they don't actually return a value and then exit.

# e.g - range() function


def cubes(n):
    for x in range(n):
        yield x**3

def fibonacci(n):
    a = 1
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a+b