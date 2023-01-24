from termcolor import colored

NONE = 0
KING = 1
PAWN = 2
KNIGHT = 3
BISHOP = 4
ROOK = 5
QUEEN = 6
WHITE = 8
BLACK = 16

TYPEMASK = 0b00111
BLACKMASK = 0b10000
WHITEMASK = 0b01000
COLOURMASK = WHITEMASK | BLACKMASK

PieceTypeFromSymbol = {
    "k": KING,
    "p": PAWN,
    "n": KNIGHT,
    "b": BISHOP,
    "r": ROOK,
    "q": QUEEN,
}

BLACK_CHARS = {
    'k': u'\u265A',
    'p': u'\u265F',
    'n': u'\u265E',
    'b': u'\u265D',
    'r': u'\u265C',
    'q': u'\u265B'
}

WHITE_CHARS = {
    'k': u'\u2654',
    'p': u'\u2659',
    'n': u'\u2658',
    'b': u'\u2657',
    'r': u'\u2656',
    'q': u'\u2655'
}


class Chess:
    board = [None] * 64
    moves = []
    legalMoves = []

    def __init__(self) -> None:
        self.FENToBoard(
            "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")

    def ShowBoard(self):
        board = ["\u2009"] * 64
        i = 0
        for piece in self.board:
            if piece:
                pieceSymbol = BLACK_CHARS[piece] if str.islower(
                    piece) else colored(WHITE_CHARS[str.lower(piece)], "black")
                board[i] = pieceSymbol
            i += 1
        splittedBoard = [f'{x//-8 + 8} ' + ' '.join(board[x:x+8])
                         for x in range(0, len(board), 8)]
        print('\n'.join(splittedBoard) + '\n  a b c d e f g')

    def FENToBoard(self, fen):
        file = 0
        rank = 7
        for symbol in fen:
            if symbol == "/":
                file = 0
                rank -= 1
            else:
                if str.isdigit(symbol):
                    file += int(symbol)
                else:
                    self.board[rank*8 + file] = symbol
                    file += 1

    def GetLegalMoves(self):
        if not self.board:
            return "No board"
        board = self.board
        i = 0
        for piece in board:
            if piece == "p" or piece == "P":
                self.legalMoves.append()
            i += 1
