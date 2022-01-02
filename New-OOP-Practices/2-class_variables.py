# !!! increase_rate class variable explained and showed how to take a variable from the object using self.increase_rate. !!!

class Personnel:

    # increase_rate = 1.05    

    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = f'{self.first_name.lower()}.{self.last_name.lower()}@firm.com'
    
    def get_full_name(self): # self represents the objects.
        return f'{self.first_name} {self.last_name}'

    def increase_salary(self):
        self.salary = int(self.salary * self.increase_rate) # if we want to reach the rate we can directly use Personnel.increase_rate or we can take it from the object as self.increase_rate
 

per_1 = Personnel("Kobe", "Bryant", 45000)


# EXAMPLE

# per_1.increase_rate = 1.05 # with this we added increase_Rate attribute to our object, now I commented the class increase_rate and I am still able to use it because I used self.increase_rate which refers to the object

# print(per_1.salary)
# per_1.increase_salary()
# print(per_1.salary)







