import functions as fn
import sys


BoardMoves = [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']
Turns = 0
Player = ""
print("""Gra jest upośledzona więc proszę podawajcie najpierw wartości
wiersza potem kolumny. Dzięki ludzie!\n""")
try:
    warunek = False
    while(warunek == False):
        if(warunek == False):
            Player1 = input("Graczu 1 podaj symbol do gry: ")
            Player1 = Player1[0]
            Player2 = input("Graczu 2 podaj symbol do gry: ")
            Player2 = Player2[0]
            warunek = fn.checkPlayerNames(Player1, Player2, warunek)
        else:
            break
except(UnboundLocalError, ValueError, IndexError):
    print("Spowodowałeś errora, zasługujesz na wyłączenie programu!")
    sys.exit("To twoja kara. Bajooo!")

print(f"Gracze to: {Player1} oraz {Player2}")

while(True):
    fn.MainGame(BoardMoves, Turns, Player1, Player2, Player)
    Turns += 1
    