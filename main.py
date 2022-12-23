import chess
from GUI import GUI
import random
from settings import WHITEAI, BLACKAI
#https://pypi.org/project/chess/


def isAI(color: str):
    if (color == "White" and WHITEAI) or (color == "Black" and BLACKAI):
        return True
    return False

def whichColor(boardTurn: bool) -> str:
    if boardTurn:
        return "White"
    return "Black"

def main():
    board = chess.Board()
    gui = GUI(board)
    while gui.running and board.legal_moves:
        move = None
        if isAI(whichColor(board.turn)):
            move = random.choice(list(board.legal_moves))
        else:
            move = gui.showBoard()
        if move != None:
            board.push(move)
    print(board.outcome)

if __name__== "__main__":
    main() 