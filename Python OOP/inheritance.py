class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self.name} is walking")
    def how_old(self):
        if self.age <= 1:
            print(f"{self.name} is {self.age} year old")
        else:
            print(f"{self.name} is {self.age} years old")
class Cat(Animal):
    def climb(self):
        print(f"{self.name} is climbing!")
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking!")
class Fish(Animal):
    def swim(self):
        print(f"{self.name} is swimming!")


tekir = Cat("Tekir",5)
# tekir.walk()
# tekir.how_old()
tekir.climb()
# Tekir is walking
rex = Dog("Rex", 1)
rex.bark()
# rex.walk()
## Rex is walking
# rex.how_old()
nemo = Fish("Nemo", 2)
nemo.swim()
