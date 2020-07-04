'''
Python tuple
1. Tuple is an ordered sequence of items same as a list. 
2. The only difference is that tuples are immutable. Tuples once created cannot be modified.
3. Tuples are used to write-protect data and are usually faster than lists as they cannot change dynamically.
4. Denoted by ().
'''

t = (5, 'program', 1+3j, 1)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
# slicing operator
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
t[0] = 10
