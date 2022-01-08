class Personnel:
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        # self.email = f'{self.first_name.lower()}.{self.last_name.lower()}@firm.com'

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    @property # When we type @property it will change the function as an attribute like per1.email even though it is not an attribute it is a function. 
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@firm.com'

    @get_full_name.setter # allows us to assign full_name and change values according to full_name
    def get_full_name(self, full_name):
        first_name,last_name = full_name.split(" ")
        self.first_name = first_name
        self.last_name = last_name
  
    @get_full_name.deleter # Allows us to delete our values inside of our object.
    def get_full_name(self):
        print("Variables deleted")
        self.first_name = None
        self.last_name = None



per1 = Personnel("John","Smith",4000)
per2 = Personnel(salary = 5000, first_name = "Ozan", last_name = "Eski")

# ***Setter
# per1.get_full_name = "Idris Bond"
# print(per1.email)
# print(per1.first_name)
# print(per1.get_full_name)


# ***Deleter
del per1.get_full_name

print(per1.first_name)