#This is a simple interest calculator

#Display a welcome line
print('Welcome to the simple interest calculator')

#Request user info
name = input('What is your name please?: ')

#Request for parameters
principal = float(input('Please enter the principal: '))
rate = float(input('Please enter the rate: '))
time = float(input('Please enter the time: '))

#Calculate the parameters
interest = (principal * rate * time)/100
interest = (round(interest, 2))

#Calculate amount
Amount= (principal + interest)

#display output
print(name,'the interest is', interest)
print('And the total amount gained in', time, 'years is', Amount)
