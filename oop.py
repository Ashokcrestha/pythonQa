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

    


        
    