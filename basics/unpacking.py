# unpacking a list
colors = ['red', 'green', 'yellow']
red, green, yellow = colors
print(red, green, yellow)

# unpacking the leftover elements with asterisk (*), the * 'll pack the leftover elements into a new list
name_1, name_2, *other_names = ['John', 'Clara', 'Sarah', 'Tim', 'Jonah']
print(name_1, name_2, other_names)

# unpacking specific elements from list and ignoring other elements using the underscore (_) convention.
python, _, ruby, _ = ['Pthon', 'JavaScript', 'Ruby', 'Java']
print(python, ruby)

# unpacking a dictionary
user = {
  'name': 'John Doe',
  'email': 'john@example.com',
  'age': 27,
}
name, email, age = user.values()
print(name, email, age)

# unpacking the leftover elements from dictionary
name, *rest = user.values()
print(name, rest)

# unpacking specific elements from dictionary
_, _, age = user.values()
print(age)

# unpacking the first and last elements from dictionary
name, *_ = user.values()
*_, age = user.values()
print(name, age)

dict_1 = { 'name': 'John', 'age': 27 }
dict_2 = { 'email': 'john@example.com', id: 256 }
dict_3 = { **dict_1, **dict_2 }
print(dict_3)