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


if __name__ == '__main__':
  product1 = Product('Laptop Asus MK100F', 1650.00)
  product2 = Product('Laptop Asus MXP240F', 1800.00)
  product3 = Product('Optical mouse Logitech MX100', 100.00)

  products = [product1, product2 ]

  order1 = Order(products)
  order1.add_product(product3)
  

print(order1)
print ('Total price: €'+str(order1.calculate_total()))