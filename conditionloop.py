# conditions syntax
# if condition 
#--code block
# elif another condition
# -- another block
# else 
# --fall back

# conditions example

# test_results ="fail"

# if test_results=="pass":
#     print("test passed! goto next test")
# elif test_results=="fail":
#     print("test failed! log a bug")
# else:
#     print("test result unknown! check again")

# age_vote  = 18

# if age_vote>=18:
#     print("eligible")
# elif age_vote<18:
#     print("not eligible")
# else:
#     print("incorrect ")



voter_age = int(input("enter your age"))
if voter_age>=18:
    print("eligible")
elif voter_age<18:
    print("not eligible") 
    # input ma string matra hunxa tesla error aayo tesla convert garne by int
  # for loop

tests = ["login", "search", "logout"]  
for t in tests:
    print("running:", t)
    print("running:", t)

    
#while loop

attempts = 0

while attempts < 4:
    print("trying to connect...")
    attempts += 1
print("done")

