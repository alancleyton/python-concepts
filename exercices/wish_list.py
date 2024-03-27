wish_list = []

while True:
  print('Select an option: ')
  option = input('[i]nsert [r]emove [l]ist [e]xit: ')

  if option == 'e':
    break
  elif option == 'i':
    new_item = input('New item value: ')
    wish_list.append(new_item)
  elif option == 'r':
    wish_list_item = input('Item index: ')
    try:
      wish_list.pop(int(wish_list_item))
    except:
        print('Item does not exist on list!')
  elif option == 'l':
    for index, item in enumerate(wish_list):
      print(index, item)
  
