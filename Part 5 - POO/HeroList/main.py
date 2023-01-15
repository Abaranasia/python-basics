from Hero import *

heroes = []

def list_heroes():
    print('You selected to list the current heroes\n')

    if len(heroes)>0: 
        for heroe in heroes:
            heroe.display_hero()
    else: 
        print ('There are no heroes yet in the list\n')

def add_hero ():
    print('Add a new hero:\n')
    alias= input ('Enter the alias:\n')
    name= input ('Enter the name:\n')
    surname= input ('Enter the surname:\n')
    # email= input ('Enter the email: ')
    heroe = Hero(alias, name, surname, '')
    heroes.append(heroe)
    
    
select= 1
while select !=0:
    option = int(input('select 1: list heroes, 2: add hero, 0: exit\n'))
    if (option == 1):
        list_heroes()
    if (option == 2):
        add_hero()
    if (option == 0):
        print('You selected 0')
        break

print ('You decided to exit, loser!')
        