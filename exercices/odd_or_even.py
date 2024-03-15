def odd_or_even(number):
  return 'even' if number % 2 == 0 else 'odd'

def number_input():
  is_valid_input = False
  while not is_valid_input:
    number = input('Type a number: ')
    if not number.isdigit():
      print('Invalid input! type only int numbers.')
    else:
      is_valid_input = True
      return int(number)

number = number_input()
print(f'{number} is {odd_or_even(number)}')
