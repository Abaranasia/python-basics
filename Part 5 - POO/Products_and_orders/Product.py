class Product:
    products_count = 0

    def __init__(self, name, price):
      Product.products_count += 1
      self._id_product = Product.products_count
      self._name = name
      self._price = price

    @property
    def id_product(self): # property getter
      return self._id_product
    
    @id_product.setter 
    def id_product(self, id_product): # property setter
      self._id_product = id_product
    
    @property
    def name(self): 
      return self._name
    
    @name.setter 
    def name(self, name): 
      self._name = name

    @property
    def price(self):
      return self._price
    
    @price.setter 
    def price(self, price): 
      self._price = price

    def __str__(self):
      return (f'Product Id: {self._id_product}, Name: {self._name}, Price: {self._price}')

if __name__ == '__main__':
  product1 = Product('Laptop Asus MK100F', 1650.00)
  print (product1)
  product2 = Product('Laptop Asus MXP240F', 1800.00)
  print (product2)
  product3 = Product('Optical mouse Logitech MX100', 100.00)
  print (product3)