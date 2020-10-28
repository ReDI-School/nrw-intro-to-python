class Car:
    """ A Class is like an object constructor, or a "blueprint" for creating objects.
    Classes provide a means of bundling data and functionality together. 

    Creating a new class creates a new type of object, allowing new instances of that type to be made. 

    Each class instance can have attributes attached to it for maintaining its state. 
    Class instances can also have methods (defined by its class) for modifying its state.
    """

    # class variable shared by all instances
    wheels = 4

    def __init__(self, kind=""):
        # instance variable unique to each instance
        self.doors = 4
        self.kind = kind
        self.speed = 0

    def honk(self):
        """Press the horn of the object """
        print('honk honk')

    def accelerate(self, new_speed):
        """Accelerates the car to a particular speed value"""
        self.speed = new_speed


polo = Car('Polo')
mini = Car('Mini')
beetle = Car('Beetle')

print(f'The car is a {polo.kind}')
print(f'The car has {polo.doors} doors')
print(f'The car has {polo.wheels} wheels')
polo.honk()
