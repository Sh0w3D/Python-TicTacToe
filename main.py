import functions as fn
import os
import sys


BoardMoves = [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']
Turns = 0
Player = ""
print("""This game is kind of retarded so please give row value first
than give column value!\n""")
try:
    warunek = False
    while(warunek == False):
        if(warunek == False):
            Player1 = input("Player 1 what's your game symbol: ")
            Player1 = Player1[0]
            Player2 = input("Player 2 what's your game symbol: ")
            Player2 = Player2[0]
            warunek = fn.checkPlayerNames(Player1, Player2, warunek)
        else:
            break
except(UnboundLocalError, ValueError, IndexError):
    print("You've raised an error, now I'll crash!")
    sys.exit("Remember, it's all thanks to you!")

print(f"Players are: {Player1} and {Player2}")

while(True):
    try:
        fn.MainGame(BoardMoves, Turns, Player1, Player2, Player)
        Turns += 1
    except(KeyboardInterrupt):
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit("Goodbye!")
    