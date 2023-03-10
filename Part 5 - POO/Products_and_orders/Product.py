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