#This program calculates the BMI 

#Display welcome message
print("This is a BMI calculator")
#Request for details
print("\t")
height_meters = float(input("What's your height in meters: \r"))
print("\t")
weight_kg = float(input("What's your weight in Kilograms: \r"))

BMI = weight_kg/(height_meters**2)
BMI = round(BMI, 2)

#Display the result
print('\t')
print('\t')
print('\t')
print("Your Body Mass Index is",BMI)
print('\t') 
if(BMI < 18.5):
    print("You're underweight")
elif((BMI >= 18.5) and (BMI < 25)):
    print("You're Normal")
elif((BMI >=25) and (BMI < 30)):
    print("You're overweight")
else:
    print("You're Obese")
