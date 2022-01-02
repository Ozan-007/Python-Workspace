# !!! increase_rate class variable explained and showed how to take a variable from the object using self.increase_rate. !!!

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
        self.salary = int(self.salary * self.increase_rate) # if we want to reach the rate we can directly use Personnel.increase_rate or we can take it from the object as self.increase_rate
 

per_1 = Personnel("Kobe", "Bryant", 45000)
per_2 = Personnel("Stephen", "Curry", 51000)


# EXAMPLE

# per_1.increase_rate = 1.1 # with this we added increase_Rate attribute to our object, now I commented the class increase_rate and I am still able to use it because I used self.increase_rate which refers to the object

# Personnel.increase_rate = 1.5
# print(per_1.salary)
# per_1.increase_salary()
# print(per_1.salary)


# ??? Questions ???

# So let say there are 2 different values as increase_rate, one of them inside of the object and the other is inside of the class. object increase_rate is 1.2 and class increase_rate is 1.05
# If we use self.increase_rate in our function it will take increase_rate as 1.2 because self refers to the object. As opposite if we use Personnel.increase_rate --our class variable-- it will
# use 1.05 as increase_rate but there is a third option. Let's say we did not define any increase_rate for our object and we used self.increase_rate but there is an increase_rate variable 
# in our Personnel class which is 1.05. What is going to happen now?
# The answer is python is not going to find an increase_rate in our object. So it is going to look into our class for increase_rate and if there is, it will take it and use it as our increase_rate
# So increase rate is going to be 1.05. But why did python look into our class? This is where Namespaces come in.




# !!! NAMESPACES  ==>  Built in Namespace > Module: Global Namespace > Function: Local Namespace
# !Extra! when we add increase_rate attribute to the object now it is going to be inside of the object's namespace and it is going to take it and use it as our increase_rate.

# from pprint import pprint

# pprint(per_1.__dict__) 
# print("______________________")
# pprint(Personnel.__dict__)

# There are  namespaces for our object and our class. If our function is looking for increase_rate and if it's inside of our class it is not going to find it in the first namespace which is
# per_1.__dict__ shows then it will look for the greater namespace and it is our class Personnel. If python finds the variable there it will take it and use it.




## !! Staff members count

print(Personnel.staff_members)



