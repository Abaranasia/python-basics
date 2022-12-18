# A list is like a JS array
# It can store objects based in the index and items can me added, updated and deleted
# A series of functions can handle most of the main operations

colors = ['white', 'grey', 'cyan', 'green', 'purple', 'black'] 
print (colors)

for item in colors: # iterates the list
    print (item)

colors.append('blue') # Adds a new item a the end
print (colors)

colors.insert(2, 'red') # inserts a item on a given position
print (colors)

colors.sort() # sorts items incrementally by default
print (colors) 

colors.reverse() # sorts items in reverse order
print (colors) 

colors.pop() # removes the last item
print (colors) 

colors.remove('grey') # removes the item based on the value
print (colors) 

del colors[0] # removes the item based on the index
print (colors) 

print (colors.index('cyan')) # displays the index of a value
print (len(colors)) # displays the length of the list

print (colors.count('red')) ## returns the number of occurrencies of a value

print ('red' in colors) ## respondes (boolean) if item is the list

colors.clear() # empties the list
print (colors) 

# del colors # removes the list and trying to access to it gives an error
# print (colors) 