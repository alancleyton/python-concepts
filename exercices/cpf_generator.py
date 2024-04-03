from random import randint

def generate() -> str:
  # generate first cpf nine digits
  nine_digits = ''
  for _ in range(9):
    nine_digits += str(randint(0, 9))
  
  nine_digits_multiplier = 10
  nine_digits_sum_result = 0
  for digit in nine_digits:
    nine_digits_sum_result += int(digit) * nine_digits_multiplier
    nine_digits_multiplier -= 1

  first_last_digit = (nine_digits_sum_result * 10) % 11
  first_last_digit = first_last_digit if first_last_digit <= 9 else 0

  ten_digits = nine_digits + str(first_last_digit)

  ten_digits_multiplier = 11
  ten_digits_sum_result = 0
  for digit in ten_digits:
    ten_digits_sum_result += int(digit) * ten_digits_multiplier
    ten_digits_multiplier -= 1
  
  second_last_digit = (ten_digits_sum_result * 10) % 11
  second_last_digit = second_last_digit if second_last_digit <= 9 else 0
  generated_cpf = f'{nine_digits}{first_last_digit}{second_last_digit}'
  return generated_cpf
  

print(generate())