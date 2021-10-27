# -*- coding: utf-8 -*-
"""
Course: Introduction to Python Programming
Student Name:Raveh
"""
#%% 
from random import randint
#note: x=randint(0, 10) will generate a random integer x and 0<=x<=10
# %%
def HumanPlayer(GameRecord):
    '''
    Parameter: GameRecord (the record of both players' choices and outcomes)
    Return: ChoiceOfHumanPlayer, a string that can only be rock, paper, scissors, or quit
    Description:
        This function asks the user to make a choice (i.e. input a string)
        This function will NOT return/exit until it gets a valid input from the user
        valid inputs are: rock or r, paper or p, scissors or s, game or g, quit or q
        quit means the user wants to quit the game
        game means the user wants to see the GameRecord
    '''
    choice = 'a'
    print()
    
    while choice != 'q':
        
        print("Enter your choice below:")
        choice = input("(R)ock, (P)aper, (S)cissors, (G)ameRecord, (Q)uit: ")
        choice= choice[0].lower()
        
        if choice != 'r' and choice != 'p' and choice !='g' and choice != 's' and choice!='q':
            print("Invalid entry, try again")
            choice = input("(R)ock, (P)aper, (S)cissors, (G)ameRecord, (Q)uit: ")
            choice= choice[0].lower()
        
        if choice == 'r' or choice == 'p' or choice == 's':
            if choice == 'r':
                choice = 'rock'
            elif choice == 'p':
                choice = 'paper'
            else:
                choice = 'scissors'
            
            computer_choice = ComputerPlayer(GameRecord)
            outcome = Judge(computer_choice, choice)
            PrintOutcome(outcome, computer_choice, choice)
            UpdateGameRecord(GameRecord, computer_choice, choice, outcome)
            
            
        elif choice == 'g':
            PrintGameRecord(GameRecord)
        elif choice == 'q':
            print('Thanks for playing! Goodbye.')
            break
            
            
            

# %%
def ComputerPlayer(GameRecord):
    '''
    Parameter: GameRecord (the record of both players' choices and outcomes)
    Return: ChoiceOfComputerPlayer, a string that can only be rock, paper, scissors
    Description:
        ComputerPlayer will randomly make a choice
        ComputerPlayer should not look at the current choice of HumanPlayer
    '''
    random_num = randint(0, 10)
    if random_num <= 3:
        return 'rock'
    elif random_num <=6:
        return 'paper'
    else:
        return 'scissors'
    

# %%
def Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    '''
    Parameters:
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
    Return: Outcome
        Outcome is 0 if it is a draw/tie
        Outcome is 1 if ComputerPlayer wins
        Outcome is 2 if HumanPlayer wins
    Description:
        this function determines the outcome of a game
    '''
    if ChoiceOfComputerPlayer == 'rock':
        if ChoiceOfHumanPlayer == 'rock':
            return 0
        elif ChoiceOfHumanPlayer == 'paper':
            return 2
        else:
            return 1
    elif ChoiceOfComputerPlayer == 'paper':
        if ChoiceOfHumanPlayer == 'paper':
            return 0
        elif ChoiceOfHumanPlayer == 'scissors':
            return 2
        else:
            return 1
    else:
        if ChoiceOfHumanPlayer == 'scissors':
            return 0
        elif ChoiceOfHumanPlayer == 'rock':
            return 2
        else:
            return 1

# %%
def PrintOutcome(Outcome, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    '''
    Parameters:
        Outcome is from Judge
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
    Return: None
    Description:
        print Outcome, Choices and Players to the console window
        the message should be human readable
    '''
    print()
    print('Outcome:')
    
    if Outcome == 0:
        print('It is a tie: ', end="")
    elif Outcome == 1:
        print('Computer wins: ', end="")
    else:
        print('Human wins: ', end="")
        
    print('Computer chose', ChoiceOfComputerPlayer, 'and you chose', ChoiceOfHumanPlayer)
  
    print()
        
        
        

# %%
def UpdateGameRecord(GameRecord, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, Outcome):
    '''
    Parameters: 
        GameRecord is the record of both players' choices and and outcomes
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
        Outcome is an integer from Judge
    Return: None
    Description:
        this function updates GameRecord, a list of three lists
    '''
    GameRecord[0].append(ChoiceOfHumanPlayer)
    GameRecord[1].append(ChoiceOfComputerPlayer)
    GameRecord[2].append(Outcome)
# %%
def PrintGameRecord(GameRecord):
    '''
    Parameters: GameRecord (the record of both players' choices and outcomes)
    Return: None
    Description: this function prints the record of the game (see the sample run)
        the number of rounds. human wins x rounds. computer wins y rounds.
        the record of choices.
    '''
    print()
    print('Game Record:')
    print('You played', len(GameRecord[2]),'numeber of games')
    print('Human wins', GameRecord[2].count(2), 'round(s)')
    print('Computer wins', GameRecord[2].count(1), 'round(s)')
    print('You   Computer')
    for n in range(0, len(GameRecord[2])):
        print(GameRecord[0][n],",", GameRecord[1][n])
    print()
# %% the game
def PlayGame():
    '''
    This is the "main" function
    In this function, human and computer play the game until the human/user wants to quit
    '''

# creat GameRecord    
    GameRecord = [[],[],[]]
    
    print('Welcome to Rock-Paper-Scissors')

    HumanPlayer(GameRecord)
# %% do not modify anything below
if __name__ == '__main__':
    PlayGame()

