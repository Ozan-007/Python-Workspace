# We use class methods because like other methods in class they use self as a refer to an object. In this case we want to be able to change the class variables. So it has to refers to the class
# So we need to use @classmethod decorator and we use (cls) as a parameter refers to class. 
class Personnel:
    staff_members = 0
    increase_rate = 1.05    

    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = f'{self.first_name.lower()}.{self.last_name.lower()}@firm.com'
     
        Personnel.staff_members += 1

    def get_full_name(self): # self represents the objects.
        return f'{self.first_name} {self.last_name}'

    def increase_salary(self):
        self.salary = int(self.salary * self.increase_rate) 

    @classmethod
    def change_increase_rate(cls,rate):
        old_rate = cls.increase_rate
        cls.increase_rate = rate
        print(f'Old rate is ({old_rate}) and new rate is {Personnel.increase_rate}')
        

per_1 = Personnel("Kobe", "Bryant", 45000)
per_2 = Personnel("Stephen", "Curry", 51000)

Personnel.change_increase_rate(1.5) # Like this we are able to change the Personnel's increase_rate and it will affect other objects that created from Personnel.

per_1.increase_salary()
per_2.increase_salary()

print(per_1.salary)
print(per_2.salary)
per_1.change_increase_rate(2) # We can change increase_rate of the class with using an object that created from the class. It is going to affect all of the objects simply because we changed the rate of the class.
  
per_1.increase_salary()
per_2.increase_salary()
print("________________________")
print(per_1.salary)
print(per_2.salary)
