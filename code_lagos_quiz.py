#Request user name
name = input("Hi please, What's your name: ")

#Display the purpose of the program
print('welcome to the code lagos quiz')
print('This will test your knowledge of codelagos')

#Display the instructions
print('select the correct option of your choice')


#initialize the score variable
score = 0

#Ask the user a question
question1 = input('How many out of school centres does codelagos have? \n(a)4 \n(b)12 \n(c)21 \n(d)30\n')

#wait for the answer

#If the question is correct, display: 'correct' and add 1 to the score
if(question1.lower()=='c'):
    print('Correct!')
    score = score + 1

#Else display: 'wrong'
else:
    print(name,'That\'s the Wrong answer')

question2 = input('In what year did codelagos start? \n(a)2017 \n(b)2012 \n(c)1999 \n(d)2018 \n')
if(question2.lower() == 'a'):
    print('Correct!')
    score = score + 1
else:
    print('Wrong')

question3 = input('How many Lagosian does Codelagos intend to have trained by 2020? \n(a)4,000,000. \n(b)3,000,000. \n(c)500,000. \n(d)1,000,000. \n')
if(question3.lower() == 'd'):
    print('Correct!')
    score = score + 1
else:
    print(name,'That\'s incorrect')

print('Thank you',name,'for participating in the quiz')

#Go back to step 3 until all the questions have been answered

#Print the score of the user
print(name,'Your score is', score)
