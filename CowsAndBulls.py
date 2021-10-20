# COWS AND BULLS

import random
 
digits = '123456789'
size_number = 4
chosen = ''.join(random.sample(digits,size_number))
print ('I have chosen a number from above unique digits from 1 to 9 arranged in a random order. You need to input a number, unique digit number as a guess at what I have chosen')
guesses = 0
while True:
    guesses += 1
    while True:
        guess = input('\nNext guess ')
        if len(guess) == size_number and \
           all(char in digits for char in guess) \
           and len(set(guess)) == size_number:
            break
        print ("Problem, try again. You need to enter unique digits from 1 to 9")
    if guess == chosen:
        print ('\nCongratulations you guessed correctly in',guesses,'attempts')
        break
    bulls = cows = 0
    for i in range(size_number):
        if guess[i] == chosen[i]:
            bulls += 1
        elif guess[i] in chosen:
            cows += 1
    print (bulls, ' Bulls\n  ', cows ,' Cows')
    if(cows==4):
        break






# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
