'''
 python output
 The actual syntax of the print() function is:
 print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
'''

import math

print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='&')

# formatting

x = 5
y = 10
print('The value of x is {} and y is {}'.format(x, y))

'''
Here, the curly braces {} are used as placeholders. We can specify the order in which they are printed by using numbers (tuple index).
'''

print('I love {0} and {1}'.format('bread', 'butter'))
print('I love {1} and {0}'.format('bread', 'butter'))

# OR

print('Hello {name}, {greeting}'.format(greeting='Goodmorning', name='John'))

# Python Inputs "input([prompt])"

num = input('Enter a number: ')
print(num)

# python imports

print(math.pi)
