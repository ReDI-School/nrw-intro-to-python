
class Zoo:

    def __init__(self, animals = []):
        self.animals = animals

    def visit(self):
        for animal in self.animals:
            print(
                f'You see a {animal.__class__.__name__} with name {animal.name}')

    def listen(self):
        for animal in self.animals:
            animal.sound()

    def add(self, animal):
        self.animals.append(animal)


class Animal:

    def __init__(self, name):
        self.name = name

    def sound(self):
        pass


class Fish(Animal):

    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Blubb")


class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Zss")


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Squeak")


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        pass


class Human(Mammal):

    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Have a good evening ReDi school")


z = Zoo()
z.add(Fish('Nemo'))
z.add(Reptile('Snake'))
z.add(Bird('Big Bird'))
z.add(Human('Mark'))

z.visit()
z.listen()
