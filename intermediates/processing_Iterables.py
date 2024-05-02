'''
the map() function executes a given function to each element of an iterable and returns a map object (which is an iterator).
'''

numbers = [3, 5, 8, 10, 4]

def square(number):
  return 2 * number

# returns the square of each number
squares = map(square, numbers)
print(list(squares))

# returns the square of each number using lambda
squares_with_lambda = map(lambda number: 2 * number, numbers)
print(list(squares_with_lambda))


'''
the filter() function filters an iterable with the execution of a function that tests each element in the sequence.
'''

products = [
  { 'name': 'product 1', 'price': 231.50 },
  { 'name': 'product 2', 'price': 59.99 },
  { 'name': 'product 3', 'price': 105.29 },
  { 'name': 'product 4', 'price': 20.19 },
  { 'name': 'product 5', 'price': 69.90 },
  { 'name': 'product 6', 'price': 48.50 },
]

# returns products with price above 100
expensive_products = list(filter(lambda product: product['price'] > 100, products))
print(expensive_products)


letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o', 'w', 't']

def filter_letters_vowels(letter):
  vowels = ['a', 'e', 'i', 'o', 'u']
  return True if letter in vowels else False

# returns only vowel letters
letters_vowels = list(filter(filter_letters_vowels, letters))
print(letters_vowels)

'''
the functools reduce() function is used to execute a function to all elements in iterable and reduce it to a single cumulative value.
'''

from functools import reduce

nums = [2, 5, 11, 35, 19, 48]

sum_of_nums = reduce(lambda acc, num: acc + num, nums)
print(sum_of_nums)