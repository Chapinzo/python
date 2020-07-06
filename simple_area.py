#Display welcome message
print("Welcome to the area calculator")

#Show options
print("\t")
area = input("I want to find the area of \na. Triangle \nb. Circle \nc. Rectangle \n")
if(area.lower() == "a"):
    print("\t")
    print("This calculates the area of a triangle")
    height = float(input("What is the height: \r"))
    print("\t")
    base = float(input("What is the base: \r"))
    area = (height * base)/2
    area = round(area, 2)
    print("\t")
    print("The area of the triangle is:", area)
elif(area.lower() == "b"):
    print("\t")
    print("This calculates the area of a circle")
    r = float(input("What's is the radius: \r"))
    area = round((3.14 *(r**2)),2)
    print("\t")
    print("The area of the circle is:", area)
elif(area.lower() == "c"):
    print("\t")
    print("This calculates the area of a rectangle")
    L = float(input("What's is the length : \r"))
    B = float(input("What's is the Breadth : \r"))
    area = round((L*B),2)
    print("\t")
    print("The area of the Rectangle is:", area)
    
    
    
#
#
#
