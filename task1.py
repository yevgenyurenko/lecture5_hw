import random
rand_num = random.randint(1,10)
while True:
    user_guess = input('Guess the number between 1 and 10: ')
    if user_guess.isdigit() and 0<=int(user_guess)<=10 and int(user_guess) == rand_num:
        print('Congratulations! Correct guess')
        break
    elif user_guess.isdigit() and 0<=int(user_guess)<=10 and int(user_guess) > rand_num:
        print('Your number is too high, try again')
        continue
    elif user_guess.isdigit() and 0<=int(user_guess)<=10 and int(user_guess) < rand_num:
        print('Your number is too low, try again')
        continue
    else:
        print('Incorrect input')
        continue
