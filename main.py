import chess
from GUI import GUI
#https://pypi.org/project/chess/


def main():
    board = chess.Board()
    gui = GUI(board)
    running = True
    while gui.running:
        move = gui.showBoard()
        if move != None:
            print(move)
            board.push(move)
            print(board)
    # board.push_san("e4")
    # board.push_san("e5")
    # board.push_san("Qh5")
    # board.push_san("Nc6")
    # board.push_san("Bc4")
    # board.push_san("Nf6")
    # board.push_san("Qxf7")

    # board.is_checkmate()

    # print(board)

if __name__== "__main__":
    main() 