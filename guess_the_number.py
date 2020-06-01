"""
GTN avec implémentation du multithreading

YYYY/MM/DD: 2019/10/05

Author: Mounir Lalami
"""

import random

def init():
    """
    initialisation du jeu, des variables
    """
    print("-----Choose difficulty-----")
    print("0 : Sandbox [0-100 ; unlimited guesses]")
    print("1 : Easy    [0-100 ; 10 guesses]")
    print("2 : Medium  [0-100 ; 8 unlimited guesses]")
    print("3 : Hard    [0-100 ; 6 unlimited guesses]")
    difficulty = int(input("Enter the number of the choosen difficulty : "))
    randomValue = random.randint(0,100)
    return difficulty, randomValue

def stats(totalGuesses,randomValue):
    if totalGuesses == -1:
        print("You lost! The hidden number was {}".format(randomValue))
    else:
        print("Congratulations ! You found the hidden number in {} guesses".format(totalGuesses))
    input("--------\n Press any key to exit \n--------")
    return 0

def main(difficulty,randomValue):
    won = False
    totalGuesses = 0
    if difficulty == 0:
        difficulty = 999999999
    elif difficulty == 1:
        difficulty = 10
    elif difficulty == 2:
        difficulty = 8
    elif difficulty == 3:
        difficulty = 6

    for i in range(difficulty):
        if totalGuesses == difficulty:
            return -1, randomValue
        guess = int(input("Guess n°{}: ".format(i+1)))
        totalGuesses += 1
        if guess == randomValue:
            return totalGuesses,randomValue
        elif guess > randomValue:
            print("The hidden number is smaller")
        else:
            print("The hidden number is bigger")

if __name__ == '__main__':
    difficulty, randomValue = init()
    result, randomValue = main(difficulty,randomValue)
    stats(result, randomValue)
