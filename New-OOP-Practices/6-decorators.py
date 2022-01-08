class Personnel:
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    @property # When we type @property it will change the function as an attribute like per1.email even though it is not an attribute it is a function. 
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@firm.com'



per1 = Personnel("John","Smith",4000)
per2 = Personnel(salary = 5000, first_name = "Ozan", last_name = "Eski")


print(per1.email)
# print(per1.email())