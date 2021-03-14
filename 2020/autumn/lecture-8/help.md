# Help

## Exercise 1 Help - Person

1. Classes are defined with the keyword `class` and the name of the class should start with a capital letter e.g. `Person`.
2. The class fields can be set in the `__init__()` method, e.g. `__init__(self, first_name, last_name, age=0)`. 
3. A class method can be defined with the keyword `def`, e.g. `def greet(self):` it should `print(f'Hello my name is {self.first_name} {self.last_name} and I am {self.age} years old')`
4. To change values inside of instances use the keyword self. `def birthday(self): self.age = self.age +1`


```python
class Person:,
    """A blueprint for a person"""
    def __init__(self, first_name, last_name, age = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def greet(self):
        """Says hello"""
        print(f'Hello my name is {self.first_name} {self.last_name} and I am {self.age} years old')
    
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
```

## Exercise 2 Help - Zoo

1. To define a zoo you might just create a class `class Zoo:` the class should a property called animals, which is a simple list `animals = []`. The zoo might have a method to add animals, e.g. `def add_animals(self, animal): self.animals.append(animal)`.
1. As all animals inherit we need to create a new class called `class Animal:`, now all species can inherit from animal, e.g. mammals: `class Mammel(Animal):`
1. Each animal can be identified by a species if you define a class for each type of species using `isinstanceof` so a mammal (`my_animal`) can be found and identified by `isinstanceof(my_animal, Mammel)`.
2. Because every animal has a name, we need to define a property `name` inside of our parent class `Animal`. For this we can create a `__init__()` function that excepts a parameter `name`, e.g. `def __init__(self, name): self.name = name`
3. As each animal makes a specific sound, we need to add a method called `sound` to all child classes. For a fish that might look like this: `def sound(self): print("Blubb")` for a bird it looks like `def sound(self): print("Tschirp)`
4. As a human we are a child of the class mammal. So a human would be a class definition like: `class Human(Mammel):`


A simple animal parent hierarchy could look like this:

```python
class Animal:

    # Each animal should have a name, hence we pass it in our initializer function
    def __init__(self, name):
        self.name = name

    # Each species has a different sound, so we just pass and don't assume..
    def sound():
        pass

# A fish is an Animal, so we need to declare it like this
class Fish(Animal):
    # As we inherit from animal we use the super functionality
    def __init__(self, name):
        super().__init__(name)

    # A fish can make a sound, so we specify it here
    def sound():
        print("Blubb")


# As a bird we do the same stuff as like a fish, however - the sound is different :)
class Bird(Animal):

    def __init__(self, name):
        super().__init__(name)

    def sound():
        print("Tschirpp")

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound():
        print("Barkk")

class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound():
        print("Tzssch")
```

To test our animals we can create some:

```python
nemo = Fish("Nemo")
snake = Reptile('Snake')
bird = Bird('Big Bird')
dog = Mammal("Tommy")

print(nemo.name)
nemo.sound()

print(dog.name)
dog.sound()
```

A zoo could look like this:

```python

class Zoo:

    # A zoo can be started with animals, if no animals are provided when *building* a zoo, we create an empty list of animals
    def __init__(self, animals = []):
        self.animals = animals

    def add_animals(self, animal):
        self.animals.append(animal)
```

a more dvanced zoo could have more methods to listen and vistit the animals:

```python

class Zoo:

    # ... see above

    # When listening, we want to hear the sound of each animal inside the zoo
    def listen(self):
        # List thru all animals in a zoo
        for animal in self.animals:
            # Each animal makes a sound
            animal.sound()

    # We can use a property provided by Python to access the class name
    # The class name is the species as we declared it earlier.
    # `animal.__class__.__name__` is a from Python provided functionality, see https://stackoverflow.com/questions/36367736/use-name-as-attribute
    def visit(self):
        for animal in self.animals:
            print(
                f'You see a {animal.__class__.__name__} with name {animal.name}')
```
