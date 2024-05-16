print('Welcome!')
print('This is a program will help you to calcuate the average of your test score')
total = 0
count = 0
score = 0

while score != 999:
    score = int(input(('Enter your score or enter 999 to quit: ')) )
    if score >= 0 and score <= 100:
        total += int(score)
        count += 1
    else:
        print('Please enter a number')

if count > 0:
    average = total / count
    print(f'Good Bye! You entered {count} test scores.With an average of {average}')