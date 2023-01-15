
# inheritance examples (and other OOP stuff)

class Grand_parent_class_1:
  # This is grand_parent class 1
 
  class_var= 'This is a grand_parent class variable'
  # A class variable can be accesed directly from the class, without an object instance
  # It can also be accesed from any object instance and its common to each of the objects

  def __init__(self, gp_prop1):
    self._gp_prop1 = gp_prop1

  @staticmethod
  def static_method(): # Static methods don't depend on a instance
    print('this a static method from Grand_parent_class_1')
    # static methods can access to the static context but not the dynamic context
    # This means that it cannot access to self (nor its methods and properties)

  @classmethod
  def class_method(cls): 
    # A class method can access to dynamic context by receiving the class as param (typically named cls)
    print (f'This is being accessed from a class method: {cls.class_var}')



class Parent_class_1 (Grand_parent_class_1):
  # This is parent class 1 and inherits from grand_parent_1
  def __init__(self, gp_prop1, prop1):
    super().__init__(gp_prop1) # We need to initialize the grand_parent_1 property
    self._prop1 = prop1



class Parent_class_2:
  # This is parent class 2
  def __init__(self, prop2):
    self._prop2 = prop2



# Multiple inheritage example
class Descendant (Parent_class_1, Parent_class_2):
  # This class inherits from parent_class_1 and parent_class_2 and, indirectly from Grand_parent_class_1
  def __init__(self, gp_prop1, prop1, prop2, desc_prop):
    Parent_class_1.__init__(self, gp_prop1, prop1)
    Parent_class_2.__init__(self, prop2)
    self._desc_prop = desc_prop    
  
  def display_details(self):
    print (f'Object details: {self._gp_prop1} {self._prop1} {self._prop2} {self._desc_prop}')


# Main execution
example = Descendant('abuelo', 'padre1', 'padre2', 'hijo')
example.display_details()
print(example.class_var) # Prints the grand_parent class variable

Grand_parent_class_1.class_var2= 'an On Demand class variable created on parent class'
print(example.class_var2) # Prints the On the fly created grand_parent class variable

Grand_parent_class_1.static_method()
Grand_parent_class_1.class_method()