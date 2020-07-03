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




