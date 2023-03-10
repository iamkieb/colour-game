#imports
import random

#Define Leaderboard
class Leaderboard():
    bot_score = 0
    player_score = 0

#Colour Options - Choice for Players & Computer
colour = [ "red", "blue", "green", "yellow", "purple", "orange", "white", "black"]

#Game Mechanic
def colourchoice(turns, options):
    random_colour = random.choice(options)
    print(random_colour) 
    try:
        while turns > 0:
            guess = input('What is your guess? ').lower()
            computer_action = random_colour
            turns -= 1
            if guess == random_colour or computer_action == random_colour:
                print("Hang on...")
                if guess == computer_action: 
                    print(f"Looks Like a Tie! Are you a bot as well? Just kidding.")
                    Leaderboard.bot_score += 1
                    Leaderboard.player_score += 1
                    break
                elif guess == random_colour:
                    print("We have a winner!")
                    print("It's all you! Well done!")
                    print(f"Who'd have guessed ;), I mean the bot chose {computer_action} LOL.")
                    Leaderboard.player_score += 3
                    break
                else:
                    print("Oh no! Looks like you were too slow!")
                    print(f"The bot got it...")
                    Leaderboard.bot_score += 3
                    break
                break
            elif guess != random_colour and computer_action != random_colour:
                print("Not quite, think harder...")
                print(f"You have {turns} more chances to guess")
            else: 
                print("Wrong!!! Try Again")    
            print(f"\nYou chose {guess}")
            print(f"The computer chose {computer_action}.\n")
        print("What a game!")
        print(f"The colour was {random_colour}!")
    except ValueError:
        print("Only colours from the list are allowed, don't get too clever!")

#define levels
def easy():
    print("You need to choose from 6 colours and you have 4 guesses")
    options = random.sample(colour, k=6)
    print(f"Here are your options: {options}")
    print("Sounds easy enough? Let's see you do it!")
    colourchoice(4,options)

def medium():
    print("You need to choose from 7 colours and you have 4 guesses")
    options = random.sample(colour, k=7)
    print(f"Here are your options: {options}")
    print("Sounds easy enough? Let's see you do it!")
    colourchoice(4,options)

def hard():
    print("You need to choose from 8 colours and you have 4 guesses")
    options = random.sample(colour, k=8)
    print(f"Here are your options: {options}")
    print("Sounds easy enough? Let's see you do it!")
    colourchoice(4,options)


#try again & leaderboard
def try_again():
    print(f"Your Score - {Leaderboard.player_score}")
    print(f"The Bot - {Leaderboard.bot_score}")
    again = input("Do you want to play again? Yes / No ")
    if again.upper() == 'YES' :
        welcome()
    elif again.upper() == "NO" : 
        print("Thanks for playing ")
        if Leaderboard.bot_score > Leaderboard.player_score:
            print(f"The bot beat you by {Leaderboard.bot_score - Leaderboard.player_score} points")
        elif Leaderboard.player_score > Leaderboard.bot_score:
            print(f"You won by {Leaderboard.player_score - Leaderboard.bot_score} points")
        elif Leaderboard.player_score == Leaderboard.bot_score:
            print("Even game! Maybe next time you can beat the bot!")
    else:
        print("Say that again...Yes or no? ")
        try_again()


# Choose level
def welcome():
    print("Welcome to the Colour Race Chase")
    print("You need to match the right colour and beat the bot to the ]!")
    difficulty = input("Choose your level - Easy, Medium and Hard? ")
    if difficulty.upper() == "EASY":
        easy()
        try_again()
    elif difficulty.upper() == "MEDIUM":
        medium()
        try_again()
    elif difficulty.upper() == "HARD":
        hard()
        try_again()
    else:
        print("That's not a level! Try again!")
        welcome()
welcome()