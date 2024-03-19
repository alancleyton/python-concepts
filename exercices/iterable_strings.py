def most_common_letter(s: str):
  idx = 0
  letters = s.replace(' ', '')
  common_letter = ''
  common_letter_count = 0
  
  while idx < len(letters):
    current_letter = letters[idx]
    current_letter_count = letters.count(current_letter)

    if current_letter_count > common_letter_count:
      common_letter_count = current_letter_count
      common_letter = current_letter
    
    idx += 1
  
  return common_letter

print(most_common_letter('Welcome to Python lang.'))