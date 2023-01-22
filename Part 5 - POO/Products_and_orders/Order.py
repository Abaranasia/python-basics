from Product import Product

class Order:
  orders_counter= 0

  def __init__(self, products):
    Order.orders_counter += 1
    self._order_id = Order.orders_counter
    self._products = list(products) # we convert it to list to ensure its a list

  def add_product(self, product): # Method to add a new product to an existing list
      self._products.append(product)
  
  def calculate_total(self):
    total = 0
    for product in self._products:
      total += product.price # here we access to the product.price getter
    return total

  def __str__(self):
    products_str = ''
    for product in self._products:
      products_str += ' - ' + product.__str__() + '\n'
    
    return f'Order #{self._order_id} includes:\n{products_str}'