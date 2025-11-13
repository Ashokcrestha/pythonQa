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

#function with parameter - you can pass data to function

def test_login(username):
   print("testing login for:", username)

test_login("admin")

def addition(num1,num2):
   sum=num1+num2
   print(sum)

addition(4,10)

#function with return value -the function send data back to where it is called

def verify_status(code):
   if code == 200:
      return "PASS"
   else:
      return "Fail"
   
result = verify_status(200)
print(result)

#function with multiple parameter - a function can take more than one parameter (input values) here  a and b are parameters where 4 and 5 is arguments 
# argumenets - real value you pass to a function when you called it . they are assigned to parameters inside the function
#parameters - name given in the function definition

def check_credentials(username,password):
   if username == "admin" and password == "12345":
       print("login successfully")
   else:
       print("login failed")
check_credentials("admin","12345")
      

#Assignement 

#function to print 'testing started' 5 times
def testing_started():
   for i in range(5):
      print("Testing started")

testing_started()

# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

check_even_odd(25)


# Function that accepts a test name and prints a running message
def run_test(test_name):
    print("Running test:", test_name)

run_test("login Test")

# Function that returns 'PASS' if code is 200, otherwise 'FAIL'
def verify_status(code):
   if code == 200:
      return "PASS"
   else:
      return "Fail"
   
result = verify_status(200)
print(result)

# Function to check if username and password match given values
def check_credentials(username,password):
   if username == "admin" and password == "12345":
       print("login successfully")
   else:
       print("login failed")
check_credentials("admin","12345")