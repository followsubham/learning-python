# Create a program that will play the “cows and bulls” game with the user.
# The game works like this: Randomly generate a 4-digit number.
# Ask the user to guess a 4-digit number. For every digit that the user guessed
# correctly in the correct place, they have a “cow”. For every digit the user guessed
# correctly in the wrong place is a “bull.” Every time the user makes a guess,
# tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout teh game and tell the
# user at the end.

import random


def compare_numbers(number, user_guess):
    cowbull = [0,0] # cows, then bulls
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1]+=1
        else:
            cowbull[0]+=1
            print(f"You have  {cowbull[0]} cows and {cowbull[1]} bulls")
    return cowbull


if __name__=="__main__":
    playing = True # gotta play the game
    number = str(random.randint(0,9999))  # random 4 digit number
    guesses = 0

    print("Let's play a game of Cowbull!")  # explanation
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")

    while playing:
        user_guess = input("Give me a 4-digit number: ")
        if user_guess == "exit":
            break

        cowbullcount = compare_numbers(number,user_guess)
        guesses+=1
        print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")
        if cowbullcount[1]==4:
            playing = False
            print("You win the game after " + str(guesses) + "! The number was "+str(number))
            break #redundant exit
            else:
                print("Your guess isn't quite right, try again.")

