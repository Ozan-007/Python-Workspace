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

    def __add__(self, other):
        return self.salary + other.salary
    
    def __sub__(self,other):
        return self.salary - other.salary

    def __len__(self):
        return len(self.get_full_name()) - 1
    

per_1 = Personnel("Kobe", "Bryant", 45000)
per_2 = Personnel("Stephen", "Curry", 51000)

# print(per_2)
# print(per_2.__repr__())
# print(per_2.__str__())
# print(str(per_2))
# print(repr(per_2))

# They are the same. Let's manipulate __add__ method in int class

# print(("1" + str(1) +'2'))
# print((1 + 21) / 2)
# print(int.__add__(1,10))
# print(int.__add__(12,15))

# so if 1 + 3 is the same as int.__add__(1,3)
#We can simply use it in our class and we can change the __add__ method and use it as per_1 + per_2. With that we give our method 2 variables and their salary values.
# print(per_2.__add__(per_1))
# print(Personnel.__add__(per_1,per_2))
# print(Personnel.__sub__(per_1,per_2))
# print(per_2 + per_1)

#***  Subtraction ****

# print(int.__sub__(per_2,per_1))
# print(per_1 - per_2)

#simply we changed + - with manipulating __add and __sub__ methods. 


# *** len **

print(int.__add__(1,3))
# print(int.__add__(per_1,per_2)) # Error
print(Personnel.__add__(per_1,per_2))
print(per_1.__add__(per_2))
print(Personnel.__sub__(per_2,per_1))
print(per_2 + per_1)
print(per_2 - per_1)
# print(len("Eski"))
# print(len(per_1))
# print("Eski".__len__())
# print("Ozan".__len__())