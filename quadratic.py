#This is a quadratic equation calculator
print("This is a Quadratic equation calculator")

#Request for parameters
print("\t")
a = int(input("What is the coefficient of a: \r"))
print("\t")
b = int(input("What is the coefficient of b: \r"))
print("\t")
c = int(input("What is the coefficient of c: \r"))
disc = ((b**2) - (4*a*c))
if(disc > 0):
    print("The equation has two real roots")
elif(disc == 0):
    print("It has one root")
else:
    print("The equation has no real roots")
