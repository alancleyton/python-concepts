CPF = '762.328.474-65'

def validate_cpf(cpf: str) -> bool:
  row_cpf = cpf.replace('.', '').replace('-', '')

  # validate cpf first nine digits
  first_digits = row_cpf[:9]
  first_digits_multiplier = 10
  first_digits_sum_result = 0
  for digit in first_digits:
    first_digits_sum_result += first_digits_multiplier * int(digit)
    first_digits_multiplier -= 1
  
  first_digit = (first_digits_sum_result * 10) % 11
  first_digit = first_digit if first_digit <= 9 else 0

  # validate cpf last two digits
  last_digits = first_digits + str(first_digit)
  last_digits_multiplier = 11
  last_digits_sum_result = 0
  for digit in last_digits:
    last_digits_sum_result += last_digits_multiplier * int(digit)
    last_digits_multiplier -= 1
  
  last_digit = (last_digits_sum_result * 10) % 11
  last_digit = last_digit if last_digit <= 9 else 0
  validated_cpf = f'{first_digits}{first_digit}{last_digit}'

  print(row_cpf)
  print(validated_cpf)
  
  return True if row_cpf == validated_cpf else False

is_cpf_valid = validate_cpf(CPF)

print(is_cpf_valid)