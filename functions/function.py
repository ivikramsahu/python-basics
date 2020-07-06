'''
Python Function
def function_name(parameters):
    """docstring"""
    statement(s)
    
Keyword def that marks the start of the function header.
A function name to uniquely identify the function. Function naming follows the same rules of writing identifiers in Python.
Parameters (arguments) through which we pass values to a function. They are optional.
A colon (:) to mark the end of the function header.
Optional documentation string (docstring) to describe what the function does.
One or more valid python statements that make up the function body. Statements must have the same indentation level (usually 4 spaces).
An optional return statement to return a value from the function.    
'''


def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")


greet("vikram")

# function with return


def absolute_value(num):
    """This function returns the absolute      ----> this is
    value of the entered number                ----> DOCSTRING """

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))

print(absolute_value(-4))
