import os
import sys


   
def MainGame(BoardMoves, Turns, Player1, Player2):
    
    if(BoardMoves[8].isspace() != True):
        TicTacBoad(BoardMoves)
        ResetOrExitGame(input("Gra skończona! Grasz of nowa (Y/N): "), BoardMoves, Turns)
    #print(Turns)
    #print(BoardMoves)
    TicTacBoad(BoardMoves)
    CurrentMoveCol = int(input("Do ktorej kolumny wstawic wartosc: "))
    CurrentMoveRow = int(input("Do ktorego wiersza wstawic wartosc: "))
    #tutaj bedzie check i potem reszta w if else
    if(Turns % 2 == 0):
       Player = Player1
       TranslateAndCheckBoardPos(CurrentMoveRow, CurrentMoveCol, BoardMoves, Player)
    else:
       Player = Player2
       TranslateAndCheckBoardPos(CurrentMoveRow, CurrentMoveCol, BoardMoves, Player)
    os.system('cls' if os.name == 'nt' else 'clear')




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


def TranslateAndCheckBoardPos(CurrentMoveCol, CurrentMoveRow, BoardMoves, Player):
    if(CurrentMoveCol == 1 and CurrentMoveRow == 1):
        BoardMoves[0] = Player
    elif(CurrentMoveCol == 1 and CurrentMoveRow == 2):
        BoardMoves[1] = Player
    elif(CurrentMoveCol == 1 and CurrentMoveRow == 3):
        BoardMoves[2] = Player
    elif(CurrentMoveCol == 2 and CurrentMoveRow == 1):
        BoardMoves[3] = Player
    elif(CurrentMoveCol == 2 and CurrentMoveRow == 2):
        BoardMoves[4] = Player
    elif(CurrentMoveCol == 2 and CurrentMoveRow == 3):
        BoardMoves[5] = Player
    elif(CurrentMoveCol == 3 and CurrentMoveRow == 1):
        BoardMoves[6] = Player
    elif(CurrentMoveCol == 3 and CurrentMoveRow == 2):
        BoardMoves[7] = Player
    elif(CurrentMoveCol == 3 and CurrentMoveRow == 3):
        BoardMoves[8] = Player
    else:
        #BoardMoves[0] = Player
        #print(BoardMoves)
        print("\nThere is some kind of mistake in TranslateBoardPos")
    
    return BoardMoves


def ResetOrExitGame(AskNewGame, BoardMoves, Turns):
        if(AskNewGame == "Y"):
            Turns = 0
            for i in range(9):
                BoardMoves[i] = ' '
                i += 1
            return Turns
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit("\nBajo Jajo")
