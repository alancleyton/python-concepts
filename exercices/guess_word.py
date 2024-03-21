import random

def play(word):
  correct_letters = ''
  attempts_number = 0

  while True:
    attempts_number += 1
    correct_word = ''
    letter_input = input('Type a letter: ')

    if len(letter_input) > 1:
      print('Invalid letter! More than one letter.')
      continue

    if letter_input in word:
      correct_letters += letter_input
    
    for letter in word:
      if letter in correct_letters:
        correct_word += letter
      else:
        correct_word += '*'

    print(correct_word)

    guess_word_input = input('The word is: ')

    if not guess_word_input:
      continue

    if guess_word_input == word:
      print(f'Congratulations! you got the correct word with {attempts_number} attempts.')
      break
    else:
      print('Wrong word! Try again.')
    
word = random.choice(['love', 'banana', 'crazy', 'awesome', 'amazing'])
play(word)

