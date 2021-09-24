import functions as fn
import sys


BoardMoves = [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']
Turns = 0
print("""Gra jest upośledzona więc proszę podawajcie najpierw wartości
wiersza potem kolumny. Dzięki ludzie!\n""")
try:
    Player1 = input("Graczu 1 podaj symbol do gry: ")
    Player1 = Player1[0]
    Player2 = input("Graczu 2 podaj symbol do gry: ")
    Player2 = Player2[0]
except(UnboundLocalError, ValueError, IndexError):
    print("Spowodowałeś errora, zasługujesz na wyłączenie programu!")
    sys.exit("To twoja kara. Bajooo!")

#fn.TicTacBoad(BoardMoves)
#os.system('cls' if os.name == 'nt' else 'clear')
print(f"Gracze to: {Player1} oraz {Player2}")

while(True):
    fn.MainGame(BoardMoves, Turns, Player1, Player2)
    Turns += 1
    