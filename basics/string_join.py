'''
The join() method joins elements of an sequence(list, string, tuple) into a string, a string must be specified as the separator.
'''

# join using space as separator
words = ["How","are","you","doing","?"]
sentence = ' '.join(words)
print(sentence)

# join using tuples
fruits = ('Banana', 'Apple', 'Watermelon')
fruits_string = ', '.join(fruits)
print(fruits_string)

# join using string
programing_language = 'Python'
programing_language_string = '-'.join(programing_language)
print(programing_language_string)