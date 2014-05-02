# Guess the Number!
# COURSERA - Interactive Programming in Python

from random import randrange
import simplegui

# initialize global variables used in your code
secret_number = 0
game_range = 100
guesses_remaining = 0

# helper function to start and restart the game
def new_game():
    global secret_number
    global game_range
    global guesses_remaining
    
    if game_range == 100:
        secret_number = randrange(0,101)
        guesses_remaining = 7
    elif game_range == 1000:
        secret_number = randrange(0,1001)
        guesses_remaining = 10
        
    print "New Game! Guess a number between 0 -", game_range
    print "Guesses Remaining: ", guesses_remaining, "\n"


# define event handlers for control panel
def range100():
    global game_range 
    game_range = 100
    new_game()

def range1000():
    global game_range 
    game_range = 1000
    new_game()
    
def count_guesses():
    """
        Count down the number of guesses and start new games
    """
    global guesses_remaining
       
    guesses_remaining -= 1
    
    if guesses_remaining <= 0:
        print "You ran out of guesses!\n GAME OVER!\n"
        new_game()
    else:
        print "Guesses Remaining:", guesses_remaining, "\n"
    
def input_guess(guess):
    """
        Input Handler -> Handle guess inputs
    """
    # Print the guess
    print "You guessed,", guess
    
    # Make sure the guess is a number
    # And Handle accordingly
    if guess.isdigit():
        guess = int(guess)
    
        if guess == secret_number:
            print guess, "was the secret number\nYOU WIN!\n"
            new_game()
        elif guess < secret_number:
            print "To Low!"
            count_guesses()
        elif guess > secret_number:
            print "To High!"
            count_guesses()
    else:
        print "INVALID GUESS! ", guess, "is not a INTEGER!\n"
        
    
# create and run frame

frame = simplegui.create_frame("Guess the Number", 300, 300)

# register event handlers for control elements

frame.add_button("New Game 0-100", range100)
frame.add_button("New Game 0-1000", range1000)
guess = frame.add_input("Guess a Number", input_guess, 50)

# start a new game
new_game()


