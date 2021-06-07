class Dog():
    SPECIES = 'Mammal'

    def __init__(self, name, breed, age):
        self.breed = breed
        self.name = name
        self.age = age
    
    def bark(self, height):
        print('Woof! My name is {}, I am {} inches tall'.format(self.name, height))


neo = Dog('neo', "cat", 14)
print(neo.name)
print(Dog.SPECIES)
neo.bark(11)





