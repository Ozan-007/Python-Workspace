class Personnel:
    
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = f'{self.first_name.lower()}.{self.last_name.lower()}@firm.com'
        self.__increase_rate = 1.1  #PRIVATE #  With using '__' underscore to attribute we convert it into Private outside of the method it can't be reachable. 

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    

    def __get_increase_rate(self):
        return self.__increase_rate 
    
    # def set_increase_rate(self, rate): 
    #     self.__increase_rate = rate


    def increase_salary(self):
        self.salary = int(self.salary * self.__increase_rate) 


per1 = Personnel("James","Bond",4000)
per2 = Personnel(salary = 5000, first_name = "Stephen", last_name = "Currry")

# Without encapsulation we can assign change the rate. We do not want that.

# per1.__increase_rate = 5
# print(per1.__dict__)
# per1.increase_salary()
# print(per1.salary)
# # per1.set_increase_rate(2)
# per1.increase_salary()
# print(per1.get_increase_rate())
# print(per1.salary)


# PRIVATE METHOD
# If we encapsulate get_increase_rate method we can not see it in help method. Why we want that because we may want to use our method inside of another method in our class.
print(help(per1))
