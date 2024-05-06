'''
In Python, the with statement replaces a try-catch block.
It ensures properly closing resources after processing them. It is known as a context manager.
- A context manager allows you to open and close resources properly when they are no longer needed.
'''

# open the file
file = open('hello.txt', 'w')

try:
    # write to the file
    file.write('Hello world!')
except Exception as error:
    print(f'An error occurred while writing to the file: {error}')
finally:
    # close the file after write
    file.close()

# write the file with (with) statement
with open('hello_2.txt', 'w') as file_2:
    file_2.write('Hello world 2!')
