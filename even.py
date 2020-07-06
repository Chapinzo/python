#Welcome user
print('Hi welcome to the even number tester')

#Display the purpose of the program
print('This program checks if any number you enter is even')

#Display the instruction
print('This works for only whole numbers')

#Ask the user to enter a number
a = int(input('Type in a whole number'))
if(a%2 == 0):
    print(a,'is an even number')
else:
    print(a,'is an odd number')
#Display if the number is even
