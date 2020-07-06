# Type conversion

print("Converting int to float", float(5))

print("converting float to int", int(5.78))

print("converting int to string", str(123.12))

set([1, 2, 3])
tuple({5, 6, 7})

# Implicit Type Conversion
# Python handles itself
# int to float

num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:", type(num_int))
print("datatype of num_flo:", type(num_flo))

print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))

# Explicit Type Conversion
# Python needs external type conversion
# This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.

num_int = 123
num_str = "456"

print("Data type of num_int:", type(num_int))
print("Data type of num_str before Type Casting:", type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:", type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:", num_sum)
print("Data type of the sum:", type(num_sum))
