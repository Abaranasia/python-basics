class Person:

    def __init__(self, name, surname, email): # constructor
            self._name= name
            self._surname = surname
            self._email= email
    
    @property # getter
    def name(self):
        return self._name
    
    @property # getter
    def surname(self):
        return self._surname

    @property # getter
    def email(self):
        return self._email

    def display_user(self):
        print (f'User: {self.email} ({self.name} {self.surname})')



