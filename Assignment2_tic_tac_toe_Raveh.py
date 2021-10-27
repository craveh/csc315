"""
Course: Introduction to Python Programming
"""
#%%
def author():
    '''
    return your name
    '''
    return 'Hannah Raveh'
#%%

import random
from random import randint
import copy
# %%
def DrawBoard(Board):
    '''
    Parameter: Board is a 3x3 matrix (a nested list).
    Return: None
    Description: this function prints the chess board    
    hint: Board[i][j] is ' ' or 'X' or 'O' in row-i and col-j
          use print function
    '''
    print()
    for n in range(0, len(Board)):
        toPrint = ""
        for m in range(0, len(Board[n])):
            toPrint += Board[n][m]
            if m < 2:
                toPrint += '|'
        print(toPrint)
        if n<2:
            print('-+-+-')
    print()       
#%% 
def IsSpaceFree(Board, i ,j):
    '''
    Parameters: Board is the game board, a 3x3 matrix
                i is the row index, j is the col index
    Return: True or False
    Description: 
        return True  if Board[i][j] is empty ' '
        return False if Board[i][j] is not empty
        return False if i or j is invalid (e.g. i = -1 or 100)
    '''
    if 0 <= i <= 2:
        if 0 <= j <= 2:
            if Board[i][j] == " ":
                return True
            else:
                return False
            
        else:
            return False
    else:
        return False
    
#%%
def GetNumberOfChessPieces(Board):
    '''
    Parameters: Board is the game board, a 3x3 matrix
    Return: the number of chess piceces on Board
            i.e. the total number of 'X' and 'O'
    hint: define a counter and use a nested for loop, like this
          for i in 0 to 3
              for j in 0 to 3
                  add one to the counter if Board[i][j] is not empty
    '''
    counter = 0
    for i in range(0, len(Board)):
        for j in range(0, len(Board[i])):
            if Board[i][j] != " ":
                counter += 1
                
    return counter
#%%
def IsBoardFull(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: True or False
    Description: 
        return True if the Board is fully occupied
        return False otherwise 
    hint: use GetNumberOfChessPieces
    '''
    num_pieces = GetNumberOfChessPieces(Board)
    if num_pieces == 9:
        return True
    else:
        return False
#%%
def IsBoardEmpty(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: True or False
    Description: 
        return True if the Board is empty
        return False otherwise 
    hint: use GetNumberOfChessPieces
    '''
    num_pieces = GetNumberOfChessPieces(Board)
    if num_pieces == 0:
        return True
    else:
        return False
#%%
def UpdateBoard(Board, Tag, Choice):
    '''
    Parameters: 
        Board is the game board, a 3x3 matrix
        Tag is 'O' or 'X'
        Choice is a tuple (row, col) from HumanPlayer or ComputerPlayer
    Return: None
    Description: 
         Update the Board after a player makes a choice
         Set an element of the Board to Tag
    '''
    i = Choice[0]
    j = Choice[1]
    Board[i][j] = Tag
#%%
def HumanPlayer(Tag, Board):
    '''
    Parameters:        
        Tag is 'X' or 'O'. If Tag is 'X': HumanPlayer goes first    
        Board is the game board, a 3x3 matrix
    Return: ChoiceOfHumanPlayer, it is a tuple (row, col)
    Description:
        This function will NOT return until it gets a valid input from the user
    Attention:
        Board is NOT modified in this function
    hint: 
        the user needs to input row-index and col-index, where a new chess will be placed
        use int() to convert string to int
        use try-except to handle exceptions if the user inputs some random string
        if (row, col) has been occupied, then ask the user to choose another spot
        if (row, col) is invalid, then ask the user to choose a valid spot
    '''
    Flag = True

    while Flag:
        print()
        print("Make your choice now!")
    
        try:
            row = input("Enter row number: ")
            row = int(row)
            
            if(row < 0 or row > 2):
                print("Number inputted for row is invalid. Try again")
            else:
                try:
                    column = input("Enter column number: ")
                    column = int(column)
                    if(column < 0 or column > 2):
                        print("Number inputted for column is invalid. Try again")
                    else:
                        if IsSpaceFree(Board, row, column):
                            Flag = False
                            return (row, column)
                        else:
                            print('Selected spot is full. Try again.')
                except:
                    print("Invalid column entry.")
            
        except:
            print("Invalid row entry.")
#%%
def ComputerPlayer(Tag, Board):
    '''
    Parameters:
        Tag is 'X' or 'O'. If Tag is 'X': ComputerPlayer goes first    
        Board is the game board, a 3x3 matrix
    Return: ChoiceOfComputerPlayer, it is a tuple (row, col)   
    Description:
        ComputerPlayer will choose an empty spot on the board
        a random strategy in a while loop:
            (1) randomly choose a spot on the Board
            (2) if the spot is empty then return the choice (row, col)
            (3) if it is not empty then go to (1)
    Attention:
        Board is NOT modified in this function
    '''
    Flag = True
    while Flag:
        rand_row = randint(0, 3)
        rand_col = randint(0,3)
        if IsSpaceFree(Board, rand_row, rand_col):
            Flag = False
            return (rand_row, rand_col)
#%%
def Judge(Board):
    '''
    Parameters:
         Board is the current game board, a 3x3 matrix
    Return: Outcome, an integer
        Outcome is 0 if the game is still in progress
        Outcome is 1 if player X wins
        Outcome is 2 if player O wins
        Outcome is 3 if it is a tie (no winner)
    Description:
        this funtion determines the Outcome of the game
    hint:
        (1) check if anyone wins, i.e., three 'X' or 'O' in
            top row, middle row, bottom row
            lef col, middle col, right col
            two diagonals
        (2) if no one wins, then check if it is a tie
                i.e. if the board is fully occupied, then it is a tie
        (3) otherwise, the game is still in progress
    '''
    
    
    
## Check if Player X wins    
    if CheckDiagonals("X", Board) or CheckCols('X', Board) or CheckRows('X', Board):
        return 1
## Check if Player O wins
    elif CheckDiagonals("O", Board) or CheckCols('O', Board) or CheckRows('O', Board):
        return 2
    elif IsBoardFull(Board):
        return 3
    else:
        return 0
#%%
def CheckDiagonals(Tag, Board):
    '''
    Parameters:
        Tag is the player piece. Either 'X' or 'O'.
        Board is the 3x3 matrix that represents the tic-tac-toe board
    Returns:
        Boolean.
        True if there is the same tag in the whole diagonal
        False if not
    Description:
        Determiners if a player wins via the diagonal being full
    '''
    if Board[0][0] == Tag and Board[1][1] == Tag and Board[2][2] == Tag:
        #print("True main diag0")
        return True
    else:
        if Board[0][2] == Tag and Board[1][1] == Tag and Board[2][0] == Tag:
            #print("True")
            return True
        else:
            return False
#%%
def CheckRows(Tag, Board):
    #print (Tag)
    '''
    Parameters:
        Tag is the player piece. Either 'X' or 'O'.
        Board is the 3x3 matrix that represents the tic-tac-toe board
    Returns:
        Boolean.
        True if there is the same tag in the whole row
        False if not
    Description:
        Determiners if a player wins via a row being full
    '''
    if Board[0][0] == Tag and Board[0][1] == Tag and Board[0][2] == Tag:
#        print("True row 0")
        return True
    elif Board[1][0] == Tag and Board[1][1] == Tag and Board[1][2] == Tag:
        #print("True row 1")
        return True
    elif Board[2][0] == Tag and Board[2][1] == Tag and Board[2][2] == Tag:
        #print("True row 2")
        return True 
    else:
        return False
#%%
def CheckCols(Tag, Board):
    '''
    Parameters:
        Tag is the player piece. Either 'X' or 'O'.
        Board is the 3x3 matrix that represents the tic-tac-toe board
    Returns:
        Boolean.
        True if there is the same tag in the whole column
        False if not
    Description:
        Determiners if a player wins via a column being full
    '''
    if Board[0][0] == Tag and Board[1][0] == Tag and Board[2][0] == Tag:
        #print("True col 0")
        return True
    elif Board[0][1] == Tag and Board[1][1] == Tag and Board[2][1] == Tag:
        #print("True col 1")
        return True
    elif Board[0][2] == Tag and Board[1][2] == Tag and Board[2][2] == Tag:
        #print("True col 2")
        return True 
    else:
        return False

#%%
def ShowOutcome(Outcome, NameX, NameO):
    '''
    Parameters:
        Outcome is from Judge
        NameX is the name of PlayerX who goes first at the beginning
        NameO is the name of PlayerO 
    Return: None
    Description:
        print a meassage about the Outcome
        NameX/NameO may be 'human' or 'computer'
    hint: the message could be
        PlayerX (NameX, X) wins 
        PlayerO (NameO, O) wins
        the game is still in progress
        it is a tie
    '''
    if Outcome == 0:
        print("The game is still in progress")
        
    elif Outcome == 1:
        print("Player X - the", NameX, "wins the game!")
        print()
    elif Outcome == 2:
        print("Player O - the", NameO, "wins the game!")
        print()
    else:    
        print("Tie game.")
        print()
        
#%% read but do not modify this function
def Which_Player_goes_first():
    '''
    Parameter: None
    Return: two function objects: PlayerX, PlayerO
    Description:
        Randomly choose which player goes first.  
        PlayerX/PlayerO is ComputerPlayer or HumanPlayer
    '''
    if random.randint(0, 1) == 0:
        print("Computer player goes first")
        PlayerX = ComputerPlayer        
        PlayerO = HumanPlayer     
    else:
        print("Human player goes first")
        PlayerO = ComputerPlayer        
        PlayerX = HumanPlayer           
    return PlayerX, PlayerO
#%% the game
def TicTacToeGame():
    #---------------------------------------------------    
    print("Welcome to the Tic Tac Toe Game!")
    Board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    DrawBoard(Board)
    # determine the order of the players
    PlayerX, PlayerO = Which_Player_goes_first()
    # get the name of each function object
    NameX = PlayerX.__name__
    NameO = PlayerO.__name__
    #---------------------------------------------------    
    # suggested steps in a while loop:
    # (1)  get the choice from PlayerX, e.g. ChoiceX=PlayerX('X', Board)
    # (2)  update the Board
    # (3)  draw the Board
    # (4)  get the outcome from Judge
    # (5)  show the outcome
    # (6)  if the game is completed (win or tie), then break the loop
    # (7)  get the choice from PlayerO
    # (8)  update the Board
    # (9)  draw the Board
    # (10) get the outcome from Judge
    # (11) show the outcome
    # (12) if the game is completed (win or tie), then break the loop
    #---------------------------------------------------
    # your code starts from here
    Outcome = 0
    while Outcome != 1 and Outcome != 2 and Outcome !=3:
        if NameX == "ComputerPlayer":
            
            Choice = ComputerPlayer('X', Board)
            print('ComputerPlayer (X) has made a choice')
            Outcome = RunThrough(Board, 'X', Choice)
            #print(Outcome)
            ShowOutcome(Outcome, NameX, NameO)
            if Outcome == 0:
                
                Choice = HumanPlayer('O', Board)
                print('HumanPlayer (O) has made a choice')
                Outcome = RunThrough(Board, 'O', Choice)
                #print(Outcome)
                ShowOutcome(Outcome, NameX, NameO)
            
        else:
            Choice = HumanPlayer('X', Board)
            print('HumanPlayer (X) has made a choice')
            Outcome = RunThrough(Board, 'X', Choice)
            #print(Outcome)
            ShowOutcome(Outcome, NameX, NameO)
            
            if Outcome == 0:
            
                Choice = ComputerPlayer('O', Board)
                print('ComputerPlayer (O) has made a choice')
                Outcome = RunThrough(Board, 'O', Choice)
                #print(Outcome)
                ShowOutcome(Outcome, NameX, NameO)
#%%
def RunThrough(Board, Tag, Choice):
    '''
    Parameters:
        Tag is the player piece. Either 'X' or 'O'.
        Board is the 3x3 matrix that represents the tic-tac-toe board
        Choice is the tuple of coordinates
    Returns:
        The outcome from judge
    Description:
        Runs the repetitive part of code from TicTacToeGame
    '''
    UpdateBoard(Board, Tag, Choice)
    DrawBoard(Board)
    Outcome = Judge(Board)
    #print (Outcome)
    return Outcome
          
            
    
#%% play the game many rounds until the user wants to quit
# read but do not modify this function
def PlayGame():
    while True:
        TicTacToeGame()
        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break
    print("GameOver")
#%% do not modify anything below
if __name__ == '__main__':
    PlayGame()
