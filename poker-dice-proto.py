# -*- coding: cp1252 -*-

import random, itertools
from itertools import groupby

# Giving names to numbers and determining how to display them
nine = 1
ten = 2
jack = 3
queen = 4
king = 5
ace = 6

names = {nine:"9", ten:"10", jack:"J", queen:"Q", king:"K", ace:"A"}

# ToDo: Score system
player_score = 0
computer_score = 0

# Start function
def start():
    print("Let's throw some dices")
    while game():
        pass
    scores()

# Game function
def game():
    throws()
    return play_again()

# Throw function handels all decision making in game
def throws():
    # Initial Throw
    roll_number = 5
    dice = roll(roll_number)
    dice.sort()
    print(dice) # This List is for the testing purposes 
    # Printing each Dice with their values
    for i in range(len(dice)):
        print("Dice",i + 1,":",names[dice[i]])

    result = hand(dice) # Checking hand
    print ("You have", result)

    # First Decision
    while True:
        rerolls = int(input("How many dices you want to reroll? "))
        try:
            if rerolls == 0:
                break
            elif rerolls == 1:
                break
            elif rerolls == 2:
                break
            elif rerolls == 3:
                break
            elif rerolls == 4:
                break
            elif rerolls == 5:
                break
        except ValueError:
            pass
        print("I didn't understand. Please press 0, 1, 2, 3, 4 or 5")
    
    # Handling user's answer & Possible second decision
    if rerolls == 0:
        print("You ended your round with ", result)
    else:
        print("Choose rerollable dices")
        if rerolls == 1:
            old_hand = dice
            count = 1

            # Loop for rerolls and changing list items
            for i in range(0,rerolls):
                change = int(input("Choose dice "+ str(count)+": "))
                new_dice = single_roll()
                old_hand[change-1] = new_dice
                count += 1

            # Printing each Dice with their values
            for i in range(len(old_hand)):
                print("Dice",i + 1,":",names[old_hand[i]])

            result = hand(old_hand) # Checking hand
            print ("You have", result)
            
        elif rerolls == 2:
            old_hand = dice
            count = 1

            # Loop for rerolls and changing list items
            for i in range(0,rerolls):
                change = int(input("Choose dice "+ str(count)+": "))
                new_dice = single_roll()
                old_hand[change-1] = new_dice
                count += 1

            # Printing each Dice with their values
            for i in range(len(old_hand)):
                print("Dice",i + 1,":",names[old_hand[i]])

            result = hand(old_hand) # Checking hand
            print ("You have", result)

        elif rerolls == 3:
            old_hand = dice
            count = 1

            # Loop for rerolls and changing list items
            for i in range(0,rerolls):
                change = int(input("Choose dice "+ str(count)+": "))
                new_dice = single_roll()
                old_hand[change-1] = new_dice
                count += 1

            # Printing each Dice with their values
            for i in range(len(old_hand)):
                print("Dice",i + 1,":",names[old_hand[i]])

            result = hand(old_hand) # Checking hand
            print ("You have", result)

        elif rerolls == 4:
            old_hand = dice
            count = 1

            # Loop for rerolls and changing list items
            for i in range(0,rerolls):
                change = int(input("Choose dice "+ str(count)+": "))
                new_dice = single_roll()
                old_hand[change-1] = new_dice
                count += 1

            # Printing each Dice with their values
            for i in range(len(old_hand)):
                print("Dice",i + 1,":",names[old_hand[i]])

            result = hand(old_hand) # Checking hand
            print ("You have", result)

        elif rerolls == 5:
            roll_number = 5
            dice = roll(roll_number)
            dice.sort()

            # Printing each Dice with their values
            for i in range(len(dice)):
                print("Dice",i + 1,":",names[dice[i]])

            result = hand(dice) # Checking hand
            print ("You have ", result)

# Function which roll initial throw
def roll(roll_number):
    numbers = range(1,7)
    dice = list(range(roll_number))
    iterations = 0
    
    while iterations < roll_number:
        iterations = iterations + 1
        dice[iterations-1] = random.choice(numbers)
    return dice

# single_roll() function is used in reroll loop
def single_roll():
    numbers = range(1,7)
    new_dice = random.choice(numbers)
    return new_dice

# Hand function makes hand analysis and returns result
def hand(dice):
    dice_hand = [len(list(group)) for key, group in groupby(dice)]
    dice_hand.sort(reverse=True)
    straight1 = [1,2,3,4,5]
    straight2 = [2,3,4,5,6]

    if dice == straight1 or dice == straight2:
        return ("A straight")
    elif dice_hand[0] == 5:
        return ("Five of a kind")
    elif dice_hand[0] == 4:
        return ("Four of a kind")
    elif dice_hand[0] == 3:
        if dice_hand[1] == 2:
            return ("A full house")
        else:
            return ("Three of a kind")
    elif dice_hand[0] == 2:
        if dice_hand[1] == 2:
            return ("Two pair")
        else:
            return ("One Pair")
    else:
        return ("A high card")

# Play_again function handels users answer 
def play_again():
    answer = input("Would you like to play again? y/n ")
    if answer in ("y", "Y", "yes", "Yes", "Of course!"):
        print("")
        print("Let's throw some dices")
        return answer
    else:
        print ("Thank you for playing.")

# Handels Scores in future
def scores():
    global player_score, computer_score
    print("")
    print("HIGH SCORES")
    print("Player: ", player_score)
    print("Computer: ", computer_score)

if __name__ == '__main__':
    start()
