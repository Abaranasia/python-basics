from Person import Person


class Hero(Person):
    def __init__ (self, alias, name, surname, email):
        super().__init__(name, surname, email)
        self._alias = alias

    @property
    def alias(self):
        self._alias

    def display_hero(self):
        print (f'Hero: {self._alias} ({self.name} {self.surname})')
        # print(f'Hero: {self._alias}')
        # self.display_user()