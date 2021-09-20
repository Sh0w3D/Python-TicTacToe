import functions as fn
import os
import sys


BoardMoves = [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']
Turns = 0
Player1 = input("Graczu 1 podaj symbol do gry: ")
Player2 = input("Graczu 2 podaj symbol do gry: ")

#fn.TicTacBoad(BoardMoves)
#os.system('cls' if os.name == 'nt' else 'clear')
print(f"Gracze to: {Player1} oraz {Player2}")

while(True):
    fn.MainGame(BoardMoves, Turns, Player1, Player2)
    Turns += 1

"""

    if(BoardMoves[8].isspace() != True):
        fn.TicTacBoad(BoardMoves)
        fn.ResetOrExitGame(input("Gra skończona! Grasz of nowa (Y/N): "), BoardMoves, Turns)
    #print(Turns)
    #print(BoardMoves)
    fn.TicTacBoad(BoardMoves)
    CurrentMoveCol = int(input("Do ktorej kolumny wstawic wartosc: "))
    CurrentMoveRow = int(input("Do ktorego wiersza wstawic wartosc: "))
    if(Turns % 2 == 0):
        Player = Player1
        fn.TranslateBoardPos(CurrentMoveRow, CurrentMoveCol, BoardMoves, Player)
    else:
        Player = Player2
        fn.TranslateBoardPos(CurrentMoveRow, CurrentMoveCol, BoardMoves, Player)
    os.system('cls' if os.name == 'nt' else 'clear')
    


"""
    