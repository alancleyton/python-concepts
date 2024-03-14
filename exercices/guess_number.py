from random import randint

def play(number):
  is_correct_number = False
  attempts_number = 0

  while not is_correct_number:
    guess = input('Type a number: ')

    if not guess.isdigit():
      print('Invalid input! type only numbers.')
    else:
      attempts_number += 1
      if int(guess) > number:
        print('Your number is greater than mine, type a less number.')
      elif int(guess) < number:
        print('Your number is less than mine, type a greater number.')
      elif int(guess) == number:
        is_correct_number = True
  
  print(f'Congratulation! You got the right number with {attempts_number} attempts.')

play(randint(0, 100))