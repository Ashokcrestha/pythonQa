#Object-Oriented Programming (OOP) is a programming style that organizes code into objects — each object represents real-world entities with data (attributes) and behavior (methods).

#class= templetes or real world entities / defines the property (variable) & behaves (function) of a object
#object = when u created something from a class it is object/instance

#__init__() = constructor (automatically runs when object is created)
# self = represent current object (link between class and object)

class students:
    def __init__(self,username,address):
        self.username=username
        self.addresss=address
        
    def greeting(self):
        print("hello",self.username)

    def address(self):
        print("you address is", self.addresss)

raminfo=students("ram","admins@123")
raminfo.greeting()
sitainfo=students("sita",'ktm')
sitainfo.greeting()
sitainfo.address()

class car:
    def __init__(self,carname):
        self.carname=carname

    def start(self):
        #print("car will start now",self.carname)
        print(f"{self.carname} will start now")
        
    def stop(self):
        print(f"{self.carname} will stop now")
       # print("carname will stop", self.carname)
honda=car("honda")
honda.start()
honda.stop()


class flower:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price

    def flowercolor(self):
        print(f"{self.name}'s color is {self.color}")
    
    def flowerprice(self):
        print(f"{self.name}'s price is {self.price}")

rose=flower("rose","red",500)
rose.flowercolor()
rose.flowerprice()

lily=flower("lily","white",500)
lily.flowercolor()
lily.flowerprice()


#Main pillars of OOP (encapuslation,abstarction,inhertiance, polymorphism)

#encapuslation - keeping data(variable) & actions(methods) together in a unite class
class Login:
 def __init__(self, username, password):
    self.__username = username   
    self.__password = password   
 def get_username(self):
    return self.__username   
 def set_password(self, new_pass):
    self.__password = new_pass  

user = Login("ram123", "pass123")
print(user.get_username())
user.set_password("newPass")


#Abstarction - hiding complexity , showing only important detail
class Laptop:
    def turn_on(self):
        print("Laptop is turning on...")
    # inside: CPU starts, RAM loads, OS boots (hidden)
    
l = Laptop()
l.turn_on()


#inhertiance - inherit from parent class to child class
class User:
    def login(self):
        print("User logged in")

class Admin(User):   # Admin inherits login()
    def delete_user(self):
        print("User deleted")

a = Admin()
a.login()      # inherited
a.delete_user()




#polymorphism - same function different behaviour
class Chrome:
    def run_test(self):
        print("Running test on Chrome")

class Firefox:
    def run_test(self):
        print("Running test on Firefox")

for browser in (Chrome(), Firefox()):
    browser.run_test()






        
    