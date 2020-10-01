# `class` identifier tells python that the following is a class definition
class Car:
    # class variable shared by all instances
    wheels = 4

    def __init__(self, kind = ""):
        # instance variable unique to each instance
        self.doors = 4
        self.kind = kind

    def honk(self):
        return 'honk honk'


polo = Car('Polo')
mini = Car('Mini')
beetle = Car('Beetle')

print(f'The car is a {polo.kind}')
print(f'The car has {polo.doors} doors')
print(f'The car has {polo.wheels} wheels')
polo.honk()