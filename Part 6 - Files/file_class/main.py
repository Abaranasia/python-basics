from File_handler import File_handler


def write_file(file_type):
  print (f'writing a {file_type} file...')
  text= input(f'Enter your text and press enter:\n')
  file = File_handler(file_type)
  file.writer(text)

def read_file(file_type):
  print (f'reading a {file_type} file...')
  file = File_handler(file_type)
  file.reader()

def erase_file(file_type):
  print (f'deleting a {file_type} file...')
  file = File_handler(file_type)
  file.delete() 

menu = 'select\n 1: Write a log file\n 2: Write a TODO list\n 3: Read log file\n 4: Read TODO List\n 5: Delete Log file\n 6: Delete TODO List\n 0: Exit\n'
select= 1
while select !=0:
    option = int(input(menu))
    if (option == 1): write_file('log')
    if (option == 2): write_file('todo')
    if (option == 3): read_file('log')
    if (option == 4): read_file('todo')
    if (option == 5): erase_file('log')
    if (option == 6): erase_file('todo')
    if (option == 0):
        print('You selected 0')
        break

print ('You decided to exit, loser!')