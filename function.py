# A function is the block of code that perform a specific task. you can call it anytime you need to call that task again-no need to rewrite same code again

#built -in function- already provided by python

print("QA Testing")
print(len("automation"))
type(10)
print(max(10,20))
print(ascii(1000))

#user-defined fumction = user gives logic

def greet_user():
    print("Hello welcome to qa testing!")

greet_user()
greet_user()

def check_results():
 test_results ="fail"

 if test_results=="pass":
   print("test passed! goto next test")
 elif test_results=="fail":
     print("test failed! log a bug")
 else:
    print("test result unknown! check again")

check_results()

def add():
   num1 = 5 
   num2 = 7 
   sum = num1 + num2
   print(sum)
add()

def add():
   num1 = int(input("enter first number"))
   num2 = int(input("enter second number"))
   sum= num1 + num2
   print("sum of (num1) and (num2) is", sum)

add()

#function with parameter

def test_login(username):
   print("testing login for:", username)

test_login("admin")

def addition(num1,num2):
   sum=num1+num2
   print(sum)

addition(4,10)

#function with return value

def verify_status(code):
   if code == 200:
      return "PASS"
   else:
      return "Fail"
   
result = verify_status(200)
print(result)

#function with multiple parameter

def check_credentials(username,password):
   if username == "admin" and password == "12345":
       print("login succesfully")
   else:
       print("login failed")
check_credentials("admin","12345")
      