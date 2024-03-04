# conditional statement based on logical expressions

print('A' == 'A') # Equals -> True
print('A' != 'a') # Not Equals -> True
print(2 < 1)      # Less than -> False
print(2 <= 1)     # Less than or equal to -> False
print(2 > 1)      # Greater than -> True
print(2 > 1)      # Greater than or equal to -> True

# conditional statement using if statement
if 2 > 1:
    print('2 is greater than 1')

# conditional statement on the same line using if short hand
if 1 < 5: print('1 is less than 5')

'''
Python allows to write if statements on one line, they are called
conditional expression(also called a ternary operator).
'''
age = 17
age_category = 'Teenage' if age <= 17 else 'Adult'
print(age_category)

# multiple conditional statement using elif statement
language = 'Ruby'

if language == "Ruby":
    print("i'm studing Ruby 💎")
elif language == "Python":
    print("i'm studing Python 🐍")
elif language == "Java":
    print("i'm studing Java ☕")
else:
    print("i'm busy!")

# multiple conditional statement using ternary operator
print("Ruby 💎") if language == 'Ruby' else print('Python 🐍') if language == 'Python' else print('Java ☕') if language == 'Java' else print('Not at all!')
