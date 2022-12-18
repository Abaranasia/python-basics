def salute(name):
  print(f'Hello {name}')

def sumar(a:int=0, b:int=0) -> int: # default values and input/output type hint
  print (a+b)

def add_to_dict(dictionary, item):
  # dictionary.update(item)
  for key, value in item.items():
    dictionary[key]= value
  print (dictionary)

def print_names(*names): # variable number of params
  for name in names:
    print (name)

def add_values(*nums):
  result= 0
  for num in nums:
    result+=num

  return result

def print_objects(dict):
  cont=0
  for key, value in dict.items():
    cont+=1
    print(f'{cont}. {key}: {value}')

def factorial(num): 
  if num == 1:
    return 1
  else:
    return num* factorial(num-1)


def tax_calculator():
  def calculate_price(amount, tax):
    return amount+(amount*tax/100)

  amount = float(input('Enter the money amount: '))
  tax = float(input('Enter the tax percentage: '))
  print(f'€{calculate_price(amount, tax)}')