'''
 1. Keywords are reserved words which cannot be used as variable name or function name.   
 2. Keywords are case sensitive (ie. VikRam and vikram are different).                      
 3. There are 33 keywords (can slightly vary) in which expect (True, False and None) all are in lowercase.
'''

import keyword

print("\nList of keywords ↠ ",  keyword.kwlist)

''' Output :

 List of keywords ↠  ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 
 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
 'try', 'while', 'with', 'yield']

 using Keywords 
 True, False and None
'''

print ("\n Boolean Operations True / False (1 or 0)")
print ("Output for 1 == 1 is ↠ " , 1 == 1)
print ("Output for 2 < 1 is ↠ " , 2 < 1)
print ("Output for 1 >= 3 is ↠ " , 1 >= 3)

''' About None datatype :
 It is a special constant that represent absence of value or null value.
 It has its own datatype "NoneType". 
 NOTE :
 1. We cannot create multiple None objects but can be assign to variables.
 2. None is not equal to False, 0 or any other datatype like empty list, dictionary, string etc 
'''
x = None
y = None
print ("\nConcepts for None keyword:")
print ("None == 0 ↠ ", None == 0)
print ("None == False ↠ ", None == False)
print ("None == [] ↠ ", None == [])
print ("Comparing x, y value as None (ie. x == y)  ↠ ", x == y)

'''
Void functions return None values
or functions which do not have a return statement
'''
def mineVoidFunction():
    x = 1
    y = 3
    z = x + y
    
print("A function mineVoidFunction with no return statement :: ",mineVoidFunction())
    
# Function with improper return

def improperReturn(a):
    if (a % 2) == 0:
        return True

print("A function with improper output :: ", improperReturn(5))

# And, OR (you can similarly follow all rules for True False)

print("True and False :: ", True and False)
print("True or False :: ", True or False)

''' as, assert, async, await, break and continue
as     ↠  alias for packages
assert ↠  debugging purposes
async and await  ↠  concurrent code
break  ↠  
continue ↠
'''

import math as vikram

print("Factorial of number using alias :: ", vikram.factorial(4))

'''
fact = 20
message = "ALert"

if not (fact > vikram.factorial(5)):
    raise AssertionError(message)
'''

import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(2)
    print ("World")

#asyncio.run(main())

for i in range(1,11):
    if i == 5:
        print("Hello man")
        continue # break
    else :
        print(i)
        
''' 
There are many more keywords that can be seen furthur with advance python and OOPs concept.

About Identifiers:
1. Identifier is name given to class, function, variables etc which helps to differentiate with others.
2. Can be combination of lowercase, uppercase and digits ie. hello_1_my_Variable
3. An identifier cannot start with digit.
4. keywords cannot be used as identifiers.
'''

