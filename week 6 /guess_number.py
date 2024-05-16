correct_answer = 13
guess_count = 0
count = 0
guess = False  # Initial guess

print("G U E S S     T H E     N U M B E R")
print("can you try to guess the correct number :>")

while guess == False:
    guess_count = int(input('Guess the number between 1 and 20 : '))
    count +=1
    if 0 >= guess_count or guess_count > 20:
        print("Sorry you have to guess again, invalid number")

    elif guess_count != correct_answer:
        if guess_count > correct_answer:
            print(' too high and guess again :)')
        else:
            print(' too low and guess again :(')
    elif guess_count == correct_answer:
        print(f'Congrats! You have guessed the correct number in {count} guesses!')
        guess = True


