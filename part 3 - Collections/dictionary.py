# Disctioaries (or dict) are objects based on key:value entries, similar to JS objects
# dicts are like sets but based on key:value entries instead of only values

dictionary = {
  'IDE': 'Integrated Development Environment',
  'OOP': 'Object Oriented Programming',
  'DBMS': 'Database Management System'
}

print (dictionary)

print (dictionary['IDE']) # prints the value of the given key
print (dictionary.get('IDE')) # prints the value of the given key

dictionary['PK'] = 'Primary key' # add a new element to the dict (overwrites if already exists)

dictionary['IDE'] = 'Integrated Drive Electronics' # Values can be updated
print (dictionary)

print (len(dictionary)) # gives dict length

for index in dictionary: # iterates the dict keys
    print (index)

for key in dictionary.keys(): # iterates the dict keys
    print (key)

for value in dictionary.values(): # iterates the dict values
    print (value)

for key, value in dictionary.items(): # iterates the dict keys and values
    print (key, value)

print ('IDE' in dictionary) # respondes (boolean) if key is in the dict
print ('Database Management System' in dictionary.values()) # respondes (boolean) if value is in the dict

dictionary.pop('IDE') # removes an item based on the key
print (dictionary)

newdict = {}
for key, value in dictionary.items(): # filters a dict by value
    if value != 'Primary key':
        newdict[key]= value
print (newdict)
