class Person:
    # Private
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender


    def Name(self):
        return self.__name

    def setName(self, value):
        if value == "John":
            self.__name = "Name cannot be John"
        else:
            self.__name = value


    # def who(self):
    #     print('name  : ', self.__name)
    #     print('age   : ', self.__age)
    #     print("gender: ", self.__gender)

p1 = Person("Ozan", 24, "Male")
p1.setName("Cafer")
print(p1.Name())






# class Animal:
#
# Public
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#
# a1 = Animal("Rex", 10, "Male")
# print(a1.name)
