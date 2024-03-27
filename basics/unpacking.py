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