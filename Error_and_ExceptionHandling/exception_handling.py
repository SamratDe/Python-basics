num1 = 10
num2 = input()

try:
    result = num1 + num2
except TypeError:
    print('Wrong addition')
except:
    print('All other exceptions')
finally:
    print('I always run')