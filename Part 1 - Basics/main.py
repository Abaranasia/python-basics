def print_hi (name):
    print (f'This file is named {name}')

if (__name__ == '__main__'): # __name__ is the file name
    print_hi ('main')
else:
  print_hi ('something else')