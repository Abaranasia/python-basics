from Product import Product
from Order import Order

if __name__ == '__main__':
  product1 = Product('Laptop Asus MK100F', 1650.00)
  product2 = Product('Laptop Asus MXP240F', 1800.00)
  product3 = Product('Optical mouse Logitech MX100', 100.00)
  product4 = Product('Magic Refiner RK68 Keyboard', 50.00)
  product5 = Product('LG 32UN500-W Monitor', 325.00)

  laptops = [product1, product2]
  peripherals = [product3, product4, product5]

  order1 = Order(laptops)
  order1.add_product(product3)

  order2 = Order(peripherals)
  order2.add_product(product2)  


print(order1)
print ('Total price: €'+str(order1.calculate_total()))

print(order2)
print ('Total price: €'+str(order2.calculate_total()))