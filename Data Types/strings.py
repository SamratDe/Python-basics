# ---------- STRINGS ----------
# Strings are not mutable

name = "Samrat"

# indexing
print(name[1])          # index at position 1 = 'a' (0-based index)

# slicing
print(name[2:])         # from position 2 to end = "mrat De"
print(name[2:4])        # from position 2 to position 3 = "mr"

# concat
name = name + " De"
print(name)

new_str = "xxx" * 5     # string xxx repeats 5 times
print(new_str)

# builtin functions
print(name.upper())     # makes the string uppercase = SAMRAT
print(name.lower())
print(name.split())     # splits the string into lists (by default based on " ")
print(name.split('a'))  # splits based on given character


# formatting (3 methods) -

# with placeholders (use this)
print('My name is %s. I study in %s.' %(name, 'NIT Durgapur'))
print('Value is : %.3f' %(10/9))

# .format() method
print('My {} {} Samrat'.format('name', 'is'))       # normal way
print('My {1} {0} Samrat'.format('is', 'name'))     # based on index
print('My {n} {i} Samrat'.format(n = 'name', i = 'is')) # giving names for strings
print('Value is {val:1.3f}'.format(val=100.0/80))   # floating number precision

# f-string method
print(f'My name is {name}')     # adding f before the string