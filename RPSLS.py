# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

names = {"rock" : 0,
         "Spock" : 1,
         "paper" : 2,
         "lizard" : 3,
         "scissors" : 4}

numbers = {0 : "rock",
           1 : "Spock",
           2 : "paper",
           3 : "lizard",
           4 : "scissors"}

# helper functions

def number_to_name(number):
    # fill in your code below
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number in range(5):
        return numbers[number]
    else:
        print "Number out of range! Defaulting to 'rock'"
        return "rock"
    
def name_to_number(name):
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name in names:
        return names[name]
    else:
        print "Invalid name! Defaulting to 'rock'"
        return 0


def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # compute difference of player_number and comp_number modulo five
    result = (player_number - comp_number) % 5
    
    # use if/elif/else to determine winner
    winner = ''
    if result == 0:
        winner = "Player and computer tie!"
    elif result == 1 or result == 2:
        winner = "Player wins!"
    elif result == 3 or result == 4:
        winner = "Computer wins!"
    else:
        winner = "Result out of range, something has gone terribly wrong!"
    

    # convert comp_number to name using number_to_name
    
    # print results
    print "Player chooses", name
    print "Computer chooses", number_to_name(comp_number)
    print winner, "\n"

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


