# Dunder stands for DOUBLE UNDERSCORE METHODS

class Personnel:

    staff_members = 0
    increase_rate = 1.05    

    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = f'{self.first_name.lower()}.{self.last_name.lower()}@firm.com'
        Personnel.staff_members += 1

    def get_full_name(self): 
        return f'{self.first_name} {self.last_name}'

    def increase_salary(self):
        self.salary = int(self.salary * self.increase_rate) 


    def __repr__(self): #"This is a dunder method and it starts when the object is called so it is representation of the object."
        return f"Personnel({self.first_name}, {self.last_name}, {self.salary})" # ** This method is important for developers. ** 
        
    def __str__(self): # This method will return us name and mail when the object is called.
        return f"{self.first_name} -  {self.email})"  # ** This method is for final users.**
        

per_1 = Personnel("Kobe", "Bryant", 45000)
per_2 = Personnel("Stephen", "Curry", 51000)

print(per_2)
# print(per_2.__repr__())
# print(per_2.__str__())
# print(str(per_2))
# print(repr(per_2))



