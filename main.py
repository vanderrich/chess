from chess import Chess

if __name__ == '__main__':
    Game = Chess()
    while True:
        Game.ShowBoard()
        move = input(
            "Make a move (learn more about move notations in https://www.chess.com/terms/chess-notation):")
