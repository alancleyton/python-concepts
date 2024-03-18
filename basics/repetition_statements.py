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