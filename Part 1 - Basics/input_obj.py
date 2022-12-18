alias = input('Alias: ')
name = input('Real Name: ')
age = input('Age: ')

hero = { # Dictionary is similar to JSON Object
  "alias":alias,
  "name":name,
  "age":age
}

hero2 = [ # List is similar to JS array
  alias,
  name,
  age
]
hero3 = ( # Tuple is similar to list but immutable; items cannot be updated
  alias,
  name,
  age
)
print (hero)
print (type(hero))
print (hero2)
print (type(hero2))
print (hero3)
print (type(hero3))