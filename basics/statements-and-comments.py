# Multiline statements 

a = 1 + 2 + \
    3 + 5 + \
    8 + 7 

print (a)
            
# OR 

b = ( 1 + 2 +
     3 + 6 +
     8 + 9
    )

print (b)

# OR 

colors = ['red',
          'blue',
          'green']

print (colors)

# OR

name = 1; surname = 2; value = 3

print(name , " + " , surname , " " + ":" , value)

# Docstrings : comment/string literal right after def/function

def sumOfTwo(p,q):
    """calculate sum of two"""
    return p+q

print(sumOfTwo(76,12))
    
