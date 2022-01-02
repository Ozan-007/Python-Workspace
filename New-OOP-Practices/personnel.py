class Personnel:
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = f'{self.first_name.lower()}.{self.last_name.lower()}@firm.com'
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_full_name(variable):
        return f'{variable.first_name} {variable.last_name}'


per1 = Personnel("John","Smith",4000)
per2 = Personnel(salary = 5000, first_name = "Ozan", last_name = "Eski")

# print(per1.email)
# print(per2.email)
# print(f'{per1.first_name} {per1.last_name} is created.')
# print('{} {} is created'.format(per2.first_name,per2.last_name))

print(per2.get_full_name()) # That is how we use it when we use self in the functions
print(Personnel.get_full_name(per1)) # Here we used the function which is belong to our class but it could be any classes method to use. Example below.

# Example 

# class Manager:
#     def get_name(person):
#         return f'{person.first_name} {person.last_name}'


# print(Manager.get_name(per1))

# Now I still can get the full name of my personnel object without using the same class. So self make it easier for us. 

# Example ended.


