class Personnel:

    staff_members = 0
    increase_rate = 1.05    

    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = f'{self.first_name.lower()}.{self.last_name.lower()}@firm.com'
        # print("New Personnel created: " + self.first_name + " "  +  self.last_name)
        Personnel.staff_members += 1

    def get_full_name(self): 
        return f'{self.first_name} {self.last_name}'

    def increase_salary(self):
        self.salary = int(self.salary * self.increase_rate) 


class Developer(Personnel):
    # increase_rate = 2 # We overwrited the increase_rate by assigning it under our class. But inside of Personnel class it's going to be the same value
    def __init__(self, first_name, last_name, salary, language):
        super().__init__(first_name, last_name, salary) # This part allows us not to repeat ourselves with typing __init__ completely we are kind of importing it from the super class which is Personnel, So we can also use Personnel.__init__(self,first_name,last_name, salary) but we have to type self if not using super().
        self.language = language
        # print("New Personnel added to Developer Section: " + self.first_name + " "  +self.last_name + " " + self.language)
        # Even if we use Developer to create a developer it is going to use Personnel's init first because we inherited from that class. So first it will say New Personnel created then the Developer Section.

dev_1 = Developer("James", "Bond", 7777, "python")
dev_2 = Developer("Peter", "Parker", 3333, "C#")

# print(dev_1.__dict__)
# print(dev_2.__dict__)


# # INCREASE_RATE changed example
# print(dev_1.salary)
# dev_1.increase_salary()
# print(dev_1.salary)

# print(help(Developer))


#How to create a manager class which is responsible from the other personnel??
# We need to add personnels to our __init__ method.

class Manager(Personnel):
    def __init__(self, first_name, last_name, salary, personnels = None):
        super().__init__(first_name, last_name, salary)
        if personnels is None:
            self.personnels = []
        else:
            self.personnels = personnels

    def add_personnel(self,per):
        if per not in self.personnels:
            self.personnels.append(per)
    
    def remove_personnel(self,per):
        if per in self.personnels:
            self.personnels.remove(per)


    def personnel_list(self):
        for num,person in enumerate(self.personnels):
            num += 1 
            return num, person

man = Manager("Ozan","Eski",8000)

man.add_personnel(dev_1.__dict__)

print(man.personnel_list())
# print(man.__dict__)