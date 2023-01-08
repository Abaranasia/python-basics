class Person:

  def __init__(self, name, email, age): # constructor (dunder method)
      self._name= name # We add underscore to indicate that this property should not be directly modified
      self._email= email
      self._age= age

  @property
  def name(self): # property getter
    return self._name
  
  @name.setter 
  def name(self, name): # property setter
    self._name = name

  def display_details(self):
    print (f'Object details: {self._name} {self._email} {self._age}')

person1 = Person('John', '@john', 39)
person2 = Person('Ann', '@ann', 27)

person1.display_details()
person2.display_details()

person1.name= "Edward" # using setter to write
print (person1.name) # using getter to read
