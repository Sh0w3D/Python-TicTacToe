import os
import sys


def checkPlayerNames(Player1, Player2, warunek):
    if(Player1 == Player2):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Given nick names are the same, please give new ones")
        warunek = False
    else:
        warunek = True
    
    return warunek


# Main game function
def MainGame(BoardMoves, Turns, Player1, Player2, Player):
    # Check if the cords are taken
    Test = False
    while(Test == False):
        # display board and ask user for cords to input symbol
        TicTacBoad(BoardMoves)
        try:
            CurrentMoveRow = int(input("Do ktorego wiersza wstawic wartosc: "))
            CurrentMoveCol = int(input("Do ktorej kolumny wstawic wartosc: "))
        except(UnboundLocalError, ValueError, IndexError):
            print("You've raised an error, now I'll crash!")
            sys.exit("Remember, it's all thanks to you!")
        Test = CheckIfPosIsSpace(CurrentMoveRow, CurrentMoveCol, BoardMoves, Test)
        if(Test == False):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Given position is already occupied, give new one!")
        else:
            break
    if(Turns % 2 == 0):
        Player = Player1
        TranslateAndCheckBoardPos(CurrentMoveRow, CurrentMoveCol, BoardMoves, Player)
        CheckWinOrTie(Turns, Player1, Player2, BoardMoves)
        print(BoardMoves)
    else:
        Player = Player2
        TranslateAndCheckBoardPos(CurrentMoveRow, CurrentMoveCol, BoardMoves, Player)
        CheckWinOrTie(Turns, Player1, Player2, BoardMoves)
        print(BoardMoves)
    os.system('cls' if os.name == 'nt' else 'clear')



# This function prints Board with array slots
def TicTacBoad(BoardMoves):
    print("""
      1   2   3
    1 %s | %s | %s
     ---+---+---
    2 %s | %s | %s
     ---+---+---
    3 %s | %s | %s
    """ % (BoardMoves[0], BoardMoves[1], BoardMoves[2], BoardMoves[3],
    BoardMoves[4], BoardMoves[5], BoardMoves[6], BoardMoves[7],
    BoardMoves[8]))

# This function checks if board is full or someone won the game
# if the board is full there is a tie
def CheckWinOrTie(Turns, Player1, Player2, BoardMoves):
    #check if expected cords are taken by Player2
    if((BoardMoves[0] == Player1 and BoardMoves[1] == Player1 and BoardMoves[2] == Player1) or
        (BoardMoves[3] == Player1 and BoardMoves[4] == Player1 and BoardMoves[5] == Player1) or
        (BoardMoves[6] == Player1 and BoardMoves[7] == Player1 and BoardMoves[8] == Player1) or
        (BoardMoves[0] == Player1 and BoardMoves[3] == Player1 and BoardMoves[6] == Player1) or
        (BoardMoves[1] == Player1 and BoardMoves[4] == Player1 and BoardMoves[7] == Player1) or
        (BoardMoves[2] == Player1 and BoardMoves[5] == Player1 and BoardMoves[8] == Player1) or
        (BoardMoves[0] == Player1 and BoardMoves[4] == Player1 and BoardMoves[8] == Player1) or
        (BoardMoves[2] == Player1 and BoardMoves[4] == Player1 and BoardMoves[6] == Player1)):
        print(f"Player {Player1} has won!")
        TicTacBoad(BoardMoves)
        ResetOrExitGame(input("Game over! Want to play one more time? (Y/N): "), BoardMoves, Turns)
    #check if expected cords are taken by Player2
    elif((BoardMoves[0] == Player2 and BoardMoves[1] == Player2 and BoardMoves[2] == Player2) or
        (BoardMoves[3] == Player2 and BoardMoves[4] == Player2 and BoardMoves[5] == Player2) or
        (BoardMoves[6] == Player2 and BoardMoves[7] == Player2 and BoardMoves[8] == Player2) or
        (BoardMoves[0] == Player2 and BoardMoves[3] == Player2 and BoardMoves[6] == Player2) or
        (BoardMoves[1] == Player2 and BoardMoves[4] == Player2 and BoardMoves[7] == Player2) or
        (BoardMoves[2] == Player2 and BoardMoves[5] == Player2 and BoardMoves[8] == Player2) or
        (BoardMoves[0] == Player2 and BoardMoves[4] == Player2 and BoardMoves[8] == Player2) or
        (BoardMoves[2] == Player2 and BoardMoves[4] == Player2 and BoardMoves[6] == Player2)):
        print(f" Player {Player2} has won!")
        TicTacBoad(BoardMoves)
        ResetOrExitGame(input("Game over! Want to play one more time? (Y/N): "), BoardMoves, Turns)
        # if one or more values are spaces than continue game
    elif(BoardMoves[0].isspace() == False and BoardMoves[1].isspace() == False and BoardMoves[2].isspace() == False
        and BoardMoves[3].isspace() == False and  BoardMoves[4].isspace() == False and BoardMoves[5].isspace() == False
        and BoardMoves[6].isspace() == False and BoardMoves[7].isspace() == False and BoardMoves[8].isspace() == False):
        # If all values are different from spaces than display board
        # and ask user for new game or if he wants to exit the game
        TicTacBoad(BoardMoves)
        ResetOrExitGame(input("Game over! Want to play one more time? (Y/N): "), BoardMoves, Turns)
    else:
        pass
    

# This function checks if the position is already taken
# If the function returns True if position is space
# else the function returns False
def CheckIfPosIsSpace(CurrentMoveRow, CurrentMoveCol, BoardMoves, Test):
    if(CurrentMoveRow == 1 and CurrentMoveCol == 1):
        Test = True if BoardMoves[0].isspace() else False
    elif(CurrentMoveRow == 1 and CurrentMoveCol == 2):
        Test = True if BoardMoves[1].isspace() else False
    elif(CurrentMoveRow == 1 and CurrentMoveCol == 3):
        Test = True if BoardMoves[2].isspace() else False
    elif(CurrentMoveRow == 2 and CurrentMoveCol == 1):
        Test = True if BoardMoves[3].isspace() else False
    elif(CurrentMoveRow == 2 and CurrentMoveCol == 2):
        Test = True if BoardMoves[4].isspace() else False
    elif(CurrentMoveRow == 2 and CurrentMoveCol == 3):
        Test = True if BoardMoves[5].isspace() else False
    elif(CurrentMoveRow == 3 and CurrentMoveCol == 1):
        Test = True if BoardMoves[6].isspace() else False
    elif(CurrentMoveRow == 3 and CurrentMoveCol == 2):
        Test = True if BoardMoves[7].isspace() else False
    elif(CurrentMoveRow == 3 and CurrentMoveCol == 3):
        Test = True if BoardMoves[8].isspace() else False
    elif(CurrentMoveRow > 3 or CurrentMoveCol > 3):
        print("\nOne or more given values are higher than expected, give new ones!")
        Test = False
    elif(CurrentMoveRow < 1 or CurrentMoveCol < 1):
        print("\nOne or more given values are lower than expected, give new ones!")
        Test = False
    else:
        print("\nThere is some kind of mistake in CheckIfPosIsSpace")
        Test = False
    
    return Test

# This function allows code to translate cords to Board position
def TranslateAndCheckBoardPos(CurrentMoveRow, CurrentMoveCol, BoardMoves, Player):
    if(CurrentMoveRow == 1 and CurrentMoveCol == 1):
        BoardMoves[0] = Player
    elif(CurrentMoveRow == 1 and CurrentMoveCol == 2):
        BoardMoves[1] = Player
    elif(CurrentMoveRow == 1 and CurrentMoveCol == 3):
        BoardMoves[2] = Player
    elif(CurrentMoveRow == 2 and CurrentMoveCol == 1):
        BoardMoves[3] = Player
    elif(CurrentMoveRow == 2 and CurrentMoveCol == 2):
        BoardMoves[4] = Player
    elif(CurrentMoveRow == 2 and CurrentMoveCol == 3):
        BoardMoves[5] = Player
    elif(CurrentMoveRow == 3 and CurrentMoveCol == 1):
        BoardMoves[6] = Player
    elif(CurrentMoveRow == 3 and CurrentMoveCol == 2):
        BoardMoves[7] = Player
    elif(CurrentMoveRow == 3 and CurrentMoveCol == 3):
        BoardMoves[8] = Player
    else:
        print("\nThere is some kind of mistake in TranslateBoardPos")
    
    return BoardMoves


# This function allows user to reset or exit game
def ResetOrExitGame(AskNewGame, BoardMoves, Turns):
        if(AskNewGame == "Y"):
            Turns = 0
            for i in range(9):
                BoardMoves[i] = ' '
                i += 1
            return Turns
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit("\nBye Bye!")