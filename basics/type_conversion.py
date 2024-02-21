'''
In programming, type conversion is the process of converting data of one type to another.
For example: converting int data to str.

There are two types of type conversion in Python.
- Implicit Conversion - automatic type conversion
- Explicit Conversion - manual type conversion

Implicit Conversion:
In certain situations, Python automatically converts one data type to another. This is known as implicit type conversion.

Explicit Conversion:
In Explicit Type Conversion, users convert the data type of an object to required data type.
'''

# implicit type conversion int to float
int_num = 15
float_num = 15.5
print(float(int_num) + float_num)
print(type(float(int_num) + float_num))

# explicit type conversion str to int
str_num = '12'
str_num = int(str_num)
print(12 + str_num)
print(type(12 + str_num))
