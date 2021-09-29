# COWS AND BULLS

import random

def compare_numbers(num, guess):
    cowbull = [0,0] #cows then bulls
    for i in range(len(num)):
        if num[i] == guess[i]:
            cowbull[1]+=1
        else:
            cowbull[0]+=1
        return cowbull

if

# cow = True
# bull = wrong spot
#
# print('cows {}, bulls {}'.format(x, y))




# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
