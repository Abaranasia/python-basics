num1 = int(input ('Enter first number: '))
num2 = int(input ('Enter second number: '))
operation = input('Write the operation (suma, resta, producto, division): ')

def suma(num1, num2):
  return num1 + num2

def resta(num1, num2):
  return num1 - num2

def producto(num1, num2):
  return num1 * num2

def division(num1, num2):
  return num1 / num2


match operation:
  case 'suma':
    print(f'Suma: {suma(num1, num2)}')
  case 'resta':
    print(f'Resta: {resta(num1, num2)}')
  case 'producto':
    print(f'Producto: {producto(num1, num2)}')
  case 'division':
    print(f'Division: {division(num1, num2)}')