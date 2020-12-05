# args & kwargs
# stands for arguments and key-word arguments

# *args is used when we want to pass arbitary number of arguments
def myFunc(*args):  # here, args is a tuple
    return sum(args) * 0.01

res = myFunc(1, 2, 3)
res = myFunc(1, 2, 3, 4)

# **kwargs builds a dictionary of key value pairs
def myFunc1(**kwargs):
    if 'Samrat' in kwargs:
        print('Samrat studies in %s' % kwargs['Samrat'])
    else:
        print('No data about Samrat !')

myFunc1(Samrat='NIT Dgp', Lila='IIT Kgp')

# Both args & kwargs combined
def myFunc2(*args, **kwargs):
    print('I want to buy %d %s' % (args[1], kwargs['fruits']))
    
myFunc2(10, 20, 30, fruits='Oranges', vegetables='Broccoli')



def find_primes(n):
    if n < 2:
        return []
    primes = [2]
    x = 3
    while x <= n:
        for y in range(3, x, 2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)