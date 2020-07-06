#Display welcome message with statement purpose
print('Welcome to The Bible quiz trivia')

#Request users name
name = input('Please what\'s your name?\r')
print('\t')
print('Hi',name,'welcome to the bible quiz trivia')
#Display instructions
print('Carefully select the correct option')
print('\t')
print('This program uses negative marking')
#intialize score
score = 0
#Ask questions
Nos_1 = input('1.\r How many books are in the bible\n(a)66\n(b)50\n(c)70\n(d)65\n')
if(Nos_1.lower() == 'a'):
    print(name,'That\'s correct!')
    score = score + 4
else:
    print(name,'Sadly, that\'s not correct')
    score = score - 4
print('\t')
Nos_2 = input('2.\r How old was david when he died \n(a)75 \n(b)90 \n(c)70 \n(d)80 \n')
if(Nos_2.lower() == 'c'):
    print(name,'That\'s correct!')
    score = score + 4
else:
    print(name,'Sadly, that\'s not correct')
    score = score - 4
print('\t')
Nos_3 = input('3.\r How many years were the israelites in captivity\n(a)2000\n(b)400\n(c)40\n(d)300\n')
if(Nos_3.lower() == 'b'):
    print(name,'That\'s correct!')
    score = score + 4
else:
    print(name,'Sadly, that\'s not correct')
    score = score - 4
print('\t')
Nos_4 = input('4.\r How does salvation occur in a man? \n(a)Faith and confession\n(b)Being Sorry for sins\n(c)Faith Alone\n(d)Confession and restitution\n')
if(Nos_4.lower() == 'c'):
    print(name,'That\'s correct!')
    score = score + 4
else:
    print(name,'Sadly, that\'s not correct')
    score = score - 4
print('\t')
Nos_5 = input('5.\r Where was Christ born?\n(a)Nazareth\n(b)Carpaneum\n(c)Jordan\n(d)Bethlehem\n')
if(Nos_5.lower() == 'd'):
    print(name,'That\'s correct!')
    score = score + 4
else:
    print(name,'Sadly, that\'s not correct')
    score = score - 4
print('\t')
#Display final result
print(name,'This is your final score',score)
#
