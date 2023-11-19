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
print ('Hero: ', hero, type(hero))
print ('Hero2: ', hero2, type(hero2))
print ('Hero3: ', hero3, type(hero3))
