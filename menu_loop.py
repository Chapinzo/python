menu_selection = input("select an option: \n(a). \n(b)..\n")

is_valid = False
#create condition
while is_valid is False:
    if(menu_selection.lower() == "a"):
        is_valid = True
        print("This is menu A")
    elif(menu_selection.lower() == 'b'):
        is_valid = True
        print("This is menu B")
    else:
        print("invalid selection")
        is_valid = False
        menu_selection = input("select an option: \n(a). \n(b)..\n")

    
