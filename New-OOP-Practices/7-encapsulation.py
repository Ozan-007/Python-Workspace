class Personnel:
    
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = f'{self.first_name.lower()}.{self.last_name.lower()}@firm.com'
        self.__increase_rate = 1.1 #  With using '__' underscore to attribute we convert it into Private outside of the method it can't be reachable. 

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def increase_salary(self):
        self.salary = int(self.salary * self.__increase_rate) 


per1 = Personnel("James","Bond",4000)
per2 = Personnel(salary = 5000, first_name = "Stephen", last_name = "Currry")

# Without encapsulation we can assign change the rate. We do not want that.

# per1.__increase_rate = 5
print(per1.__dict__)
per1.increase_salary()
print(per1.salary)