'''
Python list
List is ordered sequence of items. It is very flexible and one of the most used datatype. 
denoted by []. starting index 0
'''

a = [5, 'Pythonlist', 10, 15, 20, 25, 30, 35, 40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

# imp : Lists are mutable, meaning, the value of elements of a list can be altered.

b = [1, 2, 3]
b[2] = 4
print(b)
