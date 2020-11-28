# --------- TUPLES ---------
# they are similar to Lists. One main difference is Immutability
# once an element is inside the Tuple, it cannot be reassigned - use for Data Integrity

t = (1, 2, 3, 1, 2, 1)
type(t)     # tuple

# indexing
print(t[3])
print(t[-1])


# Functions -

# count
print(t.count(1))       # shows no.of times '1' occurs in tuple

# index
print(t.index(2))       # shows the index of 2 (first appearance) in tuple t
