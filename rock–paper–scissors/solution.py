import random
# Import the choice function of the random module
# https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list

# Assign to a list the 3 possible options: 'stone', 'paper' or 'scissors'.
options = ['stone', 'paper', 'scissors', 'lizard', 'spock']

# Assign a variable to the maximum number of games: 1, 3, 5, etc ...
numberOfGames = 5

# Assign a variable to the number of games a player must win to win.
# Preferably the value will be based on the number of maximum games
gamesToWin = (numberOfGames+1)/2

# Define a function that randomly returns one of the 3 options.
# This will correspond to the play of the machine. Totally random.
def machineTurn():
    return random.choice(options)

# Define a function that asks your choice: 'stone', 'paper' or 'scissors'
# you should only allow one of the 3 options. This is defensive programming.
# If it is not stone, paper or scissors keep asking until it is.
def userTurn():
    index = -1
    while index < 0 or index > 4:
        userinput = input("type your choice please: ")
        try:
            index = options.index(userinput)
        except:
            print("only valid choices please!")
    return userinput

# Define a function that resolves a combat.
# Returns 0 if there is a tie, 1 if the machine wins, 2 if the human player wins
def calculateBattle(userInput, machineInput):
    if userInput == machineInput:
        return 0
    if (userInput == options[0] and machineInput == options[1]):
        return 1
    if (userInput == options[0] and machineInput == options[4]):
        return 1
    elif (userInput == options[1] and machineInput == options[2]):
        return 1
    elif (userInput == options[1] and machineInput == options[3]):
        return 1
    elif (userInput == options[2] and machineInput == options[0]) :
        return 1
    elif (userInput == options[2] and machineInput == options[4]) :
        return 1
    elif (userInput == options[3] and machineInput == options[1]) :
        return 1
    elif (userInput == options[3] and machineInput == options[2]) :
        return 1
    elif (userInput == options[4] and machineInput == options[1]) :
        return 1
    elif (userInput == options[4] and machineInput == options[3]) :
        return 1
    else:
        return 2
        
    
# Define a function that shows the choice of each player and the state of the game
# This function should be used every time accumulated points are updated
def showCurrentState(userWins, machineWins, userChoice, machineChoice):
    print("User chose "+userChoice+" and machine drew "+machineChoice)
    print("User won "+str(userWins)+" times, machine won "+str(machineWins)+" times.")
        
# Create two variables that accumulate the wins of each participant
machineWins = 0
userWins = 0

# Create a loop that iterates while no player reaches the minimum of wins
# necessary to win. Inside the loop solves the play of the
# machine and ask the player's. Compare them and update the value of the variables
# that accumulate the wins of each participant.
while machineWins < gamesToWin and userWins < gamesToWin:
    userInput = userTurn()
    machineInput = machineTurn()
    outcome = calculateBattle(userInput, machineInput)

    if outcome == 1:
        machineWins += 1
    elif outcome == 2:
        userWins += 1
    else:
        print("draw")

    showCurrentState(userWins, machineWins, userInput, machineInput)
    
# Print by console the winner of the game based on who has more accumulated wins
print("User won!") if userWins > machineWins else print("Machine won!")