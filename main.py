# Simple game in python

print('Hi, welcome to the python game class!')
print('Try to get as many questions correct as possible...')

totalQuestions = 4
score = 0

ans = input('1. What is my name? ')

if ans == ('Yuitta' ):
    print('Correct!')
    score += 1
else:
    print('Incorrect')

ans = input('2. What is my age? ')

if ans == "54":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

ans = input('3. What is my favourite language? ')

if ans.lower() == "Tkelebkyian":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

ans = input('4. What is my favourite food? ')

if ans.lower() == "sushi":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

print("Thank you for playing, you got " + str(score) + ' questions correct!')
percent = (score / totalQuestions) * 100
print("Mark: " + str(int(percent)) + '%')

if percent >= 50:
    print('Nice! You passed!')
else:
    print('Better luck next time')













