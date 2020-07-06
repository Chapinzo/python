#an attempt to calculate euclids algorithm
print('Welcome to the euclid hcf calculator')


#This calculates euclids algorithm
print('This is a program to find the highest common factor of two numbers')

#Display the instructions
print('Please enter whole numbers')

#Ask the user to enter a first number
first_number = int(input('What is the first number:'))

#Ask the user to enter a second number
print("\t")
second_number = int(input('What is the second number: '))

#compare the numbers and swap if second number is greater than the first
if (second_number >= first_number):
    empty = second_number
    second_number = first_number
    first_number = empty
    print(first_number, second_number)
high_number = first_number
low_number = second_number


#find quotient and remainder of the first number in terms of the second

#assign the quotient to the number and the remainder to the second number

#if the remainder is 0, stop
while(second_number > 0):
    #find the quotient
    quotient = first_number//second_number

    #find the remainder
    remainder = first_number%second_number

    #Assign the second number to the first number
    first_number = second_number

    #assign the second number to remainder
    second_number = remainder

#print out report
print("The HCF of",high_number,"and",low_number,"is",first_number)
