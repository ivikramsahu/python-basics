'''
String is sequence of Unicode characters.
Denoted by """ or single quote
'''
s = "This is a string"
print(s)
s = '''A multiline
string'''
print(s)


s = 'Hello world!'

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

# Generates error
# Strings are immutable in Python
s[5] = 'd'
