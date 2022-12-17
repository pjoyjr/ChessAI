import chess
from GUI import GUI
#https://pypi.org/project/chess/


def main():
    board = chess.Board()
    gui = GUI(board)
    gui.showBoard()

    # board.legal_moves

    # chess.Move.from_uci("a8a1") in board.legal_moves

    # board.push_san("e4")
    # board.push_san("e5")
    # board.push_san("Qh5")
    # board.push_san("Nc6")
    # board.push_san("Bc4")
    # board.push_san("Nf6")
    # board.push_san("Qxf7")

    # board.is_checkmate()

    print(board)

if __name__== "__main__":
    main() 