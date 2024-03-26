class DogRex:
    name= 'Rex'
    def __init__(self):
        self.is_hungry = False
    def hungry(self):
       print('Dog hungry')
       self.is_hungry = True
my_dog = DogRex()
print(my_dog.name)
my_dog.hungry()
print(my_dog.is_hungry)            