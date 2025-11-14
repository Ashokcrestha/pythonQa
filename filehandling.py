#file handling is about reading from and writing to files
#files mode:
# r - read \files must exist
# w - write \ create file,overwrite if exists
# a - append \ create files , add data at end
# r+ - read & write

#writing to a file

file = open("test_data.txt", "w")
file.write("TC001: Login Test\n")
file.write("TC002: Search Feature\n")
file.close()
print("File created and data written.")

# if we write same .txt then it will be override previous file
file = open("test_datas.txt","w")
file.write("TC001:this is write file handling\n")
file.close()
print("file created and data written.")


#reading from a file

file = open("test_data.txt", "r")
print(file.read())
file.close()

# append from a file
file = open("test_data.txt", "a")
file.write("TC003: Payment Gateway\n")
file.close()

# read and write
file = open("test_data.txt","r+")
file.write("TC004: Payment Gateway\n")
print(file.read())
file.close()

# if we open file if there is not file for read case
#file = open("test_dataaa.txt","r")
#print(file.read())
#file.close()


# writting file (override)
file = open("test_data.txt", "w")
file.write("TC001: login and logout\n")
file.close()

#append file 
file = open("test_data.txt", "a")
file.write("TC001: Ashok Shrestha\n")
file.close()

# #r+ mode file handling 
file = open("test_data.txt", "r+")
file.seek(0)
file.write("TC001: Sofia\n")
file.seek(0)
print(file.read())
file.close()


def divide_by():
     num = int(input("Enter a number: "))
     result = num / 0
     print("The result after dividing by 2 is:", result)
divide_by()

#example for error handling 
try:
    num = int(input("Enter a number: "))
    print(num / 0)
except ZeroDivisionError:
    print("❌ Cannot divide by zero.")
except ValueError:
    print("❌ Invalid input.")

# example for error hanlding 
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("❌ Cannot divide by zero.")
    
print("division by zero.")