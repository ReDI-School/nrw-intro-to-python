class Person:
    """A blueprint for a person"""

    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def greet(self):
        """Says hello"""
        print(
            f'Hello my name is {self.first_name} {self.last_name} and I am {self.age} years old')

    def birthday(self):
        """Celebrates birthday, by increasing the age by one"""
        self.age = self.age + 1

    def marry(self, new_last_name):
        """Celebrating a marriage, by adopting and changing the last name"""
        self.old_last_name = self.last_name
        self.last_name = new_last_name


help(Person)

mark = Person("Mark", "Warneke", 28)
mark.greet()

print("... a year goes by")
mark.birthday()
mark.greet()

print("... and met a girl to marry")
mark.marry("NotWarnekeAnymore")
mark.greet()
print(f'Marks old last name was {mark.old_last_name}')
