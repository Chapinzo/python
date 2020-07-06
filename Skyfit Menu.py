#This is a Skyfit Menu
print("This is a Skyfit Gym Menu")

#Display the welcome message
print("\t")
print("Welcome to Sky fit Gym Menu")
#Welcome the user
#Request for details
print("\t")
first_name = input("Please what is your name:\r")
Lastname = input("What is your surname:\r")
fullname = (first_name +" "+ Lastname)
#Display Options
print("\t")
options = int(input("What would you like to do? \n1. Register \n2. Enquiry \n3. Complaint \n4. Talk to a customer representative \n"))
if(options == 1):
    print(fullname,"you want to register? Okay.")
    print("\t")
    plan_choice = int(input("What plan would you like to subscribe to: \n1. Annually (375,000)\n2. 6 months (275,000)\n3. 3 months (150,000)\n4. Monthly (70,000)\n5. 10 days (31,000)\n6. Weekly (20,500)\n"))
    if(plan_choice == 1):
        print("Okay",first_name,"You'll pay 375,000")
    elif(plan_choice == 2):
        print("Okay",first_name,"You'll pay 275,000")
    elif(plan_choice == 3):
        print("Okay",first_name,"You'll pay 150,000")
    elif(plan_choice == 4):
        print("Okay",first_name,,"You'll pay 70,000")
    elif(plan_choice == 5):
        print("Okay",first_name,"You'll pay 31,500")
    elif(plan_choice == 6):
        print("Okay",first_name,"You'll pay 20,500")
    else:
        print("Invalid Option, Kindly restart menu")

elif(options == 2):
    enquiry = int(input("What would you like to find out: \n1. \n2. \n3. \n.4 \n"))
    if(enquiry == 1):
        print()
    elif(enquiry == 2):
        print()
    elif(enquiry == 3):
        print()
    elif(enquiry == 4):
        print()
    else:
        print("Invalid Option, Kindly restart menu")
elif(options == 3):
    complaint = input("Kindly let us know what you are displeased about:\n")
    print(first_name,"your complaint has been noted and we'll look into it as soon as possible")
elif(options == 4):
    print("We are routing you to the customer care rep")
else:
    print("Invalid Choice, Kindly restart Menu")

