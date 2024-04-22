'''
List comprehension offers a shorter syntax to create a new list based on the values of an existing list.
'''

# creating a list of numbers with for statement
nums = []
for n in range(0, 10):
  nums.append(n)
print(nums) # 

# also creating a list of numbers with for statement in a short way with list comprehension
numbers = [number for number in range(0, 10)]
print(numbers)

# filtering strings from a list with list comprehension
words = ['Ball', 'Apple', 'Book', 'Chess', 'Computer', 'Water']
words_with_letter_a = [word for word in words if 'a' in word.lower()]
print(words_with_letter_a)

# filtering numbers from a list with list comprehension
even_numbers = [number for number in range(0, 10) if number % 2 == 0]
print(even_numbers)

double_numbers = [2 * number for number in range(0, 10)]
print(double_numbers)

# mapping list of dictionary with list comprehension
products = [
  {
    'name': 'notebook',
    'price': 2300,
  },
  {
    'name': 'phone',
    'price': 1100,
  },
]

products_with_discount = [
  {**product, 'discount': (20 * product['price']) / 100 }
  for product in products
]

print(products_with_discount)

# list comprehension with two for statements
list_inside_list = [(x, y) for x in range(0, 5) for y in range(0, 5)]
print(list_inside_list)