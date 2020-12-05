# function syntax
# def function_name(parameters):
#   body
#   of
#   function


def add_numbers(num1, num2):
    return num1 + num2

def check_even(num):
    return num % 2 == 0

res = add_numbers(1, 100)
res = check_even(24)



# Tuple unpacking with functions
def check(val, target):
    for name, roll in val:
        if name == target:
            return (name, roll)

tup = [('Samrat', 31), ('Lila', 21), ('Subhas', 21)]
name, roll = check(tup, 'Samrat')
print('%s has roll number %d' % (name, roll))



# Interaction between python functions
# making a guessing game, where player guesses the 'X' position in the array

def player_guess():
    guess = ''
    while guess not in ['1', '2', '3']:
        guess = input('Guess a position between 1 to 3: ')
    return int(guess) - 1

def shuffle_list(arr):
    from random import shuffle
    shuffle(arr)
    return arr

def play(arr):
    while True:
        arr = shuffle_list(arr)
        pos = player_guess()
        if arr[pos] == 'X':
            print('You guessed CORRECT !')
            break
        else:
            print('Try again !')

game = ['.', '.', 'X']
play(game)
