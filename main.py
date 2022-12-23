import chess
from GUI import GUI
#https://pypi.org/project/chess/


def whichColor(boardTurn: bool) -> str:
    if boardTurn:
        return "White"
    return "black"


def main():
    board = chess.Board()
    gui = GUI(board)
    while gui.running and board.legal_moves:
        # print(whosTurn(board.turn))
        move = gui.showBoard()
        if move != None:
            board.push(move)
    print(board.outcome)

if __name__== "__main__":
    main() 