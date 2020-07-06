#Display welcome
print("Hi, Welcome to Bruno's delivery menu")
print("\t")
#Display instructions
print("This Delivery is for lagos resident")
print("\t")
#Request User's details (include delivery location)
name = input("What is your name please:\r")
name = (name.title())
print("\t")
print ("Thank you", name,"!")
print("\t")
location = input("Where in lagos, do you want the meal delivered: \r")
print("\t")
#Request User's decision
#Display instructions

print("So",name)

meal = input("What would you like to order? \n(a)Rice \n(b)Beans \n(c)Plantain \n(d)soup \n")
if(meal.lower() =="a"):
#Assign Meal price
    a = 400
    print("Please note",name,"any plate of rice is",a,"naira")
    print("\t")
    rice_type = input("What type of rice? \n(a)Jollof rice \n(b)White rice \n(c)Fried rice \n")
    if(rice_type.lower() == "a"):
        print("Jollof rice it is!")
        print("Please type in an amount")
        rice_portion = int(input("How many plates of rice:\r"))
        amount = a * rice_portion
    elif(rice_type.lower() == "b"):
        print("White rice it is!")
        print("Please type in an amount")
        rice_portion = int(input("How many plates of rice:\r"))
        amount = a * rice_portion
    elif(rice_type.lower() == "c"):
        print("Fried rice it is!")
        print("Please type in an amount")
        rice_portion = int(input("How many plates of rice:\r"))
        amount = a * rice_portion
    else:
        print("Err",name,"Please choose a valid option")
        
elif(meal.lower()=="b"):
    b = 300
    print("Please note",name,"any plate of beans is",b,"naira")
    print("\t")
    beans_type = input("What type of Beans? \n(a)Porridge Beans \n(b)Ewa goin \n(c)Plain Beans \n")
    if(beans_type.lower() =="a"):
        print("Porridge Beans coming right up!")
        print("Please type in an amount")
        beans_portion = int(input("How many plates of beans:\r"))
        amount = b * beans_portion
    elif(beans_type.lower() =="b"):
        print("Ewa goin? You got it!")
        print("Please type in an amount")
        beans_portion = int(input("How many plates of beans:\r"))
        amount = b * beans_portion
    elif(beans_type.lower() =="b"):
        print("Plain beans? Ok!")
        print("Please type in an amount")
        beans_portion = int(input("How many plates of beans:\r"))
        amount = b * beans_portion
    else:
        print("Err",name,"abeg choose a valid option")
elif(meal.lower() == "c"):
    c = 200
    print("Please note",name,"any plate of Plantain is",c,"naira")
    print("\t")
    plantain_type = input("What type of plantain? \n(a)Fried plantain \n(b)Boiled plantain \n(c)Unripe plantain \n")
    if(plantain_type.lower() == "a"):
        print("Delightsome Fried plantain coming your way!")
        print("Please type in an amount")
        plantain_portion = int(input("How many plates of plantain:\r"))
        amount = c * plantain_portion
    elif(plantain_type.lower() == "b"):
        print("Boiled plantain? You got it!",name)
        print("Please type in an amount")
        plantain_portion = int(input("How many plates of plantain:\r"))
        amount = c * plantain_portion
    elif(plantain_type.lower() == "c"):
        print("Unripe plantain? Rare choice but,",name,"your wish is our command!")
        print("Please type in an amount")
        plantain_portion = int(input("How many plates of plantain:\r"))
        amount = c * plantain_portion
    else:
        print("Err",name,"Kindly check the options again")

elif(meal.lower()== "d"):
    d = 400
    print("Please note",name,"any plate of soup is",d,"naira")
    print("\t")
    soup_type = input("These are the soups available, which ones do you want?\n(a)Egusi \n(b)Afang \n(c)Oha \n")
    if(soup_type.lower() =="a"):
        print("Egusi soup, coming right up!")
        print("Please type in an amount")
        soup_portion = int(input("How many plates of soup:\r"))
        amount = d * soup_portion
    elif(soup_type.lower() =="b"):
        print("Afang soup? You got it!")
        print("Please type in an amount")
        soup_portion = int(input("How many plates of soup:\r"))
        amount = d * soup_portion
    elif(soup_type.lower() =="c"):
        print("Oha soup? Ok!")
        print("Please type in an amount")
        soup_portion = int(input("How many plates of soup:\r"))
        amount = d * soup_portion
    else:
        print("Err",name,"abeg choose a valid option")
else:
    print(name,"Kindly make a choice from the displayed option")    
#Display Actions
print("\t")
#Display Amount
print("Okay",name,"you'll pay",amount)
print("\t")
#Display Status
print("Your order has been placed")
print("\t")
#Display dispatch
print("Your meal is on its way to",location)
print("\t")
#Display closing
print("Thank you",name,"for using Bruno's food menu and delivery")


