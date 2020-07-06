'''
Python Dictionary
1. Dictionary is an unordered collection of key-value pairs.
2. Used when we have huge amount of data.
3. Denoted by {}, each item paired with key:value
'''

d = {1: 'value', 'key': 2}
print(type(d))

print("d[1] = ", d[1])

print("d['key'] = ", d['key'])

# Generates error
print("d[1] = ", d[2])
