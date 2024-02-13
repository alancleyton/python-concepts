'''
There are three numeric types in Python;

int
float
complex
'''

'''
Int, or integer, is a whole number without decimals
'''
int_num = 25
print(f'the value of int_num is: {int_num}')
print(f'the type of int_num is: {type(int_num)}')

'''
In Python, you can't use commas to group digits in integer literals, but you can use underscores.
'''
int_num_group = 27_59_00
print(f'the value of int_num_group is: {int_num_group}')

'''
Float, or floating point number, is a number with one or more decimals.
'''
float_num = 1.25
print(f'the value of float_num is: {float_num}')
print(f'the type of float_num is: {type(float_num)}')

'''
Float can also be scientific numbers with an "e" to indicate the power of 10.
'''
scientific_num = 12e4
print(f'the value of scientific_num is: {scientific_num}')
print(f'the type of scientific_num is: {type(scientific_num)}')

'''
Type Conversion from one type to another with the int() and float() methods.
'''
int_num = '65'
int_num_str = int(int_num)
print(f'the value of int_num_str is: {int_num_str}')
print(f'the type of int_num_str is: {type(int_num_str)}')


float_num = '54.68'
float_num_str = float(float_num)
print(f'the value of float_num_str is: {float_num_str}')
print(f'the type of float_num_str is: {type(float_num_str)}')