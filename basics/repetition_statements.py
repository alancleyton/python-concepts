'''
A while loop repeats a block of code an unknown number of times until a condition is satisfied.
'''

# condition = True
# while condition:
#   print('hello world!') # execute this block of code while condition is True


# break statement is used to terminate the execution of the loop
condition = True
while True:
  str_input = input('type something: ')
  if str_input == 'exit':
    break


# while loop execution until condition be satisfied
counter = 0
while counter < 10:
  counter += 1
  print(counter)

# continue statement is used to skip the current iteration of the loop to the next iteration
index = 0
while index < 10:
  index += 1
  if index == 5:
    continue
  print(index) # print of the number 5 will be skibed by continue statement 

'''
A for loop is used for iterating over a sequence like a string, list, tuple, dictionary or object.
For statement iterates each item in a sequence in order, executing the block each time. The loop continues until we reach the last item in the sequence.
'''

text = 'Python'
for letter in text:
  print(letter)

fruits = ['Banana', 'Apple', 'Watermelon']
for fruit in fruits:
  print(fruit)

for num in range(10):
  print(num)