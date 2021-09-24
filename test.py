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

BoardMoves = [0,1,2,3,4,5,6,7,8]
TicTacBoad(BoardMoves)